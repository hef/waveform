waveform
========

waveform Generator for logisim logs

purpose:
--------
CS266 at UIC has most students use [hades](http://tams-www.informatik.uni-hamburg.de/applets/hades/html/) to complete the projects.  The long and short of it is that The software kind of sucks.

I decideded to use [logisim](http://ozark.hendrix.edu/~burch/logisim/) insead.

As far as CS266 is concerned, logisim has one shortcoming, it cannot generate waveforms.

This project is my attempt to make up for that shortcoming.

usage:
------
*  In logisim, got Simulate >> logging...
*  In selection, add whatever inputs, output or probes you want.  The order will affect the order they come out in the plot.
*  click the file tab >> select, and save the log file somewhere.
finally, run

`./waveform.py mylogisimloggile.log > myimage.svg`

The svg image should open in firefox for viewing.  It should scale well also.
