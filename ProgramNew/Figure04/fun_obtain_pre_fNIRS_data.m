function Mean_fNIRS_Data=fun_obtain_pre_fNIRS_data(Exp_Name,NUM_CHANNEL)

Name_all_pre = strsplit(Exp_Name,'.');
Pre_data_name=strcat('.\Data_NIRS_KIT\KIT_Data\',Name_all_pre{1},'.mat');
Pre_Data_Filtering=load(Pre_data_name);

oxyData=Pre_Data_Filtering.nirsdata.oxyData;
dxyData=Pre_Data_Filtering.nirsdata.dxyData;

[KIT_Row,KIT_Column]=size(oxyData);

fNIRS_Time_Data=fun_check_pre_data(KIT_Row,Name_all_pre{1});
Pre_Data=zeros(KIT_Row,2*KIT_Column+1);
Pre_Data(:,1)=fNIRS_Time_Data;
for i=1:NUM_CHANNEL
    Pre_Data(:,2*i)=oxyData(:,i);
    Pre_Data(:,2*i+1)=dxyData(:,i);
end
% clear Name Data Time_Data
Mean_fNIRS_Data=fun_obtain_mean_fNIRS_data(Pre_Data,Name_all_pre(1));
clear Exp_Name Pre_Data_Filtering fNIRS_Time_Data  Pre_Data
end
