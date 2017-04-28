# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 11:11:14 2017

@author: APAC
"""

import pandas as pd
import numpy as np
import os
from gensim.models import word2vec


def getPointName(path):
    file_name = os.listdir(path)
    name_list = []
    for fn in file_name:
        abs_path = os.path.join(path , fn)
        if os.path.isfile(abs_path):
            f = pd.read_csv(abs_path , header = None)
            nl = f[0].tolist()
            name_list.extend(nl)
    ## delete .txt
    new_nl = []
    for nl in name_list:
       new_nl.append(str(nl).replace('.txt' , ''))
       
    fin_list = []
    for nl in new_nl:
        a=[]
        a.append(nl)
        fin_list.append(a)
       
    print len(fin_list)
    return fin_list
    

def word2vecTest(list_):
    ## init param
    num_feature = 50
    min_word_count = 20
    num_workers = 2
    context = 5
    downsampling = 1e-3
    
    model = word2vec.Word2Vec(list_ ,workers = num_workers , \
                      size = num_feature , min_count = 1,\
                      window = context , sample = downsampling)
    model.save('hdc_w2c')
    
    model.init_sims(replace = True)
    print model.most_similar('rtu_yc_71',topn = 50)
    

if __name__ =='__main__':    
    folder_path = u'D:\hemin_workspace\python_code\火电厂\k-v_file'
    name_list = getPointName(folder_path)
    word2vecTest(name_list)
















