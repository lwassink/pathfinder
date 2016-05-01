#This program gives an initiative order for a list of characters 

from random import randint #to generate random integers

numberofpcs = raw_input('How many player characters are there? ') #How many PCs are playing?
numberofpcs = int(numberofpcs)

numberofgmcs = raw_input('How many game master characters are there? ') #How many GMCs are playing?
numberofgmcs = int(numberofgmcs)

characters = [] #the list of characters

for i in range(1,numberofpcs+1):
   name = raw_input("Enter the name of PC number %d: " % i)
   initiative = int(raw_input("Now enter their initiative: "))
   characters.append((name, initiative))

for i in range(1,numberofgmcs+1):
   name = raw_input("Enter the name of GMC number %d: " % i)
   characters.append((name, 5 + randint(1,20)))

characters = sorted(characters, key = lambda tup: tup[1])[::-1]

for guy in characters:
   print "Character: %s, Initiative: %d" % (guy[0], guy[1])
