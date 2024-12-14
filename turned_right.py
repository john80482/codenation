# file called when turning right at the beginning of the game

import os
import textwrap

#game defenitions
def printtext(text):
  wrapped_text = textwrap.wrap(text, width=100)
  for line in wrapped_text:
    print(line)

#clear teh screen
os.system('cls')

printtext("On turning right you are presented with a door. A door you didnt see before, how curious. You look into the doorway ... its black, your eyes cannot adjust to it from where you are so you decide, almost without thinking, to walk into the darkness")
