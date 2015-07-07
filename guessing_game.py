#Use the random module to randomly generate a name
import random

#Create dictionary
d = {}

#Open txt file
text_file = open("team.txt")

#Read in txt file
text_read=text_file.readlines()

#Close txt file
text_file.close()

print "Hello World: Guess a Githubber!"

#Create empty list assigned to the variable people
people = []

#Start for loop to iterate through the file
for line in text_read:
    #Use the strip method to get rid of the \n
    my_line = line.strip()
    #Use strip method again to get rid of the remaining \n
    new = my_line.strip()
    #split lines on the :
    my_line = new.split(":")
    #Conditional - if the length of my_line is equal to one and the length of the dictionary is greater than 0 then add a dictionary to the people list
    if len(my_line) == 1:
    #This is here to avoid appending empty dictionary due to cases where there are 2 new lines
      if len(d) > 0:
        people.append(d)
      d = {}
      continue
    #Conditional - if my_line is equal to site then create a new list my_line which concatenates the last 2 elements in the original my_line list.
    if my_line[0] == 'Site':
        my_line = [my_line[0], my_line[1] +":" + my_line[2]]
    #Adding a key value pair to d based off of the list my_line where the key is the first item in the list and the value is the second item in the list.
    d[my_line[0]]=my_line[1]

#Create empty list assigned to the variable 'possible_locations'
possible_locations = []

#Create variable 'person' which uses the 'random' method to choose one person out of the people list created above
# person = random.choice(people[:100])
# while "Location" not in person:
#     person = random.choice(people[:100])
#
# person = random.choice(people[101:200])
# while "Location" not in person:
#     person = random.choice(people[101:200])

person = random.choice(people[200:])
while "Location" not in person:
    person = random.choice(people[200:])

#Add a person with a location to the possible_locations list
possible_locations.append(person["Location"])

#Loop through to add locations of 4 random people
for l in range(4):
  #Create a variable temp_person and use the random method to choose out a new random person
  temp_person = random.choice(people)
  #Create a while loop
  while "Location" not in temp_person:
      temp_person = random.choice(people)
  possible_locations.append(temp_person["Location"])

#Shuffle possible_locations
random.shuffle(possible_locations)

#Choose OG, Middle, or New Hubber
level = raw_input("Pick a level: \n 1. OG Hubbers - first 100 \n 2. Middle Earth - 101 - 200 \n 3. New Hubbers - From 200 on \n" )

if level == int(level) == level.index(person[]) + 1:

#Create a variable 'location_guess' that prints out a random name and 5 possible locations
location_guess = raw_input("Where does%s live? \n1. %s \n2. %s \n3. %s \n4. %s \n5. %s \n>>>  " % (person["Name"], possible_locations[0],possible_locations[1],possible_locations[2],possible_locations[3],possible_locations[4]))

#If the location_guess is equal to person at location 1 or something something
if location_guess == person["Location"][1:] or int(location_guess) == possible_locations.index(person['Location']) + 1:
  print "You got it!"
  #Print location_guess
  print person["Location"]
  print person["Site"]
else:
  print "Try again!"
  #Print location_guess
  print person["Location"]
  print person["Site"]
