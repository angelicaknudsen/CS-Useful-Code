import zipfile
import itertools
import time

#btw I highly advise just using a function that opens the text file and puts its text into a variable, which you'd split for a list.
#previously, I just copied and pasted all of the text from the textfile here intoa giant block of text, which worked, but it was a bit much

listText = 'Seriously dont do what i did... just open a file and put the text from that into this variable, like so'
listText = open('wordlist.txt', 'r')
listText = listText.read()
wordList = listText.split()

# Function for extracting zip files to test if the password works!
def extractFile(zip_file, password):
    try:
        zip_file.extractall(pwd=password)
        return True
    except KeyboardInterrupt:
        exit(0)
    except Exception, e: # for some reason, this resulted in a syntax error while I wasn't in the virtual machine, so I put 'Exception as e' as the fix
        pass

# Main code starts here...
# The file name of the zip file.
zipfilename = 'flag.zip'

first_half_password = ''
# We don't know what characters they add afterwards...
# This is case sensitive!
#alphabet = 'abcdefghijklmnopqrstuvwxyz'
zip_file = zipfile.ZipFile(zipfilename)

'''
I should explain what these for loops are doing...
The conditions of the password were that it had to have one number and one capital letter
In order to do this, I had find every possible combination of a capitalized letter and a number in any spot in the provided words (to be safe, but the number would likely just be placed at the end,
which was the case here)
Of course the main loop (c) runs for as long as the length of the word list (since the second number is exclusive in the range parameters, this worked perfectly with indexing)
Thankfully, each word in the list was only 7 characters, so that significantly helped
The x loop is for capitalizing the character
The y loop is for placing the number (since there are 7 characters, there are 8 possible spots for the number to be placed)
The z loop is for trying out every possible number (0-9, so ten possible different digits)
Btw the password ended up being Cartoon4
This makes me suspicious that I really only had to capitalize the first character and simply add on a digit (0-9) at the end...
oh well extra indexing practice
'''
for c in range (0, len(wordList)):
    # Slowing it down on purpose to make it work better with the web terminal
    # Remove at your peril
    # Jelly's Input: if I were to just leave this, I'd be here all day
    time.sleep(0.000)

    for x in range (0, 7):
	for y in range(0, 8):
	    for z in range(0, 10):
		char = wordList[c][x].upper()
		if x == 0:	
		    password = char + wordList[c][-6:]
		elif x == 1:
		    password = wordList[c][:1] + char + wordList[c][-5:]
		elif x == 2:
		    password = wordList[c][:2] + char + wordList[c][-4:]
		elif x == 3:
		    password = wordList[c][:3] + char + wordList[c][-3:]
		elif x == 4:
		    password = wordList[c][:4] + char + wordList[c][-2:]
		elif x == 5:
		    password = wordList[c][:5] + char + wordList[c][-1:]
		elif x == 6:
		    password = wordList[c][:6] + char

		if y == 0:
		    password = str(z) + password
		elif y == 1:
		    password = password[:1] + str(z) + password[-6:]
		elif y == 2:
		    password = password[:2] + str(z) + password[-5:]
		elif y == 3:
		    password = password[:3] + str(z) + password[-4:]
		elif y == 4:
		    password = password[:4] + str(z) + password[-3:]
		elif y == 5:
		    password = password[:5] + str(z) + password[-2:]
		elif y == 6:
		    password = password[:6] + str(z) + password[-1:]
		elif y == 7:
		    password = password + str(z)
		        
		# Try to extract the file.
		print "Trying: %s" % password
		# If the file was extracted, you found the right password.
		if extractFile(zip_file, password):
		    print('*' * 20)
		    print('Password found: %s' % password)
		    print('Files extracted...')
		    exit(0)

# If no password was found by the end, let us know!
print('Password not found.')
