#!/usr/bin/env python
# Marilene Soares da Costa - Script
'''
Assumptions and clarifications:

- the script below and the unit test (test_PythonEx.py) was originally
written in Python 2.7.13, and converted into Python 3 (May 2018)
obs: aside from small syntax changes (like using print()), 
the main issue was using re.compile - the keyword has to be as utf-8 now
otherwise python 3 throws an error: 
		cannot use a string pattern on a bytes-like object
- the user will enter a string or a complete regular expression (regex) 
to be located within the contents of all files in the chosen root_dir. 
- Once a the first match is found in a file, that is counted as 1 (success).
- The final output is the number of successful matches (a maximum of
one per file) for each subdirectory including the root_dir.
- The output is shown in two forms:
- - as a Python dictionary where every key is a subdirectory path (including
the root_dir), and corresponding values are the number of times the keyword
was found on a file in that subdirectory.
- - as a graph where each X corresponds to as subdir name string, and each
corresponding Y represents the count values. 

'''
import sys
import io
import os
import glob
import re
import mmap
import matplotlib.pyplot as plt

# create dict to store overall results
output = {}

# traverse the directory, calling searchSubdir 
def walk(root_dir, keyword):
	# compiles regex into a pattern object - SRE-pattern obj - to use re.search later
	
	reKey = re.compile(keyword.encode("utf-8"))

	# traverse directories
	for path, subdirs, files in os.walk(root_dir):
		output[path] = searchSubdir(path, reKey)
	return output

# counts in how many files, in each subdir, the keyword occurs at least once
def searchSubdir(subdir, reKey):
	# create dict to store results for each subdir 
	matches = {}
	count = 0
    # using glob to list directories while ignoring hidden files
	for file in glob.glob(os.path.join(subdir, '*')):
		# check if it is a file, and that is not empty (avoids Windows error) 
		if os.path.isfile(file) and os.stat(file).st_size != 0:
			with open(file) as f:
				# Memory-map files instead of reading the contents directly
				m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
				if re.search(reKey, m):
					count += 1
					m.close()

	matches[subdir] = count
	return matches[subdir]

# splits each directory string into one subdir per line for readability
def split_dir(str):
	sList = str.split("/")
	return '-\n'.join(sList[i] for i in range(0, len(sList)))

# generate 2nd required output (graph)
def Graph(outuput):
	plt.bar(range(len(output)), output.values(), align='center')
	plt.xticks(range(len(output)), [split_dir(i) for i in output.keys()])
	plt.show()

def isDirInCWD(root_dir):
	if os.path.isdir(root_dir): return True
	




if __name__ == '__main__':
	# getting use input and testing if root_dir is in cwd
	root_dir = raw_input('Enter the root directory: ')
	if isDirInCWD(root_dir):
		keyword = raw_input('Enter keyword or regex to search: ')
	else:
		print ('this directory is not in the cwd.')
		restart = raw_input('Restart script? y or n: ')
		if restart == 'y':
			os.execl(sys.executable, sys.executable, *sys.argv)
		else:
			print ('Terminating the script.')
			exit()


	# generate 1st required output (Python dict)
	print (walkroot_dir, keyword)

	# generate 2nd required output (graph)
	Graph(output)

