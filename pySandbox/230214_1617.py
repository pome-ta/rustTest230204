import ctypes
import struct
import array


def uint32(num: int) -> int:
  c_uint32 = ctypes.c_uint32(abs(num))
  return c_uint32.value


num_max = 0xffff_ffff

f2u = ctypes.c_uint32(num_max)

#sp = struct.pack('I', num_max)
sp = struct.pack('I', f2u.value)

record_size = struct.calcsize('I')

