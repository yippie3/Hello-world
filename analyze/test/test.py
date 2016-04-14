import sys
import difflib
def filter_out_qm(result):
        lres = []
        for l in result:
            if not l.startswith('? '):
                    lres.append(l)
        return lres
def filter_out_useful(result, keywords):
	a = str(keywords[0])
        lres = []
        for l in result:
            if l.startswith('? ') or l.startswith('+ ') or l.startswith('- ') or l.startswith('  '+a):
                    lres.append(l)
        return lres
def fenxi_useful(dd, keywords):
	resList = []
	resIndex = [] #same as dd
	c = '  '+str(keywords[0])
	i = 0 
	while i < len(dd)-1:

		if dd[i][0:len(str(keywords[0]))+2] in c and dd[i+1][0:len(str(keywords[0]))+2] in c:
			
			pass
	#		print "take out", i, "and", i+1
		else:
			if dd[i].startswith(c):
				print "check the command: ", dd[i]
			elif dd[i].startswith('+ ') and dd[i+1].startswith('? '):

				print "something is added\n", dd[i], dd[i+1] 
			elif dd[i].startswith('- ') and dd[i+1].startswith('? '):

				print "something is removed\n", dd[i], dd[i+1] 


	#		print "title",i
			resList.append(dd[i])
			resIndex.append(i)
		i += 1
	return resList
def fenxi_three_useful(dd, keywords):
	resList = []
	resIndex = [] #same as dd
	c = '  '+str(keywords[0])
	i = 0 
	a1 = "after"
	a2 = "before"
	count = 0
	while i < len(dd)-1:

		if dd[i][0:len(str(keywords[0]))+2] in c and dd[i+1][0:len(str(keywords[0]))+2] in c:
			
			pass
#			print "take out", i, "and", i+1
		else:
			if dd[i].startswith(c):
				count += 1
				print "\nNo.{0} Command check: {1}".format(count, dd[i]),
				print "************************************************************************************"
			elif dd[i].startswith('- ') and dd[i+1].startswith('? '):

				print "change\t\t",  dd[i][2:], 
			elif dd[i].startswith('- ') and not dd[i+1].startswith('? '):

				print "change \t\t",  dd[i][2:], 
			elif dd[i].startswith('+ ') and dd[i+1].startswith('? '):

				print "->    \t\t",  dd[i][2:], 
			elif dd[i].startswith('+ ') and not dd[i+1].startswith('? '):

				print "->    \t\t",  dd[i][2:], 


		i += 1 
	print "\t\t************************************************************************************"
	print "The total commands count:", count
	return resList
#function returns the index
print "Analysis section:"
print "Test comparision between:{0}".format(sys.argv[1]), "before\n",
print "                         {0}".format(sys.argv[2]), "after\n"
f1 = open(sys.argv[1], "r")
f2 = open(sys.argv[2], "r")
keywords = []
keywords.append(sys.argv[3])
a1 = f1.read()
a2 = f2.read()

d = difflib.Differ()
result = d.compare(a1.splitlines(1), a2.splitlines(1))

dd = filter_out_useful(result, keywords)
#final = fenxi_useful(dd, keywords)
final = fenxi_three_useful(dd, keywords)









f1.close()
f2.close()
