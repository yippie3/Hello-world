import difflib
from subprocess import call
def cmpr(dft, run):
    f1 = open(dft, 'r')
    f2 = open(run, 'r')
    t1 = f1.read().splitlines(1)
    t2 = f2.read().splitlines(1)
    d = difflib.Differ()
    lll = list(d.compare(t1,t2))
    for line in lll:
        if line.startswith("+") or line.startswith('-') or line.startswith('!'):
            print line,
    f1.close()
    f2.close()

def nd(dft, run):
    file1 = open(dft, 'r')
    file2 = open(run, 'r')

    diff = difflib.ndiff(file1.readlines(), file2.readlines())
    delta = ''.join(x for x in diff if x.startswith('-') or x.startswith('+') or x.startswith('!'))
    print delta

    file1.close()
    file2.close()

def linebyline(dft,run):
    f1 = open(dft, 'r')
    f2 = open(run, 'r')
    t1 = f1.read().splitlines()
    t2 = f2.read().splitlines()
    d = difflib.Differ()
    diff = d.compare(t1, t2)
    print '\n'.join(diff)
try:
    call(["sh", "analyze/cmp_run.sh"])
except Exception as err:
    print err 
else:
    cmpr("analyze/default_config_verbose","analyze/run_config_verbose")
    
