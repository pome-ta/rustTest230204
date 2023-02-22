import numpy as np
from PIL import Image as ImageP


UINT_MAX = 0xffffffff

sq_size = 64
RGB_SIZE = 256
color_ch = 3

length_size = sq_size * sq_size * color_ch

xyz = np.arange(0, length_size, dtype=np.uint8).reshape(sq_size, sq_size, color_ch)
#xyz = np.arange(0, 10)
zoro_uint8 = np.zeros((sq_size, sq_size, 3), dtype=np.uint8)


imgp = ImageP.fromarray(xyz)
_ = 1
