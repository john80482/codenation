# file called when turning left at the beginning of the game

import os
import textwrap

#game defenitions
def printtext(text):
  wrapped_text = textwrap.wrap(text, width=100)
  for line in wrapped_text:
    print(line)

#clear teh screen
os.system('cls')

printtext("On turning left you are presented with a wall. It would appear turning left wasn't an option at all. You return back to the options")