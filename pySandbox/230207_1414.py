from functools import reduce
from operator import add

binarius = 10111001


to_decimal = lambda bin_int: reduce(
  add, [int(b) * pow(2, n) for n, b in enumerate(str(bin_int)[::-1])])

decimal_to = to_decimal(binarius)

print(decimal_to)
print(0b10111001)

