import ctypes
import struct

from collections import UserList


class uvec2(UserList):
  def __init__(self, _xy: list = [0.0, 0.0]):
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
  def __init__(self, _xyz: list = [0.0, 0.0, 0.0]):
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


def uint32(s) -> int:
  # xxx: ????????????????????????????????????
  _s = s if s > 0 else 0
  _c_uint32 = ctypes.c_uint32(int(_s))
  return _c_uint32.value


def float32(f) -> float:
  _c_float = ctypes.c_float(f)
  return _c_float.value


def floatBitsToUint(f: float) -> int:
  # fp = struct.pack('>f', f)
  # fu = struct.unpack('>I', fp)[0]
  fp = fu_pack.pack(f)
  fu = fu_unpack.unpack(fp)[0]
  return uint32(fu)


def uint_set(num) -> int:
  return uint32(num)


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
])  # todo: ????????????


def uhash11(n) -> int:
  n ^= (n << 1)
  n ^= (n >> 1)
  n *= k
  n ^= (n << 1)
  nk = n * k

  return uint32(nk)


def hash11(p: float) -> float:
  n = floatBitsToUint(p)
  return float32(uhash11(n)) / float32(UINT_MAX)


def uhash22(n: uvec2) -> uvec2:
  n ^= (n.yx << u.xy)
  n ^= (n.yx >> u.xy)
  n *= k.xy
  n ^= (n.yx << u.xy)
  return n * k.xy


def hash22(p: list) -> uvec2:
  n = uvec2([floatBitsToUint(p[0]), floatBitsToUint(p[1])])
  uh = uhash22(n)
  _x = float32(uh.x / UINT_MAX)
  _y = float32(uh.y / UINT_MAX)
  return uvec2([_x, _y])


if __name__ == '__main__':
  sq = 256
  margin = 16
  width = sq
  height = sq

  for x in range(width):
    for y in range(height):
      px = x / sq
      py = y / sq
      pnxy = hash22([px, py])
      #print(pnxy)

  x = 1
