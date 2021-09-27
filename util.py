def clear():
	from os import system, name

	def clear_screen():
			if name == 'nt':
					_ = system('cls') 
			else:
					_ = system('clear')

	clear_screen()
def coolprint():
	# import packages
	from time import sleep
	from rrandom import randintt, choiice, shuffle
	from typping import col, c

	# initilize variables
	# random characters
	chars = '!<>-_\\/[]{}—=+*^?#________1234567890@?!,.$'

	# phrases
	#phrases = [list]

	def scramble(thing, finished, chance, canfinish=True):
		c() # clear screen.
		new = '' # to print
		undecorated = [] # return to check whether it is finished
		for i in thing:
			scramb = randintt(0, 70)

			multi = (len(finished) / 85)
			if chance * 100 * multi >= scramb:
				ch = choiice(chars)
				new += col('BRIGHT_BLACK') + ch + col('end')
				undecorated.append(ch)
			else:
				new += col('white') + i + col('end')
				undecorated.append(i)

		if not canfinish and new == finished:
			ch = choiice(chars)
			new[-1] = col('BRIGHT_BLACK') + ch + col('end')
			undecorated[-1] = ch
		# writing(new)
		print(new)
		return undecorated

	# to be added: phrase sets :D
	# basically
	# the function can take in a list of phrases and got through each list
	def matprint(phrases, random=False, sleeping=0.1, between=0.8, times='inf'):
		if random:
			lst = shuffle([list(i) for i in phrases])
		else:
			lst = [list(i) for i in phrases]

		i = 0
		div = 2
		cur = lst[i]
		prev = cur.copy()
		if times != 'inf':
			for _ in range(times * len(lst)):
				chance = 100
				if i >= len(lst) - 1:
					if random:
						lst = shuffle([list(i) for i in phrases])
					i %= len(lst)
				cur = lst[i]
				j = 0
				if len(cur) == len(prev):
					# use = cur.copy()
					# cur = []
					# j = 0
					temp = scramble(cur, cur, chance, False)
					sleep(sleeping)
					chance /= div
					while temp != cur:
						# if len(cur) != len(use):
						# 	cur.append(use[j])
						# 	j += 1
						temp = scramble(cur, cur, chance)
						chance /= div
						sleep(sleeping)
					prev = cur.copy()
				elif len(cur) < len(prev):
					dd = 5
					use = cur.copy()
					cur += [prev[i] for i in range(len(cur), len(prev) - len(cur))]
					j = 0
					temp = scramble(cur, use, chance, False)
					chance /= (div / dd)
					while temp != use:
						if len(cur) > len(use):
							cur = cur[:-1]
							temp = scramble(cur, use, chance, False)
						else:
							temp = scramble(cur, use, chance)
						chance /= (div / dd)
						if dd > 1:
							dd -= 0.5
							
						sleep(sleeping)

					prev = use.copy()
				else:
					use = cur.copy()
					cur = cur[:-len(prev)]
					# cur = []
					j = len(cur)
					# j = 0
					temp = scramble(cur, use, chance, False)
					chance /= div
					dd = len(cur) / len("The impossible is pos") * 2
					while temp != use:
						if len(cur) < len(use):
							cur.append(use[j])
							j += 1
						temp = scramble(cur, use, chance)
						
						chance /= (div / dd)
						if dd > 1:
							dd -= 0.5
								
						sleep(sleeping)
					prev = use.copy()
				if between == 'SMART':
					SLEEPS = len(''.join(cur).split(' ')) / (200 / 60) + 0.8
				else:
					SLEEPS = between
				sleep(SLEEPS)
				i += 1
		else:
			while True:
				chance = 100
				if i >= len(lst) - 1:
					if random:
						lst = shuffle([list(i) for i in phrases])
					i %= len(lst)
				cur = lst[i]
				j = 0
				if len(cur) == len(prev):
					# use = cur.copy()
					# cur = []
					# j = 0
					temp = scramble(cur, cur, chance, False)
					sleep(sleeping)
					chance /= div
					while temp != cur:
						# if len(cur) != len(use):
						# 	cur.append(use[j])
						# 	j += 1
						temp = scramble(cur, cur, chance)
						chance /= div

						sleep(sleeping)
					prev = cur.copy()
				elif len(cur) < len(prev):
					dd = 5
					use = cur.copy()
					# cur += [prev[i] for i in range(len(cur), len(prev) - len(cur))]
					# cur = []
					j = 0
					temp = scramble(cur, use, chance, False)
					chance /= (div / dd)
					while temp != use:
						# if cur == list('be turned upside downndin'): print(cur, use, temp)
						# if len(cur) > len(use):
						# 	cur = cur[:-1]
						# 	temp = scramble(cur, use, chance, False)
						temp = scramble(cur, use, chance)
						chance /= (div / dd)
						if dd > 1:
							dd -= 1.5
							
						sleep(sleeping)

					prev = use.copy()
				else:
					use = cur.copy()
					cur = cur[:-len(prev)]
					# cur = []
					j = len(cur)
					# j = 0
					temp = scramble(cur, use, chance, False)
					chance /= (div / 1)

					dd = len(cur) / len("The impossible is pos") * 5 + len(prev) / 20
					while temp != use:
						if len(cur) < len(use):
							cur.append(use[j])
							j += 1
						temp = scramble(cur, use, chance)
						
						chance /= (div / dd)
						if dd > 1:
							dd -= 0.2
								
						sleep(sleeping)
					prev = use.copy()
				if between == 'SMART':
					SLEEPS = len(''.join(cur).split(' ')) / (200 / 60) + 0.8
				else:
					SLEEPS = between
				sleep(SLEEPS)
				i += 1
	matprint(['Loading...', 'Welcome to Blooket Dupe'], random=False, sleeping=0.1, between='SMART', times=1)
	print('\u001b[38;5;10mIn the first edition of Blooket Dupe, answer questions correctly to get tokens!\nUse the shop to buy blooks. There are also chances of winning Mythical blooks!\nYour progress is also saved!')
	input("Press Enter to cont.")
	matprint(['Loading...', 'Starting Game...'], random=False, sleeping=0.1, between='SMART', times=1)
	#matprint(phrases, random=False, sleeping=0.1, between='SMART')
