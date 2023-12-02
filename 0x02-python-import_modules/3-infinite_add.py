#!/usr/bin/python3
if _name_ == "_main_":
	import sys
	sum = 0
	for i in range(len(sys.argv) - 1):
		sum += int(sys.argv[i + 1])
	print(sum)
