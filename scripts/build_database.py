import os
import glob
from utils.params import get_params

def listdir_nohidden(path):
    return glob.glob(os.path.join(path, '*'))

def build_database(params):
    # List images
    image_names = listdir_nohidden(os.path.join(params['root'],params['database'],params['split'],'images'))

    # File to be saved
    file = open(os.path.join(params['root'],params['root_save'],params['image_lists'],params['split'] + '.txt'),'w')

    # Save image list to disk
    for imname in image_names:
        file.write(imname.split('/')[-1] + "\n")
    file.close()


if __name__=="__main__":

    params = get_params()

    print ('Building validation set...')
    params['split'] = 'val'
    
    # Build image list for validation set
    build_database(params)
    
    # Switch to training set
    print ('Building training set...')
    params['split'] = 'train'
    
    # Build image list for training set
    build_database(params)

    # Switch to test set
    print ('Building testing set...')
    params['split'] = 'test'

    # Build image list for training set
    build_database(params)

    print ('Database construction complete!')