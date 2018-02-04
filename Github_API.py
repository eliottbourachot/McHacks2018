from urllib2 import Request, urlopen, URLError

def getGithubLevel(username):
	request = Request('https://api.github.com/users/'+username+'/repos')

	try:
		response = urlopen(request)
		github = response.read()
		return len(github)
	except URLError, e:
	    return 'No githubs. Got an error code:', e

#def rankGithubUsers
#def getHighestGithubRankedUser
#def getLowestGithubRankedUser
