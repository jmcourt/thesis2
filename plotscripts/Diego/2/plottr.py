from matplotlib import pyplot as pl
from matplotlib import gridspec as gs
import numpy as np

grid=gs.GridSpec(3,1)

pl.figure(figsize=(7,8))

ax1=pl.subplot(grid[0])
ax2=pl.subplot(grid[1])
ax3=pl.subplot(grid[2])

igr_x=[]
igr_y=[]
igr_e=[]

grs_x=[]
grs_y=[]
grs_e=[]

bp__x=[]
bp__y=[]
bp__e=[]

a=open('GRS.dat')
for line in a:
   l=line.split()
   grs_x.append(float(l[0]))
   grs_y.append(float(l[1]))
   grs_e.append(float(l[2]))
a.close()

a=open('IGR.dat')
for line in a:
   l=line.split()
   igr_x.append(float(l[0]))
   igr_y.append(float(l[1]))
   igr_e.append(float(l[2]))
a.close()

a=open('BP.dat')
for line in a:
   l=line.split()
   bp__x.append(float(l[0])-5.125064320739100E+08)
   bp__y.append(float(l[1]))
   bp__e.append(float(l[2]))
a.close()

grs_x=np.array(grs_x)
igr_x=np.array(igr_x)
bp__x=np.array(bp__x)

grs_s=1870
grs_f=2305
grs_m=2000
grs_M=10000
ax1.plot(grs_x-grs_s,grs_y,'k')
ax1.errorbar(grs_x-grs_s,grs_y,yerr=grs_e,fmt='0.7',zorder=-900)
ax1.set_xlim(0,grs_f-grs_s)
ax1.set_ylim(grs_m,grs_M)
ax1.text((grs_f-grs_s)/11.,(grs_M-grs_m)*(8/10.)+grs_m,'GRS 1915+105')
ax1.set_ylabel('Rate (cts/s/PCU)')

igr_s=1280
igr_f=1514
igr_m=100
igr_M=700
ax2.plot(igr_x-igr_s,igr_y,'k')
ax2.errorbar(igr_x-igr_s,igr_y,yerr=igr_e,fmt='0.7',zorder=-900)
ax2.set_xlim(0,igr_f-igr_s)
ax2.set_ylim(igr_m,igr_M)
ax2.text((igr_f-igr_s)/11.,(igr_M-igr_m)*(8/10.)+igr_m,'IGR J17091-3624')
ax2.set_ylabel('Rate (cts/s/PCU)')

bp__s=24500
bp__f=27600
bp__m=15
bp__M=50
ax3.plot(bp__x-bp__s,bp__y,'k')
ax3.errorbar(bp__x-bp__s,bp__y,yerr=bp__e,fmt='0.7',zorder=-900)
ax3.set_xlim(0,bp__f-bp__s)
ax3.set_ylim(bp__m,bp__M)
ax3.text((bp__f-bp__s)/11.,(bp__M-bp__m)*(8/10.)+bp__m,'GRO J1744-28')
ax3.set_xlabel('Time (s)')
ax3.set_ylabel('Rate (cts/s)')

pl.show()
