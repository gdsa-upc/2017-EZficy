# Reads an image from disk and scales and crops to match a target resolution and aspect ratio.
import os
from scipy import misc

FIXED_MAX_DIMENSION = 500.0

for class_ in ['desconegut', 'mercat_independencia', 'mnactec']:
    path = '../../pictures/' + class_ + '/'
    savedir = '../../resized/' + class_ + '/'

    flist = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        flist.extend(filenames)
        break

    for filename in flist:
        pic = misc.imread(path + filename)
        pic_resized = misc.imresize(pic, FIXED_MAX_DIMENSION / max(pic.shape), interp='nearest', mode=None)
        misc.imsave(savedir + filename, pic_resized)
