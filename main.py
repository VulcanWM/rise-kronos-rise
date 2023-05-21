from time import sleep
import sys
import os
import random
lose = False
Red = "\033[0;31m"
Green = "\033[0;32m"
Orange = "\033[0;33m"
Blue = "\033[0;34m"
Purple = "\033[0;35m"
Cyan = "\033[0;36m"
White = "\033[0;37m" 
black = "\033[0;30m"
red = "\033[0;91m"
green = "\033[0;92m"
yellow = "\033[0;93m"
blue = "\033[0;94m"
magenta = "\033[0;95m"
cyan = "\033[0;96m"
white = "\033[0;97m"
cyan_back = "\033[0;46m"
pink_back = "\033[0;45m"
white_back = "\033[0;47m"
blue_back = "\033[0;44m"
orange_back = "\033[0;43m"
green_back = "\033[0;42m"
red_back = "\033[0;41m"
grey_back = "\033[0;40m"
bold = "\033[1m"
underline = "\033[4m"
italic = "\033[3m"
darken = "\033[2m"
invisible='\033[08m'
reverse='\033[07m'
reset='\033[0m'

Zeus = True
Poseidon = True
Ares = True
Hera = True
Athena = True
Aphrodite = True
Hephaestus = True
Dionysus = True
Apollo = True
Artemis = True
Hermes = True
Demeter = True
win = False
def slowprint(text):
  for x in text:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.07)
def demo():
  os.system("clear")
  slowprint(red + bold + underline + "Kronos" + Cyan + bold + " talks to you in your sleep and tells you that if you defeat all the Olympians, he will make you the second most powerful person in the world (him being the first person).")
  slowprint(Orange + "\nPress enter to continue")
  input("\n")
  os.system("clear")
  slowprint(Red + bold + "You agree to what he says and set on a quest to defeat all the Olympians.")
  slowprint(Orange + "\nPress enter to continue")
  input("\n")
slowprint(green_back+"Welcome to")
print(red_back + """
_____   _________    _________    ________ 
|   |       |        |            |        
|___|       |        |________    |______  
|\          |                 |   |        
| \         |                 |   |        
|  \    ____|____     ________|   |_______ 
     ____  ______          ______  ________
| /  |  |  |    |  |\   |  |    |  |       
|/   |__|  |    |  | \  |  |    |  |_______
|\   |\    |    |  |  \ |  |    |         |
| \  | \   |____|  |   \|  |____|  _______|
_____   _________    _________    ________ 
|   |       |        |            |        
|___|       |        |________    |______  
|\          |                 |   |        
| \         |                 |   |        
|  \    ____|____     ________|   |_______ 
                                           
""")
slowprint(Orange + "Press enter to continue")
input("\n")
os.system("clear")
slowprint(White + "Do you want to see the demo? (y,n)")
demoornot = input("\n")
os.system("clear")
while demoornot != "y" and demoornot != "n":
  slowprint(red + "That is not in the menu.")
  slowprint(White + "\nDo you want to see the demo? (y,n)")
  demoornot = input("\n")
if demoornot == "y":
  demo()
