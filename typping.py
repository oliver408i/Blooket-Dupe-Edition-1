import sys, time, rrandom

WHITE = "\033[0;37m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
ORANGE = "\033[0;33m"
PINK = "\033[1;31m"
BLUE = "\033[0;34m"
PURPLE = '\033[95m'
DARKCYAN = '\033[36m'
YELLOW = '\033[93m'
RED = '\033[91m'
BLACK = "\033[0;30m"
MAGENTA = "\033[0;35m"
BRIGHT_BLACK = "\033[0;90m"
BRIGHT_RED = "\033[0;91m"
BRIGHT_GREEN = "\033[0;92m"
BRIGHT_YELLOW = "\033[0;93m"
BRIGHT_BLUE = "\033[0;94m"
BRIGHT_MAGENTA = "\033[0;95m"
BRIGHT_CYAN = "\033[0;96m"
BRIGHT_WHITE = "\033[0;97m"

# bg = Background colors
bg_black = '\x1b[40m'
bg_red = '\x1b[41m'
bg_green = '\x1b[42m'
bg_yellow = '\x1b[43m'
bg_blue = '\x1b[44m'
bg_magenta = '\x1b[45m'
bg_cyan = '\x1b[46m'
bg_white = '\x1b[47m'
bg_grey = '\x1b[100m'
bg_bright_red = '\x1b[101m'
bg_bright_green = '\x1b[102m'
bg_bright_yellow = '\x1b[103m'
bg_bright_blue = '\x1b[104m'
bg_bright_magenta = '\x1b[105m'
bg_bright_cyan = '\x1b[106m'
bg_bright_white = '\x1b[107m'

# Extras
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'
INVERT = '\330[7m'
FAINT = '\330[2m'
HIDDEN = '\330[8m'

HASBEENTYPED = ''
def col(*obs):
			lst = []
			dic = {'ORANGE': ORANGE, 'WHITE': WHITE, 'CYAN': CYAN, 'GREEN': GREEN, 'PINK': PINK, 'BLUE': BLUE, 'PURPLE': PURPLE, 'DARKCYAN': DARKCYAN, 'YELLOW': YELLOW, 'RED': RED, 'MAGENTA': MAGENTA, 'BRIGHT_BLACK': BRIGHT_BLACK, 'BRIGHT_BLUE': BRIGHT_BLUE, 'BRIGHT_GREEN': BRIGHT_GREEN, 'BRIGHT_MAGENTA': BRIGHT_MAGENTA, 'BRIGHT_RED': BRIGHT_RED, '': '', 'BOLD': BOLD, 'UNDERLINE': UNDERLINE, 'HIDDEN': HIDDEN, 'INVERT': INVERT, 'FAINT': FAINT, 'END': END, 'YEET': WHITE+bg_black, 'BG_CYAN': bg_cyan, 'BG_BLACK': bg_black, 'RAND': rrandom.choiice([ORANGE, WHITE, CYAN, GREEN, PINK, BLUE, PINK, PURPLE, DARKCYAN, YELLOW, RED, MAGENTA, BRIGHT_BLACK, BRIGHT_BLUE, BRIGHT_GREEN, BRIGHT_MAGENTA, BRIGHT_RED]), 'LIST RAND': [ORANGE, WHITE, CYAN, GREEN, PINK, BLUE, PINK, PURPLE, DARKCYAN, YELLOW, RED, MAGENTA, BRIGHT_BLACK, BRIGHT_BLUE, BRIGHT_GREEN, BRIGHT_MAGENTA, BRIGHT_RED]}
			find = False
			for ob in obs:
				if ', ' in ob:
					find = True
				if find:
					splited = ob.split(', ')
					new_list = []
					temp = dic[splited[-1].upper()]
					if type(temp) != list: temp = [temp]
					for i in temp:
						temptemp = i
						for j in splited[:-1]:
							temptemp += dic[j.upper()]
						new_list.append(temptemp)
					lst.append(new_list)
				if type(ob) != str:
					ob = ''
				if ob.upper() not in dic:
					ob = ''
				
				
				else:
					lst.append(dic[ob.upper()])
			if len(lst) > 1:
				return lst
			elif len(lst) == 1:
				return lst[0]
			else:
				return ''
def c():
	global HASBEENTYPED
	print("\033[2J\033[1;1H", end="")
	HASBEENTYPED = ''
	
	
