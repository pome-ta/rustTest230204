import ctypes
import struct

import math
import array

k = 0x456789ab
UINT_MAX = 0xffffffff


def set_index(func):
  # xxx: 色々と酷いデコレータ
  def _index(_i, _n):
    _b = int(_i + _n).to_bytes(1, byteorder='big')
    return str(_b)[-2:-1]

  b_list = [_index(i, 48) if i < 10 else _index(i, 55) for i in range(32)]
  out = 'idx:'
  for n, b in enumerate(b_list):
    out += '|' + b if n == 1 or n == 9 else b
    out += '_' if (n + 1) % 4 == 0 else ''

  lngth = 42
  separate = ''.join(['=' for _ in range(lngth)])
  bar = ''.join(['-' for _ in range(lngth)])

  def wrapper(*args, **kwargs):
    print(separate)
    print(out)
    print(bar)
    func(*args, **kwargs)
    print(bar)
    # print(out)

  return wrapper


def print_result(index: int, binary, num=''):
  row = ''
  binary_str = f'{binary:032b}'
  for n, i in enumerate(binary_str):
    row += '|' + i if n == 1 or n == 9 else i
    row += '' if not(n) or n % 4 != 0 else '_'
  result = f'[{index}]:{row}\t{num}'
  print(result)


@set_index
def binary_output(num_list):
  list_index = reversed(range(len(num_list)))
  for i, n in zip(list_index, num_list[::-1]):
    print_result(i, n)


def uint32(s) -> int:
  _c_uint32 = ctypes.c_uint32(int(s))
  return _c_uint32.value


def float32(f) -> float:
  _c_float = ctypes.c_float(f)
  return _c_float.value


def floatBitsToUint(f: float) -> int:
  fp = struct.pack('>f', f)
  fu = struct.unpack('>I', fp)[0]
  return uint32(fu)


def uint_set(num) -> int:
  return uint32(num)


t = 110.9

num_list = [
  uint32(t),
  uint32(-t),
  floatBitsToUint(t),
  0xb ^ 9,
  0xffffffff,
  0xffffffff + uint32(t),
  floatBitsToUint(math.floor(t)),
  floatBitsToUint(math.floor(-t)),
  floatBitsToUint(11.5625),
]

uint_list = [uint_set(i) for i in num_list]

binary_output(uint_list)

x = 1

