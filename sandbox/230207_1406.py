from functools import reduce

binarius = 10111001
to_decimal = reduce(lambda x, y: x + y, [
  int(b) * pow(2, n) for n, b in enumerate(str(binarius)[::-1])
])

print(to_decimal)
print(0b10111001)

