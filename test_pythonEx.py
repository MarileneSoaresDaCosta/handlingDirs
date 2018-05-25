#!/usr/bin/env python
# Marilene Soares da Costa - Python Exercise - Tests

import unittest
import os
import sys
import glob
import shutil
import pythonEx


class TestPythonEx(unittest.TestCase):

	def createDir(name):
		if os.path.isdir(name):
			print ('this dir already exists')
		else:
			print ('creating new dir')
			os.mkdir(name)
			if os.path.isdir(name):
				print ('now the dir has been created')

	def setUp(self):
		'''
		creates a test directory with files with and without keywords
		'''
		self.rootName = 'testDirRoot'
		if not os.path.isdir(self.rootName): 
			os.mkdir(self.rootName)

		# defining names of subdirs
		subdirList = []
		for i in range(1,4):
			subdirList.append(self.rootName + "/sub" + str(i))
		for subdir in subdirList:
			#createDir(subdir)
			if not os.path.isdir(subdir): 
				os.mkdir(subdir)

		not_keywords = "string for all files"
		keywords = "alpha_TESTResult.txt caterpillar CaTeRpIlLaR"

		# creates files with keywords
		k = 5
		for subdir in subdirList:
			for i in range(1, k):
				filename = "haskeys" + str(i) + ".txt"
				filepath = os.path.join(subdir, filename)
				with open(filepath, "w") as f:
					f.write(keywords)
					f.close
				filename = "haskeys"
			k += 1

		# creates files without keywords
		n = 4
		for subdir in subdirList:
			for i in range(1, n):
				filename = "nokeys" + str(i) + ".txt"
				filepath = os.path.join(subdir, filename)
				with open(filepath, "w") as f:
					f.write(not_keywords)
					f.close
				filename = "nokeys"
			n += 1

		# create one empty directory under the root
		empdir = self.rootName + "/Empty"
		if not os.path.isdir(empdir): 
				os.mkdir(empdir)

	# helper function
	def removeDir(self, path):
			if os.path.isdir(path):
				shutil.rmtree(path, ignore_errors=True)
			else:
				print ("Not a valid directory")

	
	# testing function walk
	def test_simpleString(self):
		expectedOutput = {'testDirRoot':0, 'testDirRoot/sub1': 4, 'testDirRoot/sub2': 5,'testDirRoot/sub3': 6, 'testDirRoot/Empty': 0}	
		self.assertEqual(pythonEx.walk(self.rootName, 'caterpillar'), expectedOutput)

	def test_regex1(self):
		expectedOutput = {'testDirRoot':0, 'testDirRoot/sub1': 4, 'testDirRoot/sub2': 5,'testDirRoot/sub3': 6, 'testDirRoot/Empty': 0}	
		self.assertEqual(pythonEx.walk(self.rootName, '(?i)(caterpillar)'), expectedOutput)


	def test_regex2(self):
		expectedOutput = {'testDirRoot':0, 'testDirRoot/sub1': 4, 'testDirRoot/sub2': 5,'testDirRoot/sub3': 6, 'testDirRoot/Empty': 0}	
		self.assertEqual(pythonEx.walk(self.rootName, "^[a-zA-Z]+_TESTResult.*"), expectedOutput)

	def main():
		unittest.main()

if __name__ == '__main__':
	unittest.main()
