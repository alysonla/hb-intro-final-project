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

print "Guess a Githubber!"

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
    #Conditional - if the length of my_line is equal to one
    if len(my_line) == 1:
    #Conditional - if the length of the dictionary is greater than one
      if len(d) > 0:
    #Add the dictionary to the people list
        people.append(d)
    #Something somethin
      d = {}
      continue
    if my_line[0] != 'Site':
      d[my_line[0]]=my_line[1]

#Create empty list assigned to the variable possible_locations
possible_locations = []

#Create variable person which uses the random method to choose one person out of the people list
person = random.choice(people)
while "Location" not in person:
    person = random.choice(people)

#Add a person with a location to the possible_locations list
possible_locations.append(person["Location"])

#TODO: Put this in a while loop to make sure you add 4 other locations
for l in range(4):
  temp_person = random.choice(people)
  while "Location" not in temp_person:
      temp_person = random.choice(people)
  possible_locations.append(temp_person["Location"])

#Shuffle possible_locations
random.shuffle(possible_locations)

#Create a variable location_guess that prints out a random name and 5 possible locations
location_guess = raw_input("Where does%s live? \n1. %s \n2. %s \n3. %s \n4. %s \n5. %s \n>>>  " % (person["Name"], possible_locations[0],possible_locations[1],possible_locations[2],possible_locations[3],possible_locations[4]))

#Print location_guess
print person["Location"]

#If the location_guess is equal to person at location 1 or something something
if location_guess == person["Location"][1:] or int(location_guess) == possible_locations.index(person['Location']) + 1:
  print "You got it!"
else:
  print "Try again!"