os.system("clear")
def main(god, weapon):
  slowprint(grey_back + "During the game, you can" + Blue + "\n(a)Attack" + Cyan + "\n(b)Boost or" + White + "\n(d)Defend. " + Orange + "\nPress enter to continue")
  input("")
  zeusscore = 5
  yourscore = 5
  for i in range(5):
    os.system("clear")
    print(Green + "Your health:" + str(yourscore))
    print(red + god + "'s score:" + str(zeusscore))
    lettersabc = "a","b","d"
    zeuschoice = random.choice(lettersabc)
    print(Blue + "\n(a)Attack")
    print(Cyan + "\n(b)Boost")
    print(White + "\n(d)Defend")
    print(Orange + "Type in the letter you want to do ")
    yourchoice2 = input("\n")
    yourchoice = yourchoice2.lower()
    if yourchoice == "a" and zeuschoice == "a":
      slowprint(White + "You and " + god + " both attacked. Both of you dodged the " + weapon)
    if yourchoice == "a" and zeuschoice == "b":
      slowprint(Green + "You attacked while " + god + " attempted to have a boost. Fortunately for you, you attacked " + god + " and " + god + " couldn't have his boost.")
      zeusscore = zeusscore - 1
    if yourchoice == "a" and zeuschoice == "d":
      slowprint(Blue + "You attacked while " + god + " defended, so your shot didn't hit " + god)
    if yourchoice == "b" and zeuschoice == "a":
      slowprint(red + "You tried to boost while " + god + " attcked. Unfortunately for you, they attacked you and you couldn't have your boost.")
      yourscore = yourscore - 1
    if yourchoice == "b" and zeuschoice == "b":
      slowprint(Cyan + "You and " + god + " both boosted.")
      zeusscore = zeusscore + 1
      yourscore = yourscore + 1
    if yourchoice == "b" and zeuschoice == "d":
      slowprint(Green + "You boosted while " + god + " defended.")
      yourscore = yourscore + 1
    if yourchoice == "d" and zeuschoice == "a":
      slowprint(Cyan + god + " tried to attack but you defended it.")
    if yourchoice == "d" and zeuschoice == "b":
      slowprint(red + "You defended hoping for " + god + " to attack, but they boosted instead.")
      zeusscore = zeusscore + 1
    if yourchoice == "d" and zeuschoice == "d":
      slowprint(Blue + "Both of you defended.")
    if yourchoice not in lettersabc:
      slowprint("You just stood there while " + god + " attacked.")
      yourscore = yourscore - 1
  if yourscore == zeusscore:
    slowprint(red + "\n" + god +" finished you off with " + weapon + "!")
    lose = True
    return lose
  if yourscore > zeusscore:
    slowprint(Green + "\nYou won the match!")
    if god == "Zeus":
      Zeus = False
      return Zeus
    if god == "Poseidon":
      Poseidon = False
      return Poseidon
    if god == "Ares":
      Ares = False
      return Ares
    if god == "Hera":
      Hera = False
      return Hera
    if god == "Athena":
      Athena = False
      return Athena
    if god == "Aphrodite":
      Aphrodite = False
      return Aphrodite
    if god == "Hephaestus":
      Hephaestus = False
      return Hephaestus
    if god == "Dionysus":
      Dionysus = False
      return Dionysus 
    if god == "Hermes":
      Hermes = False
      return Hermes
    if god == "Demeter":
      Demeter = False
      return Demeter
    if god == "Apollo":
      Apollo = False
      return Apollo
    if god == "Artemis":
      Artemis = False
      return Artemis
  if yourscore < zeusscore:
    slowprint(red + "\n" + god + "finished you off with" + weapon + "!")
    sleep(2)
    os.system("clear")
    slowprint(red_back + "All of the Olympians worked together to defeat you. They used their powers combined to make you disappear, you went to a different world and became immortal. Sadly for you, Kronos haunted you with nightmares forever.")
    quit()
while True:
  print(grey_back + "Menu:")
  if Zeus == True:
    print("(a) Try to destroy Zeus")
  if Poseidon == True:
    print("(b) Try to destroy Poseidon")
  if Ares == True:
    print("(c) Try to destroy Ares")
  if Hera == True:
    print("(d) Try to destroy Hera")
  if Athena == True:
    print("(e) Try to destroy Athena")
  if Aphrodite == True:
    print("(f) Try to destroy Aphrodite")
  if Hephaestus == True:
    print("(g) Try to destroy Hephaestus")
  if Dionysus == True:
    print("(h) Try to destroy Dionysus")
  if Apollo == True:
    print("(i) Try to destroy Apollo")
  if Artemis == True:
    print("(j) Try to destroy Artemis")
  if Hermes == True:
    print("(k) Try to destroy Hermes")
  if Demeter == True:
    print("(l) Try to destroy Demeter")
  print("Type in the letter of what you want to do.")
  chance = input("\n")
  os.system("clear")
  if chance == "a" and Zeus == True:
    Zeus = main("Zeus", "lightning")
  if chance == "b" and Poseidon == True:
    Poseidon = main("Poseidon", "water")
  if chance == "c" and Ares == True:
    Ares = main("Ares", "bullets")
  if chance == "d" and Hera == True:
    Hera = main("Hera", "cows")
  if chance == "e" and Athena == True:
    Athena = main("Athena", "spears")
  if chance == "f" and Aphrodite == True:
    Aphrodite = main("Aphrodite", "mirrors")
  if chance == "g" and Hephaestus == True:
    Hephaestus = main("Hephaestus", "hammers")
  if chance == "h" and Dionysus == True:
    Dionysus = main("Dionysus", "grapes")
  if chance == "i" and Apollo == True:
    Apollo = main("Apollo", "arrows")
  if chance == "j" and Artemis == True:
    Artemis = main("Artemis", "wild animals")
  if chance == "k" and Hermes == True:
    Hermes = main("Hermes", "packages")
  if chance == "l" and Demeter == True:
    Demeter = main("Demeter", "wheat")
  os.system("clear")
  if Zeus == False and Poseidon == False and Ares == False and Hera == False and Athena == False and Aphrodite == False and Hephaestus == False and Dionysus == False and Apollo == False and Artemis == False and Hermes == False and Demeter == False: 
    slowprint(red_back + "After you defeated all the Olympians, Kronos decided to get rid of you because he didn't want anyone taking the world from him so he sent you to another land.")
