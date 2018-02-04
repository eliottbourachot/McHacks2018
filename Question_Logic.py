

QA_D = {} #key["Answer_keyword"] = ""
Users_D = {}


def fillQuestionAnswerDictionary:
	QA_D[''] = ''

#States: LFM_#, 0 = beginning, 1 = answered 1st question, 2 = answered 2nd question, ...
def lookingForMember(userId):
	User_D[userid] = "LFM_0"
	question = "I understand that you're looking for a team member. What qualifications should they have?"
	easypost(msg)

def lookingForTeam
