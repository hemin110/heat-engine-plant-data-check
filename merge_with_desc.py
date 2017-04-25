# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 15:42:53 2017

@author: APAC

与表进行合并，并追加上对应的描述

"""

import os

root_path =u'D:\hemin_workspace\python_code\火电厂\k-v_file'

filename = ['电气系统.csv' , '辅机系统.csv' ,'锅炉.csv' , '回热系统.csv' , '能效指标.csv' , '汽轮机.csv']

compareFile_path = u'D:\文档\火电厂项目\测点表'

c_list = []
## 读入比较文件，形成一个列表
c_path = os.path.join(compareFile_path , 'all_point.csv')
c_file = open(c_path , 'r')
for line in c_file:
    c_list.append(line)
c_file.close

##遍历每一个文件，并将后面添加上描述
'''
for name in filename:
    #file_path_in = os.path.join(root_path , name)
    o_name = 'new_'+name
    #o_file = open(os.path.join(root_path , o_name))
    o_file = root_path+'\\'+o_name
    file_path_in = root_path+'\\'+name
    
    i_file = open(file_path_in , 'r')
    for line in i_file:
        for tmp in c_list:
            if tmp.split(',')[0] == line.split(',')[0].split('.')[0]:
                o_file.write(line+','+tmp)
    i_file.close
    o_file.close
'''   
file_path_in = u'D:\hemin_workspace\python_code\火电厂\k-v_file\汽轮机.csv'


o_file = open('new_ql.csv' , 'w')
i_file = open(file_path_in , 'r')
for line in i_file:
    for tmp in c_list:
        if tmp.split(',')[0] in line.split(',')[0]:
            o_file.write(line.replace('\n' , '')+','+tmp.split(',')[1] +','+tmp.split(',')[2]+'\n')
i_file.close
o_file.close
















