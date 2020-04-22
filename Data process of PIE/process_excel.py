import xlrd
import xlwt
import os
import xml.etree.ElementTree as ET
import json
import numpy as np
import math
import scipy.stats as st

f1name='total_post_operation.xlsx'
# fnamecode='video_0004_'
# f1name=fnamecode+'attributes.xlsx'
# f2name=fnamecode+'annt.xml'
# f3name=fnamecode+'obd.xlsx'

def  sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


def group(x):
    if (x<=4):
        ans=-0.4*x+12.6
    else:
        ans=11
    ans=ans/1.2-9.17
    return ans

def wait(x):
    ans=(np.exp(0.12*x)-np.exp(-0.12*x))/(np.exp(0.12*x)+np.exp(-0.12*x))
    return ans

def spd(x):
    x=(x-2)/0.837
    ans=st.norm.cdf(x)
    return ans


#fname='video_0001_attributes.xlsx'

bk=xlrd.open_workbook(f1name)
#bk_obd=xlrd.open_workbook(f3name)

shxrange=range(bk.nsheets)


try:
    sh=bk.sheet_by_name("Sheet1")
except:
    print("No file at all, you little boy, are you sure you have",format(f1name))

num_row=sh.nrows
writebook=xlwt.Workbook()
sheet=writebook.add_sheet("Sheet1")

# try:
#     sh_obd=bk_obd.sheet_by_name("Sheet1")
# except:
#     print('sorry ,try again')

# num_row_obd=sh_obd.nrows

row_list=[]
for i in range(0,num_row):
    row_data=sh.row_values(i)
    row_list.append(row_data)

# row_list_obd=[]
# for i in range(0,num_row_obd):
#     row_data_obd=sh_obd.row_values(i)
#     row_list_obd.append(row_data_obd)

title=['wait_agg','group_agg','perc_road','back','ped_spd_agg','accele','sig_agg_index']

for i in range(0,len(title)):
    sheet.write(0,i,title[i])

new_row_num=0
for i in range(1,num_row):
    new_row_num=new_row_num+1

    wait_agg=wait(row_list[i][3])
    sheet.write(new_row_num,0,wait_agg) #wait

    group_agg=group(row_list[i][4])
    sheet.write(new_row_num,1,group_agg) #group

    sheet.write(new_row_num,2,row_list[i][5]) #percp_road

    sheet.write(new_row_num,3,row_list[i][6]) #back or not

    spd_agg=spd(row_list[i][7])
    sheet.write(new_row_num,4,spd_agg) #ped_spd_agg

    sheet.write(new_row_num,5,row_list[i][8])  #accele

    sheet.write(new_row_num,6,row_list[i][15]) #real_agg


#filename=os.path.splitext(f1name)[0]
newfname='input.xls'

writebook.save(newfname)

#print(row_list)

