import ctypes
import struct
import array


def uint32(s: int) -> int:
  c_uint32 = ctypes.c_uint32(s)
  return c_uint32.value


def floatBitsToUint(f: float) -> int:
  fp = struct.pack('>f', f)
  fu = struct.unpack('>I', fp)[0]
  return uint32(fu)


num_max = 0xffff_ffff

f2u = ctypes.c_uint32(num_max)
uu = uint32(110)
ux = uint32(num_max)
# sp = struct.pack('I', num_max)
sp = struct.pack('>I', uu)
# sp = struct.pack('>I', ux)

record_size = struct.calcsize('I')

fup = floatBitsToUint(110.0)
fun = floatBitsToUint(-110.0)


x = 1

