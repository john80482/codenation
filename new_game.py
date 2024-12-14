# a new game

# imports
import sys,time
import textwrap
import os

# set-up some variables

read_input = 0
dir_path = os.getcwd()

# set-up some defenitions to be used

def printtext(text):
  wrapped_text = textwrap.wrap(text, width=100)
  for line in wrapped_text:
    print(line)

def char_one(txt, delay=0.1):
  for char in txt:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(delay)
  print()

def user_input():
  global read_input
  read_input = input("l, r, f .....  ").lower() 
  while read_input not in ("l","r","f"):
   print ("Not a valid option")
   read_input = input("l, r, f .....  ").lower()
  return read_input

char_one ("Welcome to my game")
print()

#start of game
def start():
#  char_one ("Welcome to my game")
#  print()
  printtext("You enter a dark corridor, you cant see infront of you")
  print()
  time.sleep(1)
  printtext("You know you have options - (l)eft, (r)ight or walk (f)orward")
  char_one("Make a choice")
  user_input()
  if read_input == "l":
    print()
    char_one("You have opted to turn left:")
    time.sleep(2)
    exec(open('turned_left.py').read())
    print()
    start()

if read_input == "r":
  print()
  char_one("You have selected to turn right:")

if read_input == "f":
  print()
  char_one("You have decided that walking forward is best:")

start()