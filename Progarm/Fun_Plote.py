import matplotlib.pyplot as plt
import numpy as np
import pdb
def fun_plot_scatter_figure(GLM_DATA,i_event):
    fNIRS_Data=GLM_DATA[:,0]
    Risk_Data =GLM_DATA[:,1]
    # pdb.set_trace()
    
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
    # plt.show()
    plt.legend(loc='best')
    plt.savefig(Fig_Scatter)

    plt.figure(2)
    plt.subplot(211)
    plt.plot(Position_X,fNIRS_Data[0:NUM_X],color="red",linewidth=1 )
    plt.subplot(212)
    plt.plot(Position_X,fNIRS_Data[NUM_X:NUM_XX],color="blue",linewidth=1 )
    # plt.xticks(range(2008, 2020, 3))
    # plt.yticks(range(0, 3200, 800))
    plt.xlabel("Time", fontdict={'size': 16})
    plt.ylabel("fNIRS", fontdict={'size': 16})
    # plt.show()
    plt.savefig(Fig_Plot)