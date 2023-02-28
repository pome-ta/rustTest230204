import struct
import math
from itertools import product
from functools import lru_cache
from io import BytesIO

import numpy as np
from PIL import Image as ImageP

import ui

UINT_MAX = 0xffff_ffff

k = np.array([0x456789ab, 0x6789ab45, 0x89ab4567]).astype(np.uint32)
u = np.array([1, 2, 3]).astype(np.uint32)

sq_size: int = 128

width_size = sq_size
height_size = sq_size

RGB_SIZE = 255
color_ch = 3
_xy = range(2)

f_pack = struct.Struct('>f')
f_unpack = struct.Struct('>I')


@lru_cache()
def floatBitsToUint(f: float) -> int:
  return f_unpack.unpack(f_pack.pack(f))[0]


np_floatBitsToUint = np.vectorize(
  floatBitsToUint, otypes=[np.uint32], cache=True)


def np_mix(x: np.array, y: np.array, a: np.array) -> np.array:
  return (x * (1.0 - a)) + (y * a)


@lru_cache()
def _vec(w: int, h: int, c: int) -> np.array:
  return np.empty((w, h, c)).astype(np.float32)


@lru_cache()
def FragCoord(width, height) -> np.array:
  _row = np.arange(0, width)
  _col = np.arange(0, height).reshape(height, 1)
  _x, _y = np.meshgrid(_row, _col)
  _pos = _vec(width, height, 2)
  _pos[..., 0] = _x
  _pos[..., 1] = _y
  return _pos


def uhash11(n: np.array) -> np.array:
  n ^= (n << u[0])
  n ^= (n >> [0])
  n *= k[0]
  n ^= (n << [0])
  return n * k[0]


def hash11(p: np.array) -> np.array:
  n = np_floatBitsToUint(p)
  return uhash11(n).astype(np.float32) / float(UINT_MAX)


def uhash22(n: np.array) -> np.array:
  _n = n.copy()
  _n[..., 0] = n[..., 1]
  _n[..., 1] = n[..., 0]
  n ^= (_n << u[:2])

  _n = n.copy()
  _n[..., 0] = n[..., 1]
  _n[..., 1] = n[..., 0]
  n ^= (_n >> u[:2])

  n *= k[:2]

  _n = n.copy()
  _n[..., 0] = n[..., 1]
  _n[..., 1] = n[..., 0]
  n ^= (_n << u[:2])
  return n * k[:2]


def uhash33(n: np.array) -> np.array:
  _n = n.copy()
  _n[..., 0] = n[..., 1]
  _n[..., 1] = n[..., 2]
  _n[..., 2] = n[..., 0]
  n ^= (_n << u)

  _n = n.copy()
  _n[..., 0] = n[..., 1]
  _n[..., 1] = n[..., 2]
  _n[..., 2] = n[..., 0]
  n ^= (_n >> u)

  n *= k

  _n = n.copy()
  _n[..., 0] = n[..., 1]
  _n[..., 1] = n[..., 2]
  _n[..., 2] = n[..., 0]
  n ^= (_n << u)
  return n * k


def hash22(p: np.array) -> np.array:
  n = np_floatBitsToUint(p)
  return uhash22(n).astype(np.float32) / float(UINT_MAX)


def hash33(p: np.array) -> np.array:
  n = np_floatBitsToUint(p)
  return uhash33(n).astype(np.float32) / float(UINT_MAX)


def hash21(p: np.array) -> np.array:
  n = np_floatBitsToUint(p)
  _h22 = uhash22(n).astype(np.float32)
  return _h22[..., 0] / float(UINT_MAX)


def hash31(p: np.array) -> np.array:
  n = np_floatBitsToUint(p)
  _h33 = uhash33(n).astype(np.float32)
  return _h33[..., 0] / float(UINT_MAX)


def vnoise21_n(p: np.array) -> np.array:
  n = np.floor(p)
  v = [hash21(n + [_i, _j]) for _j, _i in product(_xy, repeat=2)]
  # v = list(range(4))
  # for j in range(2):
  #     for i in range(2):
  #         v[i + 2 * j] = hash21(n + [i, j])
  f = p - n
  return np_mix(
    np_mix(v[0], v[1], f[..., 0]),
    np_mix(v[2], v[3], f[..., 0]),
    f[..., 1], )


