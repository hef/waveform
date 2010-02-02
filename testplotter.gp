set terminal svg enhanced size 1000 1000 fname "Times" fsize 10
#set key samplen 0 autotitle columnhead outside horizontal left
set key autotitle columnhead
#set noxtic
#set noytic
#set size 
set border 3
set multiplot layout 7,1
plot '4to1multiplexor.log' using 1 with steps
plot '4to1multiplexor.log' using 2 with steps
plot '4to1multiplexor.log' using 3 with steps
plot '4to1multiplexor.log' using 4 with steps
plot '4to1multiplexor.log' using 5 with steps
plot '4to1multiplexor.log' using 6 with steps
plot '4to1multiplexor.log' using 7 with steps
unset multiplot

