import os
from tqdm import tqdm
import numpy as np
from xml.dom.minidom import parse 
import xml.dom.minidom
import torch

'''
<annotation>
    <object>
		<name>dog</name>
		<pose>Left</pose>
		<truncated>1</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>48</xmin>
			<ymin>240</ymin>
			<xmax>195</xmax>
			<ymax>371</ymax>
		</bndbox>
	</object>
</annotation>
'''
# category_info = {'aeroplane':0, 'bicycle':1, 'bird':2, 'boat':3, 'bottle':4,
#                  'bus':5, 'car':6, 'cat':7, 'chair':8, 'cow':9,
#                  'diningtable':10, 'dog':11, 'horse':12, 'motorbike':13, 'person':14,
#                  'pottedplant':15, 'sheep':16, 'sofa':17, 'train':18, 'tvmonitor':19}
category_info = {'sunny':0, 'cloudy':1, 'foggy':2, 'rainy':3, 'snowy':4}
category = ['sunny', 'cloudy', 'foggy', 'rainy', 'snowy']


if __name__ == '__main__':
    
    # label_file = 'E:/DeepLearning/multiweather/supervised/voc/VOCdevkit/VOC2007/Annotations/000001.xml'
    # label_vector = np.zeros(20)
    # DOMTree = xml.dom.minidom.parse(label_file)
    # root = DOMTree.documentElement
    # objects = root.getElementsByTagName('object')  
    # for obj in objects:
    #     if (obj.getElementsByTagName('difficult')[0].firstChild.data) == '1':
    #         continue
    #     tag = obj.getElementsByTagName('name')[0].firstChild.data.lower()
    #     label_vector[int(category_info[tag])] = 1.0
    # print(label_vector)
    
    train_txt = 'train_map_gauss.txt'
    val_txt = 'val_map_gauss.txt'
    label_dir = 'Annotations_gauss'
    
    with open(train_txt, 'r') as f:
        lines = f.readlines()
        for line in lines:
            labels = []
            img_name = line.split(' ')[0].split('.')[0]
            for i in range(5):
                labels.append(float(line.split(' ')[i + 1].strip('\n')) / 100.0)
            lables = torch.from_numpy(np.array(labels))
            with open(os.path.join(label_dir, img_name + '.xml'), 'w') as f1:
                f1.write('<annotation>')
                f1.write('\n')
                for i, label in enumerate(labels):
                    f1.write('	<object>')
                    f1.write('\n')
                    f1.write('		<name>' + category[i] + '</name>')
                    f1.write('\n')
                    f1.write('		<gauss>' + str(label) + '</gauss>')
                    f1.write('\n')
                    f1.write('		<pose>Left</pose>')
                    f1.write('\n')
                    f1.write('		<truncated>1</truncated>')
                    f1.write('\n')
                    f1.write('		<difficult>0</difficult>')
                    f1.write('\n')
                    f1.write('		<bndbox>')
                    f1.write('\n')
                    f1.write('			<xmin>0</xmin>')
                    f1.write('\n')
                    f1.write('			<ymin>0</ymin>')
                    f1.write('\n')
                    f1.write('			<xmax>0</xmax>')
                    f1.write('\n')
                    f1.write('			<ymax>0</ymax>')
                    f1.write('\n')
                    f1.write('		</bndbox>')
                    f1.write('\n')
                    f1.write('	</object>')
                    f1.write('\n')
                f1.write('</annotation>')
                        
            
    with open(val_txt, 'r') as f:
        lines = f.readlines()
        for line in lines:
            labels = []
            img_name = line.split(' ')[0].split('.')[0]
            for i in range(5):
                labels.append(float(line.split(' ')[i + 1].strip('\n')) / 100.0)
            with open(os.path.join(label_dir, img_name + '.xml'), 'w') as f1:
                f1.write('<annotation>')
                f1.write('\n')
                for i, label in enumerate(labels):
                    f1.write('	<object>')
                    f1.write('\n')
                    f1.write('		<name>' + category[i] + '</name>')
                    f1.write('\n')
                    f1.write('		<gauss>' + str(label) + '</gauss>')
                    f1.write('\n')
                    f1.write('		<pose>Left</pose>')
                    f1.write('\n')
                    f1.write('		<truncated>1</truncated>')
                    f1.write('\n')
                    f1.write('		<difficult>0</difficult>')
                    f1.write('\n')
                    f1.write('		<bndbox>')
                    f1.write('\n')
                    f1.write('			<xmin>0</xmin>')
                    f1.write('\n')
                    f1.write('			<ymin>0</ymin>')
                    f1.write('\n')
                    f1.write('			<xmax>0</xmax>')
                    f1.write('\n')
                    f1.write('			<ymax>0</ymax>')
                    f1.write('\n')
                    f1.write('		</bndbox>')
                    f1.write('\n')
                    f1.write('	</object>')
                    f1.write('\n')
                f1.write('</annotation>')