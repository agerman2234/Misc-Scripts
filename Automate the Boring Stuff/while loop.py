#! python3

spam = 0
while spam < 10: 
    if spam == 3:
        spam += 1
        continue
    if spam == 7:
        print ('Break')
        break
    print(spam)
    spam += 1