def coolprint2():
	# import packages
	from time import sleep
	from rrandom import randintt, choiice, shuffle
	from typping import col, c

	# initilize variables
	# random characters
	chars = '!<>-_\\/[]{}—=+*^?#________1234567890@?!,.$'

	# phrases
	#phrases = [list]

	def scramble(thing, finished, chance, canfinish=True):
		c() # clear screen.
		new = '' # to print
		undecorated = [] # return to check whether it is finished
		for i in thing:
			scramb = randintt(0, 70)

			multi = (len(finished) / 85)
			if chance * 100 * multi >= scramb:
				ch = choiice(chars)
				new += col('BRIGHT_BLACK') + ch + col('end')
				undecorated.append(ch)
			else:
				new += col('white') + i + col('end')
				undecorated.append(i)

		if not canfinish and new == finished:
			ch = choiice(chars)
			new[-1] = col('BRIGHT_BLACK') + ch + col('end')
			undecorated[-1] = ch
		# writing(new)
		print(new)
		return undecorated

	# to be added: phrase sets :D
	# basically
	# the function can take in a list of phrases and got through each list
	def matprint(phrases, random=False, sleeping=0.1, between=0.8, times='inf'):
		if random:
			lst = shuffle([list(i) for i in phrases])
		else:
			lst = [list(i) for i in phrases]

		i = 0
		div = 2
		cur = lst[i]
		prev = cur.copy()
		if times != 'inf':
			for _ in range(times * len(lst)):
				chance = 100
				if i >= len(lst) - 1:
					if random:
						lst = shuffle([list(i) for i in phrases])
					i %= len(lst)
				cur = lst[i]
				j = 0
				if len(cur) == len(prev):
					# use = cur.copy()
					# cur = []
					# j = 0
					temp = scramble(cur, cur, chance, False)
					sleep(sleeping)
					chance /= div
					while temp != cur:
						# if len(cur) != len(use):
						# 	cur.append(use[j])
						# 	j += 1
						temp = scramble(cur, cur, chance)
						chance /= div
						sleep(sleeping)
					prev = cur.copy()
				elif len(cur) < len(prev):
					dd = 5
					use = cur.copy()
					cur += [prev[i] for i in range(len(cur), len(prev) - len(cur))]
					j = 0
					temp = scramble(cur, use, chance, False)
					chance /= (div / dd)
					while temp != use:
						if len(cur) > len(use):
							cur = cur[:-1]
							temp = scramble(cur, use, chance, False)
						else:
							temp = scramble(cur, use, chance)
						chance /= (div / dd)
						if dd > 1:
							dd -= 0.5
							
						sleep(sleeping)

					prev = use.copy()
				else:
					use = cur.copy()
					cur = cur[:-len(prev)]
					# cur = []
					j = len(cur)
					# j = 0
					temp = scramble(cur, use, chance, False)
					chance /= div
					dd = len(cur) / len("The impossible is pos") * 2
					while temp != use:
						if len(cur) < len(use):
							cur.append(use[j])
							j += 1
						temp = scramble(cur, use, chance)
						
						chance /= (div / dd)
						if dd > 1:
							dd -= 0.5
								
						sleep(sleeping)
					prev = use.copy()
				if between == 'SMART':
					SLEEPS = len(''.join(cur).split(' ')) / (200 / 60) + 0.8
				else:
					SLEEPS = between
				sleep(SLEEPS)
				i += 1
		else:
			while True:
				chance = 100
				if i >= len(lst) - 1:
					if random:
						lst = shuffle([list(i) for i in phrases])
					i %= len(lst)
				cur = lst[i]
				j = 0
				if len(cur) == len(prev):
					# use = cur.copy()
					# cur = []
					# j = 0
					temp = scramble(cur, cur, chance, False)
					sleep(sleeping)
					chance /= div
					while temp != cur:
						# if len(cur) != len(use):
						# 	cur.append(use[j])
						# 	j += 1
						temp = scramble(cur, cur, chance)
						chance /= div

						sleep(sleeping)
					prev = cur.copy()
				elif len(cur) < len(prev):
					dd = 5
					use = cur.copy()
					# cur += [prev[i] for i in range(len(cur), len(prev) - len(cur))]
					# cur = []
					j = 0
					temp = scramble(cur, use, chance, False)
					chance /= (div / dd)
					while temp != use:
						# if cur == list('be turned upside downndin'): print(cur, use, temp)
						# if len(cur) > len(use):
						# 	cur = cur[:-1]
						# 	temp = scramble(cur, use, chance, False)
						temp = scramble(cur, use, chance)
						chance /= (div / dd)
						if dd > 1:
							dd -= 1.5
							
						sleep(sleeping)

					prev = use.copy()
				else:
					use = cur.copy()
					cur = cur[:-len(prev)]
					# cur = []
					j = len(cur)
					# j = 0
					temp = scramble(cur, use, chance, False)
					chance /= (div / 1)

					dd = len(cur) / len("The impossible is pos") * 5 + len(prev) / 20
					while temp != use:
						if len(cur) < len(use):
							cur.append(use[j])
							j += 1
						temp = scramble(cur, use, chance)
						
						chance /= (div / dd)
						if dd > 1:
							dd -= 0.2
								
						sleep(sleeping)
					prev = use.copy()
				if between == 'SMART':
					SLEEPS = len(''.join(cur).split(' ')) / (200 / 70)
				else:
					SLEEPS = between
				sleep(SLEEPS)
				i += 1
	matprint(['If you already have a username, type that in to load your tokens and blooks.\nIf you are new, make a username!'], random=False, sleeping=0.1, between=1, times=1)
	#matprint(phrases, random=False, sleeping=0.1, between='SMART')


