'''
Author: WYN
Date: 4/22/2020
version: 2.0
'''
import matplotlib.pyplot as plt
from PIL import Image 
import imageio
from class_base import vehicle, pedestrian
from constants import constants
from functions_base_FSM import update_vehicle, update_ped, judge_crash, update_vehicle_merge

import numpy as np

cross_time_comp=[]
crash_comp=[]

Data_vehicle=[]
Data_ped=[]
cross_time=[]

Data_vehicle_merge=[]
Data_ped_merge=[]
cross_time_merge=[]


V=[]
P=[]

for i in range(0,500):
    V.append(vehicle(-15, 5, str(i)))
    temp_agg=0.1+0.8/500*i
    P.append(pedestrian(-3.5, 1.5, str(-i), temp_agg))

crash_count=0

for i in range(0, 500):
    v_data=[]
    p_data=[]
    t_cross=0
    while (V[i].x<5):
        frame_v_Data=[V[i].state, round(V[i].x, 3), round(V[i].v, 3), round(V[i].acce, 3), V[i].id]
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
merge
'''
V=[]
P=[]

for i in range(0,500):
    V.append(vehicle(-15, 5, str(i)))
    temp_agg=0.1+0.8/500*i
    P.append(pedestrian(-3.5, 1.5, str(-i), temp_agg))

crash_count=0

for i in range(0, 500):
    v_data=[]
    p_data=[]
    t_cross=0
    while (V[i].x<5):
        frame_v_Data=[V[i].state, round(V[i].x, 3), round(V[i].v, 3), round(V[i].acce, 3), V[i].id]
        v_data.append(frame_v_Data)
        frame_p_data=[round(P[i].y, 3), P[i].id]
        p_data.append(frame_p_data)
        update_vehicle_merge(V[i],P[i])
        update_ped(V[i],P[i])
        t_cross=t_cross+constants.t
        judge_crash(V[i],P[i])
    if V[i].crash==1:
        crash_count=crash_count+1
    Data_vehicle_merge.append(v_data)
    Data_ped_merge.append(p_data)
    cross_time_merge.append(round(t_cross, 1))

cross_time_comp.append(round(np.sum(cross_time_merge),1))
crash_comp.append(crash_count)

'''
display the results
'''
passlength=len(Data_ped_merge[300])

for i in range(0,passlength):
    plt.hlines(-1.75, -16, 7,color="purple",label='lower curb',linewidth=2.0)#横线
    plt.hlines(1.75, -16, 7,color="purple",label='upper curb',linewidth=2.0)#横线
    plt.hlines(0, -16, 7,color="gray",linewidth=135.0)#横线

    plt.hlines(1.05, -2, 2,color="white", linewidth=10)#竖线
    plt.hlines(0.35, -2, 2,color="white", linewidth=10)#竖线
    plt.hlines(-0.35, -2, 2,color="white", linewidth=10)#竖线
    plt.hlines(-1.05, -2, 2,color="white", linewidth=10)#竖线
    plt.vlines(0, -4, 2,color="green",linestyles='dashed', label='pedestrian route',linewidth=2.0)#竖线

    plt.plot(Data_vehicle_merge[300][i][1],0,color='blue',ms=30,marker='s',label='ego vhehicle') #vehicle
    plt.plot(0, Data_ped_merge[300][i][0],color='red',ms=10,marker='s',label='pedestrian') #pedestrian
    #plt.legend(loc='lower left')
    plt.annotate('upper curb', (-13, 2))
    plt.annotate('lower curb', (-13, -2.3))
    plt.annotate('pedestrian route', (0.5, -3.7))
    address="./images_300_merge/merge_FSM_"+str(i)+'.jpg'
    plt.savefig(address)
    #plt.show()
    #plt.pause(0.1)
    #plt.close()
    plt.cla()



print(1)
