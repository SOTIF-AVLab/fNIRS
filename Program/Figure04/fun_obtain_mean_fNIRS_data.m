function Mean_fNIRS_Data=fun_obtain_mean_fNIRS_data(fNIRS_Data,text_name)
fNIRS_Time=fNIRS_Data(:,1);
fNIRS_channel_data=fNIRS_Data(:,2:17);
[row,column]=size(fNIRS_Time);
Frequency=50;
Time=floor(row/Frequency);
Mean_fNIRS_Data=zeros(Time+1,20);
for i_time=1:Time
    Mean_fNIRS_Data(i_time,1)=fNIRS_Time((i_time-1)*Frequency+1);
    Mean_fNIRS_Data(i_time,4) =mean(fNIRS_channel_data((i_time-1)*Frequency+1:i_time*Frequency,1));
    Mean_fNIRS_Data(i_time,5) =mean(fNIRS_channel_data((i_time-1)*Frequency+1:i_time*Frequency,2));
    Mean_fNIRS_Data(i_time,6) =mean(fNIRS_channel_data((i_time-1)*Frequency+1:i_time*Frequency,3));
    Mean_fNIRS_Data(i_time,7) =mean(fNIRS_channel_data((i_time-1)*Frequency+1:i_time*Frequency,4));
    Mean_fNIRS_Data(i_time,8) =mean(fNIRS_channel_data((i_time-1)*Frequency+1:i_time*Frequency,5));
    Mean_fNIRS_Data(i_time,9) =mean(fNIRS_channel_data((i_time-1)*Frequency+1:i_time*Frequency,6));
    Mean_fNIRS_Data(i_time,10)=mean(fNIRS_channel_data((i_time-1)*Frequency+1:i_time*Frequency,7));
    Mean_fNIRS_Data(i_time,11)=mean(fNIRS_channel_data((i_time-1)*Frequency+1:i_time*Frequency,8));
    Mean_fNIRS_Data(i_time,12)=mean(fNIRS_channel_data((i_time-1)*Frequency+1:i_time*Frequency,9));
    Mean_fNIRS_Data(i_time,13)=mean(fNIRS_channel_data((i_time-1)*Frequency+1:i_time*Frequency,10));
    Mean_fNIRS_Data(i_time,14)=mean(fNIRS_channel_data((i_time-1)*Frequency+1:i_time*Frequency,11));
    Mean_fNIRS_Data(i_time,15)=mean(fNIRS_channel_data((i_time-1)*Frequency+1:i_time*Frequency,12));
    Mean_fNIRS_Data(i_time,16)=mean(fNIRS_channel_data((i_time-1)*Frequency+1:i_time*Frequency,13));
    Mean_fNIRS_Data(i_time,17)=mean(fNIRS_channel_data((i_time-1)*Frequency+1:i_time*Frequency,14));
    Mean_fNIRS_Data(i_time,18)=mean(fNIRS_channel_data((i_time-1)*Frequency+1:i_time*Frequency,15));
    Mean_fNIRS_Data(i_time,19)=mean(fNIRS_channel_data((i_time-1)*Frequency+1:i_time*Frequency,16));
