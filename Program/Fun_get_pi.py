# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 16:47:48 2022

@author: 86188
"""
import os.path
import pdb

import pandas as pd
Current_Data=os.getcwd()
Name_ParticipantsInformation='ParticipantsInformation.xlsx'
def  Fun_Get_ParticipantsInformation(Name_Data):
     Sex_Male=[]
     Sex_Female=[]
     Driving_experience_Y=[]
     Driving_experience_N=[]
     Name_people=Name_Data.split('.')[0]
     Dict_People_Positin=0
     data_frame=pd.read_excel(Name_ParticipantsInformation,sheet_name='Sheet1')
     Dict_Participants_Information=data_frame.to_dict()
     Dict_Participants_Information['NO.'].items()

     for item in Dict_Participants_Information['NO.'].items():
          if item[1]==Name_people:
               Dict_People_Positin=item[0]
          else:
               Dict_People_Positin=Dict_People_Positin
     Sex_people=Dict_Participants_Information['Sex'][Dict_People_Positin]
     Year_driving=Dict_Participants_Information['Driving experience'][Dict_People_Positin]
     del Name_Data
     return Sex_people,Year_driving