chars = '!<>-_\\/[]{}—=+*^?#________1234567890@?!,.$'

from time import sleep
from rrandom import randintt, choiice, shuffle
from typping import col, c
def scramble(thing, finished, chance, canfinish=True):
	c() # clear screen.
	new = '' # to print
	undecorated = [] # return to check whether it is finished
	for i in thing:
		scramb = randintt(0, 70)

		multi = (len(finished) / 85)
		if chance * 100 * multi >= scramb:
			ch = choiice(chars)
			new += col('BRIGHT_BLACK') + ch + col('end')
			undecorated.append(ch)
		else:
			new += col('white') + i + col('end')
			undecorated.append(i)

	if not canfinish and new == finished:
		ch = choiice(chars)
		new[-1] = col('BRIGHT_BLACK') + ch + col('end')
		undecorated[-1] = ch
	# writing(new)
	print(new)
	return undecorated

# to be added: phrase sets :D
# basically
# the function can take in a list of phrases and got through each list
def matprint(phrases, random=False, sleeping=0.1, between=0.8, times=1):
	if random:
		lst = shuffle([list(i) for i in phrases])
	else:
		lst = [list(i) for i in phrases]

	i = 0
	div = 2
	cur = lst[i]
	prev = cur.copy()
	if times != 'inf':
		for _ in range(times * len(lst)):
			chance = 100
			if i >= len(lst) - 1:
				if random:
					lst = shuffle([list(i) for i in phrases])
				i %= len(lst)
			cur = lst[i]
			j = 0
			if len(cur) == len(prev):
				# use = cur.copy()
				# cur = []
				# j = 0
				temp = scramble(cur, cur, chance, False)
				sleep(sleeping)
				chance /= div
				while temp != cur:
					# if len(cur) != len(use):
					# 	cur.append(use[j])
					# 	j += 1
					temp = scramble(cur, cur, chance)
					chance /= div
					sleep(sleeping)
				prev = cur.copy()
			elif len(cur) < len(prev):
				dd = 5
				use = cur.copy()
				cur += [prev[i] for i in range(len(cur), len(prev) - len(cur))]
				j = 0
				temp = scramble(cur, use, chance, False)
				chance /= (div / dd)
				while temp != use:
					if len(cur) > len(use):
						cur = cur[:-1]
						temp = scramble(cur, use, chance, False)
					else:
						temp = scramble(cur, use, chance)
					chance /= (div / dd)
					if dd > 1:
						dd -= 0.5
						
					sleep(sleeping)

				prev = use.copy()
			else:
				use = cur.copy()
				cur = cur[:-len(prev)]
				# cur = []
				j = len(cur)
				# j = 0
				temp = scramble(cur, use, chance, False)
				chance /= div
				dd = len(cur) / len("The impossible is pos") * 2
				while temp != use:
					if len(cur) < len(use):
						cur.append(use[j])
						j += 1
					temp = scramble(cur, use, chance)
					
					chance /= (div / dd)
					if dd > 1:
						dd -= 0.5
							
					sleep(sleeping)
				prev = use.copy()
			if between == 'SMART':
				SLEEPS = len(''.join(cur).split(' ')) / (200 / 60) + 0.8
			else:
				SLEEPS = between
			sleep(SLEEPS)
			i += 1
	else:
		while True:
			chance = 100
			if i >= len(lst) - 1:
				if random:
					lst = shuffle([list(i) for i in phrases])
				i %= len(lst)
			cur = lst[i]
			j = 0
			if len(cur) == len(prev):
				# use = cur.copy()
				# cur = []
				# j = 0
				temp = scramble(cur, cur, chance, False)
				sleep(sleeping)
				chance /= div
				while temp != cur:
					# if len(cur) != len(use):
					# 	cur.append(use[j])
					# 	j += 1
					temp = scramble(cur, cur, chance)
					chance /= div

					sleep(sleeping)
				prev = cur.copy()
			elif len(cur) < len(prev):
				dd = 5
				use = cur.copy()
				# cur += [prev[i] for i in range(len(cur), len(prev) - len(cur))]
				# cur = []
				j = 0
				temp = scramble(cur, use, chance, False)
				chance /= (div / dd)
				while temp != use:
					# if cur == list('be turned upside downndin'): print(cur, use, temp)
					# if len(cur) > len(use):
					# 	cur = cur[:-1]
					# 	temp = scramble(cur, use, chance, False)
					temp = scramble(cur, use, chance)
					chance /= (div / dd)
					if dd > 1:
						dd -= 1.5
						
					sleep(sleeping)

				prev = use.copy()
			else:
				use = cur.copy()
				cur = cur[:-len(prev)]
				# cur = []
				j = len(cur)
				# j = 0
				temp = scramble(cur, use, chance, False)
				chance /= (div / 1)

				dd = len(cur) / len("The impossible is pos") * 5 + len(prev) / 20
				while temp != use:
					if len(cur) < len(use):
						cur.append(use[j])
						j += 1
					temp = scramble(cur, use, chance)
					
					chance /= (div / dd)
					if dd > 1:
						dd -= 0.2
							
					sleep(sleeping)
				prev = use.copy()
			if between == 'SMART':
				SLEEPS = len(''.join(cur).split(' ')) / (200 / 60) + 0.8
			else:
				SLEEPS = between
			sleep(SLEEPS)
			i += 1