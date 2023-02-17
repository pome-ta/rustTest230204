import ctypes
import struct

import ui

fu_pack = struct.Struct('>f')
fu_unpack = struct.Struct('>I')


class uvec:
  def __init__(self, x: int):
    self.__x = x

  @property
  def x(self) -> int:
    return self.__x

  @x.setter
  def x(self, x: int):
    self.__x = x


class uvec2(uvec):
  def __init__(self, x, y):
    super().__init__(x)
    self.__y = y

  @property
  def y(self) -> int:
    return self.__y

  @property
  def xy(self) -> list:
    return [self.__x, self.__y]

  @property
  def yx(self) -> list:
    return [self.__y, self.__x]

  @y.setter
  def y(self, y: int):
    self.__y = y


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
  #fp = struct.pack('>f', f)
  #fu = struct.unpack('>I', fp)[0]
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


class View(ui.View):
  def __init__(self):
    self.bg_color = 1

  def draw(self):
    sq = 320
    margin = 16

    width = sq
    height = sq

    for x in range(width):
      rect = ui.Path.rect(x + margin, margin, 1, height)
      p = x / sq
      c = hash11(p)
      ui.set_color(c)
      rect.fill()


if __name__ == '__main__':
  view = View()
  #view.present()
  #view.present(hide_title_bar=True)
  #view.present(style='fullscreen', orientations=['portrait'])

