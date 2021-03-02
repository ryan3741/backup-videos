#findDiff.py is a program that when run looks through the two txt files above to see which
# files are contained in one but aren't contained within the other. It then outputs this
# result into finalDiff.txt
import os

def findDifference(fileOne,fileTwo,outputFile):
	""" Finds the difference between the two given files and outputs it to a txt file.

	parameters:
	-string: fileOne which is name of first file
	-string: fileTwo which is name of second file
	-string: outputFile which is the name of file to output data to

	Output:
	-google drive api service
	"""
	#create two sets which will be used to hold all of the different file names
	#note that making this a set assumes that there are no duplicate files within one storage system. This assumption should hold true for our files.
	setOne = set()
	setTwo = set()

	#add strings in first file to set one
	with open(fileOne) as fp:
		line = fp.readline()
		while line:
			currStr = line
			#DS_Store is an artifact of file system so we don't want to include
			if "DS_Store" not in currStr:
				#backup file contins the folder name too so we get rid of that
				finalStr = os.path.basename(currStr)
				setOne.add(finalStr)
			line = fp.readline()

	#add the second file to set two
	with open(fileTwo) as fp:
		line = fp.readline()
		while line:
			currStr = line
			#DS_Store is an artifact of file system so we don't want to include
			if "DS_Store" not in currStr:
				setTwo.add(currStr)
			line = fp.readline()

	#find the two differences of these of two lists and print these results
	fileOneExtras = setOne.difference(setTwo)
	fileTwoExtras = setTwo.difference(setOne)
	f = open(outputFile, 'w')

	#create string to tell user where these files are found
	firstFileString = "Files in " + fileOne + " but not in " + fileTwo +":"
	f.write(firstFileString)
	f.write("\n")
	f.write("\n")

	#print out all of the files in fileOne but not in fileTwo
	for difference in fileOneExtras:
		f.write(difference)
	f.write("\n")
	f.write("\n")

	#create string to tell user where these files are found
	secondFileString = "Files in " + fileTwo + " but not in " + fileOne + ":"
	f.write(secondFileString)
	f.write("\n")
	f.write("\n")

	#print out all of the files in fileTwo but not in fileOne
	for difference in fileTwoExtras:
		f.write(difference)
	f.close()

#first file to consider
fileOne = "finalVideoNamesBackup.txt"

#second file to consider
fileTwo = "recursiveVideoNamesDrive.txt"

#output file
outputFile = "recursiveFinalDiff.txt"

#run the main function
findDifference(fileOne,fileTwo,outputFile)




