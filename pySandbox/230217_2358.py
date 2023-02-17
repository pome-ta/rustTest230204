import ctypes
import struct


fu_pack = struct.Struct('>f')
fu_unpack = struct.Struct('>I')


class uvec:
  def __init__(self, x: int):
    self._x = x

  @property
  def x(self) -> int:
    return self._x

  @x.setter
  def x(self, _x: int):
    self._x = _x


class uvec2(uvec):
  def __init__(self, xy: list):
    _x, _y = xy
    super().__init__(_x)
    self._y = _y

  @property
  def y(self) -> int:
    return self._y

  @property
  def xy(self) -> list:
    return [self._x, self._y]

  @property
  def yx(self) -> list:
    return [self._y, self._x]

  @y.setter
  def y(self, _y: int):
    self._y = _y

  @xy.setter
  def xy(self, _xy: list):
    _x, _y = _xy
    self._x = _x
    self._y = _y

  @yx.setter
  def yx(self, _yx: list):
    _y, _x = _yx
    self._x = _x
    self._y = _y


class uvec3(uvec2):
  def __init__(self, xyz: list):
    _x, _y, _z = xyz
    super().__init__([_x, _y])
    self._z = _z

  # [['x', 'y', 'z'], ['x', 'z', 'y'], ['y', 'x', 'z'], ['y', 'z', 'x'], ['z', 'x', 'y'], ['z', 'y', 'x']]
  @property
  def z(self) -> int:
    return self._z

  @property
  def xyz(self) -> list:
    return [self._x, self._y, self._z]

  @property
  def xzy(self) -> list:
    return [self._x, self._z, self._y]

  @property
  def yxz(self) -> list:
    return [self._y, self._x, self._z]

  @property
  def yzx(self) -> list:
    return [self._y, self._z, self._x]

  @property
  def zxy(self) -> list:
    return [self._z, self._x, self._y]

  @property
  def zyx(self) -> list:
    return [self._z, self._y, self._x]

  @z.setter
  def z(self, z: int):
    self._z = z

  # [['x', 'y', 'z'], ['x', 'z', 'y'], ['y', 'x', 'z'], ['y', 'z', 'x'], ['z', 'x', 'y'], ['z', 'y', 'x']]
  @xyz.setter
  def xyz(self, _xyz: list):
    _x, _y, _z = _xyz
    self._x = _x
    self._y = _y
    self._z = _z

  @xzy.setter
  def xzy(self, _xzy: list):
    _x, _z, _y = _xzy
    self._x = _x
    self._y = _y
    self._z = _z

  @yxz.setter
  def yxz(self, _yxz: list):
    _y, _x, _z = _yxz
    self._x = _x
    self._y = _y
    self._z = _z

  @yzx.setter
  def yzx(self, _yzx: list):
    _y, _z, _x = _yzx
    self._x = _x
    self._y = _y
    self._z = _z

  @zxy.setter
  def zxy(self, _zxy: list):
    _z, _x, _y = _zxy
    self._x = _x
    self._y = _y
    self._z = _z

  @zyx.setter
  def zyx(self, _zyx: list):
    _z, _y, _x = _zyx
    self._x = _x
    self._y = _y
    self._z = _z


UINT_MAX = 0xffffffff
k = [
    0x456789ab,
    0x6789ab45,
    0x89ab4567,
]

u = [
    1,
    2,
    3,
]  # todo: シフト数


def uint32(s) -> int:
  # xxx: 負の値処理するかどうか？
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


def uhash22(n: list) -> list:
  n ^= (n << 1)
  n ^= (n >> 1)
  n *= k
  n ^= (n << 1)
  nk = n * k
  return uint32(nk)


if __name__ == '__main__':
  # view = View()
  # view.present()
  # view.present(hide_title_bar=True)
  # view.present(style='fullscreen', orientations=['portrait'])
  u = uvec2([1, 2])
  from itertools import product
  xyz1 = ['x', 'y', 'z']
  xyz2 = ['x', 'y', 'z']
  xyz3 = ['x', 'y', 'z']
  xyzs = list(product(xyz1, xyz2, xyz3))

  print(xyzs)
  print('---')
  out_list = []

  for xx, yy, zz in xyzs:
    if xx == yy or xx == zz or yy == zz:
      continue
    out_list.append([xx, yy, zz])
  print(out_list)

  # x = 1
  # print(u.x)
  # print(u.y)
  # print(*u.xy)
  # print(u.yx)
  x = 1
