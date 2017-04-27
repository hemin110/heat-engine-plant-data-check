# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 15:08:15 2017

@author: APAC
"""

import os
from collections import Counter
import numpy as np

# 欧式距离计算
def OsDistance(vector1, vector2):
    sqDiffVector = vector1-vector2
    sqDiffVector=sqDiffVector**2
    sqDistances = sqDiffVector.sum()
    distance = sqDistances**0.5
    return distance


def getPathList(path):
    fileList = os.listdir(path)
    f_len = len(fileList)
    print f_len
    
    osdis = []
    
    for i in range(f_len):
        all_path = os.path.join(path , fileList[i])
        tempList = []
        txt_file = open(all_path)
        for line in txt_file:
            tempList.append(float(line.replace('\n' , '')))
        txt_file.close
        # get base array
        owr = np.asarray(tempList)
        
        for j in range(f_len):
            all_path = os.path.join(path , fileList[i])
            tempList2 = []
            txt_file2 = open(all_path)
            for line in txt_file2:
                tempList2.append(float(line.replace('\n' , '')))
            txt_file2.close
            # get dest array
            nea = np.asarray(tempList2)
            
            dis = OsDistance(owr , nea)
            osdis.append(dis)
            
            
    return osdis
    '''
    output = open('result.csv', 'w')
    
    for fp in fileList:
        #获取全部路径
        all_path = os.path.join(path , fp)
        #读取对应文件
        tempList = []
        txt_file = open(all_path)
        for line in txt_file:
            tempList.append(line.replace('\n' , ''))
            
        txt_file.close
               
        #统计KV值
        dic = Counter(tempList)
        #记录文件名与个数
        length = len(dic)
        if length==1:
            output.write(fp+','+str(length)+','+str(dic.keys())+'\n')
        else:
            output.write(fp+','+str(length)+',other\n')
            
    output.close
    return True
       '''
        
        
    
if __name__ == '__main__':
    root_path = u'D:\data\电厂数据\汽轮发电机'
    osdis = getPathList(root_path)


