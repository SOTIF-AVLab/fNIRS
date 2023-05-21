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



Position_Data=Current_Data+'\data'

All_Event_Type=['EmergentAEB','left_cut_in','right_cut_in','pedestrian']  
Position_Result='Table01_Risk.xlsx'
Position_ResultTable2='Table02_MeanValueFeature.xlsx'
Position_ResultTable3='Table03_QuantifiedCongition.xlsx'
fNIRS_Index.fun_check_exist_file(Position_Result)
fNIRS_Index.fun_check_exist_file(Position_ResultTable2)
fNIRS_Index.fun_check_exist_file(Position_ResultTable3) 
writer_Data_Table1 = pd.ExcelWriter(Position_Result)  #Create an excel sheet named hhh
writer_Data_Table2 = pd.ExcelWriter(Position_ResultTable2)  #Create an excel sheet named hhh
writer_Data_Table3 = pd.ExcelWriter(Position_ResultTable3)  #Create an excel sheet named hhh
NUM_CHANNEL=8
MAX_ITER = 100
TOLERANCE = 1e-6
Num_Event=len(All_Event_Type)
Risk_Mean_Value=np.zeros([Num_Event,4])
Name_Event=os.listdir(Position_Data)
# #########################obtain data ######################

#########################################################################
num_i_event=0
for i_event in All_Event_Type:#####load each event data
    print ('It is dealing with the data of', i_event)
    Event_Position_Data=Position_Data+'\\'+i_event
    Name_Event_People=os.listdir(Event_Position_Data)
    Num_Event_People=len(Name_Event_People) 
    Low_Data_All=[]
    Hight_Data_All=[]
    Num_All_Sample=0 
    # pdb.set_trace()       
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
        # ###############################Merge  fNIRS data##############################
    [nub_index,nub_scenario,nub_channel,nub_point]=Low_Data.shape
    time_episode=int(nub_point/100)
    nub_people=len(Name_Event_People)
    TH_T_DATA   =np.zeros([Num_All_Sample,NUM_CHANNEL*3])
    Risk_Value=np.zeros([Num_All_Sample,2])
    fNIRS_MeanValue=np.zeros([Num_All_Sample,NUM_CHANNEL*2])
    fNIRS_DictionaryValue=np.zeros([Num_All_Sample,NUM_CHANNEL*2])
    GLM_Data=np.zeros([Num_All_Sample*2,2])

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
    for i_channel in range(NUM_CHANNEL):
            # print ('################################################')
        print ('It is dealing with the data in', i_channel,'channel')
        fNIRS_Hight_DictionaryValue_Feature  =dictionary.calculate_feature(TH_Hight_DATA  [:,i_channel,:],MAX_ITER,TOLERANCE)
        fNIRS_Low_DictionaryValue_Feature    =dictionary.calculate_feature(TH_Low_DATA[:,i_channel,:],MAX_ITER,TOLERANCE)
        fNIRS_DictionaryValue[:,i_channel*2]  =fNIRS_Hight_DictionaryValue_Feature[:,0]
        fNIRS_DictionaryValue[:,i_channel*2+1]=fNIRS_Low_DictionaryValue_Feature[:,0]

        del fNIRS_Hight_DictionaryValue_Feature,fNIRS_Low_DictionaryValue_Feature

        for i_nub_sample in range (i_all):
                ###########################calculate feature form TH
            fNIRS_Hight_MeanValue_Feature=np.mean(TH_Hight_DATA  [i_nub_sample,i_channel,:])
            fNIRS_Low_MeanValue_Feature  =np.mean(TH_Low_DATA    [i_nub_sample,i_channel,:])
            fNIRS_MeanValue[i_nub_sample,i_channel*2]     =fNIRS_Hight_MeanValue_Feature
            fNIRS_MeanValue[i_nub_sample,i_channel*2+1]   =fNIRS_Low_MeanValue_Feature
            del fNIRS_Hight_MeanValue_Feature,fNIRS_Low_MeanValue_Feature

            Risk_Value[:,0]=np.mean((TH_Hight_DATA  [i_nub_sample,MMTH_Column_Risk,:]))
            Risk_Value[:,1]=np.mean((TH_Low_DATA    [i_nub_sample,MMTH_Column_Risk,:]))   

    del i_nub_sample,TH_Low_DATA,TH_Hight_DATA
    ##############################################save data####################################
    Risk_Value  =pd.DataFrame(Risk_Value)#Convert ndarray format to DataFrame
    Risk_Value.to_excel (writer_Data_Table1,sheet_name=i_event+'RiskField')
    
    fNIRS_MeanValue_df  =pd.DataFrame(fNIRS_MeanValue)#Convert ndarray format to DataFrame
    fNIRS_MeanValue_df.to_excel (writer_Data_Table2,sheet_name=i_event+'MeanValue')

    fNIRS_DictionaryValue_df=pd.DataFrame(fNIRS_DictionaryValue)#Convert ndarray format to DataFrame
    fNIRS_DictionaryValue_df.to_excel (writer_Data_Table2,sheet_name=i_event+'Dictionary')

    Risk_Mean_Value[num_i_event,0]=np.mean(TH_T_DATA[:,21])#low risk mean value
    Risk_Mean_Value[num_i_event,1]=np.mean(TH_T_DATA[:,20])#hight risk mean value
    Risk_Mean_Value[num_i_event,2]=Risk_Mean_Value[num_i_event,1]-Risk_Mean_Value[num_i_event,0]#hight risk mean value-low risk mean value
    Risk_Mean_Value[num_i_event,3]=time_episode
    Risk_Value=np.array(Risk_Value)
    if i_event=='pedestrian':
        GLM_Data[0:Num_All_Sample,0]               =Risk_Value[:,1]
        GLM_Data[Num_All_Sample:2*Num_All_Sample,0]=Risk_Value[:,0]

        GLM_Data[0:Num_All_Sample,1]               =fNIRS_MeanValue[:,15]
        GLM_Data[Num_All_Sample:2*Num_All_Sample,1]=fNIRS_MeanValue[:,14]
        GLM_Data_df=pd.DataFrame(GLM_Data)#Convert ndarray format to DataFrame
        GLM_Data_df.to_excel (writer_Data_Table3,sheet_name=i_event+'GLM_Data')

    del Risk_Value, fNIRS_MeanValue, fNIRS_DictionaryValue, time_episode
    num_i_event=num_i_event+1
Risk_Mean_Value =pd.DataFrame(Risk_Mean_Value)  
Risk_Mean_Value.to_excel (writer_Data_Table1,sheet_name='RiskFieldMean')
writer_Data_Table1.save()
writer_Data_Table2.save()
writer_Data_Table3.save()