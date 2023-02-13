import struct
import statistics
import random

k = 0x456789ab
UINT_MAX = 0xffffffff


def set_index(func):
  # xxx: 色々と酷いデコレータ
  def _index(_i, _n):
    _b = int(_i + _n).to_bytes(1, byteorder='big')
    return str(_b)[-2:-1]

  b_list = [_index(i, 48) if i < 10 else _index(i, 55) for i in range(32)]
  out = 'idx: '
  for n, b in enumerate(b_list):
    out += '|' + b if n == 1 or n == 9 else b

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


def number_to_binary(num) -> str:
  if isinstance(num, int):
    u32 = f'{num:032b}' [-32:]  # オーバーフローとして
  elif isinstance(num, float):
    u32 = _floatBitsToUint(num)
  return u32


def float_to_hex(f: float) -> str:
  """
   [Pythonで浮動小数点数floatと16進数表現の文字列を相互に変換 |
note.nkmk.me](https://note.nkmk.me/python-float-hex/)
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


def overflow_cast(num: int) -> int:
  _b = '0b' + number_to_binary(num)
  b2d = int(_b, 2)
  return b2d


def uhash11(n):
  n ^= (n << 1)
  n ^= (n >> 1)
  n *= k
  n ^= (n << 1)
  nk = n * k
  return nk


MAX_CAST = overflow_cast(UINT_MAX)


def hash11(p: float) -> float:
  n = floatBitsToUint(p)
  return overflow_cast(uhash11(n)) / overflow_cast(UINT_MAX)


def print_result(index: int, binary: str, num=''):
  row = ''
  for n, i in enumerate(binary):
    row += '|' + i if n == 1 or n == 9 else i
  result = f'[{index}]: {row}\t{num}'
  print(result)


@set_index
def binary_output(num_list: list):
  list_index = reversed(range(len(num_list)))
  for i, n in zip(list_index, num_list[::-1]):
    b = number_to_binary(n)
    #print_result(i, b, n)
    print_result(i, b)


r = [hash11(float(i)) for i in range(10000)]
print(statistics.mean(r))
x = 1

