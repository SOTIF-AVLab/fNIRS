clear;
clc; 

%道路宽为3.75m
Road_Width=3.75;%autonomous emergency braking in short distance
figure(1)
x = linspace(0,60,200);
y = linspace(0,7.5,11.25);
[X,Y] = meshgrid(x,y);
ego_speed = 40;
% G=0.001;M_2=5000;R_2=1;K_1=1;K_2=0.05;
G=0.01;M_2=5000;R_2=1;K_1=1;K_2=0.05;
EGO_Y=Y-Road_Width;EGO_X=X-10;
EGO_Z=((G*R_2*M_2)./sqrt(EGO_X.^2+EGO_Y.^2)).*exp(K_2.* EGO_X.* ego_speed./sqrt(EGO_X.^2+EGO_Y.^2));
surf(X,Y,EGO_Z)

TAEGET_SPEED=40;
TAEGET_Y=Y-Road_Width;TAEGET_X=X-30;%cutin改位置
TAEGET_Z=((G*R_2*M_2)./sqrt(TAEGET_X.^2+TAEGET_Y.^2)).*exp(K_2.* TAEGET_X.* TAEGET_SPEED./sqrt(TAEGET_X.^2+TAEGET_Y.^2));
hold on;
surf(X,Y,TAEGET_Z)

% %AEB改位置
% hold on;
% TAEGET_SPEED1=40;
% TAEGET_Y1=Y-3.75;TAEGET_X1=X-50;
% DISTANCE=sqrt(TAEGET_Y1.^2+TAEGET_X1.^2);
% theta=acos(abs(TAEGET_X1)./DISTANCE);
% 
% TAEGET_Z1=((G*R_2*M_2)./sqrt(TAEGET_X1.^2+TAEGET_Y1.^2)).*exp(K_2.* TAEGET_X1.* TAEGET_SPEED1.*cos(theta)./sqrt(TAEGET_X1.^2+TAEGET_Y1.^2));
% hold on;
% surf(X,Y,TAEGET_Z1)
% 
% % hold on;
% % TAEGET_Z2=((G*R_2*M_2)./sqrt(TAEGET_X1.^2+TAEGET_Y1.^2)).*exp(K_2.* TAEGET_X1.* TAEGET_SPEED1./sqrt(TAEGET_X1.^2+TAEGET_Y1.^2));
% % surf(X,Y,TAEGET_Z2)
% % colormap( [0 0 0] );
% % colormap jet
% % 
% 
% % colorbar('Direction','reverse')
% 
% caxis([0 20])
% 
% set(gca,'FontSize',16)
% %xlabel('x(m)')
% ylabel('y(m)')
% xlim([0 60]) 
% ylim([0 7.5])
% zlim([0 20])

