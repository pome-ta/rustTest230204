import struct


def float_to_hex(f: float) -> str:
  """
  [Pythonで浮動小数点数floatと16進数表現の文字列を相互に変換 | note.nkmk.me](https://note.nkmk.me/python-float-hex/)
  """
  return hex(struct.unpack('>I', struct.pack('>f', f))[0])


# todo: 浮動小数点数処理する
def floatBitsToUint(num: float) -> str:
  sign_is = 1 if num < 0.0 else 0
  hex_str = float_to_hex(num)
  bin_str = bin(int(hex_str, 16))[2:]
  return str(sign_is) + bin_str


def number_to_binary(num) -> str:
  if isinstance(num, int):
    u32 = f'{num:032b}' [-32:]  # オーバーフローとして
  elif isinstance(num, float):
    u32 = floatBitsToUint(num)
  return u32


def print_result(index: int, binary: str, num):
  row = ''
  for n, i in enumerate(binary):
    row += '|' + i if n == 1 or n == 9 else i
  result = f'[{index}]: {row}\t{num}'
  print(result)


def binary_output(num_list):
  list_index = reversed(range(len(num_list)))
  for i, n in zip(list_index, num_list[::-1]):
    b = number_to_binary(n)
    print_result(i, b, n)


def set_index():
  def _index(_i, _n):
    _b = int(_i + _n).to_bytes(1, byteorder='big')
    return str(_b)[-2:-1]

  b_list = [_index(i, 48) if i < 10 else _index(i, 55) for i in range(32)]
  out = 'idx: '
  for n, b in enumerate(b_list):
    out += '|' + b if n == 1 or n == 9 else b
  print(out)


if __name__ == '__main__':
  u_time = 110

  value_list = [
    u_time,
    0xb,
    9,
    0xb ^ 9,
    0xffffffff,
    0xffffffff + u_time,
    11.5625,
  ]
  set_index()
  binary_output(value_list)
  set_index()

