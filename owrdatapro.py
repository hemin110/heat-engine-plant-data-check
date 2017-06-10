# -*- coding: utf-8 -*-
"""
Created on Thu Jun 08 11:14:26 2017

@author: APAC
"""

import pandas as pd
import time
import numpy as np
from pandas import DataFrame


#0x数据转x
def datachange(newtime):
    #两个都是0的时候000
    if list(newtime.split(' ')[0].split('/')[1])[0]=='0' and list(newtime.split(' ')[0].split('/')[2])[0]=='0' and list(newtime.split(' ')[1].split(':')[0])[0]=='0' :
        return newtime[:5]+newtime[6:8]+newtime[9:11]+newtime[12:]
    #前者是0 011
    if list(newtime.split(' ')[0].split('/')[1])[0]=='0' and list(newtime.split(' ')[0].split('/')[2])[0]!='0':
        return newtime[:5]+newtime[6:]
    #后者是101
    if list(newtime.split(' ')[0].split('/')[1])[0]!='0' and list(newtime.split(' ')[0].split('/')[2])[0]=='0':
        return newtime[:8]+newtime[9:]
    #100
    if list(newtime.split(' ')[0].split('/')[1])[0]!='0' and list(newtime.split(' ')[0].split('/')[2])[0]=='0' and list(newtime.split(' ')[1].split(':')[0])[0]=='0' :
        pass
    #010
    if list(newtime.split(' ')[0].split('/')[1])[0]=='0' and list(newtime.split(' ')[0].split('/')[2])[0]!='0' and list(newtime.split(' ')[1].split(':')[0])[0]=='0' :
        pass
    #001
    if list(newtime.split(' ')[0].split('/')[1])[0]=='0' and list(newtime.split(' ')[0].split('/')[2])[0]=='0' and list(newtime.split(' ')[1].split(':')[0])[0]!='0' :
        pass
    #110
    if list(newtime.split(' ')[0].split('/')[1])[0]!='0' and list(newtime.split(' ')[0].split('/')[2])[0]!='0' and list(newtime.split(' ')[1].split(':')[0])[0]=='0' :
        pass
    #111
    if list(newtime.split(' ')[0].split('/')[1])[0]!='0' and list(newtime.split(' ')[0].split('/')[2])[0]!='0' and list(newtime.split(' ')[1].split(':')[0])[0]!='0' :
        return newtime
#读取需要的文本，以单个文本为例
o_path = r"D:\hemin_workspace\final_project\package\test\1RTUAI004.txt"
data = pd.read_table(o_path , header = None)
#读取表单中的起讫时间
beg_time = "2017/3/1 0:00:00"
end_time = "2017/3/1 0:02:00"
#读取表单中的时间间隔
sep_time = 5
#读取填充null的方法
fill_method = "liner"
#时间转换
beg_temp_time = time.strptime(beg_time , "%Y/%m/%d %H:%M:%S")
end_temp_time = time.strptime(end_time , "%Y/%m/%d %H:%M:%S")

beg_form_time = time.strftime("%Y/%m/%d %H:%M:%S", beg_temp_time)
end_form_time = time.strftime("%Y/%m/%d %H:%M:%S", end_temp_time)

time_beg_pri = time.mktime(beg_temp_time)
time_end_pri = time.mktime(end_temp_time)
#样本的数量
sample_num = int(time_end_pri) - int(time_beg_pri)+1
#循环遍历
record_bi = 0
record_ei = 0
read_time = data[0][0]
base_temp_time = time.strptime(read_time , "%Y/%m/%d %H:%M:%S")
#临时时间戳
temp_print = time.mktime(base_temp_time)
#比较时间戳
et = abs(int(temp_print)-int(time_end_pri))
bt = abs(int(temp_print)-int(time_beg_pri))
    
for i in range(200):
    
    tmpet = abs(int(time.mktime(time.strptime(data[0][i] , "%Y/%m/%d %H:%M:%S")))-int(time_end_pri))
    tmpbt = abs(int(time.mktime(time.strptime(data[0][i] , "%Y/%m/%d %H:%M:%S")))-int(time_beg_pri))
    if tmpet<=et:
        record_ei = i
        et = tmpet
    if tmpbt<bt:
        record_bi = i
        bt = tmpbt
        
print record_bi
print record_ei
#绘制新的表格
#此时需要注意，每个文档中的数据不同，长度以及质量都不尽相同
time_point = []
for i in range(int(time_beg_pri) , int(time_end_pri)+1):
    beg = time.localtime(i)
    #时间戳转字符串
    print_time = time.strftime('%Y/%m/%d %H:%M:%S',beg)
    time_point.append([datachange(print_time)])
#print time_point
time_data = np.asarray(time_point)
df_time = DataFrame(time_data , columns = ['time'] )#
#原始数据
ori_data = np.asarray(data)[:record_ei,:]
df_ori = DataFrame(ori_data , columns = ['time' , 'value'])#
#合并dataframe
final_data = pd.merge(df_time ,  df_ori , how = 'left')
print final_data





    

    
    




