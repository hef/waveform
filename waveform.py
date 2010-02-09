#!/usr/bin/env python
import sys
import Gnuplot

log = open(sys.argv[1])
header = log.readline().strip()
columns = len(header.split("\t"))
print columns



