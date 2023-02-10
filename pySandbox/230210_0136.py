# todo: 浮動小数点数処理する
def floatBitsToUint(num: float) -> str:
  pass


def print_result(index, num):
  u32 = f'{num:032b}' [-32:]  # オーバーフローとして
  result = f'[{index}]: {u32}\t{num}'
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

