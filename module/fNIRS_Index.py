# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 16:47:48 2022

@author: 86188
"""
###############################load python module##########################
import numpy as np
import pandas as pd
from scipy.io import loadmat
from PIL import Image
import math
import pdb
import dict
import pandas as pd
from sklearn import linear_model 
import os
#coding:UTF-8
import scipy.io as scio
import math
import os.path
import fNIRS_Index
import Fun_Plote
NUM_CHANNEL=8
Colimn_Risk=18
Column_Risk_Add=NUM_CHANNEL+2
################################################################################
def fun_check_contian_sound(Data_First,Num_scene,Num_people):#Check if the data contains sound
    if Data_First<1:
        Flag_Sound=False
    else:
        Flag_Sound=False
    return Flag_Sound
########################################################################
def fun_get_scene_fNIRS_data(Fragment_Effective_data,Num_people):
    Num_Index=1
    [Num_i_Fragment,Num_Fragment_Sample,Column]=Fragment_Effective_data.shape
    Sample_Low_Num=int(Num_Fragment_Sample/2)
    Low_fNIRS   =np.zeros([Num_Index,Num_i_Fragment,Column_Risk_Add,Sample_Low_Num])
    Hight_fNIRS =np.zeros([Num_Index,Num_i_Fragment,Column_Risk_Add,Sample_Low_Num])
    for i_fragment in range(Num_i_Fragment):#####load each people data
        for i_sample in range(Sample_Low_Num):
            for i_channl in range (NUM_CHANNEL):
                    ####################the first is TH index
                Low_fNIRS  [0,i_fragment,i_channl,i_sample] =(Fragment_Effective_data[i_fragment,i_sample               ,i_channl*2+21]-Fragment_Effective_data[i_fragment,i_sample               ,i_channl*2+20])/math.sqrt(2)
                Hight_fNIRS[0,i_fragment,i_channl,i_sample] =(Fragment_Effective_data[i_fragment,i_sample+Sample_Low_Num,i_channl*2+21]-Fragment_Effective_data[i_fragment,i_sample+Sample_Low_Num,i_channl*2+20])/math.sqrt(2)
                ##################The last column (column nine) is the risk field####################################   
            Low_fNIRS  [0,i_fragment,8,i_sample] = Fragment_Effective_data[i_fragment,i_sample               ,Colimn_Risk]
            Hight_fNIRS[0,i_fragment,8,i_sample] = Fragment_Effective_data[i_fragment,i_sample+Sample_Low_Num,Colimn_Risk]
    return Low_fNIRS, Hight_fNIRS,Num_i_Fragment

def fun_check_exist_file(Position_Result):#Check if file exists
    if os.path.isfile(Position_Result):
        os.remove(Position_Result)
    else:
        print('The result file does not exist and does need not to remove it')

def fun_get_fNIRS_not_contian_stimulatingsound(Fragment_Effective_data,Num_people):
    Num_Index=1
    [Num_i_Fragment,Num_Fragment_Sample,Column]=Fragment_Effective_data.shape
    Sample_Low_Num=int(Num_Fragment_Sample/2)
    Low_fNIRS   =np.zeros([Num_Index,Num_i_Fragment,Column_Risk_Add,Sample_Low_Num])
    Hight_fNIRS =np.zeros([Num_Index,Num_i_Fragment,Column_Risk_Add,Sample_Low_Num])
    Num_Valid_Data=Num_i_Fragment
    for i_fragment in range(Num_i_Fragment):#####load each people data
         if fun_check_contian_sound (Fragment_Effective_data[i_fragment,0,36],i_fragment,Num_people):
             Num_Valid_Data=Num_Valid_Data-1
         else:
             Num_Valid_Data=Num_Valid_Data
    Low_fNIRS   =np.zeros([Num_Index,Num_Valid_Data,Column_Risk_Add,Sample_Low_Num])
    Hight_fNIRS =np.zeros([Num_Index,Num_Valid_Data,Column_Risk_Add,Sample_Low_Num])   
    i_Num_Valid_Data=0
    for i_fragment in range(Num_i_Fragment):#####load each people data
        if fun_check_contian_sound (Fragment_Effective_data[i_fragment,0,36],i_fragment,Num_people):#Delete data if it contains sound data
            i_Num_Valid_Data=i_Num_Valid_Data
        else:
            for i_sample in range(Sample_Low_Num):
                for i_channl in range (NUM_CHANNEL):
                        ####################the first is TH index
                        Low_fNIRS  [0,i_Num_Valid_Data,i_channl,i_sample] =(Fragment_Effective_data[i_fragment,i_sample               ,i_channl*2+21]-Fragment_Effective_data[i_fragment,i_sample               ,i_channl*2+20])/math.sqrt(2)
                        Hight_fNIRS[0,i_Num_Valid_Data,i_channl,i_sample] =(Fragment_Effective_data[i_fragment,i_sample+Sample_Low_Num,i_channl*2+21]-Fragment_Effective_data[i_fragment,i_sample+Sample_Low_Num,i_channl*2+20])/math.sqrt(2)
                ##################The last column (column nine) is the risk field####################################
                Colimn_Risk=18
                ####################the first is TH index
                Low_fNIRS  [0,i_Num_Valid_Data,8,i_sample] = Fragment_Effective_data[i_fragment,i_sample               ,Colimn_Risk]
                Hight_fNIRS[0,i_Num_Valid_Data,8,i_sample] = Fragment_Effective_data[i_fragment,i_sample+Sample_Low_Num,Colimn_Risk]
            i_Num_Valid_Data=i_Num_Valid_Data+1
    return Low_fNIRS, Hight_fNIRS,Num_Valid_Data
