'''
Author: WYN
Date: 4/17/2020
Content: definition of basic functions in simulation
version: 1.0
'''

from class_base import vehicle, pedestrian
from constants import constants
import math
import random

def judge_interaction(v, p):
    if (-15<=v.x<0)&(-4<=p.y<0):
        return 1
    else:
        return 0

def accelerate_con(vehicle):
    vel=vehicle.v
    dynamic_dist=vel*constants.T+vel*vel/2/math.sqrt(constants.a_set*constants.b)
    s_star=constants.s_0+max(0,dynamic_dist)
    a_ego=constants.a_set*(1-math.pow(vehicle.v/constants.v_d,constants.delta)-math.pow(s_star/abs(vehicle.x),2))
    if abs(a_ego)>constants.a_max:
        a_ego=-constants.a_max
    return a_ego

def accelerate_con_merge_1(vehicle, ped):
    vel=vehicle.v
    dynamic_dist=vel*constants.T+vel*vel/2/math.sqrt(constants.a_set*constants.b)
    merge_s=constants.s_base+ped.agg*(constants.s_0-constants.s_base)
    s_star=merge_s+max(0,dynamic_dist)
    a_ego=constants.a_set*(1-math.pow(vehicle.v/constants.v_d,constants.delta)-math.pow(s_star/abs(vehicle.x),2))
    if abs(a_ego)>constants.a_max:
        a_ego=-constants.a_max
    return a_ego

def accelerate_con_merge_2(vehicle, ped):
    vel=vehicle.v
    dynamic_dist=vel*constants.T+vel*vel/2/math.sqrt(constants.a_set*constants.b)
    s_star=constants.s_0+max(0,dynamic_dist)
    merge_delta=constants.delta*(2-ped.agg)
    a_ego=constants.a_set*(1-math.pow(vehicle.v/constants.v_d,merge_delta)-math.pow(s_star/abs(vehicle.x),2))
    if abs(a_ego)>constants.a_max:
        a_ego=-constants.a_max
    return a_ego

def accelerate_con_merge_3(vehicle, ped):
    vel=vehicle.v
    dynamic_dist=vel*constants.T*ped.agg+vel*vel/2/math.sqrt(constants.a_set*constants.b)
    merge_s=constants.s_base+ped.agg*(constants.s_0-constants.s_base)
    s_star=merge_s+max(0,dynamic_dist)
    a_ego=constants.a_set*(1-math.pow(vehicle.v/constants.v_d,constants.delta)-math.pow(s_star/abs(vehicle.x),2))
    if abs(a_ego)>constants.a_max:
        a_ego=-constants.a_max
    return a_ego   

def accelerate_non(vehicle):
    # vel=vehicle.v
    a_ego=constants.a_set*(1-math.pow(vehicle.v/constants.v_d,constants.delta))
    return a_ego

def accelerate_non_merge_2(vehicle, ped):
    # vel=vehicle.v
    merge_delta=constants.delta*(constants.set_merge_delta-ped.agg)
    a_ego=constants.a_set*(1-math.pow(vehicle.v/constants.v_d,merge_delta))
    return a_ego

def update_vehicle(vehicle, ped):
    if judge_interaction(vehicle,ped)==1:
        if ped.freeze < constants.pass_freeze:
            vehicle.acce=accelerate_con(vehicle)
        else:
            vehicle.acce=accelerate_non(vehicle)
    else:
        vehicle.acce=accelerate_non(vehicle)   #update acceleration

    temp_v=vehicle.v+vehicle.acce*constants.t
    vehicle.v=temp_v if temp_v>0 else 0        #update velocity
    vehicle.x=vehicle.x+vehicle.v*constants.t  #update position

def update_vehicle_merge_1(vehicle, ped):
    if judge_interaction(vehicle,ped)==1:
        if ped.freeze < constants.pass_freeze:
            vehicle.acce=accelerate_con_merge_1(vehicle, ped)
        else:
            vehicle.acce=accelerate_non(vehicle)
    else:
        vehicle.acce=accelerate_non(vehicle)   #update acceleration

    temp_v=vehicle.v+vehicle.acce*constants.t
    vehicle.v=temp_v if temp_v>0 else 0        #update velocity
    vehicle.x=vehicle.x+vehicle.v*constants.t  #update position

def update_vehicle_merge_2(vehicle, ped):
    if judge_interaction(vehicle,ped)==1:
        if ped.freeze < constants.pass_freeze:
            vehicle.acce=accelerate_con_merge_2(vehicle, ped)
        else :
            vehicle.acce=accelerate_non_merge_2(vehicle, ped)
    else:
        vehicle.acce=accelerate_non(vehicle)   #update acceleration

    temp_v=vehicle.v+vehicle.acce*constants.t
    vehicle.v=temp_v if temp_v>0 else 0        #update velocity
    vehicle.x=vehicle.x+vehicle.v*constants.t  #update position

def update_vehicle_merge_3(vehicle, ped):
    if judge_interaction(vehicle,ped)==1:
        if ped.freeze < constants.pass_freeze:
            vehicle.acce=accelerate_con_merge_3(vehicle, ped)
        else :
            vehicle.acce=accelerate_non_merge_2(vehicle, ped)
    else:
        vehicle.acce=accelerate_non(vehicle)   #update acceleration

    temp_v=vehicle.v+vehicle.acce*constants.t
    vehicle.v=temp_v if temp_v>0 else 0        #update velocity
    vehicle.x=vehicle.x+vehicle.v*constants.t  #update position

def aggre_prob(vehicle, ped):
    if vehicle.v==0:
        return 1
    else:    
        exponent=constants.s_safe/abs(vehicle.x)-1
        agg_index=math.pow(ped.agg,exponent)
        return agg_index

def update_ped(vehicle, ped):
    if (judge_interaction(vehicle,ped)==0):
        ped.v=constants.ped_set_v
    if (judge_interaction(vehicle,ped)==1) and (random.random()>(ped.Neglect/10)) and (ped.freeze<constants.pass_freeze): #if interact and not neglect, make decisions
        if (ped.ass_count%5==0):
            agg_prob=aggre_prob(vehicle,ped)  #probability to keep moving forward
            if random.random()>agg_prob:
                ped.v=0
                ped.freeze=ped.freeze+1
            else:
                ped.v=constants.ped_set_v
                ped.freeze=0
    ped.y=ped.y+ped.v*constants.t


def judge_crash(vehicle, ped):
    if vehicle.crash!=0:
        if (abs(vehicle.x)<0.5) and (abs(ped.y)<0.2):
            vehicle.crash=1