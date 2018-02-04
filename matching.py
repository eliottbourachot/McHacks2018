

class student:
    def __init__(self, name, languages, interest, gitLevel, LFM):
        """ Create a new point at x, y """
        self.name = name
        self.languages = languages
        self.interest = interest
        self.gitLevel = gitLevel
        self.LFM = LFM
        self.LFT = LFT

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
Users[8] = student(None, None, None, None, None)

matchedUsers = matchUsers(8, "I need someone who knows python and javascript")    
print matchedUsers


def fillStudents(webhook, userId):
    if Users[userId].LFM == 0:
        Users[userId].LFM = 1
        question = "I understand that you're looking for a team member. What languages do you know?"
        easyPost(webhook, question)

    if Users[userId].LFM == 1:
        parseUserLanguages(userId, response_str) #fills the student()
        
        Users[userId].LFM = 2
        question = "Awesome! And what kind of projects would you be interested in working on?"
        easyPost(webhook, question)

    if Users[userId].LFM = 2:
        parseUserInterest(userId, response_str)