# Read, Write, Empty, Copy files

from os.path import os, exists

selections = """\nWhat would you like to do with this file?\n 	        
Add to the file? (Enter 'A')\nDelete file? (Enter 'D')\nRead what's in the file? (Enter 'R')
Copy over to new file? (Enter 'C')"""
filename = ""
choice  = " "		# set our choice variable to blank
answers = "adrcn"		# set our answer string to test for input

while choice not in answers: 				# as long as choice isn't found in our answer string, follow code below
	filename = raw_input("\nWhat file would you like to modify?\n")	# enter filename to modify
	print selections
	choice = raw_input("\nEnter your selection: ").lower()		# ask for user input, convert it to lowercase
	if choice == "a":											# testing for input
		target = open(filename, "a+")							# open our filename with append rights and set target equal to it
		append = raw_input("\nOkay, enter what you would like to add:\n")	# ask for user input to append to file
		target.write(append + "\n")								# write what we appended to file plus a new line to keep it clean
		target.close()											# close the file in order to save it
		print "\nThis is your edited file: \n"
		target = open(filename)									# re-open the file
		print target.read()										# print our file to the screen
	elif choice == "d":
		if exists(filename):
			os.remove(filename)
			print "\nYour file has been deleted!"
		else:
			print "That file does not exist. Please try again.\n"
			choice = ""
	elif choice == "r":			
		target = open(filename)									# open our file with read rights, automatically 'read' if arg is empty
		print "Here is your file:\n"
		print target.read()										# print our file to the screen
		target.close()											# close to save file
	elif choice == "c":
		target = open(filename, "r+")							# open old file with read+ rights so it can read/write w/o truncating
		newfile = raw_input("\nWhat file would you like to copy to?\n")	# asks for name of file you would like to copy to
		out_file = open(newfile, 'w')							# opens that file (creates it if it doesn't exist), empties before writing
		indata = target.read()									# data that we want to transfer over is our target file
		out_file.write(indata)									# writes over our new file with data from target file
		print "\nYour file has been copied to: " + newfile
		out_file.close()										# close the 2 files to save over them
		target.close()
		out_file = open(newfile)								# re-opens new file to view contents
		print "\nHere is your new file: \n\n" + out_file.read()									# print new file to screen
	else:
		print "\nYou didn't make a valid selection. I'm sorry, try again."		# repeat loop if invalid input