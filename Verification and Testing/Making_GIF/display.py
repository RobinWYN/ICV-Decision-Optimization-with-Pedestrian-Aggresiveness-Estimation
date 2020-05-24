import matplotlib.pyplot as plt

framex=[-3,'1']
framep=[-1.5,'1']

y=[0,0]

a=[0,0]
b=[]

plt.hlines(-1.75, -20, 7,color="purple",label='lower curb',linewidth=2.0)#横线
plt.hlines(1.75, -20, 7,color="purple",label='upper curb',linewidth=2.0)#横线
plt.hlines(0, -20, 7,color="gray",linewidth=90.0)#横线

plt.hlines(1.05, -2, 2,color="white", linewidth=10)#竖线
plt.hlines(0.35, -2, 2,color="white", linewidth=10)#竖线
plt.hlines(-0.35, -2, 2,color="white", linewidth=10)#竖线
plt.hlines(-1.05, -2, 2,color="white", linewidth=10)#竖线
plt.vlines(0, -6, 3,color="green",linestyles='dashed', label='pedestrian route',linewidth=2.0)#竖线

plt.plot(framex[0],0,color='blue',ms=30,marker='s',label='ego vhehicle') #vehicle
plt.plot(0, framep[0],color='red',ms=10,marker='s',label='pedestrian') #pedestrian
#plt.legend(loc='lower left')
plt.annotate('upper curb', (-15, 2))
plt.annotate('lower curb', (-15, -2.3))
plt.annotate('pedestrian route', (0.5, -5.5))

i=1
address="./images_300_nomerge/test"+str(i)+'.jpg'

plt.savefig(address)

plt.show()
plt.cla()

print(1)