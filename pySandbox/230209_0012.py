for n, i in enumerate(range(512)):
  b = int(i).to_bytes(2, byteorder='big')
  print(f'{n:03}: {b}')
