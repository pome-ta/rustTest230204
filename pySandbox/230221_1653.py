import numpy as np
from PIL import Image as ImageP


UINT_MAX = 0xffffffff

sq_size = 8
RGB_SIZE = 256

# xyz = np.arange(0, RGB_SIZE, RGB_SIZE/sq_size).reshape(sq_size, sq_size, 3)
xyz = np.arange(0, 10)
zoro_uint8 = np.zeros((sq_size, sq_size, 3), dtype=np.uint8)

_ = 1
