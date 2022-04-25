# Cloverblack44
# Combines two wordlists to create a new recursively combined wordlist for dictionary attacks

import sys

# Receives arguments
arguments = []

for i, arg in enumerate(sys.argv):
	arguments.append(arg)

firstList = open(str(arguments[1]), "r")
finalList = open(str(arguments[3]), "w")

wordList = []

# Combines the first two wordlists
while True:
	secondList = open(str(arguments[2]), "r")
	word1 = firstList.readline().strip()
	if (word1 == ''):
		break
	while True:
		word2 = secondList.readline().strip()
		if (word2 == ''):
			secondList.close()
			break
		word = word1 + word2
		# print(word)
		wordList.append(word)

# Extra bit of code that adds 2 digit numbers to the end of each word (NCL Challenge)
if (arguments[3] == "-N"):
	count = 0
	length = len(wordList)
	while True:
		for x in range(10,100):
			wordList.append(wordList[count] + str(int(x)))
			# print(wordList[-1])
		count += 1
		if (count == length):
			break

# write
for i in wordList:
	finalList.write(i)
	finalList.write("\n")
