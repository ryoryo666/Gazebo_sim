# -*- coding: utf-8 -*-

def kill_node(nodename):
    p2=Popen(['rosnode','list'],stdout=PIPE)
    p2.wait()
    nodelist=p2.communicate()
    nd=nodelist[0]
    nd=nd.split("\n")
    for i in range(len(nd)):
        tmp=nd[i]
        ind=tmp.find(nodename)
        if ind==1:
            call(['rosnode','kill',nd[i]])
            break
