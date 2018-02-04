from urllib2 import Request, urlopen, URLError

username = "arknave"
request = Request('https://api.github.com/users/'+username+'/repos')

try:
	response = urlopen(request)
	github = response.read()
	print len(github)
except URLError, e:
    print 'No githubs. Got an error code:', e