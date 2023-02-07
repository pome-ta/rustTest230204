from functools import reduce
from operator import add

binarius = 10111001
to_decimal = reduce(
  add, [int(b) * pow(2, n) for n, b in enumerate(str(binarius)[::-1])])

print(to_decimal)
print(0b10111001)

