import os
import glob

for j in range(1,8):
    path = glob.glob("images//train//*_{}.jpg".format(j))
    for i in path:
        os.remove(i)
