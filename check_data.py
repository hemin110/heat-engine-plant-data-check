# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 21:59:57 2017

@author: APAC
"""

import os
from collections import Counter


def getPathList(path):
    fileList = os.listdir(path)
    
    output = open('锅炉.csv', 'w')
    
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
        
        
        
    
if __name__ == '__main__':
    root_path = u'D:\data\电厂数据\锅炉'
    getPathList(root_path)
    