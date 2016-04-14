f = open("enable_port_slot","w")
f.write("con t\n")
for i in range(1,73):
    f.write("int e {}/{}\nno sh\n".format(1,i))

for i in range(3,61):
    f.write("int e {}/{}\nno sh\n".format(3,i))

for i in range(7,73):
    f.write("int e {}/{}\nno sh\n".format(7,i))

f.write("end\n")

f = open("disble_port_slot","w")
f.write("con t\n")
for i in range(1,73):
    f.write("int e {}/{}\nsh\n".format(1,i))

for i in range(3,61):
    f.write("int e {}/{}\nsh\n".format(3,i))

for i in range(7,73):
    f.write("int e {}/{}\nsh\n".format(7,i))

f.write("end\n")

