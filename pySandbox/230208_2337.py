cell = range(32)

binary_list = [bin(9 << b >> 31)[-1] for b in cell]

