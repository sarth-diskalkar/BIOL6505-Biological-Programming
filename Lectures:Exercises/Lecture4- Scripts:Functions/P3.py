"""Create a script that takes in four integers from the user. Store this information as a list. Print out the sum,
median, and mean of the four numbers. Print out the numbers (one per line) from highest to lowest. You can follow
the same general script structure you used in problem 2 -- i.e., writing separate functions for getting input,
calculating and printing the sum, calculating and printing the median, and calculating and printing the mean, then
a final function that call all 4 of these functions in sequence. Try to make this script command-line executable,
as explained in the previous problem."""

def GetDigits():
	x,y,z,w = input("Enter 4 digits with spaces in between them: ").split() #1 2 3 4
	#print(type(x))
	lis = []
	lis.append(int(x))
	lis.append(int(y))
	lis.append(int(z))
	lis.append(int(w))
	lis.sort()
	print(lis)
	return lis

def getSum(lis):
	print('Sum:', sum(lis))
def getMedian(lis):
	median = (lis[len(lis)//2] + lis[(len(lis)//2)-1])/2
	print("Median:",median)
def getMean(lis):
	mean = (sum(lis))/len(lis)
	print('Mean:',mean)

x = GetDigits()
getSum(x)
getMedian(x)
getMean(x)





