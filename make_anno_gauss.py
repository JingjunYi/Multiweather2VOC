import os
from tqdm import tqdm



if __name__ == '__main__':
    
    origin_train_txt = 'train_map_gauss.txt'
    origin_val_txt = 'val_map_gauss.txt'
    new_train_txt = 'ImageSets/Main/trainval_gauss.txt'
    new_val_txt = 'ImageSets/Main/test_gauss.txt'
    
    img_name_train = []
    with open(origin_train_txt, 'r') as f:
        lines = f.readlines()
        for line in lines:
            img_name = line.split(' ')[0].split('.')[0]
            img_name_train.append(img_name)
            
    img_name_val = []
    with open(origin_val_txt, 'r') as f:
        lines = f.readlines()
        for line in lines:
            img_name = line.split(' ')[0].split('.')[0]
            img_name_val.append(img_name)
    
    with open(new_train_txt, 'w') as f:
        for i, img_name in enumerate(img_name_train):
            f.write(img_name)
            if i < len(img_name_train) - 1:
                f.write('\n')
    
    with open(new_val_txt, 'w') as f:
        for i, img_name in enumerate(img_name_val):
            f.write(img_name)
            if i < len(img_name_val) - 1:
                f.write('\n')