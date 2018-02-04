from itty import *
import urllib2
import json

######################################


class student:
    def __init__(self, name, languages, interest, gitLevel, LFM):
        """ Create a new point at x, y """
        self.name = name
        self.languages = languages
        self.interest = interest
        self.gitLevel = gitLevel
        self.LFM = LFM

def parseUserLanguages(userId, response):
    #upper case, take spaces out and parse the languages array (can do the same thing for the
    # interests array)
    
    #reads the array of all existing languages (not really necesary)
    file = open("programingLanguages.txt", "r")
    masterLanguages = ["" for x in range(256)]
    for i in range(256):
        masterLanguages[i] = file.readline()

    for i in  range(len(masterLanguages)):
        masterLanguages[i] = masterLanguages[i].upper()
        masterLanguages[i] = masterLanguages[i].replace(" ", "")
        masterLanguages[i] = masterLanguages[i].split(",")
        masterLanguages[i] = masterLanguages[i][0][:-1]
    for word in response.split(" "):
        word = word.upper()
        word = word.replace(",", "")
        if word in masterLanguages:
            if str(Users[userId].languages) == "None":
                Users[userId].languages = str(word)+","
            else:
                Users[userId].languages = str(Users[userId].languages)+str(word)+","
    return 0

def parseUserInterests(userId, response):
    Users[userId].interest = response
    return 0

def fillStudents(webhook, userId, name):
	if Users[userId] == None:
		Users[userId] = student(name, None, None, None, 0)
		question = "Hey, what can I help you with?"
		easyPost(webhook, question)
	if Users[userId].LFM == 0:
		Users[userId].LFM = 1
		question = "I understand that you're looking for a team member. What languages do you know?"
		easyPost(webhook, question)

	if Users[userId].LFM == 1:
		parseUserLanguages(userId, response_str) #fills the student()

		Users[userId].LFM = 2
		question = "Awesome! And what kind of projects would you be interested in working on?"
		easyPost(webhook, question)

	if Users[userId].LFM == 2:
		parseUserInterest(userId, response_str)

##################################################


Users = {}
# userId: student
# 123456: (self, name, languages, interest, gitLevel, LFM, LFT)

#create some Users
Users[0] = student("carlos","JAVASCRIPT,PYTHON","game development, bots",14352, 0)
Users[1] = student("stacy","javascript, Python ","game development, bots",12, 0)
Users[2] = student("lucy","Java Script , c++","game development, bots",15,0)
Users[3] = student("andres","c++,PYTHON","game development, bots",142,0)
Users[4] = student("erin","javascript,c, Python, unity ","game development, bots",143652,0)
Users[5] = student("john","javascript,c, dart,  ","game development, bots",152,0)
Users[6] = student("hector","javascript,c, Python ","game development, bots",1442,0)
Users[7] = student("mark","javascript, Python ","game development, bots",1152,0)
Users[8] = student(None, None, None, None, 0)

##################################################


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
		fillStudents(webhook, webhook['data']['personId'], content['personEmail'])
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