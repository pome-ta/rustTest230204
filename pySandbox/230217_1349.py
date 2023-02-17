import ctypes
import struct

import ui

fu_pack = struct.Struct('>f')
fu_unpack = struct.Struct('>I')

k = 0x456789ab
UINT_MAX = 0xffffffff


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


class View(ui.View):
  def __init__(self):
    self.bg_color = 1

  def draw(self):
    margin = 16
    sq = 320
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
  view.present(style='fullscreen', orientations=['portrait'])

