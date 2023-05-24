function [ATHR,BTHR]=calculate_ATHR_BTHR(fnirs_data,p,interval)
%###################################calculate ATHR BHR############################################%

[Row_fNIRS,Column_fNIRS]=size(fnirs_data);
min_p=max(1,p-interval);
max_p=min(p+interval,Row_fNIRS);
value_min=min(max_p-p,p-min_p);
min_p=p-value_min;
max_p=p+value_min;

fnirs_data_b = squeeze(fnirs_data((min_p+1):(p),1:16));
B_HBO=fnirs_data_b(:,1:2:15);
B_HBR=fnirs_data_b(:,2:2:16);
B_TH= B_HBR - B_HBO;
B_TH=B_TH/sqrt(2);
% BTHR = max(B_TH) - min(B_TH);
BTHR=B_TH;

fnirs_data_a = squeeze(fnirs_data((p+1):(max_p),1:16));
A_HBO=fnirs_data_a(:,1:2:15);
A_HBR=fnirs_data_a(:,2:2:16);
A_TH=A_HBR - A_HBO;
A_TH=A_TH/sqrt(2);
% ATHR = max(A_TH)-min(A_TH);
ATHR=A_TH;
%X=ATHR-BTHR
%###################################delete############################################%
%补充：删除fNIRS信号波动较大数据,效果不明显
% for k=1:16
%     windowSize = 20;
%     b = (1/windowSize)*ones(1,windowSize);
%     a = 1;
%     fnirs_data_b_filter = filter(b,a,fnirs_data_b(:,k));
%     fnirs_data_a_filter = filter(b,a,fnirs_data_a(:,k));
%     %###################################delete-1############################################%
%     % figure (k)
%     % plot(fnirs_data_b(:,k),'r')
%     % hold on
%     % plot(fnirs_data_b_filter,'b')
%     % hold off
%     %求导
%     [row,col]=size(fnirs_data_b_filter);
%     slope = zeros(1,row - 2);
%     time_window=1:row;
%     for i = 3 : (row - 2)
%         dy =  fnirs_data_b_filter(i+2)-fnirs_data_b_filter(i-2);
%         %dx =  (time_window(1,i+2)-time_window(1,i-2))/10000;
%         %slope(1,i-2) = dy / dx;
%         slope(1,i-2) = dy;
%     end
%     %检测异常值
%     [slope_row,slope_cols] = size(slope);
%     for i = 1: slope_cols
%         if slope(1,i)>6
%             ATHR=0;
%             BTHR=0;
%         end
%     end
%     %###################################delete-2############################################%
%     %         figure (k)
%     %         plot(fnirs_data_a(:,k),'r')
%     %         hold on
%     %         plot(fnirs_data_a_filter,'b')
%     %         hold off
%     %求导
%     [row,col]=size(fnirs_data_a_filter);
%     slope = zeros(1,row - 2);
%     time_window=1:row;
%     for i = 3 : (row - 2)
%         dy =  fnirs_data_b_filter(i+2)-fnirs_data_a_filter(i-2);
%         %dx =  (time_window(1,i+2)-time_window(1,i-2))/10000;
%         %slope(1,i-2) = dy / dx;
%         slope(1,i-2) = dy;
%     end
%     %检测异常值
%     [slope_row,slope_cols] = size(slope);
%     for i = 1: slope_cols
%         if slope(1,i)>6
%             ATHR=0;
%             BTHR=0;
%         end
%     end
% end
end
