#!/usr/bin/env python
"""
  Simple binary dump compare, can be used to compare two dumps of registers values.
  Lists the offset where two 32bit values differ + both values.
  Probably not the most optimal for using on large dumps, it's for quick compare
  of dumps up to few KB (e.g. ethernet controller registers compare while debuging).

  Usage: ./dmpdiff.py dump_file1.img dump_file2.img

"""
import sys, struct

if len(sys.argv) > 1:
	name1=sys.argv[len(sys.argv)-2]
	name2=sys.argv[len(sys.argv)-1]
## open files
try: 
	file1=open(name1, "rb")
except: 
	print "cannot open file:", name1
	file1.close()
	exit()
try: 
	file2=open(name2, "rb")
except: 
	print "cannot open file:", name2 
	file2.close()
	exit()

x=4
y=4
which_word=0
reg_diff_cnt=0
print "Comparission of:"
print "File A -- %s" % name1
print "File B -- %s" % name2
print "--------------------------------------"
print "| Offset:  | ValA:      | ValB:      |"
print "--------------------------------------"
while (x == 4) and (y == 4):
	a=file1.read(4)
	b=file2.read(4)
	x=len(a)
	y=len(b)
	if (a != b):
		reg_diff_cnt+=1
		# always prints in BE (just as it was read, intepretation to be done by user)
		print " %Xh       0x%.8x   0x%.8x" % (which_word*4, struct.unpack('>L', a)[0], struct.unpack('>L', b)[0])
	which_word+=1
print "--------------------------------------"
print " Summary:"
print " Diff registers count %d           " % reg_diff_cnt

file2.close()
file1.close() 
