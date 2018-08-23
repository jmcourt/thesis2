import numpy as np
from matplotlib import pyplot as pl
import random
from matplotlib import gridspec as gs

grid=gs.GridSpec(4,10)


x=np.arange(0,30,1/30.00000000)
addon=np.sin(2*(x+0.5*2*np.pi))+1
addon[addon<0]=0
addon=2/(addon+1)**100
y=5+2*np.sin(2*x)+np.random.randn(len(x))+addon-1
ye=np.array([1]*len(x))

ax1=pl.subplot(grid[0,:])
ax1.errorbar(x,y,yerr=ye,fmt='0.7',zorder=-1)
ax1.plot(x,y,'k',zorder=1)
ax1.text(0.3,12,'1)')
ax1.set_ylim(-1,15)
ax1.set_xlim(0,30)
ax1.set_xticks([])
ax1.set_yticks([])

foldybits=np.array([0]*94)
print len(foldybits)

ax2=pl.subplot(grid[1,:])
ax2.text(0.3,12,'2)')
ax2.errorbar(x,y,yerr=ye,fmt='0.7',zorder=-1)
ax2.plot(x,y,'r',zorder=1)
for i in range(0,5):
   pl.axvline(i*2*np.pi,color='k',zorder=6)
   pl.axvline((i*2+1)*np.pi,color='k',zorder=6)
   mask=np.logical_and(x>i*2*np.pi,x<(i*2+1)*np.pi)
   ax2.plot(x[mask],y[mask],'b',zorder=2)
ax2.set_xlim(0,30)
ax2.set_ylim(-1,15)
ax2.set_xticks([np.pi,2*np.pi,3*np.pi,4*np.pi,5*np.pi,6*np.pi,7*np.pi,8*np.pi,9*np.pi])
ax2.set_xticklabels([1,2,3,4,5,6,7,8,9])
ax2.set_yticks([])

ax3=pl.subplot(grid[2:,0:4])
ax3.text(0.1,15,'3)')
spacing=-6
for i in range(0,9):
   if i%2:
      col='r'
   else:
      col='b'
   mask=np.logical_and(x>i*np.pi,x<(i+1)*np.pi)
   print sum(mask)
   foldybits=foldybits+y[mask][:94]
   tx=x-i*np.pi
   ax3.errorbar(tx[mask],y[mask]+i*spacing,yerr=ye[mask],fmt='0.7',zorder=-1)
   ax3.plot(tx[mask],y[mask]+i*spacing,col,zorder=1)

ax3.set_xlim(0,np.pi)
ax3.set_ylim(-50,20)
ax3.set_yticks([])
ax3.set_xticks([])

ax4=pl.subplot(grid[2:,4:])
ax4.text(0.7,59,'4)')
ax4.plot(range(94),foldybits,'k',zorder=1)
ax4.errorbar(range(94),foldybits,yerr=3,zorder=-1,fmt='0.7')
ax4.set_yticks([])
ax4.set_xlim(0,93)
ax4.set_xticks([0,93/4.,93/2.,3*93/4.,93])
ax4.set_xticklabels([0,0.25,0.5,0.75,1])
ax4.set_xlabel('Phase')

pl.show()
