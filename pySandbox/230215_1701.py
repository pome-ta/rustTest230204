import ctypes
import struct

import math
import array


def uint32(s) -> int:
  _c_uint32 = ctypes.c_uint32(int(s))
  return _c_uint32.value

def float32(f)->float:
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


for n, u in enumerate(uint_list[::-1]):
  sf32 = f'{u:032b}'
  print(len(uint_list) - n - 1, sf32)




x = 1

