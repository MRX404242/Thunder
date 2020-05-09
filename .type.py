from urllib import urlopen
from os import system
from readline import parse_and_bind
from time import sleep
from colorama import Fore
import sys
w = Fore.WHITE
b = Fore.BLUE
r = Fore.RED
parse_and_bind('tab:complete')
def slowprint(s):
 for c in s + '\n':
  sys.stdout.write(c)
  sys.stdout.flush()
  sleep(10. / 400)
web = ['']
while True:
 try:
  ask = raw_input('{}<{}Service-TYPE{}>'.format(w,r,w))
  if ask == 'show options' or ask == 'help' or ask == '?':
   slowprint ('\noption             select            info')
   slowprint ('______             ______           _______\n')
   slowprint ('domain             {}               Domain website\n'.format(web[0]))
  elif 'set domain' in ask:
   web[0] = ask.split(' ')[2]
   slowprint ('{}[{}+{}] Domain => '.format(w,b,w)+web[0])
  elif ask == 'run':
   result = urlopen(web[0])
   server = dict(result.headers)['server']
   slowprint ('{}[{}+{}] Server => {}'.format(w,b,w,server))
  elif ask == 'exit':exit()
  elif ask == 'back':
   system('python Thunder.py')
   exit()
  elif ask == 'banner':system('bash .banner.sh')
  elif ask == 'clear':system('clear')
 except KeyboardInterrupt:exit()
 except Exception as e:print (e)
