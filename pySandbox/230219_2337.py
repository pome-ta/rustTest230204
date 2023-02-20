import ctypes
import struct
import math
from collections import UserList
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


sq_size = 320

init_img = ImageP.new('RGB', (sq_size, sq_size))
base_array = np.asarray(init_img)
print(base_array.shape)
diff_array = np.zeros((sq_size, sq_size, 3), dtype=np.uint8)
'''
def show_canvas(_cpu):
  #canvas = _cpu.memory[0x200:0x600]
  #canvas = [_cpu.mem_read(i) for i in range(0x200, 0x600)]
  canvas = _cpu.bus.cpu_vram[0x200:0x600]
  count = 0
  for x, y in product(range(32), range(32)):
    byt = canvas[count]
    diff_array[x][y] = color(palette(byt))
    count += 1
  #del canvas
  out_array = base_array + diff_array
  out_img = ImageP.fromarray(out_array)
  re_out = out_img.resize((320, 320))
  with BytesIO() as bIO:
    re_out.save(bIO, 'png')
    re_img = ui.Image.from_data(bIO.getvalue())
    del bIO
    return re_img
'''


class View(ui.View):
  def __init__(self):
    self.bg_color = 1
    self.update_interval = 1 / 30
    self._time = 0.0
    self.u_time = 0.0

  def draw(self):
    sq = 64
    margin = 16

    width = sq
    height = sq

    for x in range(width):
      for y in range(height):
        rect = ui.Path.rect(x + margin, y + margin, 1, 1)

        px = x / sq + self.u_time
        py = y / sq + self.u_time

        if x > sq / 2:
          _x = hash21([px, py])
          ui.set_color(_x)
        else:
          _x, _y = hash22([px, py])
          ui.set_color((_x, _y, 1.0))
        rect.fill()

  def update(self):
    self._time += self.update_interval
    self.u_time = math.floor(60.0 * self._time)
    self.set_needs_display()


if __name__ == '__main__':
  view = View()
  #view.present()
  #view.present(hide_title_bar=True)
  #view.present(style='fullscreen', orientations=['portrait'])

  for x in range(sq_size):
    for y in range(sq_size):

      diff_array[x][y] = np.asarray([x, y, 255])
      #print(diff_array[x][y])
    #out_array = base_array + diff_array
    #out_img = ImageP.fromarray(out_array)
  out_img = ImageP.fromarray(diff_array)

  x = 1

