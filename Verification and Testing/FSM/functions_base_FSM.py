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

def exist_conflict(v, p):
    if (v.x>=0) or (p.y>0) or (p.v==0):   #if the vehicle or pedestrian has passed
        return 0
    else:
        if abs((-v.x)/v.v-(-p.y)/p.v)<constants.T_FSM:
            return 1
        else:
            return 0

def exist_nonconflict(v, p):
    if (v.x>=0) or (p.y>0):
        return 1
    else:
        if p.v==0:
            return 1
        else:
            if abs((-v.x)/v.v-(-p.y)/p.v)>constants.T_FSM:
                return 1
            else:
                return 0

def merge_T_judge(v, p):
    te=-v.x/v.v
    tp=-p.y/p.v
    if te-tp < constants.T_FSM:
        return (te-tp/p.agg)
    else:
        return (te-tp)

def exist_conflict_merge(v, p):
    if (v.x>=0) or (p.y>0) or (p.v==0):   #if the vehicle or pedestrian has passed
        return 0
    else:
        if abs(merge_T_judge(v, p))<constants.T_FSM:
            return 1
        else:
            return 0

def exist_nonconflict_merge(v, p):
    if (v.x>=0) or (p.y>0):
        return 1
    else:
        if p.v==0:
            return 1
        else:
            if abs(merge_T_judge(v, p))>constants.T_FSM:
                return 1
            else:
                return 0


def update_vehicle(vehicle, ped):
    if vehicle.state =='start':
        if exist_conflict(vehicle, ped)==1:
            vehicle.acce=-2
            vehicle.state='dece'
        elif exist_nonconflict(vehicle, ped)==1:
            vehicle.acce=1
            vehicle.state='acce'
    elif vehicle.state =='dece':
        if exist_conflict(vehicle, ped)==1:
            vehicle.acce=-2
            vehicle.state='dece'
        elif exist_nonconflict(vehicle, ped)==1:
            vehicle.acce=1
            vehicle.state='acce'
    elif vehicle.state == 'acce':
        if exist_conflict(vehicle, ped)==1:
            vehicle.acce=-2
            vehicle.state='dece'
        elif exist_nonconflict(vehicle, ped)==1:
            vehicle.acce=1
            vehicle.state='acce'
    elif vehicle.state == 'stop':
        if exist_conflict(vehicle, ped) ==1:
            vehicle.state=='stop'
        elif exist_nonconflict(vehicle, ped)==1:
            vehicle.acce=1
            vehicle.state=='acce'

    temp_v=vehicle.v+vehicle.acce*constants.t
    vehicle.v=temp_v if temp_v>0 else 0        #update velocity
    vehicle.x=vehicle.x+vehicle.v*constants.t  #update position

def update_vehicle_merge(vehicle, ped):
    if vehicle.state =='start':
        if exist_conflict_merge(vehicle, ped)==1:
            vehicle.acce=-2
            vehicle.state='dece'
        elif exist_nonconflict_merge(vehicle, ped)==1:
            vehicle.acce=1
            vehicle.state='acce'
    elif vehicle.state =='dece':
        if exist_conflict_merge(vehicle, ped)==1:
            vehicle.acce=-2
            vehicle.state='dece'
        elif exist_nonconflict_merge(vehicle, ped)==1:
            vehicle.acce=1
            vehicle.state='acce'
    elif vehicle.state == 'acce':
        if exist_conflict_merge(vehicle, ped)==1:
            vehicle.acce=-2
            vehicle.state='dece'
        elif exist_nonconflict_merge(vehicle, ped)==1:
            vehicle.acce=1
            vehicle.state='acce'
    elif vehicle.state == 'stop':
        if exist_conflict_merge(vehicle, ped) ==1:
            vehicle.state=='stop'
        elif exist_nonconflict_merge(vehicle, ped)==1:
            vehicle.acce=1
            vehicle.state=='acce'

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