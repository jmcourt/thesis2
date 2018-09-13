set terminal postscrip enhance color 20
set output "page8.ps"
set key off
set multiplot layout 2,1
plot [383:470]"545168464_96420-01-07-01_FS_event_gx0_chan_0_50.in" u ($1):($2/2.):($3/2.) w yerrorl lt 1 lc rgb "black"
set xlabel "Time (sec)"
plot [5:150]  "GRS1915_93701-01-02-01_pcu2.in" u 1:($2/1.):($3/1.) w yerrorl lt 1 lc rgb "black"
unset multiplot


