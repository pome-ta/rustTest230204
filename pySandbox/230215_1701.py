import ctypes
import struct

import math
import array


k = 0x456789ab
UINT_MAX = 0xffffffff


def reference_grid(div_chrs: str,  head_str: str = '') -> str:
  row = head_str
  for n, c in enumerate(div_chrs):
    row += '|' + c if n == 1 or n == 9 else c
    row += '_' if n and (n + 1) % 4 == 0 else ''
  return row[:-1]  # xxx: お尻`_` 切り捨て


def set_index(func):
  # xxx: 色々と酷いデコレータ、そしてlambda
  to_0v = (lambda n, j: int(n + j).to_bytes(1, byteorder='big'))
  repeat_chrs = (lambda chr, l: ''.join(chr for _ in range(l)))

  zoro2v = [to_0v(i, 48).decode('utf8') if i <
            10 else to_0v(i, 55).decode('utf8') for i in range(32)]
  hd = 'inx :'
  lngth = 48

  def wrapper(*args, **kwargs):
    output_list = [
        repeat_chrs('=', lngth),
        reference_grid(zoro2v, hd),
        repeat_chrs('-', lngth),
        func(*args, **kwargs),
        repeat_chrs('-', lngth),
    ]
    return '\n'.join(output_list)
  return wrapper


def print_result(index: int, binary, num=''):
  hd = f'[{index}] :'
  binary_str = f'{binary:032b}'
  row = reference_grid(binary_str)
  result = f'{hd}{row}\t{num}'
  return result


@set_index
def binary_output(num_list):
  output_list: list = []
  list_index = reversed(range(len(num_list)))
  for i, n in zip(list_index, num_list[::-1]):
    output_list.append(print_result(i, n))
  return '\n'.join(output_list)


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

hoge = binary_output(uint_list)

print(hoge)
x = 1
