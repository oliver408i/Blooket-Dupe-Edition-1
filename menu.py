def getMenu():
	print("\u001b[38;5;87m -----------------> MENU <----------------")
	print("\u001b[38;5;141m1. Answer a Question!\n2. Escape the Snake!\n8. Cypto Hack (Beta)\n3. View or Sell Blooks\n4. View Profile (tokens)\n5. Shop\n6. Reset Account\n7. Quit and Save")
	menuItem = input("\u001b[38;5;111mEnter a number: ")
	return menuItem
def cyptoHack(username):
	from util import matprint, clear
	import random
	from replit import db
	clear()
	welcomeSign = 'Welcome ' + username + '!'
	matprint(['Cypto Hacking Terminal', welcomeSign], random=False, sleeping=0.1, between=0.8, times=1)
	mathqset = ["2 + 2", "3 + 8"]
	answerkey = [4, 11]
	cq = random.randint(0, 1)
	cqy = mathqset[cq]
	answer = input("What is " + cqy + "? ")
	if answer == str(answerkey[cq]):
		matprint(['Correct!', '+ 3 tokens'],random=False, sleeping=0.1, between=0.8, times=1)
		db[username + "tokens"] += 3
		botnamelist = ["Eatingchikens", "IWantCypto", "Hecker1", "yeetthehack", "notBlooketPlayer", "noUsername"]
		botname = random.choice(botnamelist)
		matprint(["Hacking " + botname + "...", ])
		matprint(["Choose a password from this list", "BlOkEtDupe, sNakeGamePro980, cypto234, passwordU34, SUS"])
		input("Guess the password: ")
		matprint(["Hacking..."])
		import time
		time.sleep(1)
		gotCorrect = random.randint(1, 2)
		if gotCorrect == 2:
			cyptoGot = random.randint(10, 130)
			matprint(["Correct!", "You stole " + str(cyptoGot) + " cypto!"])
			matprint(["END", "You got " + str(int(cyptoGot/4)) + " tokens!", "Returning to main menu..."])
			db[username + "tokens"] += int(cyptoGot/7)
		else:
			matprint(["Failed to log in!", "Incorrect password!"])

	else:
		matprint(['Incorrect!!', '- 2 tokens'],random=False, sleeping=0.1, between=0.8, times=1)
		curtokens = db[username + "tokens"]
		newtokesn = curtokens - 2
		db[username + "tokens"] = newtokesn
		