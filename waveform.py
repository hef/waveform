#!/usr/bin/env python
import sys
import Gnuplot
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--format", dest="format", help="Format to use", default="svg")
parser.add_option("-i", "--input", dest="input", help="Input File")
parser.add_option("-o", "--output", dest="output", help="Output File")
(options, args) = parser.parse_args()
print options
print options.input
formatString = {
	'svg': "svg enhanced size 1000 1000 fname \"Times\" fsize 10",
	'epslatex': "epslatex size 12cm,12cm font \"ptm\" 8"
}

#calculate number of plots to make
log = open(options.input)
header = log.readline().strip()
columns = len(header.split("\t"))

waveform = Gnuplot.Gnuplot(debug=1)
waveform("set terminal %s"%(formatString[options.format]))
waveform("set output \"%s\""%(options.output) )
waveform("set key autotitle columnhead")
waveform("set border 3")
waveform("set multiplot layout %d,1"%(columns))
for plotIndex in range(1,columns+1):
	waveform.plot("'%s' using %d with steps"%(options.input,plotIndex))
waveform("unset multiplot")


