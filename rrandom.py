import numpy
def choiice(lst):
  try: return lst[numpy.random.randint(0, len(lst))]
  except: return lst[numpy.random.randint(0, len(lst)-1)]
  
import time
def sleepy(times):
  time.sleep(choiice(times))
  
def randintt(lo,hi):
  return numpy.random.randint(lo,hi)
  
def shuffle(lst):
  new_lst = []
  for i in range(len(lst)):
    new_lst.append(lst.pop(randintt(0, len(lst))))
  return new_lst