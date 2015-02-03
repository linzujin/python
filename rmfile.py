#!user/bin/python
#coding:utf8

import os

fp = open('files.txt','r')
content = fp.readlines()
for i in content:
    print i.strip('\n')
    os.remove(i.strip('\n'))
fp.close()
