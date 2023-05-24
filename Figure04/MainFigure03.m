clc
close all
clear
%#############################parameter##########################################%
NUM_CHANNEL=8; %通道数
interval=10;
Key_Space={32};
Event_Type='cut_in';
All_Event_Type={'AEB','cut_in'};
Current_Position=pwd;
fNIRS_Data_Postiton=strcat(Current_Position,'\','cutinfNIRS');
File_Name_fNIRS=ls(fNIRS_Data_Postiton);
VTD_Data_Postiton=strcat(Current_Position,'\','cutinrisk');
File_Name_VTD=ls(VTD_Data_Postiton);
[Row_Sample, Column_Sample]=size(File_Name_VTD);
Data_COE=zeros(Row_Sample-2,NUM_CHANNEL*2);%The front 8 columns is hight-risk episode and the later 8 columns is low-risk episode
Risk_Data=zeros(7,40);
for i=3: 9
    VTD_Data_Name = strcat(Current_Position,'\','cutinrisk\',strtrim(File_Name_VTD(i,:))); 
    VTD_Data=xlsread(VTD_Data_Name);
%     fNIRS_Data=fun_obtain_fNIRS_data(strtrim(File_Name_fNIRS(i,:)));
    fNIRS_Data=fun_obtain_pre_fNIRS_data(strtrim(File_Name_fNIRS(i,:)),NUM_CHANNEL);
    %##########################load data#############################%
    Effective_Data_Vehicle=VTD_Data(:,8:12);
    Effective_Data_Ego=VTD_Data(:,4:7);
    Effective_Data_Time =VTD_Data(:,1:3);
    [Row_Effective,Column_Effective]=size(Effective_Data_Time);
    
    Effective_Event_Data=zeros(Row_Effective,12);
    
    Effective_Event_Data(:,1:4)=Effective_Data_Ego;
    Effective_Event_Data(:,5:9)=Effective_Data_Vehicle;
    Effective_Event_Data(:,10)=Effective_Data_Time(:,2)*60+Effective_Data_Time(:,3);
    Effective_Event_Data(:,11)=sqrt(Effective_Data_Vehicle(:,4).*Effective_Data_Vehicle(:,4)+Effective_Data_Vehicle(:,5).*Effective_Data_Vehicle(:,5));
    [VTD_risk_field,Information_Stimulation_Temp,ALL_Risk_Field]=fun_risk_field_calculation(Effective_Event_Data,interval,Event_Type,All_Event_Type);
    VTD_risk_field(:,3)=Effective_Event_Data(:,10);
    
    fNIRS_Data(:,20)=fNIRS_Data(:,2)*60+fNIRS_Data(:,3);
    
    [data_TA,Error]=fun_time_align(VTD_risk_field,fNIRS_Data);
    [Row_Risk,Column_Risk]=size(data_TA);
%   [a,b]=size(Data_COE)
    fnirs_data=data_TA(:,4:19);
%     p=Information_Stimulation_Temp(:,2);
    p=floor(Row_Risk/2);
    [data_ATHR,data_BTHR]=calculate_ATHR_BTHR(fnirs_data,p,interval);
    i_data=i-2; 
    Risk_Data(i_data,1:Row_Risk)=data_TA(1:Row_Risk,2);
    for j=1:NUM_CHANNEL
        Data_COE(i_data,j*2-1)=mean(data_BTHR(:,j));
        Data_COE(i_data,j*2)  =mean(data_ATHR(:,j));
    end
end
fun_plot_trajectory_risk(Risk_Data,Data_COE)
% fun_plot_trajectory_one()
filename='fNIRS.xlsx';
sheet=1;
xlRange='A1';
%################如果存在已经存在的文件则删除文件
if exist('filename','file')
    delete filename
else
;
end
xlswrite(filename,Data_COE,sheet,xlRange);