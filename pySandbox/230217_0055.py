import ctypes
import struct
import statistics
import cProfile

# import matplotlib.pyplot as plt

k = 0x456789ab
UINT_MAX = 0xffffffff


def reference_grid(div_chrs: str, head_str: str = '') -> str:
  row = head_str
  for n, c in enumerate(div_chrs):
    row += '|' + c if n == 1 or n == 9 else c
    row += '_' if n and (n + 1) % 4 == 0 else ''
  return row[:-1]  # xxx: お尻`_` 切り捨て


def set_index(func):
  # xxx: 色々と酷いデコレータ、そしてlambda
  to_0v = (lambda n, j: int(n + j).to_bytes(1,
           byteorder='big').decode(encoding='utf8'))
  repeat_chrs = (lambda chr, l: ''.join(chr for _ in range(l)))

  zoro2v = [to_0v(i, 48) if i < 10 else to_0v(i, 55) for i in range(32)]
  hd = 'inx:'
  lngth = 46

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
  hd = f'[{index}]:'
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
  # xxx: 負の値処理するかどうか？
  _s = s if s > 0 else 0
  _c_uint32 = ctypes.c_uint32(int(_s))
  return _c_uint32.value


def float32(f) -> float:
  _c_float = ctypes.c_float(f)
  return _c_float.value


fu_pack = struct.Struct('>f')
fu_unpack = struct.Struct('>I')


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


def run():
  r = [hash11(float(i)) for i in range(10000)]
  # plt.hist(r)
  # plt.show()
  # print('平均:', statistics.mean(r))
  # print('標準偏差:', statistics.stdev(r))


cProfile.run('run()', sort=1)

x = 1
