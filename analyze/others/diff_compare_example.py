import sys
import difflib
def grab_roi(result, keywords):
        a = []
        identical = True
        for index, l in enumerate(result):
                if l.startswith(keywords):
                        a.append(l)
                elif l.startswith('+ ') or l.startswith('- '):# or l.startswith('? '):
                        a.append(l)
                        identical = False
                else:
                        pass
        if identical == True:
                print "\t\tnothing changed!"
        return a

f1 = open(sys.argv[1], "r")
f2 = open(sys.argv[2], "r")
fileOne = f1.read()
fileTwo = f2.read()

d = difflib.Differ()
result = d.compare(fileOne.splitlines(1),fileTwo.splitlines(1))

keywords = '  '+sys.argv[3]

#keywords = '  telnet@BR2#'
analysis_1st = grab_roi(result, keywords)
print analysis_1st
#case function here
#################
#   +    #   -
#   _    #   +
#       #
#       #
#       #
###################

f1.close()
f2.close()

