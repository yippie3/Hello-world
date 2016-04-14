import sys
from subprocess import Popen, PIPE, STDOUT
def log_cast(show_file,log_file):
    cmd = 'expect telnet_lib/fusion23.exp 10.20.98.200 {}'.format(show_file)
    print "\ngenerating log\n"
    f = open(log_file,"w")
    p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    for line in p.stdout:
        print "*",
        line = line.rstrip()
        f.write("{}\n".format(line))
    f.close()
    print "\n\nanalyzing log\n"
show_file = sys.argv[1] 
log_file = sys.argv[2]
try:
    log_cast(show_file,log_file)
except Exception as err:
    print err

















