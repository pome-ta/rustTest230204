def print_result(index, num):
  result = f'[{index}]: {num:032b}\t{num}'
  print(result)


def binary_output(num_list):
  list_index = reversed(range(len(num_list)))
  for i, n in zip(list_index, num_list[::-1]):
    print_result(i, n)


if __name__ == '__main__':
  u_time = 110

  value_list = [u_time, 0xb, 9, 0xb ^ 9]
  binary_output(value_list)

