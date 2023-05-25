# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 16:47:48 2022

@author: 86188
"""
import sys
import numpy as np
import math
import pdb
import matplotlib.pyplot as plt
import matplotlib
import os

##############################Plot mean value#############################################

def fun_plot_mean_value(Low_Data_Mean,Hight_Data_Mean):
     [Num_Event_DM,Num_People_DM]=Low_Data_Mean.shape
     NUM_X=int(Num_People_DM)
     

     labels = ['Sub01', 'Sub02', 'Sub03', 'Sub04', 'Sub05','Sub06', 'Sub07', 'Sub08', 'Sub09', 'Sub10','Sub11', 'Sub12', 'Sub13', 'Sub14', 'Sub15','Sub16', 'Sub17', 'Sub18', 'Sub19', 'Sub20']
     
     Position_X=np.zeros(NUM_X)
     for i in range(NUM_X):
        Position_X[i]=i
#########################################Lead vehicle autonomous emergency braking in a short distance scenario#####################
     plt.figure(1)
     line1=plt.plot(Position_X,Low_Data_Mean[0,0:NUM_X],color="red",linewidth=1,  marker='o',markersize = 10)
     line2=plt.plot(Position_X,Hight_Data_Mean[0,0:NUM_X],color="blue",linewidth=1,marker='o',markersize = 10 )
     plt.ylabel(r'$\Delta$COE(umol/L)')
     plt.xticks(Position_X, labels, rotation=45)
     # 添加图例
     plt.title('Lead vehicle autonomous emergency braking in a short distance scenario')
     plt.legend(('Low Risk',  'Hight Risk'))
     Fig01='ASEB.pdf'
     plt.savefig(Fig01)
#########################################Lead vehicle cut-in from left lane in a short distance scenario#####################
     plt.figure(2)
     line1=plt.plot(Position_X,Low_Data_Mean[1,0:NUM_X],color="red",linewidth=1,  marker='o',markersize = 10)
     line2=plt.plot(Position_X,Hight_Data_Mean[1,0:NUM_X],color="blue",linewidth=1,marker='o',markersize = 10 )
     plt.ylabel(r'$\Delta$COE(umol/L)')
     plt.xticks(Position_X, labels, rotation=45)
     plt.title('Lead vehicle cut-in from left lane in a short distance scenario')
     plt.legend(('Low Risk',  'Hight Risk'))

     Fig02='LCI.pdf'
     plt.savefig(Fig02)

#########################################Lead vehicle cut-in from right lane in a short distance scenario#####################
     plt.figure(3)
     line1=plt.plot(Position_X,Low_Data_Mean[2,0:NUM_X],color="red",linewidth=1,  marker='o',markersize = 10)
     line2=plt.plot(Position_X,Hight_Data_Mean[2,0:NUM_X],color="blue",linewidth=1,marker='o',markersize = 10 )
     plt.ylabel(r'$\Delta$COE(umol/L)')
     plt.xticks(Position_X, labels, rotation=45)
     plt.title('Lead vehicle cut-in from right lane in a short distance scenario')
     plt.legend(('Low Risk',  'Hight Risk'))

     Fig03='RCI.pdf'
     plt.savefig(Fig03)

#########################################Pedestrian crossing road from right scenario#####################
     plt.figure(4)
     line1=plt.plot(Position_X,Low_Data_Mean[3,0:NUM_X],color="red",linewidth=1,  marker='o',markersize = 10)
     line2=plt.plot(Position_X,Hight_Data_Mean[3,0:NUM_X],color="blue",linewidth=1,marker='o',markersize = 10 )
     plt.ylabel(r'$\Delta$COE(umol/L)')
     plt.xticks(Position_X, labels, rotation=45)
     plt.title('Pedestrian crossing road from right scenario')
     plt.legend(('Low Risk',  'Hight Risk'))
     plt.show()
     Fig04='RPCR.pdf'
     plt.savefig(Fig04)

##############################Plot mean value#############################################
def fun_plot_mean_value_people(Low_Data_Mean,Hight_Data_Mean):
     [Num_Event_DM,Num_People_DM]=Low_Data_Mean.shape
     NUM_X=int(Num_People_DM)
     

     labels = ['Sub01', 'Sub02', 'Sub03', 'Sub04', 'Sub05','Sub06', 'Sub07', 'Sub08', 'Sub09', 'Sub10','Sub11', 'Sub12', 'Sub13', 'Sub14', 'Sub15','Sub16', 'Sub17', 'Sub18', 'Sub19', 'Sub20']
     
     Position_X=np.zeros(NUM_X)
     for i in range(NUM_X):
        Position_X[i]=i
#########################################Lead vehicle autonomous emergency braking in a short distance scenario#####################
     plt.figure(1)
     line1=plt.plot(Position_X,Hight_Data_Mean[0,0:NUM_X],color="red",linewidth=1,  marker='o',markersize = 10)
     line2=plt.plot(Position_X,Hight_Data_Mean[1,0:NUM_X],color="blue",linewidth=1,marker='o',markersize = 10 )
     line3=plt.plot(Position_X,Hight_Data_Mean[2,0:NUM_X],color="k",linewidth=1,  marker='o',markersize = 10)
     line4=plt.plot(Position_X,Hight_Data_Mean[3,0:NUM_X],color="g",linewidth=1,marker='o',markersize = 10 )

def fun_plot_sex(Data_Sex_Male,Data_Sex_Female):
    Event_All=len(Data_Sex_Male)
    Position_Channel=7
    Position_Index=0
    Num_Figure=1
    Event_Name=['Pedestrian crossing road from right scenario','Lead vehicle cut-in from left lane in a short distance scenario','Lead vehicle cut-in from right lane in a short distance scenario','Lead vehicle autonomous emergency braking in a short distance scenario']
    for key, value in Data_Sex_Male.items():
        Current_Postion=os.getcwd()
        Name_Figure=Current_Postion+'/Result/Sex'+key+'.svg'
        if os.path.exists(Name_Figure):
           os.remove (Name_Figure)
        Num_Sex_Male=int(len(value)/2)
        Num_Sex_FeMale=int(len(Data_Sex_Female[key])/2)
        Mean_Data_Sex_Male=np.zeros([Num_Sex_Male,2])
        Mean_Data_Sex_FeMale=np.zeros([Num_Sex_FeMale,2])
        for i_num in range(Num_Sex_Male):
            Mean_Data_Sex_Male[i_num,0]=value[i_num][Position_Index][Position_Channel]
            Mean_Data_Sex_Male[i_num,1]=value[i_num*2+1][Position_Index][Position_Channel]
        for j_num in range(Num_Sex_FeMale):
            Mean_Data_Sex_FeMale[j_num,0]=Data_Sex_Female[key][j_num][Position_Index][Position_Channel]
            Mean_Data_Sex_FeMale[j_num,1]=Data_Sex_Female[key][j_num*2+1][Position_Index][Position_Channel]
        
        plt.figure(Num_Figure)
        plt.ylabel(r'$\Delta$COE(umol/L)')
        labels = 'LM','HM','LF','HF'
        plt.boxplot([Mean_Data_Sex_Male[:,0],Mean_Data_Sex_Male[:,1],Mean_Data_Sex_FeMale[:,0],Mean_Data_Sex_FeMale[:,1]],labels = labels)
        
        plt.ylim(-0.1, 0.15)
        matplotlib.rcParams.update({'font.size': 10})
        plt.savefig(Name_Figure)
        Num_Figure=Num_Figure+1
        del key,value,Mean_Data_Sex_Male, Mean_Data_Sex_FeMale
def fun_plot_driver(Data_Driver_No,Data_Driver_Yes):
    Event_All=len(Data_Driver_No)
    Position_Channel=7
    Position_Index=0
    Num_Figure=5
    Event_Name=['Pedestrian crossing road from right scenario','Lead vehicle cut-in from left lane in a short distance scenario','Lead vehicle cut-in from right lane in a short distance scenario','Lead vehicle autonomous emergency braking in a short distance scenario']
    for key, value in Data_Driver_No.items():
        Current_Postion=os.getcwd()
        Name_Figure=Current_Postion+'/Result/Driver'+key+'.svg'
        if os.path.exists(Name_Figure):
           os.remove (Name_Figure)
        Num_driver_no=int(len(value)/2)
        Num_driver_yes=int(len(Data_Driver_Yes[key])/2)
        Mean_Data_Driver_No=np.zeros([Num_driver_no,2])
        Mean_Data_Driver_Yes=np.zeros([Num_driver_yes,2])
        for i_num in range(Num_driver_no):
            Mean_Data_Driver_No[i_num,0]=value[i_num][Position_Index][Position_Channel]
            Mean_Data_Driver_No[i_num,1]=value[i_num*2+1][Position_Index][Position_Channel]
        for j_num in range(Num_driver_yes):
            Mean_Data_Driver_Yes[j_num,0]=Data_Driver_Yes[key][j_num][Position_Index][Position_Channel]
            Mean_Data_Driver_Yes[j_num,1]=Data_Driver_Yes[key][j_num*2+1][Position_Index][Position_Channel]
        
        plt.figure(Num_Figure)
        plt.ylabel(r'$\Delta$COE(umol/L)')
        labels01 = 'LN','HN','LY','HY'
       
        plt.boxplot([Mean_Data_Driver_No[:,0],Mean_Data_Driver_No[:,1],Mean_Data_Driver_Yes[:,0],Mean_Data_Driver_Yes[:,1]],labels = labels01)
        
        plt.ylim(-0.1, 0.15)

        matplotlib.rcParams.update({'font.size': 10})
        plt.savefig(Name_Figure)

        Num_Figure=Num_Figure+1
        del key,value,Mean_Data_Driver_No, Mean_Data_Driver_Yes