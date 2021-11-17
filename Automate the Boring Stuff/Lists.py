#! python3

spam = ['cat','dog','mouse','elephant']
print(spam)

#Print cat
print(spam[0])

#Print elephant
print(spam[-1])

#Print a slice from a list
print(spam[1:3])

#Concatenate
print('The ' + spam[0] + ' chased the ' + spam[-2])

#Change an indexed value
spam[1] = 'No longer a dog'
spam[2] = 'Not a mouse anymore either'
print(spam)

#Change items simultaneously
spam[1:3] = ['dog','mouse']
print(spam)

#index values are not necessary for the start or end of a slice
print(spam[:3])
print(spam[2:])

#Delete from list
del spam[2]
print(spam)

#LIST METHODS SECTION BELOW

#remove (only the first instance in a list)
spam.remove('dog')
print(spam)

#Evaluate True False in list
'cat' not in spam
'cat' in spam

#Append
spam.append('moose')
print(spam)

#Insert
spam.insert(2,'eagle')
print(spam)

#Index
print(spam.index('elephant'))

#Extend
list_num = []

# extending list elements
list_num.extend([1, 2])  
print(list_num)

# extending tuple elements
list_num.extend((3, 4))  
print(list_num)

# extending string elements
list_num.extend("ABC")  
print(list_num)

#Sort (arguments for how to sort available)
nums = [4,2,3,5,1]
nums.sort()
spam.sort()
print(nums, spam)
#sorting is ASCII-betical order so capitol lettes come first
letters = ['a','A','b','c','C','Z']
print(letters)
letters.sort()
print('ASCII-bettical:')
print(letters)
#Switch to actual alphabetical
letters.sort(key = str.lower)
print('Actual alphabetical:')
print(letters)







