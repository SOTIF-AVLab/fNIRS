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
####################################if there are file. delete it ########################
if os.path.isfile('ANOVA_DATA.xlsx'):
    os.remove('ANOVA_DATA.xlsx')
else:
    print('There are no ANOVA_DATA.xlsx')

if os.path.isfile('T_DATA.xlsx'):
    os.remove('T_DATA.xlsx')
else:
    print('There are no GLM_DATA.xlsx')

if os.path.isfile('GLM_DATA.xlsx'):
    os.remove('GLM_DATA.xlsx')
else:
    print('There are no GLM_DATA.xlsx')


MAX_ITER = 200
TOLERANCE = 1e-6
NUM_CHANNEL=8
#########################obtain data position######################
Current_Data=os.getcwd()
Position_Data=Current_Data+'\data\EmergentAEB'
print ('The position of data is', Position_Data)

Num_Data=os.listdir(Position_Data)
Num_Sample=len(Num_Data)
Low_fNIRS_All=[]
Hight_fNIRS_All=[]
Low_Risk_Field_All=[]
Hight_Risk_Field_All=[]
Num_All_Sample=0

#######################load data################################%
for i_people in range(Num_Sample):#####load each people data
    People_Position_Data=Position_Data+'\\'+Num_Data[i_people]
    print ('################################################')
    print ('It is dealing with the data of', People_Position_Data)
   ##############################define data#####################%
    People_Data=scio.loadmat(People_Position_Data)
    Effective_data=People_Data['Effective_Data']
    Scene_num=People_Data['Scene_num']
    Scene_Num_Int=Scene_num.astype(int)[0][0]-1
    [Event,Sample_Num,Column]=Effective_data.shape
    Sample_Low_Num=int(Sample_Num/2)
    Sample_Low_Range=np.zeros(Sample_Low_Num)
    Sample_Hight_Range=np.zeros(Sample_Low_Num)
    Low_fNIRS   =np.zeros([Scene_Num_Int,NUM_CHANNEL,Sample_Low_Num])
    Hight_fNIRS =np.zeros([Scene_Num_Int,NUM_CHANNEL,Sample_Low_Num])
    Low_Risk_Field    =np.zeros([Scene_Num_Int,Sample_Low_Num])
    Hight_Risk_Field  =np.zeros([Scene_Num_Int,Sample_Low_Num])
#################################################################################################################
    for i_scenario in range(Scene_Num_Int):#####load each people data
        for i_sample in range(Sample_Low_Num):
            for i_channl in range (NUM_CHANNEL):
                Low_fNIRS  [i_scenario,i_channl,i_sample] =(Effective_data[i_scenario,i_sample               ,i_channl*2+21]-Effective_data[i_scenario,i_sample               ,i_channl*2+20])/math.sqrt(2)
                Hight_fNIRS[i_scenario,i_channl,i_sample] =(Effective_data[i_scenario,i_sample+Sample_Low_Num,i_channl*2+21]-Effective_data[i_scenario,i_sample+Sample_Low_Num,i_channl*2+20])/math.sqrt(2)
            Low_Risk_Field[i_scenario,i_sample]           = Effective_data[i_scenario,i_sample               ,18]#
            Hight_Risk_Field[i_scenario,i_sample]         = Effective_data[i_scenario,i_sample+Sample_Low_Num,18]

    Low_fNIRS_All       .append(Low_fNIRS) 
    Hight_fNIRS_All     .append(Hight_fNIRS) 
    Low_Risk_Field_All  .append(Low_Risk_Field) 
    Hight_Risk_Field_All.append(Hight_Risk_Field) 
    Num_All_Sample=Num_All_Sample+Scene_Num_Int
###############################Merge  fNIRS data##############################
Low_fNIRS_All_Array    = np.array(Low_fNIRS_All)
Hight_fNIRS_All_Array  = np.array(Hight_fNIRS_All)
Low_Risk_Field_Array   = np.array(Low_Risk_Field_All)
Hight_Risk_Field_Array = np.array(Hight_Risk_Field_All)
[nub_people,nub_scenario,nub_channel,nub_point]=Low_fNIRS_All_Array.shape
Low_ANOVA_DATA  =np.zeros((Num_All_Sample,nub_channel,nub_point), dtype=float)
Hight_ANOVA_DATA=np.zeros((Num_All_Sample,nub_channel,nub_point), dtype=float)

