#Do not attempt to add new questions/answers or blooks!
#these are currently hard coded! I aim to change that in the future

from menu import getMenu, cyptoHack
from snakeGame import runSnakeGame
from util import clear, coolprint, coolprint2
import time
import random

global questionSet
global answerSet
questionSet = {"1": "Which rarity of blooks cannot be sold? ", "2": "What is the highest rarity of blooks? ", "3": "Which rarity of blooks sell for 20 tokens? ", "4": "The lowest drop rate of chroma blooks is (decimal with % sign) ", "5": "The lengendary blook in the bot box is (2 words!) ", "6": "The Buddy Bot is (rarity) ", "7": "Who made blooket? ", "8": "The paid version of Blooket is Blooket (__) ", "9": "The spooky box is only shown during (holiday) ", "10": "The bizzard box is only shown during (holiday) "}
answerSet = {"1": "common", "2": "mythical", "3": "rare", "4": "0.02%", "5": "mega bot", "6": "rare", "7": "tom", "8": "plus", "9": "halloween", "10": "christmas"}
print("\u001b[38;5;50m-------------- BlooketDupe -----------------")
print("\u001b[38;5;87mEdition Chroma")
time.sleep(1.5)
from replit import db
print(" ")
coolprint()
print(" ")
time.sleep(0.5)
clear()
global username
coolprint2()
username = input("\u001b[38;5;50mEnter username: ")
try: 
	test = db[username + "blooks"]
except:
	print("NEW USER! Creating new account!")
	db[username + "blooks"] = ["starter"]
else:
	print("Welcome back " + username + "!")
	print("Number of tokens you have: " + str(db[username + "tokens"]))
try:
	test = db[username + "tokens"]
except:
	db[username + "tokens"] = 0
time.sleep(1.5)


