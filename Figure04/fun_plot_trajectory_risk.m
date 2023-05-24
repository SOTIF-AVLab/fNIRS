function  []=fun_plot_trajectory_target_vehicle_one(Risk_Data,Data_COE)
%####################obtain data##############################%
[Row,Column]=size(Risk_Data);
[Row_fNIRS,Column_fNIRS]=size(Data_COE);
Low_X=1:Row_fNIRS;
X=1:Column;
Risk=Risk_Data(5,:);
Risk(Risk==0)=[];
[Row_Risk,Column_Risk]=size(Risk);


Low_Sample=floor(Column_Risk/2);
Risk_X=1:Low_Sample;
Risk_HX=Low_Sample:2*Low_Sample-1;
W_line=1.6;

figure(1)
g=plot(Risk_X,Risk(1:Low_Sample),'g','LineWidth',W_line); 
set(g,'color',[0, 0.39216, 0]);
hold on 
r=plot(Risk_HX,Risk(Low_Sample:2*Low_Sample-1),'r','LineWidth',W_line); 
set(r,'color',[0.69804,0.1333,0.1333]);
set(gca,'FontSize',14)
xlabel('Time(s)')
ytex= ylabel('Risk Field(kg/s)');
legend('low-risk episode','hight-risk episode')


Low_XX=1:8;
Hight_Position=[1,3,5,7,9, 11,13,15];
Low_Position  =[2,4,6,8,10,12,14,16];
figure(2)
g1=plot(Low_XX,Data_COE(1,Low_Position),'*'); 
set(g1,'color',[0, 0.39216, 0]);
hold on 
r1=plot(Low_XX,Data_COE(1,Hight_Position),'*'); 
set(r1,'color',[0.69804,0.1333,0.1333]);
hold on 
g2=plot(Low_XX,Data_COE(2,Low_Position),'*'); 
set(g2,'color',[0, 0.39216, 0]);
hold on 
r2=plot(Low_XX,Data_COE(2,Hight_Position),'*'); 
set(r2,'color',[0.69804,0.1333,0.1333]);
hold on 
g3=plot(Low_XX,Data_COE(3,Low_Position),'*'); 
set(g3,'color',[0, 0.39216, 0]);
hold on 
r3=plot(Low_XX,Data_COE(3,Hight_Position),'*'); 
set(r3,'color',[0.69804,0.1333,0.1333]);
hold on 
g4=plot(Low_XX,Data_COE(4,Low_Position),'*'); 
set(g4,'color',[0, 0.39216, 0]);
hold on 
r4=plot(Low_XX,Data_COE(4,Hight_Position),'*'); 
set(r4,'color',[0.69804,0.1333,0.1333]);
hold on 
g5=plot(Low_XX,Data_COE(5,Low_Position),'*');
set(g5,'color',[0, 0.39216, 0]);
hold on 
r5=plot(Low_XX,Data_COE(5,Hight_Position),'*'); 
set(r5,'color',[0.69804,0.1333,0.1333]);
hold on 
g6=plot(Low_XX,Data_COE(6,Low_Position),'*'); 
set(g6,'color',[0, 0.39216, 0]);
hold on 
r6=plot(Low_XX,Data_COE(6,Hight_Position),'*'); 
set(r6,'color',[0.69804,0.1333,0.1333]);
hold on 
g7=plot(Low_XX,Data_COE(7,Low_Position),'*'); 
set(g7,'color',[0, 0.39216, 0]);
hold on 
r7=plot(Low_XX,Data_COE(7,Hight_Position),'*'); 
set(r7,'color',[0.69804,0.1333,0.1333]);
ylim([-2 5])
xlim([0 8])

xlabel('Channel')
ytex= ylabel('$\triangle COE$');
set(ytex, 'Interpreter', 'latex');
legend('low-risk episode','hight-risk episode')
set(gca,'FontSize',14)


end

function []=fun_plot_risk_field(One_ALL_Ego,One_ALL_Target,One_ALL_Risk_Field,One_Fragment_Ego,One_Fragment_Target,One_Fragment_Risk_Field,figure_i,Risk_Field_Name,Point_Stimulation,Interval)
    
    Value_Point=Point_Stimulation(1);
    X_Point    =Point_Stimulation(2);
    figure(figure_i);
    
    [Row,Column]=size(One_ALL_Ego);
    [Row_Fragment,Column_Fragment]=size(One_Fragment_Ego);
    X_Position=1:Row;
    Distance_Stimulus=Interval*100; 
    X_Position_Fragment=X_Point-Distance_Stimulus+1:X_Point+Distance_Stimulus;
    subplot(211)
  
    X=One_ALL_Ego(:,1);
    plot(One_ALL_Ego(:,1),One_ALL_Ego(:,2),'k');
    hold on
    plot(One_ALL_Ego(X_Position_Fragment,1),One_ALL_Ego(X_Position_Fragment,2),'r');
    hold on
    plot(One_ALL_Target(:,1),One_ALL_Target(:,2),'k');
    hold on
    plot(One_ALL_Target(X_Position_Fragment,1),One_ALL_Target(X_Position_Fragment,2),'r');
    hold on
    plot(One_ALL_Ego(X_Point,1),One_ALL_Ego(X_Point,2),'*r');
    hold on 
    plot(One_ALL_Target(X_Point,1),One_ALL_Target(X_Point,2),'*k');
    
    subplot(212)
    plot(X_Position,One_ALL_Risk_Field,'k');
    hold on
    plot(X_Position_Fragment,One_ALL_Risk_Field(X_Position_Fragment),'r');
    hold on 
    plot(X_Point,One_ALL_Risk_Field(X_Point),'*r');
    
    saveas(gcf, Risk_Field_Name{1}, 'jpg');
    delete(gcf);
end

%#####################find check file######################################################
function Str_File_People_Num=fun_check_file(Event_Type,file_name)
    File_Position= strsplit(file_name,'.') ;
    File_People_Num=strcat('figure_gif\riskfield\',Event_Type,'\',File_Position{1});
    Str_File_People_Num=File_People_Num;
    if ~exist(Str_File_People_Num,'dir')
    mkdir(Str_File_People_Num);
    else
        ;
    end

end

