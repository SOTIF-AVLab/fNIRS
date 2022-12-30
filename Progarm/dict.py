# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 16:47:48 2022

@author: 86188
"""

import numpy as np
import pandas as pd
from scipy.io import loadmat
from PIL import Image
import math
import pdb
from sklearn import linear_model 

def dict_update(X, d, a, n_components):
    """
    使用KSVD更新字典的过程
    """
    #pdb.set_trace()
    for i in range(n_components):
        index = np.nonzero(a[i, :])[0]
        if len(index) == 0:
            continue
        # 更新第i列
        d[:, i] = 0
        # 计算误差矩阵
        r = (X - np.dot(d, a))[:, index]
        # 利用svd的方法，来求解更新字典和稀疏系数矩阵
        u, s, v = np.linalg.svd(r, full_matrices=False)
        # 使用左奇异矩阵的第0列更新字典
        d[:, i] = u[:, 0]
        # 使用第0个奇异值和右奇异矩阵的第0行的乘积更新稀疏系数矩阵
        for j,k in enumerate(index):
            a[i, k] = s[0] * v[0, j]
    return d, a
def calculate_feature(Low_fNIRS,MAX_ITER,TOLERANCE):
    Low_Data_u, Low_Data_s, Low_Data_v = np.linalg.svd(Low_fNIRS)
    n_comp = 1
    Low_dict_data = Low_Data_u[:, :n_comp]
    ##############################################################
    Low_dictionary = Low_dict_data
    Low_X = Low_fNIRS
    [Num_Scene,Num_Point]=Low_X.shape
    for i in range(MAX_ITER):
        # 稀疏编码
        Low_a = linear_model.orthogonal_mp(Low_dictionary, Low_X)# inversion
        Low_a=np.reshape(Low_a,(1,Num_Point))
        Low_lamba1=np.random.random()
        Low_lamba2=np.random.random()
        Low_lamba2=0.5*Low_lamba2
        Low_a11=np.linalg.norm(Low_a,ord=1)#L1  norm
        Low_a12=np.linalg.norm(Low_a,ord=None)#L2 norm
        Low_e11 = np.linalg.norm(Low_X -np.dot(Low_dictionary, Low_a))
        Low_e11=0.5*Low_e11
        Low_e=Low_e11+Low_lamba1*Low_a11+Low_lamba2*Low_a12*Low_a12
        #print(Low_e)
        if Low_e < TOLERANCE:
            break
        Low_dictionary,Low_a=dict_update(Low_X,Low_dictionary,Low_a,n_comp)
    return Low_dictionary

def calculate_mean(Data,MAX_SAMPLE):
    Data_Mean=np.zeros((MAX_SAMPLE,1), dtype=float)
    for i in range(MAX_SAMPLE):  
            # print(Data[i,:]) 
            # pdb.set_trace()
            Data_Mean[i,0]=np.average(Data[i,:])# 按行求均值
    return Data_Mean