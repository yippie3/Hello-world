import re
import sys
import collections
# parsing GVR 2 column PORTs, i.e. show gvr gi-ports
def show_gvr_2_column_port(show_gvr_pat,m1,i,origin,r1,qianzhui,path):
                        port = ""
                        if m1.group(1) == show_gvr_pat:
                                f = open(path+qianzhui+'-'+show_gvr_pat.replace(' ','-'),'w')
                                f.write('global ayr\n')
                                while i+1<len(origin) and not re.search(r1,origin[i+1]):
                                        r2 = r'(\d+/\d+)\s+(\w+).{2}'
                                        m2 = re.search(r2, origin[i])#match show gvr gi ports
                                        if m2:
                                                p_s1 ='set ayr({0},{1},{2},state) "{3}"\n'.format(qianzhui, show_gvr_pat.replace(' ',''), m2.group(1).replace(' ', ','), m2.group(2))
                                                f.write(p_s1)
                                                port+=str(m2.group(1)+' ')
                                        i = i+1

                                r2 = r'(\d+/\d+)\s+(\w+).{2}'
                                m2 = re.search(r2, origin[i])#add one more line due to while loop...
                                if m2:
                                        p_s1 ='set ayr({0},{1},{2},state) "{3}"\n'.format(qianzhui, show_gvr_pat.replace(' ',''), m2.group(1).replace(' ', ','), m2.group(2))
                                        f.write(p_s1)
                                        port+=str(m2.group(1)+' ')

                                intro = 'set ayr({0},{1},{2}) "{3}"\n'.format(qianzhui, show_gvr_pat.replace(' ', ''), 'port', port)
                                f.write(intro)
## parsing GVR 3 columns PORTS i.e. show gvr analyzer-ports, ingress-ports
def show_gvr_3_column_port(show_gvr_pat,m1,i,origin,r1,qianzhui, path):
                        port = ""
                        if m1.group(1) == show_gvr_pat:
                                f = open(path + qianzhui+ '-' + show_gvr_pat.replace(' ', '-'),'w')
                                f.write('global ayr\n')
                                while i+1<len(origin) and not re.search(r1,origin[i+1]):
                                        r2 = r'(\d+/\d+)\s+(\w+)\s+(\w+).{2}'
                                        m2 = re.search(r2, origin[i])#match show gvr 3 colums ports
                                        if m2:
                                                p_s1 ='set ayr({0},{1},{2},state) "{3}"\n'.format(qianzhui, show_gvr_pat.replace(' ',''), m2.group(1).replace(' ', ','), m2.group(2))
                                                p_s2 ='set ayr({0},{1},{2},disabledbygvr) "{3}"\n'.format(qianzhui, show_gvr_pat.replace(' ',''), m2.group(1).replace(' ', ','), m2.group(3))
                                                f.write(p_s1)
                                                f.write(p_s2)
                                                port+=str(m2.group(1)+' ')
                                        i = i+1

                                r2 = r'(\d+/\d+)\s+(\w+)\s+(\w+).{2}'
                                m2 = re.search(r2, origin[i])#match show gvr 3 colums ports
                                if m2:
                                        p_s1 ='set ayr({0},{1},{2},state) "{3}"\n'.format(qianzhui, show_gvr_pat.replace(' ',''), m2.group(1).replace(' ', ','), m2.group(2))
                                        p_s2 ='set ayr({0},{1},{2},disabledbygvr) "{3}"\n'.format(qianzhui, show_gvr_pat.replace(' ',''), m2.group(1).replace(' ', ','), m2.group(3))
                                        f.write(p_s1)
                                        f.write(p_s2)
                                        port+=str(m2.group(1)+' ')

                                intro = 'set ayr({0},{1},{2}) "{3}"\n'.format(qianzhui, show_gvr_pat.replace(' ', ''), 'port', port)
                                f.write(intro)
## parsing GVR 2 columns i.e. show gvr gvcp, show gvr
def show_gvr_2_column(show_gvr_pat,m1,i,origin,r1,qianzhui,path):
                        if m1.group(1) == show_gvr_pat:
                                f = open(path + qianzhui + '-' + show_gvr_pat.replace(' ', '-'),'w')
                                f.write('global ayr\n')
                                while i+1<len(origin) and not re.search(r1,origin[i+1]):
                                        r2 = r'(.*\b).*:\s+(.*)\D{2}'
                                        m2 = re.search(r2, origin[i])#match show gvr
                                        if m2:
                                                tcl_show_gvr ='set ayr({0},{1},{2}) "{3}"\n'.format(qianzhui, 'showgvr', m2.group(1).replace(' ', ','), m2.group(2))
                                                f.write(tcl_show_gvr)
                                        i = i+1

                                r2 = r'(.*\b).*:\s+(.*)\D{2}'
                                m2 = re.search(r2, origin[i])#match show gvr
                                if m2:
                                        tcl_show_gvr ='set ayr({0},{1},{2}) "{3}"\n'.format(qianzhui, 'showgvr', m2.group(1).replace(' ', ','), m2.group(2))
                                        f.write(tcl_show_gvr)


                                f.close()
