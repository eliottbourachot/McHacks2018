from itty import *
import urllib2
import json

def sendSparkGET(url):
	request = urllib2.Request(url,
    	headers={"Accept" : "application/json",
    	"Content-Type":"application/json"})
	request.add_header("Authorization", "Bearer "+bearer)
	contents = urllib2.urlopen(request).read()
	response = json.loads(contents)
	return response

def sendSparkPOST(url, data):

	request = urllib2.Request(url, json.dumps(data),
		headers={"Accept" : "application/json",
		"Content-Type":"application/json"})
	request.add_header("Authorization", "Bearer "+bearer)
	contents = urllib2.urlopen(request).read()
	print "sendSparkPOST"
	return contents

def easyPost(webhook, msg):
	return sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "text": msg})

'''
def sendSparkMessage(url, roomId, text):
	request = urllib2.Request(
		url,
		data={"roomId" : roomId,
		"text" : text},
		headers={"Accept" : "application/json",
		"Content-Type":"application/json"})
	request.add_header("Authorization", "Bearer "+bearer)
	contents = urllib2.urlopen(request).read()
	echo = json.loads(contents)
	return echo
'''
@get('/')
def index(request):
	print("gottem")
	return "true"

@post('/')
def index(request):
	print "INDEX_start"
	webhook = json.loads(request.body)
	content = sendSparkGET('{0}/{1}'.format(msgUrl,webhook['data']['id']))
	print str(content['text'])
	print("ID"+webhook['data']['personId'])
	print("ID"+botId)
	if webhook['data']['personId'] != botId:
		msg = "Andres is the best"
		print webhook['data']['id']
		result = easyPost(webhook, msg)
		#result = sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "text": msg})
		#sendSparkGET('{0}/{1}'.format(msgUrl,webhook['data']['id']))
		print result
		return "true"
		print "INDEX_end"
	else:
		return 0
####CHANGE THIS VALUE#####
botId = "Y2lzY29zcGFyazovL3VzL1BFT1BMRS81NDIxNjk5ZC0zYzIzLTQ1NjUtOTk2YS01NmZhNjU2M2ZlNWE"
msgUrl = "https://api.ciscospark.com/v1/messages"
bearer = "MTQxNjUxMWYtYjA3My00M2UzLTlkMzItN2M2MmE4Y2JlNGMzMWFjNmRmMWQtMjJj"

run_itty(server='wsgiref', host='0.0.0.0', port=8080)

#my id is Y2lzY29zcGFyazovL3VzL1BFT1BMRS9hYmIzN2QwNi1jMWM1LTQ2MDktOThlYS0zYzk5OWFhYjk2MjE
#bots id is Y2lzY29zcGFyazovL3VzL1BFT1BMRS81NDIxNjk5ZC0zYzIzLTQ1NjUtOTk2YS01NmZhNjU2M2ZlNWE