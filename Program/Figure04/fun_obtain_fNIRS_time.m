function Mean_fNIRS_Time=fun_obtain_mean_fNIRS_data(Mean_fNIRS_Data,text_name)
filein='fNIRS_Time.txt';
fileID=fopen(filein,'r');
Information_Time=[];
for i=1:7
    Time_temp=fgetl(fileID);   
    Information_Time=[Information_Time;Time_temp];
end
Information_Time_Final=0;
for i=1:7
    Information_arry=regexp(Information_Time(i,:), '\s+', 'split');
    str_text_name=cell2str(text_name);
    str_Information=cell2str(Information_arry(1));
    tf = strcmp(str_text_name,str_Information);
    if tf==1
       Information_Time_Final=str2num(cell2mat(Information_arry(3)))*60+str2num(cell2mat(Information_arry(4)));
    else
       Information_Time_Final=Information_Time_Final;  
    end
end
[Row,Column]=size(Mean_fNIRS_Data);
Information_Time_Initial=Information_Time_Final-Row+1;
for i_mean=1:Row
    Mean_fNIRS_Data(i_mean,2)=floor(Information_Time_Initial/60);
    Mean_fNIRS_Data(i_mean,3)=Information_Time_Initial-floor(Information_Time_Initial/60)*60;
    Information_Time_Initial=Information_Time_Initial+1;
end

Mean_fNIRS_Time=Mean_fNIRS_Data;

clear Information_Time_Initial， Information_Time_Final
end