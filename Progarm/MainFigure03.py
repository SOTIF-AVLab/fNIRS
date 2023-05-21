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
import math
import pdb
from sklearn import linear_model 
import os
#coding:UTF-8
import scipy.io as scio
import math
import os.path
import Fun_Plote
import fNIRS_Index
import matplotlib.pyplot as plt
import Fun_plot_sex_driver  as fpr
import Fun_Get_ParticipantsInformation as fgpi
Position_Data=Current_Data+'\data'
All_Index_Type=['TH','HB','Hbo']
All_Event_Type=['pedestrian','left_cut_in','right_cut_in','EmergentAEB']
Num_Index=len(All_Index_Type)   
Num_Event=len(All_Event_Type)
Num_People=20
Num_Channel=10
Low_Index_Average_Value  =np.zeros([Num_Event,Num_People,Num_Index,Num_Channel])
Hight_Index_Average_Value=np.zeros([Num_Event,Num_People,Num_Index,Num_Channel])
##########################################################################################
Low_fNIRS_All=[]
Hight_fNIRS_All=[]
Num_All_Sample=0 
##############################Calculate mean value#############################################
def fun_calculate_mean_value(Data_fNIRS):
    [Num_Index_MV,Num_Scene_MV,Num_Channel_MV,Num_Channel_Sample]=Data_fNIRS.shape 
    Mean_Value=np.zeros([Num_Index_MV,Num_Channel_MV])
    for i_Num_Index_MV in range(Num_Index_MV):
        for i_Num_Channel_MV in range(Num_Channel_MV):
                Mean_Value[i_Num_Index_MV,i_Num_Channel_MV]=np.mean(Data_fNIRS[i_Num_Index_MV,:,i_Num_Channel_MV,:])
    return Mean_Value
##############################Plot mean value#############################################

num_i_event=0

Event_All_Sex_Male={}
Event_All_Sex_Female={}
Event_All_Driving_experience_Y={}
Event_All_Driving_experience_N={}

for i_event in All_Event_Type:#####load each event data
    print ('It is dealing with the data of', i_event)   
    Event_Position_Data=Position_Data+'\\'+i_event
    Name_Event_People=os.listdir(Event_Position_Data)
    Num_Event_People=len(Name_Event_People)
    num_i_event_people=0 
    Sex_Male=[]
    Sex_Female=[]
    Driving_experience_Y=[]
    Driving_experience_N=[]
    for i_event_people in Name_Event_People:#####load each people data 
        People_Position_Data=Event_Position_Data+'\\'+i_event_people 
        People_Data=scio.loadmat(People_Position_Data)
        Effective_data=People_Data['Effective_Data']
        Scene_num=People_Data['Scene_num']
        Scene_Num_Int=Scene_num.astype(int)[0][0]-1  
        [Num_Fragment,Num_Fragment_Sample,Column]=Effective_data.shape 
        Sample_Low_Num=int(Num_Fragment_Sample/2)
        Fragment_Effective_data=Effective_data[0:Scene_Num_Int,:,:]    
        [Low_fNIRS, Hight_fNIRS,Num_Fragment_People]=fNIRS_Index.fun_get_scene_fNIRS_data(Fragment_Effective_data,i_event_people)
        
        Low_Index_Average_Value_01 =fun_calculate_mean_value(Low_fNIRS)
        Hight_Index_Average_Value_01=fun_calculate_mean_value(Hight_fNIRS)
        [Sex_people,Year_driving]=fgpi.Fun_Get_ParticipantsInformation(i_event_people)
###############################################Judging gender and driving experience###########################################################
        if   Sex_people=='Male':
             Sex_Male.append(Low_Index_Average_Value_01)
             Sex_Male.append(Hight_Index_Average_Value_01)      
        else:
             Sex_Female.append(Low_Index_Average_Value_01)   
             Sex_Female.append(Hight_Index_Average_Value_01)   
        if Year_driving==0:   
             Driving_experience_N.append(Low_Index_Average_Value_01)
             Driving_experience_N.append(Hight_Index_Average_Value_01)
        else:
             Driving_experience_Y.append(Low_Index_Average_Value_01)   
             Driving_experience_Y.append(Hight_Index_Average_Value_01)    

        Low_Index_Average_Value[num_i_event,num_i_event_people,:,:]=Low_Index_Average_Value_01
        Hight_Index_Average_Value[num_i_event,num_i_event_people,:,:]=Hight_Index_Average_Value_01
         
        num_i_event_people=num_i_event_people+1
        del People_Position_Data, Effective_data, Fragment_Effective_data, Low_fNIRS, Hight_fNIRS,i_event_people,Sex_people,Year_driving
    Event_All_Sex_Male[i_event]=Sex_Male
    Event_All_Sex_Female[i_event]=Sex_Female
    Event_All_Driving_experience_Y[i_event]=Driving_experience_Y
    Event_All_Driving_experience_N[i_event]=Driving_experience_N
    num_i_event=num_i_event+1
    
    del i_event,Sex_Male,Sex_Female,Driving_experience_Y,Driving_experience_N
##################################################plot figure##################################################
fpr.fun_plot_sex(Event_All_Sex_Male,Event_All_Sex_Female)
fpr.fun_plot_driver(Event_All_Driving_experience_N,Event_All_Driving_experience_Y)