# Reads an image from disk and scales and crops to match a target resolution and aspect ratio.
import os
from scipy import misc

# Specifies which is the largest size on any side of the picture. (Caters for portrait and landscape)
FIXED_MAX_DIMENSION = 500.0

# For each allocated class, save pictures in their containing class folder.
for class_ in ['desconegut', 'mercat_independencia', 'mnactec']:
    path = '../../pictures/' + class_ + '/'
    savedir = '../../resized/' + class_ + '/'

    # Create a list describing only the files inside a the specified path. (Omits filesystem folders and files)
    flist = []
    for (dirpath, dirnames, filenames) in os.walk(path):    # Crawl through directories,
        flist.extend(filenames)                             # to find the full file paths.
        break

    for filename in flist:                                  # With each file's name,
        pic = misc.imread(path + filename)                  # decode the file contents,
        pic_resized = misc.imresize(pic, FIXED_MAX_DIMENSION / max(pic.shape), interp='nearest', mode=None) # scale,
        misc.imsave(savedir + filename, pic_resized)        # and save into a new folder.
