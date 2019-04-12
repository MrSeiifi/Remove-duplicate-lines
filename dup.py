import sys
try:	
	n = sys.argv[1]
	if n == "-h":
		2/0
	try:
		qq = n.split(".")
		s = qq[0]+"2."+qq[1]
	except:
		pass
	f = open(n, "r")
	l = open(s, "w")
	g = open(s, "r")
	e = open(n, "a")
	e.writelines("\n")
	e.close()

	x = []
	y = []
	o = 0
	for i in f:
		x.append(i)
	for a in x:
		if a not in y:
			q = open(s, "a")
			q.writelines(a)
			q.close()
		else:
			print "found "+a
		for i in g.readlines():
			y.append(i)
except IndexError as i:
	print """

	python dup.py -h

		"""
except IOError as IO:
	print IO
except ZeroDivisionError as z:
	print """

	Usage: python dup.py source.txt

		"""
