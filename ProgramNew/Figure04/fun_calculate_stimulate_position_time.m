function [Value_Stimulation,Total_Position_Stimulation]=fun_calculate_stimulate_position_time(risk_field_data,Event_Type,All_Event_Type)

[Value_Max,Index_Max]=max(risk_field_data);
[Row_Risk_Field,Column_Risk_Field]=size(risk_field_data);
%##################################寻找大于阈值的风险场#####################
num_i=1;
Risk_Field_Threshold_New=fun_find_threshold_risk_field(Event_Type,All_Event_Type);
while(1) 
    Value_Min_Threshold=min(risk_field_data(num_i:num_i+5,:));
    if (Value_Min_Threshold>Risk_Field_Threshold_New)||(num_i>Index_Max-10)
        clear Risk_Field_Threshold_New
        break; 
    else
        num_i=num_i+1; 
    end
end  
Total_Position_Stimulation=num_i;
Value_Stimulation=risk_field_data(Total_Position_Stimulation);
end

function Risk_Field_Threshold=fun_find_threshold_risk_field(Event_Type,All_Event_Type)
AEB   =All_Event_Type{1};
cut_in  =All_Event_Type{2};
Problem_Message= 'Please enter the correct event name, the error is location in the ”fun_calculate_stimulate_time” function';
if strcmp(Event_Type,AEB)%%%pedestrian
        Risk_Field_Threshold=0.11;
elseif strcmp(Event_Type,cut_in)%%%left_cut_in
        Risk_Field_Threshold=0.0064;
% elseif strcmp(Event_Type,right_cut_in)%%%left_cut_in
%         Risk_Field_Threshold=0.05;
% elseif strcmp(Event_Type,EmergentAEB)%%%EmergentAEB
%         Risk_Field_Threshold=0.05;
else
     disp(Problem_Message);
     clear Problem_Message;
end
end
