# todo: 2進数を10進数へ愚直に出す

from functools import reduce

binarius = 10111001
# bin_array = reversed([int(b) for b in str(binarius)])
# bin_array = [[n,int(b)] for n, b in enumerate(str(binarius)[::-1])]

to_decimal = 0

for n, b in enumerate(str(binarius)[::-1]):
  print(pow(2, n))
  to_decimal += int(b) * pow(2, n)

print(to_decimal)
print(0b10111001)
