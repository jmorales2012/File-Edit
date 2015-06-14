# Read, Write, Empty, Copy files
from os.path import os, exists

def read_file(filename):										# create function for reading a file
	target = open(filename)										# opens entered file
	print "\nHere is your file:\n\n", target.read()				# prints file to screen
	target.close()												# closes file

def append_file(filename):										# create function for appending a file
	target = open(filename, 'a+')								# open file with append rights
	append = raw_input("\nEnter the text you would like to add:\n")
	target.write(append + "\n")									# appends entered text to end of file
	target.close()												# close file to save it


def copy_file(filename):										# create function for copying a file
	target = open(filename, 'r+')								# open the file with read/write rights
	new_file = raw_input("\nEnter the name of the file you'd like to copy to: ")
	out_file = open(new_file, 'w')								# open the new file, truncating it
	indata = target.read()										# copies data from old file to new string
	out_file.write(indata)										# write into new file with string from old file
	print "\nYour file has been copied to: ", new_file
	out_file.close()											# close new file to save it
	print "\nHere is your new file: \n\n", open(new_file).read()# prints new file to screen

def delete_file(filename):										# create function to delete a file
	if exists(filename):										# checks to see if file exists
		os.remove(filename)										# if it does, delete it
		print "\nYour file has been deleted!"
	else:														# if not, print that and set choice to blank to repeat loop
		print "\nThat file does not exist. Please try again.\n"
		choice = " "

def second_choice(choice):										# create function for allowing user another choice at end of program
	choice = raw_input("Would you like to do anything else? (Y/N): ").lower()
	if choice == 'y':											# if choice is 'y' return a blank space to repeat loop
		return " "
	else: 														# if not, return 'e' to exit loop
		return "e"

selections = """\nWhat would you like to do?\n\n1. Read a file? (Enter 'R')
2. Create/Add to a file? (Enter 'A')\n3. Copy a file? (Enter 'C')\n4. Delete a file? (Enter 'D')
5. Exit (Enter 'E')\n"""
choice = " "													# set choice to blank space to initiate loop
answers = "racde"												# string of answers to check in loop

while choice not in answers:									# initiate loop
	print selections
	choice = raw_input("\nEnter your selection: ").lower()		# convert selection to lowercase, assign to choice
	filename = raw_input("\nEnter file name to modify: ")		# enter file name
	if not exists(filename) and choice != 'a':					# check to see if filename exists and if choice isn't 'a'
		print "\nSorry, that file doesn't exist.\n"				# checking for 'a' because we can create new file with choice 'a'
		choice = " "
	elif choice == 'r':											# if 'r', call read_file
		read_file(filename)
	elif choice == 'a':											# if 'a', call append_file
		append_file(filename)
	elif choice == 'c':											# if 'c', call copy_file
		copy_file(filename)
	elif choice == 'd':											# if 'd', call delete_file
		delete_file(filename)
	elif choice == 'e':											# if 'e', exit program
		break
	else:														# if choice isn't a valid selection, repeat loop
		print "\nNot a valid selection. Please try again."
	choice = second_choice(choice)								# call second_choice to see if user wants to run program again