reset
#set terminal postscrip port enhance color 16
#set output "3in1.ps"


set key off

set lmargin 10
set tmargin 2
set bmargin 2
set tics front

a=0
b=3500-a

set multiplot layout 2,1
plot [:b][:]    \
"GRS1915_alpha.asc" u ($1-a):($4):(0) w filledcur x1 lc rgb "grey",\
"GRS1915_alpha.asc" u ($1-a):($4):($5) w yerrorl ps 1 pt 7 lt 1 lc rgb "black"

#set log y
a=780
b=3250-a
plot [0:b][100:] \
"FS46_4ac77b7-4ac85e1.asc" u ($1-a):($4/1.):($5/1.) w filledcu x1 lc rgb "grey",\
"FS46_4ac77b7-4ac85e1.asc" u ($1-a):($4/1.):($5/1.) w yerrorl ps 1 pt 7 lt 1 lc rgb "black"




unset multiplot


