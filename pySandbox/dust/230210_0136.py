import struct

# [Pythonで浮動小数点数floatと16進数表現の文字列を相互に変換 | note.nkmk.me](https://note.nkmk.me/python-float-hex/)


def float_to_hex(f):
  return hex(struct.unpack('>I', struct.pack('>f', f))[0])


# todo: 浮動小数点数処理する
def floatBitsToUint(num: float) -> str:
  sign_is = 1 if num < 0.0 else 0
  hex_str = float_to_hex(num)
  bin_str = bin(int(hex_str, 16))[2:]
  return str(sign_is) + bin_str


def print_result(index, num):
  if isinstance(num, int):
    u32 = f'{num:032b}' [-32:]  # オーバーフローとして
  elif isinstance(num, float):
    u32 = floatBitsToUint(num)

  row = ''
  for n, i in enumerate(u32):
    row += '|' + i if n == 1 or n == 9 else i
  result = f'[{index}]: {row}\t{num}'
  print(result)


def binary_output(num_list):
  list_index = reversed(range(len(num_list)))
  for i, n in zip(list_index, num_list[::-1]):
    print_result(i, n)


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

  binary_output(value_list)
  #h = float_to_hex(11.5625)
  #i = int(h, 16)
  #b = bin(int(h, 16))
  #bb = b[2:]
  #bbb = '0' + bb
  f2u = floatBitsToUint(11.5625)
  b = '0b' + f2u
  q = int(b, 0)
  b8 = struct.pack("I", q)
  #print(struct.unpack("f", b8)[0])

  #print(bin(h))

