#!/usr/bin/ruby
require 'rubygems'
require 'gnuplot'

filename = ARGV.first
IO.readlines(filename).first do |names|
	names.split(\t).each do |header|
		p values
	end
end
IO.readlines( filename).each do |line|
	values = line.split("\t") 
	p values
end