def revtyping(color=""):
  # Note that revtyping does not allow you to only untype certain things... You can overide color.
  global HASBEENTYPED
  #if overridetorainbow is None:
  #  overridetorainbow = False
  #if overridetorainbow:
  #  color=[ORANGE, WHITE, CYAN, GREEN, PINK, BLUE, PINK, PURPLE, DARKCYAN, YELLOW, RED, MAGENTA, BRIGHT_BLACK, BRIGHT_BLUE, BRIGHT_GREEN, BRIGHT_MAGENTA, BRIGHT_RED]
  c()
  #if overridetorainbow:
  #  sys.stdout.write(rrandom.choiice(color)+HASBEENTYPED+END)
  #else:
  sys.stdout.write(color+HASBEENTYPED+END)
  sys.stdout.flush()
  time.sleep(rrandom.choiice([0.01,0.02]))
  c()
  for char in range(len(HASBEENTYPED)-1,-1,-1):
    #if overridetorainbow:
    #  sys.stdout.write(rrandom.choiice(color)+HASBEENTYPED[:char]+END)
    #else:
    sys.stdout.write(color+HASBEENTYPED[:char]+END)
    sys.stdout.flush()
    time.sleep(rrandom.choiice([0.01,0.02,0.03])*0.5)
    c()
def rainbowtype(*messages, colors=[], shouldundo=False, spliters=[], multis=[], endchooses=[], seps=[]):
						for i in range(len(messages)):
							message = str(messages[i])
							if i < len(colors):
								color=colors[i]
							else:
								color=col('list rand')
							if i < len(spliters):
								spliter=spliters[i]
							else:
								spliter = None
							if i < len(multis):
								multi=multis[i]
							else:
								multi = 1
							if i < len(endchooses):
								endchoose=endchooses[i]
							else:
								endchoose = False
							if i < len(seps):
								sep=seps[i]
							else:
								sep = ' '
							if multi == 0 or (type(multi) != int and type(multi) != float):
								multi = 1
							global HASBEENTYPED
							if shouldundo is None:
								shouldundo = False
							if spliter is not None:
								message = message.split(spliter)
							else:
								spliter = ""
							c = 0
							for char in message:
								HASBEENTYPED += rrandom.choiice(color)+char
								if c < len(message)-1 or endchoose: 
									sys.stdout.write(rrandom.choiice(color)+char+spliter+END)
									sys.stdout.flush()
									HASBEENTYPED += spliter
								else:
									sys.stdout.write(rrandom.choiice(color)+char+END)
									sys.stdout.flush()
								HASBEENTYPED += END
								time.sleep(rrandom.choiice([0.01, 0.02, 0.03, 0.04, 0.05])*multi)
								c += 1
							sys.stdout.write(sep)
							sys.stdout.flush()
						if shouldundo:
							revtyping()

def typing(*messages, colors=[], shouldundo=False, spliters=[], multis=[], endchooses=[], seps=[]):
  for i in range(len(messages)):
    message = str(messages[i])
    if i < len(colors):
      color=colors[i]
    else:
      color=''
    if i < len(spliters):
      spliter=spliters[i]
    else:
      spliter = None
    if i < len(multis):
      multi=multis[i]
    else:
      multi = 1
    if i < len(endchooses):
      endchoose=endchooses[i]
    else:
      endchoose = False
    if i < len(seps):
      sep=seps[i]
    else:
      sep = ' '
    if multi == 0 or (type(multi) != int and type(multi) != float):
      multi = 1
    global HASBEENTYPED
    if shouldundo is None:
      shouldundo = False
    if spliter is not None:
      message = message.split(spliter)
    else:
      spliter = ""
    c = 0
    for char in message:
      HASBEENTYPED += color+char
      if c < len(message)-1 or endchoose: 
        sys.stdout.write(color+char+spliter+END)
        sys.stdout.flush()
        HASBEENTYPED += spliter
      else:
        sys.stdout.write(color+char+END)
        sys.stdout.flush()
      HASBEENTYPED += END
      time.sleep(rrandom.choiice([0.01, 0.02, 0.03, 0.04, 0.05])*multi)
      c += 1
    sys.stdout.write(sep)
    sys.stdout.flush()
  if shouldundo:
    revtyping()
    
    
def inputt(*messages, thiscolors=[], thisshouldundo=False, thisspliters=[], thismultis=[], thisendchooses=[], thisseps=[]):
  typing(messages, colors=thiscolors, shouldundo=thisshouldundo, spliters=thisspliters, multis=thismultis, endchooses=thisendchooses, seps=thisseps)
  thing = input('')
  return thing
def printy(*message, color=""):
  for i in message:
    sys.stdout.write(color+i+END)
    sys.stdout.flush()
    
