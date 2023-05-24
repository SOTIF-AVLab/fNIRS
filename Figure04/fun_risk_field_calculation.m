function [VTD_risk_field,Information_Stimulation,ALL_Risk_Field]=fun_risk_field_calculation(data,interval,Event_Type,All_Event_Type)
%output
%    VTD_risk_field: the first Column is Time
%    VTD_risk_field: the second Column is the risk field
%    data: Data_Time_Aligned
%####################obtain data##############################%
[row,col]=size(data);
vehicle_speed=data(:,9);
%Time_Clock   =data(:,10);
%Time_Numb    =data(:,11);
Point_interval=interval;
%Point_interval=interval*100;
%#####################define parameters##########################%
G=0.001;k_1=1;k_2=0.05;
M=1705;  %Mass
R=1;
risk_field             =zeros(row,1);
VTD_risk_field         =zeros(interval*2,2);
%VTD_risk_field         =zeros(interval*100*2,2);%前一半为低风险和后一半为高风险，第1列风险的世界时间，第2列风险的相对时间
%第3列为风险 
Information_Stimulation=zeros(row,2);%保存刺激时刻的位置以及刺激时刻的风险场
%######################################################################%
for num_i=1:row
    dis_x=data(num_i,1)-data(num_i,8);
    dis_y=data(num_i,2)-data(num_i,9);
    theta=atan(dis_y/dis_x);
    distance=sqrt(dis_x^2+dis_y^2);
    value_1=(G*R*M)/(distance^(k_1));
    risk_field(num_i,1)=value_1*exp(k_2*vehicle_speed(num_i)*cos(theta));
end
ALL_Risk_Field=risk_field;
%##########################计算刺激时间以及刺激点#########################%
for num_i=1:row
%     [Value_Stimulation,Position_Stimulation] = fun_calculate_stimulate_time(risk_field(num_i,:,1),Event_Type);
    [Value_Stimulation,Position_Stimulation] = fun_calculate_stimulate_position_time(risk_field,Event_Type,All_Event_Type);
    Information_Stimulation(num_i,:)         =[Value_Stimulation,Position_Stimulation];
    VTD_risk_field(num_i,1)=data(num_i,1);
    VTD_risk_field(num_i,2)=risk_field(num_i,1);
end
end