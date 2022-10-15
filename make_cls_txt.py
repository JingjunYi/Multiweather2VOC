import os 
from tqdm import tqdm
import numpy as np



if __name__ == '__main__':
    
    object_categories = ['sunny', 'cloudy', 'foggy', 'rainy', 'snowy']
    main_pth = 'E:/DeepLearning/multiweather/dataset/MultiWeather/VOC/ImageSets/Main'
    trainvaltxt_pth = 'E:/DeepLearning/multiweather/dataset/MultiWeather/VOC/train_map.txt'
    testtxt_pth = 'E:/DeepLearning/multiweather/dataset/MultiWeather/VOC/val_map.txt'
    
    ## Make trainval_txt
    label_trainval = []
    img_trainval = []
    with open(trainvaltxt_pth, 'r') as f:
        lines = f.readlines()
        for line in lines:
            label_line = []
            line = line.strip('\n')
            img_trainval.append(line.split('.')[0])
            for i in range(len(object_categories)):
                label_line.append(line.split(' ')[i+1])
            label_line = np.array(label_line)
            label_trainval.append(label_line)
    label_trainval = np.array(label_trainval)
    for i, cl in enumerate(object_categories):
        with open(os.path.join(main_pth, cl+'_trainval.txt'), 'a') as f:
            for j in range(len(img_trainval)):
                if int(label_trainval[j, i]) == 1:
                    f.write(img_trainval[j]+' 1\n')
                elif int(label_trainval[j, i]) == 0:
                    f.write(img_trainval[j]+' -1\n')
    ## Make test_txt
    label_test = []
    img_test = []
    with open(testtxt_pth, 'r') as f:
        lines = f.readlines()
        for line in lines:
            label_line = []
            line = line.strip('\n')
            img_test.append(line.split('.')[0])
            for i in range(len(object_categories)):
                label_line.append(line.split(' ')[i+1])
            label_line = np.array(label_line)
            label_test.append(label_line)
    label_test = np.array(label_test)
    for i, cl in enumerate(object_categories):
        with open(os.path.join(main_pth, cl+'_test.txt'), 'a') as f:
            for j in range(len(img_test)):
                if int(label_test[j, i]) == 1:
                    f.write(img_test[j]+' 1\n')
                elif int(label_test[j, i]) == 0:
                    f.write(img_test[j]+' -1\n')