<<<<<<< HEAD
print("Hello World!")

print(type("pter"))
my_tuple = (1,3341)
print(type(my_tuple))

print(type(73.41))

num_candidates = 3
winning_percentage = 73.81
candidate = 'Diane'
won_election = True


print("------------------------")
print(num_candidates)
print(winning_percentage)
print(candidate)
print(won_election)

#CALCULATIONS
print('-------------------------')
print(5 + 2 * 3)
print(8 // 5 - 3)
print(8 + 22 * 2 - 4)
print(16 - 3 / 2 + 7 - 1)
print(3 ** 3 % 5)
print(5 + 9 * 3 /2 -4)

#LISTS
print('-'*20)
counties = ['arapahoe', 'denver','jefferson']
print(counties)
print(counties[0])
print(counties[1])
print(counties[2])
print(counties[-1])
print(len(counties))

print('-'*20)

#SLICING
print("SLICING")
print(counties[ : 2]) #prints 1st and second item

#ADD TO LISTS
counties.append('el paso')
print(counties)


#INSERT
counties.insert(2, 'el paso')
print(counties)

counties.remove('el paso') #removes first occurence
print(counties)

counties.pop(3) #removes 4th item
print(counties)

counties[2] = "el paso"  #replaces 3rd item with el paso
print(counties)

#TUPLES
print('-'*20)
counties_tuple = ('arapahoe', 'denver', 'jefferson')
print(counties_tuple)
print(len(counties_tuple))
print(counties_tuple[1])


#DICTIONARIES
print('-'*20)
counties_dict = {}
counties_dict['arapahoe'] = 422829
print(counties_dict)

counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict)
print(counties_dict.items())  #view object
print(counties_dict.values()) #view values
print(counties_dict.keys())




#VOTING DATA
print('-' * 20)
voting_data = []
voting_data.append({'county' : 'arapahoe' , 'registered voters' : 422829})
voting_data.append({'county' : 'denver' , 'registered voters' : 463353})
voting_data.append({'county' : 'jefferson' , 'registerd voters' : 432438})

print(voting_data)
print(len(voting_data))

voting_data.append({'county' : 'el paso' , 'registered voters' : 461149})
voting_data.pop(0)
print(voting_data)

print('-'*20)
voting_data.insert(2, {'county' : 'denver', 'registered voters' : 463353})
voting_data.remove({'county' : 'denver' , 'registered voters' : 463353})
voting_data.remove({'county' : 'el paso' , 'registered voters' : 461149})
voting_data.insert(0,{'county' : 'el paso' , 'registered voters' : 461149})
voting_data.append({'county' : 'arapahoe' , 'registered voters' : 422829})

print(voting_data)



#DECISION STMTS
print('-'*20)
print(counties)

if counties[1] == 'denver' :
    print(counties[1])

#if counties[3] != 'jefferson'
 
 #   print(counties[2])



#IF-ELSE
#print('-'*20)

#temperature = int(input('What is the temperture outside?')) #int() converts user input from string to integer


#if temperature > 80:
 #   print('Turn on AC."')

#else:
 #   print('Open the windows.')


# What is the score?
#score = int(input("What is your test score? "))

# Determine the grade.3
# if score >= 90:
#    print('Your grade is an A.')
#elif score >= 80:
#    print('Your grade is a B.')
#elif score >= 70:
#    print('Your grade is a C.')
#elif score >= 60:
#    print('Your grade is a D.')
#else:
#    print('Your grade is an F.')

#MEMBERSHIP AND LOGICAL OPERATORS
print('-'*20)

counties = ['arapahoe', 'denver', 'jefferson']
if  'el paso' in counties :
    print('el paso is in the list of counties.')

else:
    print('el paso is not in the list of counties. ')

print('-'*20)

if 'arapahoe' in counties and 'el paso' not in counties :
    print('only arapahoe is in the list of counties.')
else: 
    print('arapahoe is in the list of countioes and el paso is not in the list of counties.')


#REPETIIVE STMTS
print('-'*20)

x = 0
while x <= 5 :
    print (x)
    x = x + 1 #IMPORTANT!!! MUST INCLUDE CODE THAT MAKES THE CONDITION FALSE 

print('-'*20)

for county in counties :
    print(county)

print('-'*20)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)
print('fuka')
for num in range(5) :
    print(num)

#INDEXING
print('-'*20)
for i in range(len(counties)) :
    print(counties[i])

print('u faka')
counties_tuple = ('arapahoe', 'denver', 'jefferson')
for i in range(len(counties_tuple)) :
    print(counties_tuple[i])

print('wait, what?')
for county in counties_tuple :
    print(county)

print('-')

for county in counties_dict :
    print(county)
print('--')
for county in counties_dict.keys() :
    print(county)
print('---')
for county in counties_dict :
    print(counties_dict[county])

for county in counties_dict :
    print(counties_dict.get(county))

#KEY-VALUE PAIRS IN DICTIONARY
print('-'*20)