def vnoise21_f(p: np.array) -> np.array:
  n = np.floor(p)
  v = [hash21(n + [_i, _j]) for _j, _i in product(_xy, repeat=2)]
  # v = list(range(4))
  # for j in range(2):
  #     for i in range(2):
  #         v[i + 2 * j] = hash21(n + [i, j])
  f = p - n
  f = f * f * (3.0 - 2.0 * f)
  return np_mix(
    np_mix(v[0], v[1], f[..., 0]),
    np_mix(v[2], v[3], f[..., 0]),
    f[..., 1], )


def vnoise31(p: np.array) -> np.array:
  n = np.floor(p)
  v = [hash31(n + [_i, _j, _k]) for _k, _j, _i in product(_xy, repeat=3)]
  # v = list(range(8))
  # for k in range(2):
  #     for j in range(2):
  #         for i in range(2):
  #             v[i + 2 * j + 4 * k] = hash31(n + [i, j, k])
  f = p - n
  f = f * f * (3.0 - 2.0 * f)

  w = [
    np_mix(
      np_mix(v[4 * _i], v[4 * _i + 1], f[..., 0]),
      np_mix(v[4 * _i + 2], v[4 * _i + 3], f[..., 0]), f[..., 1]) for _i in _xy
  ]

  return np_mix(w[0], w[1], f[..., 2])


def imageP2uint8_convert(_rgb):
  _l = _rgb * RGB_SIZE
  _l[np.less(_l, 0)] = 0
  _l[np.less(RGB_SIZE, _l)] = RGB_SIZE
  return _l


canvas_px = np.zeros((width_size, height_size, 3)).astype(np.uint8)
fragCoord = FragCoord(width_size, height_size)

pos = fragCoord / sq_size
split_num = int(sq_size / 3)


@lru_cache()
def setup_img(_time=0, u_time=0.0):
  _pos = 10.0 * pos + u_time

  vec3 = _vec(width_size, height_size, 3)
  vec3[..., 0] = _pos[..., 0]
  vec3[..., 1] = _pos[..., 1]
  vec3[..., 2] = u_time

  v21_n = vnoise21_n(_pos)
  v21_f = vnoise21_f(_pos)
  v31 = vnoise31(vec3)

  out_n = imageP2uint8_convert(v21_n)
  out_f = imageP2uint8_convert(v21_f)
  out_3 = imageP2uint8_convert(v31)

  for div in range(3):
    if div == 0:
      for i in range(3):
        s = split_num * div
        e = split_num * (div + 1)
        canvas_px[..., s:e, i] = out_n[..., s:e]
    if div == 1:
      for i in range(3):
        s = split_num * div + 1
        e = split_num * (div + 1)
        canvas_px[..., s:e, i] = out_f[..., s:e]
    if div == 2:
      for i in range(3):
        s = split_num * div + 1
        e = sq_size
        canvas_px[..., s:e, i] = out_3[..., s:e]

  imgp = ImageP.fromarray(canvas_px)

  with BytesIO() as bIO:
    imgp.save(bIO, 'png')
    return ui.Image.from_data(bIO.getvalue())


class View(ui.View):
  def __init__(self, *args, **kwargs):
    self.name = 'vnoise'
    self.bg_color = 1
    self.update_interval = 1 / 30
    self.u_time = 0.0
    self.f_time = 0.0
    self.im_view = ui.ImageView()
    self.im_view.content_mode = ui.CONTENT_SCALE_ASPECT_FIT
    self.im_view.flex = 'WH'
    self.add_subview(self.im_view)

  def update(self):
    self.u_time += self.update_interval
    self.f_time = math.floor(60.0 * self.u_time)
    self.im_view.image = setup_img(self.f_time, self.u_time)


if __name__ == '__main__':
  view = View()
  # view.present()
  # view.present(hide_title_bar=True)
  view.present(style='fullscreen', orientations=['portrait'])

  x = 1

