reset
#set terminal postscrip port enhance color 16
#set output "3in1.ps"


set key off

set lmargin 10
set tmargin 2
set bmargin 2
set tics front

a=383
b=470-a

set multiplot layout 3,1
plot [0:b][50:]    \
"545168464_96420-01-07-01_FS_event_gx0_chan_0_50.in" u ($1-a):($2/2.):(0) w filledcur x1 lc rgb "grey",\
"545168464_96420-01-07-01_FS_event_gx0_chan_0_50.in" u ($1-a):($2/2.):($3/2.) w yerrorl ps 1 pt 7 lt 1 lc rgb "black"

a=5
b=150-a
plot [0:b][1000:] \
"GRS1915_93701-01-02-01_pcu2.in" u ($1-a):($2/1.):($3/1.) w filledcu x1 lc rgb "grey",\
"GRS1915_93701-01-02-01_pcu2.in" u ($1-a):($2/1.):($3/1.) w yerrorl ps 1 pt 7 lt 1 lc rgb "black"

#set log y

set xlabel "Time (sec)"

#a=200
#b=900-a
#plot [0:b][70:220]\
#"BP_obs_Rho" u ($1-a):3:4 w filledc x1 lc rgb "grey",\
#"BP_obs_Rho" u ($1-a):3:4 w yerrorl ps 1 pt 7 lt 1 lc rgb "black"

a=77957177
b=800
plot [0:730][200:]\
"77957176_10401-01-58-00_FS3b_4a5882b-4a58c9e.in" u ($1-a):2:3 w filledc x1 lc rgb "grey",\
"77957176_10401-01-58-00_FS3b_4a5882b-4a58c9e.in" u ($1-a):2:3 w yerrorl ps 1 pt 7 lt 1 lc rgb "black"



unset multiplot


