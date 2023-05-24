clc
clear all
close all
%#############################load data################################%
fNRISCOEDATA=zeros(4,8);
fNRISCOEDATA(1:4,:)=[-1.284,  -0.817,  -0.181,  0.745,  -0.844,  -0.145,   0.426, 1.199;
                     -1.181,   1.610,   1.529,  1.884,   0.797,   0.998,   2.690, 3.205;
                     -1.120,   1.287,   0.451,  1.907,  -1.002,   0.888,   1.102, 2.572;
                      1.139,   2.343,   3.052,  4.043,   1.075,   3.423,   1.755, 4.439];
fNRISCOEDATA(5,:)=[-2.366, -1.859, -2.197, -1.183, -2.366,-2.366,-2.366,-2.366];
MNI_ALL=zeros(8,4);
MNI_ALL=[57,    50.56,  19.33, 1;
          57.12, 56.1,   1.26,  1;
          38.41, 70.37,  19.56, 1;
          32.83, 76.89, -0.91,  1;
         -31.45, 75.44,  21.04, 2;
         -33.04, 77.66,  0.59,  2;
         -56.11, 54.37,  19.49, 2;
         -55.73, 60.39,  -1,    2];
  
[Row,Column]=size(fNRISCOEDATA);
Age_Data=[24,46,42,25,21,32,22,28,24,25,25,32,24,41,24,41,25,31,33,24];

for i=1:5
    fun_plot_brain_figure(fNRISCOEDATA(i,:),i,MNI_ALL)
end
Channel8_Positin=MNI_ALL(8,1:3);
aff_mni2tal(Channel8_Positin);
%#############################load data################################%
function []=fun_plot_brain_figure(fNRISData,Num_fig,MNI)
%Load Data Needed for plotting
load('BrainField.mat'); 
handles.BrainField = BrainField; 
load cmap_jet; 
handles.cmap = cmap;
BrainSurface = load('BrainSurface.mat');
handles.BrainSurface=BrainSurface;

figure(Num_fig)
%#####################################plot figure#########################%
[theta, phi, radius, value, region] = topo_map_rot(MNI, fNRISData);
handles.map.tHbO2 = value; clear radius value region;
handles.map.theta = theta;
handles.map.phi = phi; 
%#################################plot 2D figure#########################%
map = handles.map.tHbO2;
h = imagesc(handles.map.phi(1,:),handles.map.theta(:,1),map,[-max(abs(map(:))) max(abs(map(:)))]); set(gca,'Ydir','normal');
hold on; 
contour(handles.map.phi,handles.map.theta,handles.BrainField,5);          
xlabel('\phi (degree)'); ylabel('\theta (degree)');         
colormap(handles.cmap); colorbar;          
handles.img.tHbO2 = topo_surf_rot(MNI, fNRISData, handles.BrainSurface.vertices);
%#################################plot 3D figure#########################%

%HbO: 3D image on brain surface
vertvalue = handles.img.tHbO2;
vertcolor = repmat([1 1 1], length(handles.BrainSurface.vertices), 1);
vertplot = vertvalue/max(abs(vertvalue));
regIdx = find(isnan(vertplot)==0);
cidx = round(31.5*vertplot(regIdx)+32.5);
cidx(find(cidx>64)) = 64;
cidx(find(cidx<1)) = 1;
vertcolor(regIdx,:) = handles.cmap(cidx,:);
clear vertvalue vertplot regIdx cidx
 h = plotimage(handles.BrainSurface.vertices,handles.BrainSurface.faces, vertcolor, [0 0 1]);    
 colormap(handles.cmap);   
 contextMenuImg(h,vertcolor,handles);
%########################add channel#####################################%
Postion_x=MNI(1:8,1);
Postion_y=MNI(1:8,2);
Postion_z=MNI(1:8,3);
text(Postion_x(1),Postion_y(1),Postion_z(1),'ch1','FontSize',12)
text(Postion_x(2),Postion_y(2),Postion_z(2),'ch2','FontSize',12)
text(Postion_x(3),Postion_y(3),Postion_z(3),'ch3','FontSize',12)
text(Postion_x(4),Postion_y(4),Postion_z(4),'ch4','FontSize',12)
text(Postion_x(5),Postion_y(5),Postion_z(5),'ch5','FontSize',12)
text(Postion_x(6),Postion_y(6),Postion_z(6),'ch6','FontSize',12)
text(Postion_x(7),Postion_y(7),Postion_z(7),'ch7','FontSize',12)
text(Postion_x(8),Postion_y(8),Postion_z(8),'ch8','FontSize',12)
end


 