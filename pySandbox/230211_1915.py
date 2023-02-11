import struct
import statistics
import random

k = 0x456789ab
UINT_MAX = 0xffffffff


def float_to_hex(f: float) -> str:
  """
  [Pythonで浮動小数点数floatと16進数表現の文字列を相互に変換 | note.nkmk.me](https://note.nkmk.me/python-float-hex/)
    """
  return hex(struct.unpack('>I', struct.pack('>f', f))[0])


# todo: 浮動小数点数処理する 32bit
def _floatBitsToUint(num: float) -> str:
  sign_is = '' if num < 0.0 else 0
  hex_str = float_to_hex(num)
  to_int_bin = bin(int(hex_str, 16))
  _bin = to_int_bin[2:]
  bin_raw = '0' * (31 - len(_bin)) + _bin
  bin_str = str(sign_is) + bin_raw
  return bin_str[:32]


def floatBitsToUint(num: float) -> int:
  b = _floatBitsToUint(num)
  return int('0b' + b, 2)


def uhash11(n):
  n ^= (n << 1)
  n ^= (n >> 1)
  n *= k
  n ^= (n << 1)
  nk = n * k
  return nk


def uint_to_float(u_num: int) -> float:
  b8 = struct.pack('f', u_num)
  f32 = struct.unpack('f', b8)
  return f32[0]


uMaxFloat = uint_to_float(UINT_MAX)


def hash11(p: float):
  n = floatBitsToUint(p)
  # uint_hash = uhash11(n)
  # to_float = uint_to_float(uint_hash)
  # return uint_to_float(uint_hash) / uMaxFloat
  # return float(uhash11(n)) / float(UINT_MAX)
  return uhash11(n) / UINT_MAX


r = [hash11(random.random()) for _ in range(1000)]
# r = [hash11(float(i)) for i in range(1000)]
print(statistics.mean(r))

# hash11(1.0)

# uu = _floatBitsToUint(1.0)

# yint = int('0b' + uu, 2)
# zint = int('0b' + uu, 0)

# b8 = struct.pack('f', yint)

'''
q = int(b, 0)
b8 = struct.pack("I", q)
print(struct.unpack("f", b8)[0])
'''
x = 1
