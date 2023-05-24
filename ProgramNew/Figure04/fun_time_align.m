function [data_TA,Error]=fun_time_align(data_event,data_fnirs)

[DISTANCE_MAX,COLUMN]=size(data_event);
data_fnirs_clock=data_fnirs(:,20);
data_fnirs_time=data_fnirs(:,2:3);
data_TA=zeros(DISTANCE_MAX,COLUMN+16);
Error=0;
%MINTEST=fopen('F:\fNIRS\test\MIN.txt','wt');
% max(data_event(:,:,18))
% max(data_fnirs_clock)
[Min_Data_fNIRS]=min(data_fnirs_clock);
[Max_Data_fNIRS]=max(data_fnirs_clock);
[Min_Data_VTD]  =min(data_event(:,3));
[Max_Data_VTD]  =max(data_event(:,3));

Min_Value=max(Min_Data_fNIRS,Min_Data_VTD);
Max_Value=min(Max_Data_fNIRS,Max_Data_VTD);

Start_fNIRS=find(data_fnirs_clock==Min_Value);
Start_VTD  =find(data_event(:,3)==Min_Value);
DISTANCE_f_V=Max_Value-Min_Value;
data_TA=zeros(DISTANCE_f_V,COLUMN+20);

for i=1:DISTANCE_f_V
      data_TA(i,1:COLUMN)=data_event(Start_VTD,1:COLUMN);
      data_TA(i,COLUMN+1:COLUMN+16)=data_fnirs(Start_fNIRS,4:19);
      data_TA(i,COLUMN+17)=data_fnirs_clock(Start_fNIRS);
      data_TA(i,COLUMN+18)=data_fnirs_time(Start_fNIRS,1);
      data_TA(i,COLUMN+19)=data_fnirs_time(Start_fNIRS,2);
      
Start_VTD=Start_VTD+1;
Start_fNIRS=Start_fNIRS+1;
end
Error=0;
for j=1:DISTANCE_f_V
    MIN=data_TA(j,3)-data_TA(j,COLUMN+17);
    Error=max(MIN,Error);
end
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