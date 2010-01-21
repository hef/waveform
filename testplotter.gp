set term svg
set key samplen 0 autotitle columnhead outside horizontal left
set noxtic
set noytic
set size 
set border 0
set multiplot layout 9,1
plot 'testlog' using 1 with steps
plot 'testlog' using 2 with steps
plot 'testlog' using 3 with steps
plot 'testlog' using 4 with steps
plot 'testlog' using 5 with steps
plot 'testlog' using 6 with steps
plot 'testlog' using 7 with steps
plot 'testlog' using 8 with steps
plot 'testlog' using 9 with steps
unset multiplot

