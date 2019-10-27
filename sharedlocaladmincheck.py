#!/usr/bin/python
'''
Checking shared local administrators 
Created by DVS
'''
import subprocess, os, argparse, time, datetime, socket, base64, threading, Queue, hashlib, binascii, signal, sys, getpass
from subprocess import check_output
from subprocess import PIPE
import re
import shlex
import sys
import getopt
from collections import Counter
import collections
list = []
a=0
dom = "workgroup"
try:
    opts, args = getopt.getopt(sys.argv[1:], 'h:', ['help'])
except getopt.GetoptError:
    print("Usage: sharedlocalhashv3 [hash file from mysecretdump.py]")
    sys.exit(2)

for opt, arg in opts:
        if opt in ('-h', '--help'):
                print("Usage: hashcatmatch [hash file from mysecretdump.py]")

file_1 = str(sys.argv[1])
for line_1 in open(file_1):
	line_1 = line_1.strip()
	lm = line_1.split(":")[2]
	ntlm = line_1.split(":")[3]
	hash = lm+":"+ntlm
	hash = list.insert(a, hash)
counter = collections.Counter(list)
common = counter.most_common()
num = len(common)
for j in range(0, num):
	numb = common[j][1]
	if numb > 1:
		print "HASH:","["+str(common[j][0])+"]", "No. of times password is shared:","("+str(common[j][1])+")"
		for line_2 in open(file_1):
			line_2 = line_2.strip()
			ip = line_2.split("\t")[0]
			uname2 = line_2.split("\t")[1]
			uname2 = uname2.split(":")[0]
			lm2 = line_2.split(":")[2]
			ntlm2 = line_2.split(":")[3]
			hash2 = lm2+":"+ntlm2
			if str(common[j][0]) == hash2:
				cmd2 = ("cme smb -u {} -H {} -d {} {} | grep -v '[*]' 2> /dev/null").format(uname2, hash2, dom, ip)
				proc = os.popen(cmd2).readlines()
#				print proc
				for x in proc:	
					admin = filter(None, x)
					admin = admin.split()
					ansi_escape = re.compile(r'\x1b[^m]*m')
#					print admin
					ips = admin[1]
					hname = admin[3]
					uname3 = admin[5].split("\\")[1]
					cmd3 = ("cme smb {} | grep '[*]' | grep -v 'KTHXBYE!' 2> /dev/null").format(ip)
					proc2 = proc = os.popen(cmd3).readlines()
					for w in proc2:
						w = filter(None, w)
						w = w.split()
						ansi_escape = re.compile(r'\x1b[^m]*m')
						doma = w[-3].split(":")[1].split(")")[0]
#						print doma
						if "Pwn3d" in admin[7]:
							print ips+"\t"+hname+"\t"+uname3+"\t"+doma+"\t"+"Local Administrator"
						if "Pwn3d" not in admin[7] and "[+]" in admin[4]:
							print ips+"\t"+hname+"\t"+uname3+"\t"+doma+"\t"+"Local User"
						if "STATUS_PASSWORD_EXPIRED" in admin[7]:
							print ips+"\t"+hname+"\t"+uname3+"\t"+doma+"\t"+"PASSWORD EXPIRED"
						if "STATUS_LOGON_FAILURE" in admin[7]:
							print ips+"\t"+hname+"\t"+uname3+"\t"+doma+"\t"+"THIS IS UNUSUAL - SAYS LOGON FAILURE (CHECK MANUALLY)"

