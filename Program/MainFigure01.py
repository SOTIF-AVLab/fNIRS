# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 16:47:48 2022

@author: 86188
"""
import sys
import os.path
Current_Data=os.getcwd()
sys.path.append(Current_Data+"\module")
###############################load python module##########################
import numpy as np
import pandas as pd
from scipy.io import loadmat
import math
import pdb
import pandas as pd
from sklearn import linear_model 
import os
import dictionary
#coding:UTF-8
import scipy.io as scio
import seaborn as sns
import fNIRS_Index
from scipy.stats import kstest
import scipy.stats as stats
import matplotlib.pyplot as plt
import Fun_Plote

Position_Data=Current_Data+'\data'
Event_Position_Data=Position_Data+'\\'+'pedestrian'
Name_Event_People=os.listdir(Event_Position_Data)
Num_Event_People=len(Name_Event_People) 
Low_Data_All=[]
Hight_Data_All=[]
Num_All_Sample=0
NUM_CHANNEL=8
FRONTSIZE=12

    
    
for i_event_people in Name_Event_People:#####load each people data   
        People_Position_Data=Event_Position_Data+'\\'+i_event_people
        People_Data=scio.loadmat(People_Position_Data)
        Effective_data=People_Data['Effective_Data']
        Scene_num=People_Data['Scene_num']
        Scene_Num_Int=Scene_num.astype(int)[0][0]-1
        [Num_Fragment,Num_Fragment_Sample,Column]=Effective_data.shape
        Sample_Low_Num=int(Num_Fragment_Sample/2)
        Fragment_Effective_data=Effective_data[0:Scene_Num_Int,:,:] 
        [Low_Data, Hight_Data ,Num_Fragment_People]=fNIRS_Index.fun_get_scene_fNIRS_data(Fragment_Effective_data,i_event_people)
        Low_Data_All       .append(Low_Data) 
        Hight_Data_All     .append(Hight_Data) 
        Num_All_Sample=Num_All_Sample+Num_Fragment_People
[nub_index,nub_scenario,nub_channel,nub_point]=Low_Data.shape
nub_people=len(Name_Event_People)

fNITS_Data    =np.zeros([Num_All_Sample,2])
Risk_Mean_Data=np.zeros([Num_All_Sample,2])
TH_Low_DATA    =np.zeros((Num_All_Sample,nub_channel,nub_point), dtype=float)
TH_Hight_DATA  =np.zeros((Num_All_Sample,nub_channel,nub_point), dtype=float)

del nub_index,nub_scenario,nub_channel,nub_point
i_all=0
for i_nub_people in range(nub_people):
    Low_Data_All_Array  =Low_Data_All  [i_nub_people]
    Hight_Data_All_Array=Hight_Data_All[i_nub_people]
    [nub_index,nub_scenario,nub_channel,nub_point]=Low_Data_All_Array.shape

    for i_nub_scenario in range(nub_scenario):
        TH_Low_DATA   [i_all,:,:] =Low_Data_All_Array   [0,i_nub_scenario,:,:]
        TH_Hight_DATA [i_all,:,:] =Hight_Data_All_Array [0,i_nub_scenario,:,:]

        i_all=i_all+1    
    del i_nub_people, i_nub_scenario,Low_Data_All_Array,Hight_Data_All_Array
    #########################################################################################
MMTH_Column_Risk=8
Sensitive_Channel=7
for i_nub_sample in range (i_all):
    fNIRS_Low_MeanValue_Feature     =np.mean(TH_Low_DATA    [i_nub_sample,Sensitive_Channel,:])   
    fNIRS_Hight_MeanValue_Feature   =np.mean(TH_Hight_DATA  [i_nub_sample,Sensitive_Channel,:])

    fNITS_Data[i_nub_sample,0]      =fNIRS_Low_MeanValue_Feature
    fNITS_Data[i_nub_sample,1]      =fNIRS_Hight_MeanValue_Feature

    del fNIRS_Low_MeanValue_Feature, fNIRS_Hight_MeanValue_Feature
Time_Episode=600
RiskField_Data=np.zeros([Time_Episode,2])
RiskField_Data[:,0]  =TH_Low_DATA    [0,MMTH_Column_Risk,:]
RiskField_Data[:,1]  =TH_Hight_DATA   [0,MMTH_Column_Risk,:]

Fun_Plote.fun_plot_mean_value(fNITS_Data,RiskField_Data,Risk_Mean_Data)