end
Mean_fNIRS_Data(Time+1,1)=fNIRS_Time(Time*Frequency+1);
Mean_fNIRS_Data(Time+1,4) =mean(fNIRS_channel_data(Time*Frequency+1:row,1));
Mean_fNIRS_Data(Time+1,5) =mean(fNIRS_channel_data(Time*Frequency+1:row,2));
Mean_fNIRS_Data(Time+1,6) =mean(fNIRS_channel_data(Time*Frequency+1:row,3));
Mean_fNIRS_Data(Time+1,7) =mean(fNIRS_channel_data(Time*Frequency+1:row,4));
Mean_fNIRS_Data(Time+1,8) =mean(fNIRS_channel_data(Time*Frequency+1:row,5));
Mean_fNIRS_Data(Time+1,9) =mean(fNIRS_channel_data(Time*Frequency+1:row,6));
Mean_fNIRS_Data(Time+1,10)=mean(fNIRS_channel_data(Time*Frequency+1:row,7));
Mean_fNIRS_Data(Time+1,11)=mean(fNIRS_channel_data(Time*Frequency+1:row,8));
Mean_fNIRS_Data(Time+1,12)=mean(fNIRS_channel_data(Time*Frequency+1:row,9));
Mean_fNIRS_Data(Time+1,13)=mean(fNIRS_channel_data(Time*Frequency+1:row,10));
Mean_fNIRS_Data(Time+1,14)=mean(fNIRS_channel_data(Time*Frequency+1:row,11));
Mean_fNIRS_Data(Time+1,15)=mean(fNIRS_channel_data(Time*Frequency+1:row,12));
Mean_fNIRS_Data(Time+1,16)=mean(fNIRS_channel_data(Time*Frequency+1:row,13));
Mean_fNIRS_Data(Time+1,17)=mean(fNIRS_channel_data(Time*Frequency+1:row,14));
Mean_fNIRS_Data(Time+1,18)=mean(fNIRS_channel_data(Time*Frequency+1:row,15));
Mean_fNIRS_Data(Time+1,19)=mean(fNIRS_channel_data(Time*Frequency+1:row,16));




Mean_fNIRS_Time=fun_obtain_fNIRS_time(Mean_fNIRS_Data,text_name);
Mean_fNIRS_Data=Mean_fNIRS_Time;
% fileID=fopen(filein,'r');
% for i=1:line
%     fgetl(fileID);                     
% end
% 
% Mean_fNIRS_Data=1
% 
% % fNIRS_Data_Name = strcat(Current_Position,'\','cutin\',File_Name_fNIRS); 
% Current_Position=pwd;
% File_Position_all=strcat(Current_Position,'\','cutin\');
% NEW_Position       =strcat(File_Position_all,'test_new.txt');
% fNIRS_Data_Postiton=strcat(File_Position_all,fNIRS_Name);
% flag_fNIRS=datahandle(fNIRS_Data_Postiton,NEW_Position,67);             
% fNIRS_Data=importdata(NEW_Position);
% fun_check_fNIRS_data(fNIRS_Data,fNIRS_Data_Postiton)
% fNIRS_Time=fNIRS_Data(:,1);
% fNIRS_channel_data=fNIRS_Data(:,2:17);
% [row,column]=size(fNIRS_Time);
% % data_fnirs=zeros(row,18);
% % 
% % for i=1:row
% %     data_fnirs(i,1)=fNIRS_Time(i,5)*60+fNIRS_Time(i,6);
% %     data_fnirs(i,2)=fNIRS_Time(i,7);
% %     data_fnirs(i,3:18)=fNIRS_channel_data(i,:);
% % end

% data_fNIRS=1;
% [DISTANCE_MAX,COLUMN]=size(data_event);
% data_fnirs_clock=data_fnirs(:,20);
% data_TA=zeros(DISTANCE_MAX,COLUMN+16);
% Error=0;
% %MINTEST=fopen('F:\fNIRS\test\MIN.txt','wt');
% % max(data_event(:,:,18))
% % max(data_fnirs_clock)
% for j=1:DISTANCE_MAX
%     if data_event(j,3)==0
%         data_TA(j,:)=0;
%     elseif data_event(j,3)>max(data_fnirs_clock)
%         data_TA(j,:)=0;
%     else
%         [MIN,TA_row]=min(abs(data_fnirs_clock-data_event(j,3)));
%         %fprintf(MINTEST,'%f\t %f\t %f\n',MIN,data_event(i,j,18),data_fnirs_clock(TA_row));
%         Error=max(MIN,Error);
%         data_TA(j,1:COLUMN)=data_event(j,1:COLUMN);
%         data_TA(j,COLUMN+1:COLUMN+16)=data_fnirs(TA_row,4:19);
%     end
% end
%fclose(MINTEST);
end