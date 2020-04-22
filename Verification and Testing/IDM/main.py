'''
Author: WYN
Date: 4/22/2020
version: 2.0
'''

from class_base import vehicle, pedestrian
from constants import constants
from functions_base import update_ped, update_vehicle
from functions_base import update_vehicle_merge_1, update_vehicle_merge_2, update_vehicle_merge_3
from functions_base import judge_crash

import numpy as np

cross_time_comp=[]
crash_comp=[]

Data_vehicle=[]
Data_ped=[]
cross_time=[]

Data_vehicle_merge1=[]
Data_ped_merge1=[]
cross_time_merge1=[]

Data_vehicle_merge2=[]
Data_ped_merge2=[]
cross_time_merge2=[]

Data_vehicle_merge3=[]
Data_ped_merge3=[]
cross_time_merge3=[]

V=[]
P=[]

for i in range(0,500):
    V.append(vehicle(-20, 5, str(i)))
    temp_agg=0.1+0.8/500*i
    P.append(pedestrian(-5, 1.5, str(-i), temp_agg))

crash_count=0

for i in range(0, 500):
    v_data=[]
    p_data=[]
    t_cross=0
    while (V[i].x<5):
        frame_v_Data=[round(V[i].x, 3), round(V[i].v, 3), round(V[i].acce, 3), V[i].id]
        v_data.append(frame_v_Data)
        frame_p_data=[round(P[i].y, 3), P[i].id]
        p_data.append(frame_p_data)
        update_vehicle(V[i],P[i])
        update_ped(V[i],P[i])
        t_cross=t_cross+constants.t
        judge_crash(V[i],P[i])
    if V[i].crash==1:
        crash_count=crash_count+1
    Data_vehicle.append(v_data)
    Data_ped.append(p_data)
    cross_time.append(round(t_cross, 1))

cross_time_comp.append(round(np.sum(cross_time),1))
crash_comp.append(crash_count)

'''
merge_1
'''
V=[]
P=[]

for i in range(0,500):
    V.append(vehicle(-20, 5, str(i)))
    temp_agg=0.1+0.8/500*i
    P.append(pedestrian(-5, 1.5, str(-i), temp_agg))

crash_count=0

for i in range(0, 500):
    v_data=[]
    p_data=[]
    t_cross=0
    while (V[i].x<5):
        frame_v_Data=[round(V[i].x, 3), round(V[i].v, 3), round(V[i].acce, 3), V[i].id]
        v_data.append(frame_v_Data)
        frame_p_data=[round(P[i].y, 3), P[i].id]
        p_data.append(frame_p_data)
        update_vehicle_merge_1(V[i],P[i])
        update_ped(V[i],P[i])
        t_cross=t_cross+constants.t
        judge_crash(V[i],P[i])
    if V[i].crash==1:
        crash_count=crash_count+1
    Data_vehicle_merge1.append(v_data)
    Data_ped_merge1.append(p_data)
    cross_time_merge1.append(round(t_cross, 1))

cross_time_comp.append(round(np.sum(cross_time_merge1), 1))
crash_comp.append(crash_count)

'''
merge_2
'''
V=[]
P=[]

for i in range(0,500):
    V.append(vehicle(-20, 5, str(i)))
    temp_agg=0.1+0.8/500*i
    P.append(pedestrian(-5, 1.5, str(-i), temp_agg))

crash_count=0

for i in range(0, 500):
    v_data=[]
    p_data=[]
    t_cross=0
    while (V[i].x<5):
        frame_v_Data=[round(V[i].x, 3), round(V[i].v, 3), round(V[i].acce, 3), V[i].id]
        v_data.append(frame_v_Data)
        frame_p_data=[round(P[i].y, 3), P[i].id]
        p_data.append(frame_p_data)
        update_vehicle_merge_2(V[i],P[i])
        update_ped(V[i],P[i])
        t_cross=t_cross+constants.t
        judge_crash(V[i],P[i])
    if V[i].crash==1:
        crash_count=crash_count+1
    Data_vehicle_merge2.append(v_data)
    Data_ped_merge2.append(p_data)
    cross_time_merge2.append(round(t_cross, 1))

cross_time_comp.append(round(np.sum(cross_time_merge2),1))
crash_comp.append(crash_count)

'''
merge_3
'''
V=[]
P=[]

for i in range(0,500):
    V.append(vehicle(-20, 5, str(i)))
    temp_agg=0.1+0.8/500*i
    P.append(pedestrian(-5, 1.5, str(-i), temp_agg))

crash_count=0

for i in range(0, 500):
    v_data=[]
    p_data=[]
    t_cross=0
    while (V[i].x<5):
        frame_v_Data=[round(V[i].x, 3), round(V[i].v, 3), round(V[i].acce, 3), V[i].id]
        v_data.append(frame_v_Data)
        frame_p_data=[round(P[i].y, 3), P[i].id]
        p_data.append(frame_p_data)
        update_vehicle_merge_3(V[i],P[i])
        update_ped(V[i],P[i])
        t_cross=t_cross+constants.t
        judge_crash(V[i],P[i])
    if V[i].crash==1:
        crash_count=crash_count+1
    Data_vehicle_merge3.append(v_data)
    Data_ped_merge3.append(p_data)
    cross_time_merge3.append(round(t_cross, 1))

cross_time_comp.append(round(np.sum(cross_time_merge3), 1))
crash_comp.append(crash_count)


print(1)
