reset
#set terminal postscrip port enhance color 16
#set output "3in1.ps"


set key off

set lmargin 10
set tmargin 2
set bmargin 2
set tics front

a=1280
b=1514-a

set multiplot layout 3,1
plot [0:b][50:]    \
"543881874_96420-01-05-00_FS_event_gx1_chan_0_50.in" u ($1-a):($2/2.):(0) w filledcur x1 lc rgb "grey",\
"543881874_96420-01-05-00_FS_event_gx1_chan_0_50.in" u ($1-a):($2/2.):($3/2.) w yerrorl ps 1 pt 7 lt 1 lc rgb "black"

a=1870
b=2305-a
plot [0:b][1000:] \
"GRS1915_10408-01-40-00_pcu2.in" u ($1-a):($2/1.):($3/1.) w filledcu x1 lc rgb "grey",\
"GRS1915_10408-01-40-00_pcu2.in" u ($1-a):($2/1.):($3/1.) w yerrorl ps 1 pt 7 lt 1 lc rgb "black"

#set log y

set xlabel "Time (sec)"

a=24500
b=27600-a
plot [0:b][10:50]\
"2014/16605_lc_heg_meg_10s.asc" u ($1-5.125064320739100E+08-a):2:3 w filledc x1 lc rgb "grey",\
"2014/16605_lc_heg_meg_10s.asc" u ($1-5.125064320739100E+08-a):2:3 w yerrorl ps 1 pt 7 lt 1 lc rgb "black"



unset multiplot