while True:
	clear()
	itemMenu = getMenu()
	if itemMenu == "1":
		clear()
		qn = []
		for i in range(0, len(questionSet)):
			qn.append(i+1)
		print("-------------- Questions -----------------")
		qsn = str(random.choice(qn))
		print("\u001b[38;5;10mAnswer the question. \nQuestions and answers are from/related to the acutal Blooket. \nThey do not relate with Blooket Dupe (this game). \nWrong caps do not count as incorrect!")
		time.sleep(1)
		print(" ")
		question = questionSet[qsn]
		answer = answerSet[qsn]
		playerAn = input("\u001b[38;5;202m" + question)
		if playerAn.lower() == answer:
			print("\u001b[38;5;82mCORRECT!!")
			tokensAdded = random.randint(5, 10)
			db[username + "tokens"] += tokensAdded
			print("You got " + str(tokensAdded) + " tokens!")
		else:
			print("\u001b[38;5;1mINCORRECT!")
			print("No tokens added")
		time.sleep(1)
	elif itemMenu == "2":
		clear()
		rawtokens = runSnakeGame()
		Gottokens = int(rawtokens/4)
		time.sleep(1)
		clear()
		print("\u001b[38;5;230mYou got " + str(Gottokens) + " tokens!")
		db[username + "tokens"] += int(Gottokens)
		input("\u001b[38;5;1mGame Ended! Press enter to return to menu ")

		
	elif itemMenu == "3":
		clear()
		blooks = db[username + "blooks"]
		print("\u001b[38;5;87mBlooks are:")
		for i in range(0, len(blooks)):
			curBlook = blooks[i]
			if curBlook != "starter":
				print("\u001b[38;5;87m" + str(i) + ". " + curBlook)
		global sell
		sell = input("\u001b[38;5;230mTo sell blooks, enter it's number in the list above\nTo exit, type anything that is not number ")
		try:
			int(sell)
		except:
			pass
		else:
			int(sell)
			try:
				Blooks = db[username + "blooks"]
				curBlook = Blooks[int(sell)]
			
			except:
				print("\u001b[38;5;1mInvaild number")
			else:
				if curBlook == "Octopus":
					print("\u001b[38;5;230mSold Octopus for 3 tokens")
					db[username + "tokens"] += 3
					blooklist = db[username + "blooks"]
					blooklist.pop(int(sell))
					db[username + "blooks"] = blooklist
				elif curBlook == "Dog":
					print("\u001b[38;5;230mSold Dog for 7 tokens")
					db[username + "tokens"] += 7
					blooklist = db[username + "blooks"]
					blooklist.pop(int(sell))
					db[username + "blooks"] = blooklist
				elif curBlook == "Astronaut":
					print("\u001b[38;5;230mSold Astronaut for 20 tokens")
					db[username + "tokens"] += 20
					blooklist = db[username + "blooks"]
					blooklist.pop(int(sell))
					db[username + "blooks"] = blooklist
				elif curBlook == "Stars":
					print("\u001b[38;5;230mSold Stars for 3 tokens")
					db[username + "tokens"] += 3
					blooklist = db[username + "blooks"]
					blooklist.pop(int(sell))
					db[username + "blooks"] = blooklist
				else:
					print("\u001b[38;5;1mCannot sell this blook")
				
			time.sleep(1)	
	elif itemMenu == "4":
		clear()
		print("\u001b[38;5;87mProfile:")
		print("Username: " + username)
		print("Tokens: " + str(db[username + "tokens"]))
		print("View blooks via the main menu")
		input("\u001b[38;5;50mEnter to go back to menu")
	elif itemMenu == "5":
		while True:
			clear()
			print("\u001b[38;5;11mWelcome to the Blook Shop")
			print("Buy Blooks by entering the number!")
			print("Tokens: " + str(db[username + "tokens"]))
			print(" ")
			print("1. Astronaut: 25 tokens")
			print("2. Octopus: 5 tokens")
			print("3. Stars: 5 tokens")
			print("4. Box - equal chance of 4 blooks: 15 tokens")
			print("Type 5 to exit shop")
			buy = input("Enter number: ")
			if buy == "1":
				if db[username + "tokens"] >= 25:
					print("You got the Astronaut blook!")
					db[username + "blooks"].append("Astronaut")
					curtokens = db[username + "tokens"]
					newtokesn = curtokens - 25
					db[username + "tokens"] = newtokesn
					time.sleep(1)
				else:
					print("\u001b[38;5;1mNot enough tokens!")
					time.sleep(1)
			elif buy == "2":
				if db[username + "tokens"] >= 5:
					print("You got the Octopus blook!")
					db[username + "blooks"].append("Octopus")
					curtokens = db[username + "tokens"]
					newtokesn = curtokens - 5
					db[username + "tokens"] = newtokesn
					time.sleep(1)
				else:
					print("\u001b[38;5;1mNot enough tokens!")
					time.sleep(1)
			elif buy == "3":
				if db[username + "tokens"] >= 5:
					print("You got the Stars blook!")
					db[username + "blooks"].append("Stars")
					curtokens = db[username + "tokens"]
					newtokesn = curtokens - 5
					db[username + "tokens"] = newtokesn
					time.sleep(1)
				else:
					print("\u001b[38;5;1mNot enough tokens!")
					time.sleep(1)
			elif buy == "4":
				if db[username + "tokens"] >= 15:
					curtokens = db[username + "tokens"]
					newtokesn = curtokens - 15
					db[username + "tokens"] = newtokesn
					choosenBlook = random.randint(1, 4)
					print("OPENING BOX...")
					time.sleep(1.5)
					if choosenBlook == 1:
						print("You got the Stars blook!")
						db[username + "blooks"].append("Stars")
					elif choosenBlook == 2:
						print("You got the Octopus blook!")
						db[username + "blooks"].append("Octopus")
					elif choosenBlook == 3:
						print("You got the Astronaut blook!")
						db[username + "blooks"].append("Astronaut")
					elif choosenBlook == 4:
						print("You got the Dog blook!")
						db[username + "blooks"].append("Dog")
					time.sleep(1.5)
				else:
					print("\u001b[38;5;1mNot enough tokens!")
					time.sleep(1)

			elif buy == "5":
				break
			else:
				print("\u001b[38;5;1mInvalid")
				time.sleep(1)
		time.sleep(0.3)
	elif itemMenu == "6":
		clear()
		hum = input("\u001b[38;5;1mReally reset account? This will reset tokens to 0 and delete all your blooks.\n Type yes to confirm \nAnything else to cancel ")
		if hum == "yes":
			del db[username + "tokens"]
			del db[username + "blooks"]
			print("DELETED USER " + username + "!")
			input("The game will quit after you press enter\nStart the game again to create a new account!")
			break
		else:
			print("\u001b[38;5;10mYour account is safe!")
			input("Press enter to return to the menu")
	elif itemMenu == "7":
		print("Thanks for playing! Your blooks and tokens have been saved.\nJust put in the username you used (" + username + ") next time!")
		print("Write any issues at https://github.com/oliver408i/Blooket-Dupe-Edition-1/issues")
		break
	elif itemMenu == "8":
		cyptoHack(username)