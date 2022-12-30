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
import seaborn as sns
#data = scio.loadmat(dataFile)
####################################if there are file. delete it ########################
# pdb.set_trace()
if os.path.isfile('Mean_T_DATA.xlsx'):
    os.remove('Mean_T_DATA.xlsx')
else:
    print('There are no Mean_T_DATA.xlsx')
#####################################
MAX_ITER = 100
TOLERANCE = 1e-6
NUM_CHANNEL=8
#########################obtain data position######################
Current_Data=os.getcwd()
Position_Data=Current_Data+'\data'
print ('The position of data is', Position_Data)

Name_Event=os.listdir(Position_Data)
# Num_Sample=len(Num_Data)
All_Index_Type=['TH','HB','Hbo','MMTH']
# All_Event_Type=['pedestrian','left_cut_in','right_cut_in','EmergentAEB']
All_Event_Type=['right_cut_in']
Num_Index=len(All_Index_Type)   
Num_Event=len(All_Event_Type)
Risk_Mean_Value=np.zeros([3,2*Num_Event])
writer_T_DATA = pd.ExcelWriter('Mean_T_DATA.xlsx')  #创建名称为hhh的excel表格
num_i_event=0
for i_event in All_Event_Type:#####load each event data
    Event_Position_Data=Position_Data+'\\'+i_event
    Name_Event_People=os.listdir(Event_Position_Data)
    Num_Event_People=len(Name_Event_People) 
    Low_fNIRS_All=[]
    Hight_fNIRS_All=[]
    Num_All_Sample=0
    
    for i_event_people in Name_Event_People:#####load each people data   
        People_Position_Data=Event_Position_Data+'\\'+i_event_people
        # print ('################################################')
        # print ('It is dealing with the data of', People_Position_Data)
        People_Data=scio.loadmat(People_Position_Data)
        Effective_data=People_Data['Effective_Data']
        Scene_num=People_Data['Scene_num']
        Scene_Num_Int=Scene_num.astype(int)[0][0]-1
        [Num_Fragment,Num_Fragment_Sample,Column]=Effective_data.shape
        Sample_Low_Num=int(Num_Fragment_Sample/2)
        Fragment_Effective_data=Effective_data[0:Scene_Num_Int,:,:]
        [Low_fNIRS, Hight_fNIRS,Num_Fragment_People]=fNIRS_Index.fun_get_scene_fNIRS_data(Fragment_Effective_data,Num_Index-1)
        Low_fNIRS_All       .append(Low_fNIRS) 
        Hight_fNIRS_All     .append(Hight_fNIRS) 
        Num_All_Sample=Num_All_Sample+Num_Fragment_People
    # ###############################Merge  fNIRS data##############################
    [nub_index,nub_scenario,nub_channel,nub_point]=Low_fNIRS.shape
    nub_people=len(Name_Event_People)
    #nub_scenario 每个人这个数据长度不一致，所以不能直接用
    # pdb.set_trace()
    # [nub_sample,nub_channel,nub_point]=Low_fNIRS_All_Array.shape
    TH_T_DATA   =np.zeros([Num_All_Sample,NUM_CHANNEL*2])
   

    TH_Low_DATA    =np.zeros((Num_All_Sample,nub_channel,nub_point), dtype=float)
    TH_Hight_DATA  =np.zeros((Num_All_Sample,nub_channel,nub_point), dtype=float)


    del nub_index,nub_scenario,nub_channel,nub_point
    # MMTH_Low_DATA  =np.zeros((Num_All_Sample,nub_channel,nub_point), dtype=float)
    # MMTH_Hight_DATA=np.zeros((Num_All_Sample,nub_channel,nub_point), dtype=float)

    i_all=0
    for i_nub_people in range(nub_people):
        Low_fNIRS_All_Array  =Low_fNIRS_All  [i_nub_people]
        Hight_fNIRS_All_Array=Hight_fNIRS_All[i_nub_people]
        [nub_index,nub_scenario,nub_channel,nub_point]=Low_fNIRS_All_Array.shape


        for i_nub_scenario in range(nub_scenario):
            TH_Low_DATA   [i_all,:,:] =Low_fNIRS_All_Array   [0,i_nub_scenario,:,:]
            TH_Hight_DATA [i_all,:,:] =Hight_fNIRS_All_Array [0,i_nub_scenario,:,:]
            i_all=i_all+1       
    del i_nub_people, i_nub_scenario,Low_fNIRS_All_Array,Hight_fNIRS_All_Array

    GLM_DATA=np.zeros((i_all*2,2),dtype=float)
    # pdb.set_trace()
    MMTH_Column_Risk=8
    for i_nub_sample in range (i_all):
        # print ('################################################')
        # print ('It is dealing with the data in', i_channel,'channel')
        for i_channel in range(NUM_CHANNEL):
            ###########################calculate feature form TH
            # print ('It is dealing with the data in', i_channel,'channel')
            # pdb.set_trace()
            TH_Low_Risk_Feature  =np.mean(TH_Low_DATA    [i_nub_sample,i_channel,:])
            TH_Hight_Risk_Feature=np.mean(TH_Hight_DATA  [i_nub_sample,i_channel,:])
            TH_T_DATA[i_nub_sample,i_channel*2]         =TH_Low_Risk_Feature
            TH_T_DATA[i_nub_sample,i_channel*2+1]       =TH_Hight_Risk_Feature
            del TH_Low_Risk_Feature,TH_Hight_Risk_Feature
    del i_nub_sample,TH_Low_DATA,TH_Hight_DATA
        
    num_i_event=num_i_event+1
    # ###################################save date to excel############################
    TH_T_DATA_df  =pd.DataFrame(TH_T_DATA)#将ndarray格式转换为DataFrame
    # MMTH_T_DATA_df=pd.DataFrame(MMTH_T_DATA)#将ndarray格式转换为DataFrame


    TH_T_DATA_df.to_excel  (writer_T_DATA,sheet_name=i_event+'TH')
    # MMTH_T_DATA_df.to_excel(writer_T_DATA,sheet_name=i_event+'MMTH')
    
writer_T_DATA.save()  
 # ###################################save date to excel############################
