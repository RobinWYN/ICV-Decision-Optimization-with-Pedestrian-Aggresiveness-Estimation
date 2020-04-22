'''
Author: WYN
Date: 4/17/2020
Content: definition of basic classes in simulation
version: 1.0
'''


class vehicle:
    def __init__(self,posi_x,v_init,id):
        self.x=posi_x
        self.y=0
        self.v=v_init   
        self.acce=0
        self.id=id
        self.crash=0


class pedestrian:
    def __init__(self,posi_ped,v_ped_init,id,agg):
        self.x=0
        self.y=posi_ped
        self.v=v_ped_init
        self.id=id
        self.agg=agg
        self.Neglect=0
        self.ass_count=0
        self.freeze=0
