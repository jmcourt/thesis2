import numpy as np
from matplotlib import pyplot as pl
from matplotlib import gridspec as gs

grid=gs.GridSpec(5,1)

freq=1/27.0
sreq=1/5.0
sqq=1/sreq

x=np.arange(0.0001,100,0.0001)
y=(np.sin(2*np.pi*x*freq)+1)/2.0
w=np.logical_and(x>10,x<90)
s=np.logical_or(x%sqq<0.0001,x%sqq>sqq-0.0001)

fig=pl.figure()
ax1=fig.add_subplot(grid[0,0])
ax1.text(2,1.2,r'$y(t)$')
ax1.set_xlim(0,100)
ax1.set_ylim(-0.3,1.7)
ax1.plot(x,y,'k')
ax1.set_xticks([])
ax1.set_yticks([])
ax2=fig.add_subplot(grid[1,0])
ax2.text(2,1.1,r'$w(t)$')
ax2.set_xlim(0,100)
ax2.set_ylim(-0.0,1.4)
ax2.plot(x,w,'k')
ax2.set_xticks([])
ax2.set_yticks([])
ax3=fig.add_subplot(grid[2,0])
ax3.text(2,1.1,r'$s(t)$')
ax3.set_xlim(0,100)
ax3.set_ylim(-0.0,1.4)
ax3.plot(x,s,'k')
ax3.set_xticks([])
ax3.set_yticks([])
ax4=fig.add_subplot(grid[3,0])
ax4.text(2,1.2,r'$y(t)\times w(t)\times s(t)$')
ax4.set_ylim(-0.3,1.7)
ax4.set_xticks([])
ax4.set_yticks([])
ax4.set_xlim(0,100)
mask=w*s
ax4.plot(x[mask],y[mask],'ok')

ax4=fig.add_subplot(grid[4,0])
ax4.set_ylim(-0.3,1.7)
ax4.set_xticks([])
ax4.set_yticks([])
ax4.set_xlim(0,100)
mask=w*s
ax4.plot(x[mask],y[mask],'ok',zorder=1)

thr=0.001

#for i in np.arange(0,20,0.001):
#   m0=(np.sin(2*np.pi*(x[mask][0]-i)*(sreq-freq))+1)/2.0
#   n0=(np.sin(2*np.pi*(x[mask][1]-i)*(sreq-freq))+1)/2.0
#   o0=(np.sin(2*np.pi*(x[mask][4]-i)*(sreq-freq))+1)/2.0
#   m=m0-y[mask][0]
#   n=n0-y[mask][1]
#   o=o0-y[mask][4]
#   if np.abs(m)<thr and np.abs(n)<thr and np.abs(o)<thr:
#      print i

ax4.plot(x,y,'r',zorder=0)
ax4.plot(x,(np.sin(2*np.pi*(x-3.069)*(sreq-freq))+1)/2.0,'b',zorder=-5)

pl.show()
