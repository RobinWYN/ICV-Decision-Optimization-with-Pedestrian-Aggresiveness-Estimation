# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 03:26:39 2020

@author: wyn
"""

"""
View more, visit my tutorial page: https://morvanzhou.github.io/tutorials/
My Youtube Channel: https://www.youtube.com/user/MorvanZhou

Dependencies:
torch: 0.4
matplotlib
"""
import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt
import xlrd
import os
import numpy as np
import math
from sklearn.model_selection import train_test_split

f1name='input.xlsx'
f2name='realvalues_v2.xlsx'
f3name='input_test.xlsx'
f4name='realvalues_test_v2.xlsx'
# torch.manual_seed(1)    # reproducible
bk=xlrd.open_workbook(f1name)
shxrange=range(bk.nsheets)
try:
    sh=bk.sheet_by_name("Sheet1")
except:
    print("No file at all, you little boy, are you sure you have",format(f1name))
    
num_row=sh.nrows
row_list=[]
for i in range(0,num_row):
    row_data=sh.row_values(i)
    row_list.append(row_data)


bk2=xlrd.open_workbook(f2name)
shxrange2=range(bk2.nsheets)
try:
    sh2=bk2.sheet_by_name("Sheet1")
except:
    print("No file at all, you little boy, are you sure you have",format(f2name))

num_row2=sh2.nrows
row_list2=[]
for i in range(0,num_row2):
    row_data2=sh2.row_values(i)
#    row_Data2_float=[]
#    for num in row_data2:
#        row_Data2_float.append(float(num))
    row_list2.append(row_data2)

#row_list2new=map(float)

bk3=xlrd.open_workbook(f3name)
shxrange3=range(bk3.nsheets)
try:
    sh3=bk3.sheet_by_name("Sheet1")
except:
    print("No file at all, you little boy, are you sure you have",format(f3name))

num_row3=sh3.nrows
row_list3=[]
for i in range(0,num_row3):
    row_data3=sh3.row_values(i)
    row_list3.append(row_data3)


bk4=xlrd.open_workbook(f4name)
shxrange4=range(bk4.nsheets)
try:
    sh4=bk4.sheet_by_name("Sheet1")
except:
    print("No file at all, you little boy, are you sure you have",format(f4name))

num_row4=sh4.nrows
row_list4=[]
for i in range(0,num_row4):
    row_data4=sh4.row_values(i)
    row_list4.append(row_data4)

#print(row_list2)


row_list2new=[]
for i in range(0,num_row2):
    row_data2new=sh2.row_values(i)
    row_Data2_float=[]
    for num in row_data2new:
        row_Data2_float.append(float(num))
    row_list2new.append(row_Data2_float)

#print(row_data2new)

x=torch.tensor(row_list)
y=torch.tensor(row_list2)

x_test=torch.tensor(row_list3)
y_test=torch.tensor(row_list4)

#print(len(x))
#print(len(y))
#print(len(x_test))
#print(len(y_test))

#train_x, test_x = torch.utils.data.random_split(x, [469, 50])
#x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.1,random_state=0)

#print(len(x_train))
#print(len(y_train))

#x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)  # x data (tensor), shape=(100, 1)
#y = x.pow(2) + 0.2*torch.rand(x.size())                 # noisy y data (tensor), shape=(100, 1)



nonsense=1

#class Mydataset(Dataset):

# torch can only train on Variable, so convert them to Variable
# The code below is deprecated in Pytorch 0.4. Now, autograd directly supports tensors
# x, y = Variable(x), Variable(y)

# plt.scatter(x.data.numpy(), y.data.numpy())
# plt.show()


class Net(torch.nn.Module):
    def __init__(self, n_feature, n_hidden, n_output):
        super(Net, self).__init__()
        self.hidden1 = torch.nn.Linear(n_feature, n_hidden)   # hidden layer
        self.hidden2 = torch.nn.Linear(n_hidden, n_hidden)
        self.hidden3 = torch.nn.Linear(n_hidden, n_hidden)
        self.hidden4 = torch.nn.Linear(n_hidden, n_hidden)
        self.predict = torch.nn.Linear(n_hidden, n_output)   # output layer

    def forward(self, x):
        x = F.relu(self.hidden1(x))      # activation function for hidden layer
        x = F.relu(self.hidden2(x))
        x = F.relu(self.hidden3(x))
        x = F.relu(self.hidden4(x))
        x = self.predict(x)             # linear output
        return x

net = Net(n_feature=6, n_hidden=20, n_output=1)     # define the network
#print(net)  # net architecture

epoch=220
l_r=0.05

print(epoch)
print(l_r)
print('layer number=4')

optimizer = torch.optim.SGD(net.parameters(), lr=l_r)
#loss_func = torch.nn.MSELoss()  # this is for regression mean squared loss
loss_func = torch.nn.MSELoss()  # this is for regression mean squared loss

plt.ion()   # something about plotting
mean_loss_test=[]
epoch_plt=[]
train_loss=[]

for t in range(epoch):
    l_r=0.1/(1+0.2*t)
    prediction = net(x)     # input x and predict based on x
    loss = loss_func(prediction, y)     # must be (1. nn output, 2. target)
#    print(loss)
#    print(loss.data)
    
    loss_total=loss.item()
    #print(loss_total)
    
    test = net(x_test)
#    test_result_data=test.detach().numpy()
#    print(test_result_data)
    #print(test.item())
    loss_test = loss_func(test,y_test)
    loss_test_total=loss_test.item()

    optimizer.zero_grad()   # clear gradients for next train
    loss.backward()         # backpropagation, compute gradients
    optimizer.step()        # apply gradients

    if t==epoch-1:
        data_index=[]
        test_result_data=[]
        test_y_raw=[]
        difference=[]
        test_result=net(x_test).detach().numpy()
#        test_result=net(x).detach().numpy()
        for i in range(0,41):
            test_result_data.append(test_result[i][0])
            test_y_raw.append(row_list4[i][0])
            difference.append(test_result[i][0]-row_list4[i][0])
            data_index.append(i+1)
        plt.figure()
        plt.scatter(data_index,test_result_data,label='train_value',color='red')
        plt.scatter(data_index,test_y_raw, label='test_real_value',color='blue')
        plt.xlabel("data ID")
        plt.ylabel("aggresive_index")
        plt.legend(loc="upper right")
        plt.show()

    if t % 2 == 0:
        mean_loss_test.append(loss_test_total)
        epoch_plt.append(t)
        train_loss.append(loss_total)
        # plot and show learning process
#        plt.cla()
#        plt.scatter(x.data.numpy(), y.data.numpy())
#        plt.plot(x.data.numpy(), prediction.data.numpy(), 'r-', lw=5)
#        plt.text(0.5, 0, 'Loss=%.4f' % loss.data.numpy(), fontdict={'size': 20, 'color':  'red'})
#        plt.pause(0.1)



plt.bar(data_index,difference,label='deviation',color='blue')
plt.xlabel("data ID")
plt.ylabel("aggresive_index deviation")
plt.legend(loc="lower right")
plt.show()

a=int(epoch/2-1)
print(mean_loss_test[a])

plt.figure()
torch.save(net,'saved_model')
plt.plot(epoch_plt,mean_loss_test,label='test loss')
plt.plot(epoch_plt,train_loss,color='red',linewidth=1,linestyle='--',label='train loss')
plt.xlabel("epoch")
plt.ylabel("mean square loss")
plt.legend(loc="upper right")
plt.ioff()
plt.show()
