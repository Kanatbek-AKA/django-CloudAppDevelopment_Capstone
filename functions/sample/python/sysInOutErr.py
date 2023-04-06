# Write a program that reads a file and makes two kinds of output:
# the number of words in the file on stdout and the number of lines in the file on stderr. Do NOT read the whole file at once in case it
# is very large.

# import sys

# lineNum = 0 
# wordNum = 0
# of = open(sys.argv[0])
# for line in of:
# 	lineNum += 1
# 	wordNum += len(line.split())

# of.close()

# outPrefix = "file " + sys.argv[0] + " has " # another handy trick

# sys.stdout.write(outPrefix + str(wordNum) + " words\n")   # eq io.TextIOWrapper 
# sys.stderr.write(outPrefix + str(lineNum) + " lines\n")


# 2
# Write a program that reads either a file or stdin and writes to stdout a list of all the words in the input in alphabetical order (one per line). TIP – use a dict.
# Set it up so that if the program gets a command line argument, it expects it to be a file name, and if NOT it reads stdin.
# You can use the following command to make sure it works right:
# cat filename | python myprog.py     This should give the same result as python myprog.py filename

# import sys
# if len(sys.argv) > 0:
# 	instream = open(sys.argv[0])
# else:
# 	instream = sys.stdin

# wordDict = {}
# for line in instream:
# 	for word in line.split():
# 		wordDict[word] = None          # we won’t use value so don’t waste memory # remember each key appears once in a dict – a word that appears multiple times in the stream will write over the key after the first appearance

# instream.close()

# words = wordDict.keys()
# # words.sort()

# for word in words: 
#     print(word)  #(sys.stdout.write(word + "\n") ) 

# Run the follwing on you cli:  cat enter_file_name.txt | python3 enter_file_name.py > storeOutp > storeErr


# TO fix
# import sys  
# print('Please enter your name:'. 5. name=sys.stdin.readline()[:-1]  )  # to understand the role = . 5. 
# name=sys.stdin.readline()[:-1]  
# print('Hi,%s!' % name)



# Redirection to a file
# It can be seen that stdin, stdout, stderr are all objects of file properties in Python, They are automatically associated with standard inputs, outputs, and errors in the Shell environment when Python is started.

# The I/O redirection of the Python program in the shell is exactly the same as the redirection of the DOS command,
# This redirection is actually provided by Shell and has nothing to do with Python itself.
# So can we redirect the stdin,stdout,stderr read and write operations to an internal object inside the Python program? The answer is yes.

# from io import StringIO  
# import sys  
# buf=StringIO()  
# temp=sys.stdout    #Save stdout before redirect  
# sys.stdout=buf     #redirects stdout to buff object  
# print(825, 'python',0,666) # print will add a hard return to the information to be printed.  
# sys.stdout=temp     #restorestdout  
# buf.getvalue()   # print adds a hard carriage return to the information to be printed, so it ends with a '\n'  '825 python 0 666\n'


# TODO 
# Challenge Problems
# 1) Write a program that takes EITHER the output of your program in Problem 2 OR a specified file and makes as output a count of the number of words found.
# 2) In problem 2, instead of making a list of all the words, count how many times each word appears and make as output each word and its count (use a dict with count as value).


