function theta=fun_theta_calculation(dis_x_v2t,dis_y_v2t,ufo_speed_x,ufo_speed_y)

%output 
%    theta: 为物体i 速度方向与r_ij的夹角，顺时针方向为正
[row,column]=size(dis_x_v2t);

theta=zeros(row,3);
for i=1:row

     if(dis_y_v2t(i)==0)
     theta(i,2)=0;
     else
     theta(i,2)=atan(dis_x_v2t(i)/dis_y_v2t(i));
     end

     if(ufo_speed_y(i)==0)
      theta(i,3)=0;
     else
     theta(i,3)=atan(ufo_speed_x(i)/ufo_speed_y(i));
     end     
     theta(i,1)=theta(i,2)-theta(i,3);

end

end
