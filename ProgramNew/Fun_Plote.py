import matplotlib.pyplot as plt
import numpy as np
import pdb
def fun_plot_scatter_figure(GLM_DATA,i_event):
    fNIRS_Data=GLM_DATA[:,0]
    Risk_Data =GLM_DATA[:,1]
    
    Num_Sample=Risk_Data.shape
    Num_Sample_Array=np.array(Num_Sample,dtype=float)
    NUM_X=int(Num_Sample_Array[0]/2)
    NUM_XX=int(Num_Sample_Array[0])
    Position_X=np.zeros(NUM_X)
    for i in range(NUM_X):
        Position_X[i]=i

    Fig_Scatter=i_event+'Scatter.jpg'
    Fig_Plot   =i_event+'plote.jpg'
    plt.figure(1)
    plt.subplot(211)
    plt.scatter(Risk_Data[0:NUM_X], fNIRS_Data[0:NUM_X], c='red', s=50, label='legend')
    plt.subplot(212)
    plt.scatter(Risk_Data[NUM_X:NUM_XX], fNIRS_Data[NUM_X:NUM_XX], c='blue', s=50, label='legend')
    plt.legend(loc='best')
    plt.savefig(Fig_Scatter)

    plt.figure(2)
    plt.subplot(211)
    plt.plot(Position_X,fNIRS_Data[0:NUM_X],color="red",linewidth=1 )
    plt.subplot(212)
    plt.plot(Position_X,fNIRS_Data[NUM_X:NUM_XX],color="blue",linewidth=1 )
    plt.xlabel("Time", fontdict={'size': 16})
    plt.ylabel("fNIRS", fontdict={'size': 16})
    plt.savefig(Fig_Plot)
def fun_plot_sample_point(num_i,Sample_point):
    [Num_Index,Num_Valid_Data,Column_Risk_Add,Sample_Low_Num]=Sample_point.shape
    fNIRS_Data=Sample_point[0,num_i,0,:]
    Position_X=np.zeros(Sample_Low_Num)
    for i in range(Sample_Low_Num):
        Position_X[i]=i
    plt.figure(1)
    plt.plot(Position_X,fNIRS_Data[0:Sample_Low_Num],color="red",linewidth=1 )
    pdb.set_trace()
  
def fun_plot_mean_value(fNITS_Data,RiskField_Data,Risk_Mean_Data):
    FRONTSIZE=14
    [Num_Sample,Num_Column]=fNITS_Data.shape
    NUM_X=int(Num_Sample)
    Position_X=np.zeros(NUM_X)
    for i in range(NUM_X):
        Position_X[i]=i
    plt.figure(1)  
    line1=plt.scatter(Position_X,fNITS_Data[:,0],color="blue",  marker='*')
    line2=plt.scatter(Position_X,fNITS_Data[:,1],color="red", marker='*')
    Fig01='.\Result\Figure01_CerebralOxygenExchange.pdf'
    plt.legend(('Low-risk episode',  'Hight-risk episode'),fontsize=FRONTSIZE)
    plt.ylabel(r'$\Delta$COE(umol/L)',fontsize=FRONTSIZE)
    plt.xlabel('Sample',fontsize=FRONTSIZE)
    plt.tick_params(labelsize=FRONTSIZE)
    plt.ylim((-2, 2))
    plt.savefig(Fig01)
    del line1, line2
    [Num_Time,Num_Column]=RiskField_Data.shape
    Position_XX=np.zeros(Num_Time)
    for i in range(Num_Time):
        Position_XX[i]=i/100
    plt.figure(2)  
    
    line1=plt.plot(Position_XX,RiskField_Data[:,0],color="blue",linewidth=1)
    line2=plt.plot(Position_XX+Num_Time/100,RiskField_Data[:,1],color="red",linewidth=1)
    Fig02='.\Result\Figure01_Risk.pdf'
    plt.legend(('Low-risk episode',  'Hight-risk episode'),fontsize=FRONTSIZE)
    plt.ylabel('RiskField(kg/s)',fontsize=FRONTSIZE)
    plt.xlabel('Time(s)',fontsize=FRONTSIZE)
    plt.tick_params(labelsize=FRONTSIZE)
    plt.ylim((0, 0.5))
    plt.savefig(Fig02)
    
def fun_plot_ridkfield(RiskField_Data,i_event):

    [Num_Time,Num_Column]=RiskField_Data.shape
    FRONTSIZE=14
    Position_XX=np.zeros(Num_Time)
    for i in range(Num_Time):
        Position_XX[i]=i/100
    plt.figure(2)  

    line1=plt.plot(Position_XX,RiskField_Data[:,0],color="blue",linewidth=1)
    line2=plt.plot(Position_XX+Num_Time/100,RiskField_Data[:,1],color="red",linewidth=1)
    Fig01='.\Result\Figure08_'+i_event+'.pdf'
    plt.legend(('Low-risk episode',  'Hight-risk episode'),fontsize=FRONTSIZE)
    plt.ylabel('RiskField(kg/s)',fontsize=FRONTSIZE)
    plt.xlabel('Time(s)',fontsize=FRONTSIZE)
    plt.tick_params(labelsize=FRONTSIZE)
    plt.savefig(Fig01)