## main fuction to analysis baseline log and put into variables
#==============================================================
def show_int_cast(pat,m1,i,origin,r1):
                        if m1.group(1).startswith(pat):
				rx = map(int, re.findall(r'casts: (\d+)', origin[i+1]))#match device_keywords
				tx = map(int, re.findall(r'casts: (\d+)', origin[i+2]))#match device_keywords
				if rx and tx:
				    if all(v == 0 for v in tx) and all(v == 0 for v in rx): 
					pass
				    else:
					print origin[i],
					print origin[i+1],
					print origin[i+2],
def show_int_rate(pat,m1,i,origin,r1):
                        if m1.group(1).startswith(pat):
				linerate = re.findall(r'Line-rate\s+(\S+)%\s+(\S+)%', origin[i+1])#match device_keywords
				if linerate:
				    linerate = map(float, (linerate[0]))
				    if all(v == 0 for v in linerate): 
					pass
				    else:
					print origin[i],
					print origin[i+1],
def show_sfm_link_conn(pat,m1,i,origin,r1):
                        r2 = r'SFM'
                        r3 = r'FAP'
                        if m1.group(1).startswith(pat):
                                while i+1<len(origin) and not re.search(r1,origin[i+1]):
                                        m2 = re.search(r2, origin[i])#match sfm 
                                        m3 = re.search(r3, origin[i])#match fap 
                                        if m2 or not m3:
                                            print origin[i]
                                        i = i+1
                                if m2 or not m3:
                                    print origin[i]
def show_sfm_sta(pat,m1,i,origin,r1):
                        r2 = r'SFM'
                        r3 = r'DC'
                        r4 = r'Total\D+(\d+)'
                        r5 = r'Dropped\D+(\d+)'
                        if m1.group(1).startswith(pat):
                                while i+1<len(origin) and not re.search(r1,origin[i+1]):
                                        m2 = re.search(r2, origin[i])#match sfm 
                                        m3 = re.search(r3, origin[i])#match dch dcm dcl
                                        m4 = re.search(r4, origin[i])#match total 
                                        m5 = re.search(r5, origin[i])#match dropped
                                        if m2 or m3:
                                            print origin[i],
                                        elif m4:
                                            print '\t', ''.join(origin[i].split()[1:6])
                                        elif m5:
                                            print '\t', ''.join(origin[i].split()[1:5])
                                        i = i+1
                                if m2 or m3 or m4:
                                    print origin[i]
                                elif m4:
                                    print ''.join(origin[i].split()[1:6])
                                elif m5:
                                    print '\t', ''.join(origin[i].split()[1:5])
def show_sfm_link(pat,m1,i,origin,r1):
                        r2 = r'SFM'
                        r3 = r'\|(.*?)\|'
                        if m1.group(1).startswith(pat):
                                while i+1<len(origin) and not re.search(r1,origin[i+1]):
                                        m2 = re.search(r2, origin[i])#match sfm 
                                        m3 = re.search(r3, origin[i])#match sfm 
                                        if m2:
                                            print origin[i]
                                        elif m3:
                                            if m3.group(1) != '    -      ':
                                                print origin[i]
                                        i = i + 1
                                if m2:
                                    print origin[i]
                                elif m3:
                                    if m3.group(1) != '    -      ':
                                        print origin[i]

def cast_to_object(baselinelog, device_keywords):
#        print "the log you are checking is", baselinelog
#        print "the device prompt you are checking is", device_keywords
        fr = open(baselinelog, 'r')
        origin = fr.readlines()
#        r0=r'(.*\/)Baseline_(\d+)_log'
#        m0=re.search(r0,baselinelog)
#        path = m0.group(1)
#        qianzhui=m0.group(2)
#       print "qianzhui is", qianzhui
#       print "path is", path
        r1 = r'(?:{0})(.*\b)'.format(device_keywords)
####============================
        i = 0
        while i < len(origin):
                m1 = re.search(r1, origin[i])#match device_keywords
                if m1: 
                    show_int_cast(" sh int e ",m1,i,origin,r1)                
                    show_int_rate(" sh int stats d int e ",m1,i,origin,r1)                
                    show_sfm_link_conn(" sh sfm link-conn | nomore",m1,i,origin,r1)                
                    show_sfm_sta(" sh sfm sta | nomore",m1,i,origin,r1)
                    show_sfm_link(" sh sfm link | nomore",m1,i,origin,r1)
#                else:
#                        pass
#                       print "nothing found for this cmd"
                i = i+1
####===============================
        fr.close()
#print sys.argv
#['analyze.py', 'log/well', 'MMVM#', '|', 'tee', 'log/well_result']
if len(sys.argv) == 3:
    keywords = sys.argv[2]#'telnet@BR2#' 'telnet@MLX-GVR#'
    cast_to_object(sys.argv[1], keywords)
else:
    print "usage: "
    print "python analyze.py log/to_be_analyzed 'MMVM#'"