Low_GLM_DATA    =np.zeros((Num_All_Sample,nub_point), dtype=float)
Hight_GLM_DATA  =np.zeros((Num_All_Sample,nub_point), dtype=float)

ANOVA_DATA=np.zeros((Num_All_Sample,NUM_CHANNEL*2), dtype=float)
T_DATA    =np.zeros((Num_All_Sample,NUM_CHANNEL), dtype=float)
GLM_DATA  =np.zeros((Num_All_Sample,NUM_CHANNEL*2), dtype=float)  #sanmple nubmer,channel number,fNIRS,risk field
i_all=0

for i_nub_people in range(nub_people):
    for i_nub_scenario in range(nub_scenario):
        Low_ANOVA_DATA  [i_all,:,:]=Low_fNIRS_All_Array   [i_nub_people,i_nub_scenario,:,:]
        Hight_ANOVA_DATA[i_all,:,:]=Hight_fNIRS_All_Array [i_nub_people,i_nub_scenario,:,:]
        Low_GLM_DATA    [i_all,:]  =Low_Risk_Field_Array  [i_nub_people,i_nub_scenario,:]
        Hight_GLM_DATA  [i_all,:]  =Hight_Risk_Field_Array[i_nub_people,i_nub_scenario,:]
        i_all=i_all+1
del i_nub_people
# ######################Calculate risk features##############################
for i_channel in range(nub_channel):
     Low_Risk_Feature  =dict.calculate_feature(Low_ANOVA_DATA  [:,i_channel,:],MAX_ITER,TOLERANCE)
     Hight_Risk_Feature=dict.calculate_feature(Hight_ANOVA_DATA[:,i_channel,:],MAX_ITER,TOLERANCE)
     ANOVA_DATA[:,i_channel*2]         =Low_Risk_Feature[:,0]
     ANOVA_DATA[:,i_channel*2+1]       =Hight_Risk_Feature[:,0]
     T_DATA[:,i_channel]               =Hight_Risk_Feature[:,0]-Low_Risk_Feature[:,0]
     del Low_Risk_Feature, Hight_Risk_Feature
del i_channel
#############################Calculate  mean value##############################
for i_All_Sample in range(Num_All_Sample):
    for i_channel in range(nub_channel):
        GLM_DATA[i_All_Sample,i_channel*2]=np.mean(Hight_ANOVA_DATA[i_All_Sample,i_channel,:])-np.mean(Low_ANOVA_DATA[i_All_Sample,i_channel,:])
        GLM_DATA[i_All_Sample,i_channel*2+1]=np.mean(Hight_GLM_DATA[i_All_Sample,:]) -np.mean(Low_GLM_DATA[i_All_Sample,:])

del Low_ANOVA_DATA, Hight_ANOVA_DATA,Low_fNIRS_All_Array,Hight_fNIRS_All_Array,Low_fNIRS_All,Hight_fNIRS_All
del Low_Risk_Field, Hight_Risk_Field,Hight_Risk_Field_Array,Low_Risk_Field_Array,Hight_Risk_Field_All,Low_Risk_Field_All

###################################save date to excel############################
ANOVA_DATA_df=pd.DataFrame(ANOVA_DATA)#Convert ndarray format to DataFrame
writer_ANOVA_DATA = pd.ExcelWriter('ANOVA_DATA.xlsx')  #Create an excel sheet named hhh
ANOVA_DATA_df.to_excel(writer_ANOVA_DATA)
writer_ANOVA_DATA.save()  

T_DATA_df=pd.DataFrame(T_DATA)#Convert ndarray format to DataFrame
writer_T_DATA = pd.ExcelWriter('T_DATA.xlsx')  #Create an excel sheet named hhh
T_DATA_df.to_excel(writer_T_DATA)
writer_T_DATA.save()  


GLM_DATA_df=pd.DataFrame(GLM_DATA)#Convert ndarray format to DataFrame
writer_GLM_DATA = pd.ExcelWriter('GLM_DATA.xlsx')  #Create an excel sheet named hhh
GLM_DATA_df.to_excel(writer_GLM_DATA)
writer_GLM_DATA.save()  
