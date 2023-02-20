import ctypes
import struct
import math
from collections import UserList

from functools import lru_cache
from io import BytesIO

import numpy as np
from PIL import Image as ImageP

import ui


class uvec2(UserList):
  def __init__(self, _xy: list=[0.0, 0.0]):
    super().__init__(_xy)

  def __add__(self, other: list) -> list:
    _x = uint32(self.data[0] + other[0])
    _y = uint32(self.data[1] + other[1])
    return uvec2([_x, _y])

  def __sub__(self, other: list) -> list:
    _x = uint32(self.data[0] - other[0])
    _y = uint32(self.data[1] - other[1])
    return uvec2([_x, _y])

  def __mul__(self, other: list) -> list:
    _x = uint32(self.data[0] * other[0])
    _y = uint32(self.data[1] * other[1])
    return uvec2([_x, _y])

  def __truediv__(self, other: list) -> list:
    _x = uint32(int(self.data[0] / other[0]))
    _y = uint32(int(self.data[1] / other[1]))
    return uvec2([_x, _y])

  def __floordiv__(self, other: list) -> list:
    _x = uint32(int(self.data[0] // other[0]))
    _y = uint32(int(self.data[1] // other[1]))
    return uvec2([_x, _y])

  def __lshift__(self, other: list) -> list:
    _x = uint32(self.data[0] << other[0])
    _y = uint32(self.data[1] << other[1])
    return uvec2([_x, _y])

  def __rshift__(self, other: list) -> list:
    _x = uint32(self.data[0] >> other[0])
    _y = uint32(self.data[1] >> other[1])
    return uvec2([_x, _y])

  def __and__(self, other: list) -> list:
    _x = uint32(self.data[0] & other[0])
    _y = uint32(self.data[1] & other[1])
    return uvec2([_x, _y])

  def __xor__(self, other: list) -> list:
    _x = uint32(self.data[0] ^ other[0])
    _y = uint32(self.data[1] ^ other[1])
    return uvec2([_x, _y])

  def __or__(self, other: list) -> list:
    _x = uint32(self.data[0] | other[0])
    _y = uint32(self.data[1] | other[1])
    return uvec2([_x, _y])

  def __iadd__(self, other: list) -> list:
    _x = uint32(self.data[0] + other[0])
    _y = uint32(self.data[1] + other[1])
    return uvec2([_x, _y])

  def __isub__(self, other: list) -> list:
    _x = uint32(self.data[0] - other[0])
    _y = uint32(self.data[1] - other[1])
    return uvec2([_x, _y])

  def __imul__(self, other: list) -> list:
    _x = uint32(self.data[0] * other[0])
    _y = uint32(self.data[1] * other[1])
    return uvec2([_x, _y])

  def __itruediv__(self, other: list) -> list:
    _x = uint32(int(self.data[0] / other[0]))
    _y = uint32(int(self.data[1] / other[1]))
    return uvec2([_x, _y])

  def __ifloordiv__(self, other: list) -> list:
    _x = uint32(int(self.data[0] // other[0]))
    _y = uint32(int(self.data[1] // other[1]))
    return uvec2([_x, _y])

  def __ilshift__(self, other: list) -> list:
    _x = uint32(self.data[0] << other[0])
    _y = uint32(self.data[1] << other[1])
    return uvec2([_x, _y])

  def __irshift__(self, other: list) -> list:
    _x = uint32(self.data[0] >> other[0])
    _y = uint32(self.data[1] >> other[1])
    return uvec2([_x, _y])

  def __iand__(self, other: list) -> list:
    _x = uint32(self.data[0] & other[0])
    _y = uint32(self.data[1] & other[1])
    return uvec2([_x, _y])

  def __ixor__(self, other: list) -> list:
    _x = uint32(self.data[0] ^ other[0])
    _y = uint32(self.data[1] ^ other[1])
    return uvec2([_x, _y])

  def __ior__(self, other: list) -> list:
    _x = uint32(self.data[0] | other[0])
    _y = uint32(self.data[1] | other[1])
    return uvec2([_x, _y])

  @property
  def x(self) -> int:
    return uint32(self.data[0])

  @property
  def y(self) -> int:
    return uint32(self.data[1])

  @property
  def xy(self) -> list:
    _x, _y = self.data
    return uvec2([uint32(_x), uint32(_y)])

  @property
  def yx(self) -> list:
    _x, _y = self.data
    return uvec2([uint32(_y), uint32(_x)])

  @x.setter
  def x(self, _x: int):
    self.data[0] = uint32(_x)

  @y.setter
  def y(self, _y: int):
    self.data[1] = uint32(_y)

  @xy.setter
  def xy(self, _xy: list):
    _x, _y = _xy
    self.data[0] = uint32(_x)
    self.data[1] = uint32(_y)

  @yx.setter
  def yx(self, _yx: list):
    _y, _x = _yx
    self.data[0] = uint32(_x)
    self.data[1] = uint32(_y)


class uvec3(UserList):
  def __init__(self, _xyz: list=[0.0, 0.0, 0.0]):
    super().__init__(_xyz)

  def __add__(self, other: list) -> list:
    _x = uint32(self.data[0] + other[0])
    _y = uint32(self.data[1] + other[1])
    _z = uint32(self.data[2] + other[2])
    return uvec3([_x, _y, _z])

  def __sub__(self, other: list) -> list:
    _x = uint32(self.data[0] - other[0])
    _y = uint32(self.data[1] - other[1])
    _z = uint32(self.data[2] - other[2])
    return uvec3([_x, _y, _z])

  def __mul__(self, other: list) -> list:
    _x = uint32(self.data[0] * other[0])
    _y = uint32(self.data[1] * other[1])
    _z = uint32(self.data[2] * other[2])
    return uvec3([_x, _y, _z])

  def __truediv__(self, other: list) -> list:
    _x = uint32(int(self.data[0] / other[0]))
    _y = uint32(int(self.data[1] / other[1]))
    _z = uint32(int(self.data[2] / other[2]))
    return uvec3([_x, _y, _z])

  def __floordiv__(self, other: list) -> list:
    _x = uint32(int(self.data[0] // other[0]))
    _y = uint32(int(self.data[1] // other[1]))
    _z = uint32(int(self.data[2] // other[2]))
    return uvec3([_x, _y, _z])

  def __lshift__(self, other: list) -> list:
    _x = uint32(self.data[0] << other[0])
    _y = uint32(self.data[1] << other[1])
    _z = uint32(self.data[2] << other[2])
    return uvec3([_x, _y, _z])

  def __rshift__(self, other: list) -> list:
    _x = uint32(self.data[0] >> other[0])
    _y = uint32(self.data[1] >> other[1])
    _z = uint32(self.data[2] >> other[2])
    return uvec3([_x, _y, _z])

  def __and__(self, other: list) -> list:
    _x = uint32(self.data[0] & other[0])
    _y = uint32(self.data[1] & other[1])
    _z = uint32(self.data[2] & other[2])
    return uvec3([_x, _y, _z])

  def __xor__(self, other: list) -> list:
    _x = uint32(self.data[0] ^ other[0])
    _y = uint32(self.data[1] ^ other[1])
    _z = uint32(self.data[2] ^ other[2])
    return uvec3([_x, _y, _z])

  def __or__(self, other: list) -> list:
    _x = uint32(self.data[0] | other[0])
    _y = uint32(self.data[1] | other[1])
    _z = uint32(self.data[2] | other[2])
    return uvec3([_x, _y, _z])

  def __iadd__(self, other: list) -> list:
    _x = uint32(self.data[0] + other[0])
    _y = uint32(self.data[1] + other[1])
    _z = uint32(self.data[2] + other[2])
    return uvec3([_x, _y, _z])

  def __isub__(self, other: list) -> list:
    _x = uint32(self.data[0] - other[0])
    _y = uint32(self.data[1] - other[1])
    _z = uint32(self.data[2] - other[2])
    return uvec3([_x, _y, _z])

  def __imul__(self, other: list) -> list:
    _x = uint32(self.data[0] * other[0])
    _y = uint32(self.data[1] * other[1])
    _z = uint32(self.data[2] * other[2])
    return uvec3([_x, _y, _z])

  def __itruediv__(self, other: list) -> list:
    _x = uint32(int(self.data[0] / other[0]))
    _y = uint32(int(self.data[1] / other[1]))
    _z = uint32(int(self.data[2] / other[2]))
    return uvec3([_x, _y, _z])

  def __ifloordiv__(self, other: list) -> list:
    _x = uint32(int(self.data[0] // other[0]))
    _y = uint32(int(self.data[1] // other[1]))
    _z = uint32(int(self.data[2] // other[2]))
    return uvec3([_x, _y, _z])

  def __ilshift__(self, other: list) -> list:
    _x = uint32(self.data[0] << other[0])
    _y = uint32(self.data[1] << other[1])
    _z = uint32(self.data[2] << other[2])
    return uvec3([_x, _y, _z])

  def __irshift__(self, other: list) -> list:
    _x = uint32(self.data[0] >> other[0])
    _y = uint32(self.data[1] >> other[1])
    _z = uint32(self.data[2] >> other[2])
    return uvec3([_x, _y, _z])

  def __iand__(self, other: list) -> list:
    _x = uint32(self.data[0] & other[0])
    _y = uint32(self.data[1] & other[1])
    _z = uint32(self.data[2] & other[2])
    return uvec3([_x, _y, _z])

  def __ixor__(self, other: list) -> list:
    _x = uint32(self.data[0] ^ other[0])
    _y = uint32(self.data[1] ^ other[1])
    _z = uint32(self.data[2] ^ other[2])
    return uvec3([_x, _y, _z])

  def __ior__(self, other: list) -> list:
    _x = uint32(self.data[0] | other[0])
    _y = uint32(self.data[1] | other[1])
    _z = uint32(self.data[2] | other[2])
    return uvec3([_x, _y, _z])

  @property
  def x(self) -> int:
    return uint32(self.data[0])

  @property
  def y(self) -> int:
    return uint32(self.data[1])

  @property
  def z(self) -> int:
    return uint32(self.data[2])

  @property
  def xy(self) -> list:
    _x, _y, _ = self.data
    return uvec2([uint32(_x), uint32(_y)])

  @property
  def yx(self) -> list:
    _x, _y, _ = self.data
    return uvec2([uint32(_y), uint32(_x)])

  @property
  def xyz(self) -> list:
    _x, _y, _z = self.data
    return uvec3([uint32(_x), uint32(_y), uint32(_z)])

  @property
  def xzy(self) -> list:
    _x, _y, _z = self.data
    return uvec3([uint32(_x), uint32(_z), uint32(_y)])

  @property
  def yxz(self) -> list:
    _x, _y, _z = self.data
    return uvec3([uint32(_y), uint32(_x), uint32(_z)])

  @property
  def yzx(self) -> list:
    _x, _y, _z = self.data
    return uvec3([uint32(_y), uint32(_z), uint32(_x)])

  @property
  def zxy(self) -> list:
    _x, _y, _z = self.data
    return uvec3([uint32(_z), uint32(_x), uint32(_y)])

  @property
  def zyx(self) -> list:
    _x, _y, _z = self.data
    return uvec3([uint32(_z), uint32(_y), uint32(_x)])

  @x.setter
  def x(self, _x: int):
    self.data[0] = uint32(_x)

  @y.setter
  def y(self, _y: int):
    self.data[1] = uint32(_y)

  @xy.setter
  def xy(self, _xy: list):
    _x, _y = _xy
    self.data[0] = uint32(_x)
    self.data[1] = uint32(_y)

  @yx.setter
  def yx(self, _yx: list):
    _y, _x = _yx
    self.data[0] = uint32(_x)
    self.data[1] = uint32(_y)

  @z.setter
  def z(self, _z: int):
    self.data[2] = uint32(_z)

  @xyz.setter
  def xyz(self, _xyz: list):
    _x, _y, _z = _xyz
    self.data[0] = uint32(_x)
    self.data[1] = uint32(_y)
    self.data[2] = uint32(_z)

  @xzy.setter
  def xzy(self, _xzy: list):
    _x, _z, _y = _xzy
    self.data[0] = uint32(_x)
    self.data[1] = uint32(_y)
    self.data[2] = uint32(_z)

  @yxz.setter
  def yxz(self, _yxz: list):
    _y, _x, _z = _yxz
    self.data[0] = uint32(_x)
    self.data[1] = uint32(_y)
    self.data[2] = uint32(_z)

  @yzx.setter
  def yzx(self, _yzx: list):
    _y, _z, _x = _yzx
    self.data[0] = uint32(_x)
    self.data[1] = uint32(_y)
    self.data[2] = uint32(_z)

  @zxy.setter
  def zxy(self, _zxy: list):
    _z, _x, _y = _zxy
    self.data[0] = uint32(_x)
    self.data[1] = uint32(_y)
    self.data[2] = uint32(_z)

  @zyx.setter
  def zyx(self, _zyx: list):
    _z, _y, _x = _zyx
    self.data[0] = uint32(_x)
    self.data[1] = uint32(_y)
    self.data[2] = uint32(_z)


fu_pack = struct.Struct('>f')
fu_unpack = struct.Struct('>I')


@lru_cache()
def uint32(s) -> int:
  _s = s if s > 0 else 0
  return int(_s) if _s <= 0xffffffff else ctypes.c_uint32(int(_s)).value


@lru_cache()
def float32(f) -> float:
  _c_float = ctypes.c_float(f)
  return _c_float.value


@lru_cache()
def floatBitsToUint(f: float) -> int:
  # fp = struct.pack('>f', f)
  # fu = struct.unpack('>I', fp)[0]
  fp = fu_pack.pack(f)
  fu = fu_unpack.unpack(fp)[0]
  return uint32(fu)


UINT_MAX = 0xffffffff
k = uvec3([
  0x456789ab,
  0x6789ab45,
  0x89ab4567,
])

u = uvec3([
  1,
  2,
  3,
])  # todo: シフト数


def uhash11(n) -> int:
  n ^= (n << u.x)
  n ^= (n >> u.x)
  n *= k.x
  n ^= (n << 1)
  return uint32(n * k.x)


def uhash22(n: uvec2) -> uvec2:
  n ^= (n.yx << u.xy)
  n ^= (n.yx >> u.xy)
  n *= k.xy
  n ^= (n.yx << u.xy)
  return n * k.xy


def uhash33(n: uvec3) -> uvec3:
  n ^= (n.yzx << u)
  n ^= (n.yzx >> u)
  n *= k
  n ^= (n.yzx << u)
  return n * k


def hash11(p: float) -> float:
  n = floatBitsToUint(p)
  return float32(uhash11(n) / UINT_MAX)


def hash21(p: list) -> float:
  n = uvec2([floatBitsToUint(p[0]), floatBitsToUint(p[1])])
  uh = uhash22(n)
  _x = float32(uh.x / UINT_MAX)
  return _x


def hash22(p: list) -> list:
  n = uvec2([
    floatBitsToUint(p[0]),
    floatBitsToUint(p[1]),
  ])
  uh = uhash22(n)
  _x = float32(uh.x / UINT_MAX)
  _y = float32(uh.y / UINT_MAX)
  return [_x, _y]


def hash31(p: list) -> float:
  n = uvec3([
    floatBitsToUint(p[0]),
    floatBitsToUint(p[1]),
    floatBitsToUint(p[2]),
  ])
  uh = uhash33(n)
  return float32(uh.x / UINT_MAX)


def hash33(p: list) -> list:
  n = uvec3([
    floatBitsToUint(p[0]),
    floatBitsToUint(p[1]),
    floatBitsToUint(p[2]),
  ])
  uh = uhash33(n)
  _x = float32(uh.x / UINT_MAX)
  _y = float32(uh.y / UINT_MAX)
  _z = float32(uh.z / UINT_MAX)
  return [_x, _y, _z]


sq_size = 64

RGB_SIZE = 256
ratio = RGB_SIZE / sq_size

init_img = ImageP.new('RGB', (sq_size, sq_size))
base_array = np.asarray(init_img)
diff_array = np.zeros((sq_size, sq_size, 3), dtype=np.uint8)


@lru_cache()
def setup_img(_time=0):
  for x in range(sq_size):
    for y in range(sq_size):
      '''
      _x = x * ratio
      _y = y * ratio
      diff_array[x][y] = np.asarray([_x, _y, 255])
      '''

      px = x / sq_size + _time
      py = y / sq_size + _time
      '''
      __x = hash21([px, py])
      _x = __x * RGB_SIZE
      diff_array[x][y] = np.asarray([_x, _x, _x])
      '''
      p_hash = hash22([px, py])
      _x = p_hash[0] * RGB_SIZE
      _y = p_hash[1] * RGB_SIZE
      diff_array[x][y] = np.asarray([_x, _y, 255])

  imgp = ImageP.fromarray(diff_array)
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
    #self.img = setup_img()
    #self.im_view.image = self.img
    self.add_subview(self.im_view)

  def update(self):
    self._time += self.update_interval
    self.u_time = math.floor(60.0 * self._time)
    self.im_view.image = setup_img(self.u_time)


if __name__ == '__main__':
  view = View()
  #view.present()
  #view.present(hide_title_bar=True)
  view.present(style='fullscreen', orientations=['portrait'])

  x = 1

