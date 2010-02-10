#!/usr/bin/env python
import sys
import Gnuplot

#calculate number of plots to make
log = open(sys.argv[1])
header = log.readline().strip()
columns = len(header.split("\t"))

waveform = Gnuplot.Gnuplot(debug=1)
waveform("set terminal svg enhanced size 1000 1000 fname \"Times\" fsize 10")
waveform("set key autotitle columnhead")
waveform("set border 3")
waveform("set multiplot layout %d,1"%(columns))
for plotIndex in range(1,columns):
	waveform.plot("'%s' using %d with steps"%(sys.argv[1],plotIndex))
waveform("unset multiplot")


