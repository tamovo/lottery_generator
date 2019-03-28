import random
#
# lottery_generator
#
# generate 6 numbers in 1-49 to simulate the lottery system
#
# Using random function and print out each of the number that has been generated. print out the collection of the lucky number!!
#Tasks:
#6/49 to win lottery
#make a list to simulate delete 1 each time
# write a result to a text file.

# this can generate the value without repeating the random number
# randomNumbers = random.sample(listOfNumber, 1)

# print(randomNumbers)
#write a file to export data


y = 49
f = open("data", "w+")
#initial the list of number
listOfNumber = [x+1 for x in range(y)]
print(listOfNumber, sep=", ")
f.write("%s \n" % listOfNumber)
listOfDraw = []

for i in range(6):
    randomNumbers = random.choice(listOfNumber)
    print(randomNumbers)
    f.write("%s \n" % randomNumbers)
    listOfDraw.append(randomNumbers)
    listOfNumber.remove(randomNumbers)
    print(listOfNumber, sep=", ")
    f.write("%s \n" % listOfNumber)

print("listOfDraw : ", listOfDraw)
f.write("%s \n" % listOfDraw)
f.close()





