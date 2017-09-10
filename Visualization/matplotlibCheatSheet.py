import matplotlib.pyplot as plt
import numpy as np

################################################################
#Function Method
################################################################
# x = np.linspace(0,5,11)
# y = x ** 2

# print (x)
# print (y)
#
# plt.plot(x,y)
# plt.xlabel('X Label')
# plt.ylabel('y Label')
# plt.title('Title')
# plt.subplot(1,2,1)
# plt.plot(x,y,'r')
# plt.subplot(1,2,2)
# plt.plot(y,x,'b')
# plt.show()

################################################################
#Object Oriented Method
################################################################

# fig = plt.figure()
#
# axes = fig.add_axes([0.1,0.1,0.8,0.8])
# axes.plot(x,y)
# axes.set_xlabel('X Label')
# axes.set_ylabel('y Label')
# axes.set_title('Title')
# plt.show()

# fig = plt.figure()
# axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
# axes2 = fig.add_axes([0.2,0.4,0.3,0.4]) #[from left,from bottom,30% of canvas size in width,40% of canvas size in height]
# axes1.plot(x,y)
# axes2.plot(y,x)
# plt.show()

################################################################
#Object Oriented Method  --- Sub Plots
################################################################
# fig,axes = plt.subplots(nrows = 1, ncols=2)
# axes[0].plot(x,y)
# axes[1].plot(y,y)
# # plt.tight_layout()
# # axes.plot(x,y)
# plt.show()

################################################################
#Object Oriented Method  --- Figure Size and DPI
################################################################

# fig = plt.figure(figsize = (5,3))
# ax = fig.add_axes([0.1,0.1,0.8,0.8])
# ax.plot(x,y)
# plt.show()

# fig,axes = plt.subplots(nrows = 2, ncols = 1, figsize = (8,3))
# ax = fig.add_axes([0.1,0.1,0.8,0.8])
# axes[0].plot(x,y)
# axes[0].plot(y,x)
# plt.show()

################################################################
#Object Oriented Method  --- Save a figure
################################################################

# fig.savefig('my_picture.png')

################################################################
#Object Oriented Method  --- Legends, appearance
################################################################

# fig = plt.figure()
#
# ax = fig.add_axes([.1,.1,.8,.8])
# # ax.plot(x,x**2,color = 'green',linewidth = 3,linestyle = '-',marker = 'o',markerfacecolor='yellow',markeredgewidth = 3,markeredgecolor = 'green',label = 'x squared') # linewidth has shortname as lw and linestyle as ls
# # ax.plot(x,x**3, label = 'x cubed')
# ax.plot(x,x**2,color = 'green',linewidth = 3,linestyle = '-')
# ax.set_xlim(0,1)
# ax.set_ylim(0,2)
#
# # ax.legend()
#
# plt.show()

################################################################
#Exercise
################################################################

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Part1
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

x = np.arange(0,100)
y = x*2
z = x**2
#
# fig = plt.figure()
# ax1 = fig.add_axes([.1,.1,.8,.8])
# ax2 = fig.add_axes([0.2,0.5,.2,.2])
# ax1.plot(x,z)
# ax1.set_ylabel('Z')
# ax1.set_xlabel('X')
#
# ax2.plot(x,y)
# ax2.set_ylabel('Y')
# ax2.set_xlabel('X')
# ax2.set_title('Zoom')
# ax2.set_xlim([20,22])
# ax2.set_ylim([30,50])
# plt.show()

fig,axes = plt.subplots(nrows=1,ncols=2,figsize=(5,3))
axes[0].plot(x,y,color ='blue',linestyle ='--')
axes[1].plot(x,z,color ='red')
plt.tight_layout()

plt.show()
