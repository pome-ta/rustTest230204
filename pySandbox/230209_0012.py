for n, i in enumerate(range(256)):
  b = int(i).to_bytes(1, byteorder='big')
  print(f'{n:03}: {b}')
