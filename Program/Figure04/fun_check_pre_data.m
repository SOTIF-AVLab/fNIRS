<<<<<<< HEAD
function fNIRS_Time_Data=fun_check_pre_data(KIT_Row,Name_Experiment)

File_Time_Position='.\Data_NIRS_KIT\Time';
Time_Data_Postion=strcat(File_Time_Position,'\',Name_Experiment,'.xlsx');
Time_Data=xlsread(Time_Data_Postion);

[Time_Data_Row,Time_Data_Column]=size(Time_Data);
%#####################################################################%
fNIRS_Time_Data=zeros(KIT_Row,1);
if(abs(Time_Data(1,1)-KIT_Row)<5)
    for i=1:KIT_Row
    fNIRS_Time_Data(i,1)= i;
    end
% if (Time_Data(1,1)==KIT_Row+1)
%     fNIRS_Time_Data=Time_Data(3:Time_Data_Row,1);
else
    fNIRS_Time_Data=0;
    error('There are error in the data proproccesing')
end

end
=======
function fNIRS_Time_Data=fun_check_pre_data(KIT_Row,Name_Experiment)

File_Time_Position='.\Data_NIRS_KIT\Time';
Time_Data_Postion=strcat(File_Time_Position,'\',Name_Experiment,'.xlsx');
Time_Data=xlsread(Time_Data_Postion);

[Time_Data_Row,Time_Data_Column]=size(Time_Data);
%#####################################################################%
fNIRS_Time_Data=zeros(KIT_Row,1);
if(abs(Time_Data(1,1)-KIT_Row)<5)
    for i=1:KIT_Row
    fNIRS_Time_Data(i,1)= i;
    end
% if (Time_Data(1,1)==KIT_Row+1)
%     fNIRS_Time_Data=Time_Data(3:Time_Data_Row,1);
else
    fNIRS_Time_Data=0;
    error('There are error in the data proproccesing')
end

end
>>>>>>> origin/main
