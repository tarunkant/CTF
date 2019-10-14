import os
from sys import argv


i=0
f=open(argv[1])
r=f.read()
r=r.split('\n')
#Password

for p in r:

	if(len(p)==6 and not p.isdigit()):
		print p 
        	os.system("unzip -B -P " + p + " ~/CTF/2017/SHACTF/zipfiletwo.zip")

os.system("cat flag.txt*")        
