import os, sys, select, subprocess

temp = ['mosquitto_sub', '-h', 'localhost', '-t', 'projet/temp']
hum = ['mosquitto_sub', '-h', 'localhost', '-t', 'projet/humidity']
p1 = subprocess.Popen(temp, stdout=subprocess.PIPE)
p2 = subprocess.Popen(hum, stdout=subprocess.PIPE)

poll = select.poll()
poll.register(p1.stdout)
poll.register(p2.stdout)

while True:
    rlist = poll.poll()
    for fd, event in rlist:
        with open('test.txt', 'w') as f:
            f.write(os.read(fd, 1024).decode("utf-8"))