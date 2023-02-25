import ctypes
import struct
import math

from functools import lru_cache
from io import BytesIO

import numpy as np
from PIL import Image as ImageP

import ui

UINT_MAX = 0xffff_ffff

k = np.array([0x456789ab, 0x6789ab45, 0x89ab4567]).astype(np.uint32)
u = np.array([1, 2, 3]).astype(np.uint32)

sq_size: int = 320

width_size = sq_size
height_size = sq_size

RGB_SIZE = 255
color_ch = 3


def FragCoord(width, height) -> np.array:
  _row = np.arange(0, width)
  _col = np.arange(0, height).reshape(height, 1)
  _x, _y = np.meshgrid(_row, _col)
  _pos = np.empty((width, height, 2)).astype(np.float32)
  _pos[:, :, 0] = _x
  _pos[:, :, 1] = _y
  return _pos


@lru_cache()
def uint32(s) -> int:
  _s = s if s > 0 else 0
  return int(_s) if _s <= UINT_MAX else ctypes.c_uint32(int(_s)).value


fu_pack = struct.Struct('>f')
fu_unpack = struct.Struct('>I')


@lru_cache()
def floatBitsToUint(f: float) -> int:
  fp = fu_pack.pack(f)
  fu = fu_unpack.unpack(fp)[0]
  return fu  #uint32(fu)


np_floatBitsToUint = np.vectorize(
  floatBitsToUint, otypes=[np.uint32], cache=True)


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


def hash22(p: np.array) -> np.array:
  n = np_floatBitsToUint(p)
  return uhash22(n).astype(np.float32) / float(UINT_MAX)


pos = FragCoord(width_size, height_size)
canvas_px = np.zeros((width_size, height_size, 3)).astype(np.uint8)


@lru_cache()
def setup_img(_time=0):
  _pos = pos + _time
  hash_xy = hash22(_pos)
  canvas_px[..., 0] = hash_xy[..., 0] * RGB_SIZE
  canvas_px[..., 1] = hash_xy[..., 1] * RGB_SIZE
  canvas_px[..., 2] = RGB_SIZE
  imgp = ImageP.fromarray(canvas_px)

  with BytesIO() as bIO:
    imgp.save(bIO, 'png')
    return ui.Image.from_data(bIO.getvalue())


class View(ui.View):
  def __init__(self):
    self.bg_color = 1
    self.update_interval = 1 / 60
    self._time = 0.0
    self.u_time = 0.0
    self.im_view = ui.ImageView()
    self.im_view.content_mode = ui.CONTENT_SCALE_ASPECT_FIT
    self.im_view.flex = 'WH'
    self.add_subview(self.im_view)

  def update(self):
    self._time += self.update_interval
    self.u_time = math.floor(60.0 * self._time)
    self.im_view.image = setup_img(self.u_time)


if __name__ == '__main__':
  view = View()
  # view.present()
  # view.present(hide_title_bar=True)
  view.present(style='fullscreen', orientations=['portrait'])

  x = 1

