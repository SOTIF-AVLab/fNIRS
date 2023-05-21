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
import dict
import pandas as pd
from sklearn import linear_model 
import os
#coding:UTF-8
import scipy.io as scio
import math
import os.path
import Fun_Plote
import seaborn as sns
import fNIRS_Index
from scipy.stats import kstest
import scipy.stats as stats
Position_Data=Current_Data+'\data'

All_Event_Type=['EmergentAEB','left_cut_in','right_cut_in','pedestrian']  
Position_StimulatingSound='TableStimulatingSound.xlsx'
fNIRS_Index.fun_check_exist_file(Position_StimulatingSound) 
writer_Data_Table1 = pd.ExcelWriter(Position_StimulatingSound)  #Example Create an excel table named hhh

NUM_CHANNEL=8

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
    for i_event_people in Name_Event_People:#####load each people data   
        People_Position_Data=Event_Position_Data+'\\'+i_event_people
        People_Data=scio.loadmat(People_Position_Data)
        Effective_data=People_Data['Effective_Data']
        Scene_num=People_Data['Scene_num']
        Scene_Num_Int=Scene_num.astype(int)[0][0]-1
        [Num_Fragment,Num_Fragment_Sample,Column]=Effective_data.shape
        Sample_Low_Num=int(Num_Fragment_Sample/2)
        Fragment_Effective_data=Effective_data[0:Scene_Num_Int,:,:]
        [Low_Data, Hight_Data ,Num_Fragment_People]=fNIRS_Index.fun_get_fNIRS_not_contian_stimulatingsound(Fragment_Effective_data,i_event_people)
        Low_Data_All       .append(Low_Data) 
        Hight_Data_All     .append(Hight_Data) 
        Num_All_Sample=Num_All_Sample+Num_Fragment_People
    [nub_index,nub_scenario,nub_channel,nub_point]=Low_Data.shape

    nub_people=len(Name_Event_People)
    fNIRS_MeanValue=np.zeros([Num_All_Sample,NUM_CHANNEL*2])

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

        for i_nub_sample in range (i_all):
                ###########################calculate feature form TH
            fNIRS_Hight_MeanValue_Feature=np.mean(TH_Hight_DATA  [i_nub_sample,i_channel,:])
            fNIRS_Low_MeanValue_Feature  =np.mean(TH_Low_DATA    [i_nub_sample,i_channel,:])
            fNIRS_MeanValue[i_nub_sample,i_channel*2]     =fNIRS_Hight_MeanValue_Feature
            fNIRS_MeanValue[i_nub_sample,i_channel*2+1]   =fNIRS_Low_MeanValue_Feature
            del fNIRS_Hight_MeanValue_Feature,fNIRS_Low_MeanValue_Feature

    del i_nub_sample,TH_Low_DATA,TH_Hight_DATA
    ##############################################save data####################################
    
    fNIRS_MeanValue_df  =pd.DataFrame(fNIRS_MeanValue)#Convert ndarray format to DataFrame
    fNIRS_MeanValue_df.to_excel (writer_Data_Table1,sheet_name=i_event+'MeanValue')
    del fNIRS_MeanValue
    num_i_event=num_i_event+1
   

writer_Data_Table1._save()


