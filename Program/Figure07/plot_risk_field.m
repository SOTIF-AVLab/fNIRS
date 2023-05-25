clear;
clc; 

x = linspace(0,60,200);
y = linspace(-3.5,7.5,11.25);
[X,Y] = meshgrid(x,y);
ego_speed = 40;
G=0.001;M_2=5000;R_2=1;K_1=1;K_2=0.05;
EGO_Y=Y-3.75;EGO_X=X-10;
EGO_Z=((G*R_2*M_2)./sqrt(EGO_X.^2+EGO_Y.^2)).*exp(K_2.* EGO_X.* ego_speed./sqrt(EGO_X.^2+EGO_Y.^2));
surf(X,Y,EGO_Z)

% %cut-in 改位置
GG_R_2=0.2;
G_K_2=0.08;
G_M_2=5000;
TAEGET_SPEED=60;
TAEGET_Y=Y-3.75;TAEGET_X=X-35;%cutin改位置
TAEGET_Z=((G*GG_R_2*G_M_2)./sqrt(TAEGET_X.^2+TAEGET_Y.^2)).*exp(G_K_2.* TAEGET_X.* TAEGET_SPEED./sqrt(TAEGET_X.^2+TAEGET_Y.^2));
hold on;
surf(X,Y,TAEGET_Z)
grid off

% hold on;
% TAEGET_SPEED1=40;
% TAEGET_Y1=Y-3.75;TAEGET_X1=X-35;
% DISTANCE=sqrt(TAEGET_Y1.^2+TAEGET_X1.^2);
% theta=acos(abs(TAEGET_X1)./DISTANCE);
% 
% TAEGET_Z1=((G*R_2*M_2)./sqrt(TAEGET_X1.^2+TAEGET_Y1.^2)).*exp(K_2.* TAEGET_X1.* TAEGET_SPEED1.*cos(theta)./sqrt(TAEGET_X1.^2+TAEGET_Y1.^2));
% hold on;
% surf(X,Y,TAEGET_Z1)
% 
% xlabel("Longitudinal Distance (m)");
% ylabel("Lateral Distance (m)");
% zlabel("Risk Field Indicator");

% hold on;
% TAEGET_Z2=((G*R_2*M_2)./sqrt(TAEGET_X1.^2+TAEGET_Y1.^2)).*exp(K_2.* TAEGET_X1.* TAEGET_SPEED1./sqrt(TAEGET_X1.^2+TAEGET_Y1.^2));
% surf(X,Y,TAEGET_Z2)
% colormap( [0 0 0] );
% colormap jet
% 

% colorbar('Direction','reverse')

caxis([0 20])

set(gca,'FontSize',8)

xlim([0 60]) 
ylim([0 7.5])
zlim([0 20])

% shading flat;
% ufo_speed = 50;
% %theta=fun_theta_calculation(X,Y,ufo_speed_x,ufo_speed_y);
% 
% G=0.001;M_2=5000;R_2=1;K_1=1;K_2=0.05;
% 
% Z=((G*R_2*M_2)./sqrt(X.^2+Y.^2)).*exp(K_2.* X.* ufo_speed./sqrt(X.^2+Y.^2));
% size(Y)
% 
% surf(X,Y,Z)
% colorbar
