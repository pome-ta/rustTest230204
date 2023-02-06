from functools import reduce

binarius = 10111001
#bin_array = reversed([int(b) for b in str(binarius)])
bin_array = [[n,int(b)] for n, b in enumerate(str(binarius)[::-1])]

#to_decimal = 
