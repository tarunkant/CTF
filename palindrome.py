import itertools
from pwn import *
r = remote('ppc1.chal.ctf.westerns.tokyo',8765)
g=r.recv()
g=r.recv()
print g
g=g.split("\n")

name = 	g[5]
count=0
name = name.split(" ")	
words = list(itertools.product(name, repeat=2))
word_list = []
for i in words:
   		word_list.append("".join(i))	
for hell in word_list:
	if(hell[::-1]==hell):
		count=count+1
r.sendline(str(count))
print g
#print g[2]
for i in range(0,50):
	g=r.recv()
	print g
	g=r.recv()
	g=g.split("\n")
	print g
	name1 = g[2]
	print g[2]
	count1 = 0
	name1 = name1.split(" ")	
	words1 = list(itertools.product(name1, repeat=2))
	word_list1 = []
	for i in words1:
	    word_list1.append("".join(i))	
	for hell in word_list1:
		if(hell[::-1]==hell):
			count1=count1+1
	r.sendline(str(count1))