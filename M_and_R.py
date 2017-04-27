# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 09:46:08 2017

@author: APAC
"""

import os
from collections import Counter
import numpy as np

def getPathList(path):
    fileList = os.listdir(path)
    
    output = open('resultms.csv', 'w')
    
    for fp in fileList:
        #获取全部路径
        all_path = os.path.join(path , fp)
        #读取对应文件
        mysum = []
        txt_file = open(all_path)
        for line in txt_file:
            mysum.append(float(line.replace('\n' , '')))
            
        m =  np.mean(mysum)
        s = np.std(mysum)
        txt_file.close
               
        #统计KV值
        dic = Counter(mysum)
        #记录文件名与个数
        length = len(dic)
        
        output.write(fp+','+str(length)+','+str(m)+','+str(s)+'\n')
        
        
        '''
        if length==1:
            output.write(fp+','+str(length)+','+str(dic.keys())+'\n')
        else:
            output.write(fp+','+str(length)+',other\n')
            
        '''
            
    output.close
    return True
        
        
        
    
if __name__ == '__main__':
    root_path = u'D:\data\电厂数据\汽轮发电机'
    getPathList(root_path)
    