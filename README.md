# backup-videos-storywall
Get a list of all of the videos from backup server file system and all of the videos from google drive. Compare these to make sure that everything is currently backed up correctly. Back up videos that haven’t been backed up yet.

# backup-videos-storywall
Get a list of all of the videos from the TeachAids backup server file system and all of the videos from the TeachAids google drive. Compare these to make sure that everything is currently backed up correctly. Back up videos that haven’t been backed up yet.

Steps to run the code:
1. Run quickstart.py to set up google drive API system
2. Run recursiveCreateListDrive.py to create the list of files in the google drive
3. Run findDiff.py to create list of files in one location but not the other

Different files Contained:

-quickstart.py is the code neccesary to first implement the google drive API.

-credentials.json are credentials unique to each account that allow one to run the google drive API. These are not currently uploaded

-recursiveCreateListDrive.py is the code to go through the entire google drive final video folder to find all of the files and then output them to the recusiveVideoNamesDrive.txt file. This recursively searches through all folders within to do so.

-finalVideoNamesBackup.txt is a text file containing all of the files within the backup server that was created simply by navigating within the file space locally on the computer to the location of the server and then running the command line code:
find . -type f > /pathOfInterest/finalVideoNamesBackup.txt

-recursiveVideoNamesDrive.txt is a txt file that contains all of the files within the google drive folder. It was created by running the recursiveCreateListDrive.py file

-findDiff.py is a program that when run looks through the two txt files (finalVideoNamesBackup.txt and recursiveVideoNamesDrive.txt) to see which files are contained in one but aren't contained within the other. It then outputs this result into recursiveFinalDiff.txt

recursiveFinalDiff.txt contains the final difference between the two documents in terms of which files are present in one location but not the other.

