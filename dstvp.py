from collections import defaultdict
from sys import argv

myId = argv[1]

routeTable = defaultdict(defaultdict)
fp = open('initial_dv.txt')

while 1:
	line = fp.readline()
	if not line:
		break
	mylist = line.strip().split(',')
	if mylist[0] == myId:
		routeTable[mylist[1]]['via'] = mylist[1]
		routeTable[mylist[1]]['port'] = mylist[2]
		routeTable[mylist[1]]['cost'] = mylist[3]	