for county, voters in counties_dict.items() :
    print(county, voters)
print('items')
for shit, fuck in counties_dict.items() : #doesnt matter what you call key and value
    print(shit, fuck)
print('-')
print('items')
for shit, fuck in counties_dict.items() : #doesnt matter what you call key and value
    print(shit, 'has', fuck, 'registered voters.')

print('-')
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data: 
    print(county_dict)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
print(':)')
for shit in voting_data:  # can name the variable (county_dict) anything
    print(shit)


for county in range(len(voting_data)) :
    print(voting_data[county]['county'])

print('-')
for i in range(len(voting_data)) :
    print(voting_data[i]['county'])




#GET VALUES FROM LIST OF DICTIONARIES

#avoid double for loops
# county_dict is dictionary, voting_data is list of dictionaries
print('-'*20)
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
#when using the values() method, it doesn't matter what variable name 
#we use in the for loop. The values() method will print each value in order.


print('-'*20)

#F-STRINGS

#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#  #percentage_votes = (my_votes / total_votes) * 100 (replaced code)
#  #print("I received " + str(percentage_votes)+"% of the total votes.") (replaced code)
#print(f"I received {my_votes / total_votes * 100}% of the total votes.")
#print('=' * 20)


for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")


print('-'*20)

candidate_votes = int(input("how many votes did the candidate get in the election?"))
total_votes = int(input('what is the total number of votes in the election?'))
message_to_candidate = (
    f'you received {candidate_votes} number of votes. '
    f'the total number of votes in the election was {total_votes}. '
    f'you received {candidate_votes / total_votes * 100 : .2f}% of the total votes.')
# f'{value : {width} , . {precision}}'
print(message_to_candidate)


print('-'*20)
=======
print("Hello World!")

print(type("pter"))
my_tuple = (1,3341)
print(type(my_tuple))

print(type(73.41))

num_candidates = 3
winning_percentage = 73.81
candidate = 'Diane'
won_election = True


print("------------------------")
print(num_candidates)
print(winning_percentage)
print(candidate)
print(won_election)

#CALCULATIONS
print('-------------------------')
print(5 + 2 * 3)
print(8 // 5 - 3)
print(8 + 22 * 2 - 4)
print(16 - 3 / 2 + 7 - 1)
print(3 ** 3 % 5)
print(5 + 9 * 3 /2 -4)

#LISTS
print('-'*20)
counties = ['arapahoe', 'denver','jefferson']
print(counties)
print(counties[0])
print(counties[1])
print(counties[2])
print(counties[-1])
print(len(counties))

print('-'*20)

#SLICING
print("SLICING")
print(counties[ : 2]) #prints 1st and second item

#ADD TO LISTS
counties.append('el paso')
print(counties)


#INSERT
counties.insert(2, 'el paso')
print(counties)

counties.remove('el paso') #removes first occurence
print(counties)

counties.pop(3) #removes 4th item
print(counties)

counties[2] = "el paso"  #replaces 3rd item with el paso
print(counties)

#TUPLES
print('-'*20)
counties_tuple = ('arapahoe', 'denver', 'jefferson')
print(counties_tuple)
print(len(counties_tuple))
print(counties_tuple[1])


#DICTIONARIES
print('-'*20)
counties_dict = {}
counties_dict['arapahoe'] = 422829
print(counties_dict)

counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict)
print(counties_dict.items())  #view object
print(counties_dict.values()) #view values
print(counties_dict.keys())




#VOTING DATA
print('-' * 20)
voting_data = []
voting_data.append({'county' : 'arapahoe' , 'registered votes' : 422829})
voting_data.append({'county' : 'denver' , 'registered voters' : 463353})
voting_data.append({'county' : 'jefferson' , 'registerd voters' : 432438})

print(voting_data)
print(len(voting_data))

voting_data.append({'county' : 'el paso' , 'registered voters' : 461149})
voting_data.pop(0)
print(voting_data)

print('-'*20)
voting_data.insert(2, {'county' : 'denver', 'registered voters' : 463353})
voting_data.remove({'county' : 'denver' , 'registered voters' : 463353})
voting_data.remove({'county' : 'el paso' , 'registered voters' : 461149})
voting_data.insert(0,{'county' : 'el paso' , 'registered voters' : 461149})
voting_data.append({'county' : 'arapahoe' , 'registered voters' : 422829})

print(voting_data)



#DECISION STMTS
print('-'*20)
print(counties)

if counties[1] == 'denver' :
    print(counties[1])

#if counties[3] != 'jefferson'
 
 #   print(counties[2])



#IF-ELSE
print('-'*20)

#temperature = int(input('What is the temperture outside?')) #int() converts user input from string to integer


#if temperature > 80:
 #   print('Turn on AC."')

#else:
 #   print('Open the windows.')


# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

>>>>>>> 987cf262dcc9fd8baa9608e7ff3433c8177286cb
