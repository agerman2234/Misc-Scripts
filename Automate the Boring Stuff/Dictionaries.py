#! python3

#Made up of "key:item". When referred to together they are called values
myCat = {'size':'fat', 'color':'orange','food':'lasagna'}

print(myCat['size'])  


#check if a key is in the dictionary
print('name' in myCat)
print('color' in myCat)

#output certain values
print(myCat.keys())
print(myCat.values())
print(myCat.items())

#output certain values AS A LIST
print(list(myCat.keys()))
print(list(myCat.values()))
print(list(myCat.items()))

for k in myCat.keys():
    print(k)

for k,v in myCat.items():
    print(k,v)

#Avoid key error errors by using .get() method to return a default value if a key doesn't exist
print(myCat.get('height','this key does not exist and i am printing the default return variable'))

#setdefault method()
eggs = {'name':'Sophie', 'species':'cat', 'age':'8'}
print(eggs)
eggs.setdefault('color','black')
print(eggs)
eggs.setdefault('color','orange')
print(eggs)


#Create a program to count the number of letters in a string
message = 'It was a bright cold day in April, and the clocks were striking thirteen'
count = {}

for character in message.lower():
    count.setdefault(character,0)
    count[character] = count[character] + 1

print(count)

#pprint module 'pretty print' to clean up dictionary output
import pprint
pprint.pprint(count)
#set pretty print to a string variable with pformat method to use later
sentence = pprint.pformat(count)
print(sentence) 



















