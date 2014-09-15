#!/usr/bin/python
# - *-coding: utf- 8 - *-
#title:start.py
#description:start python: filesystems
#author:aref
#date:20140915
#version:0.1.0
#usage:python start.py
#python_version:2.7.6
#notes:
#==============================================================================

#imports
import os
import platform
import shutil
from os.path import exists
from os.path import realpath
from os.path import dirname
from os.path import isfile
from os.path import isdir

def listContent():
	inPath = dirname(realpath(__file__))
	contentIdx = 1
	dirContentDict = {}
	print "\tpath: %s\n" % inPath
	for contentName in sorted(os.listdir(inPath)):
		if contentName != __file__:
			#get content type
			contentType = "unknown"
			if isfile(inPath + "/" + contentName):
				contentType = "file"
			elif isdir(inPath + "/" + contentName):
				contentType = "directory"

			dirContentDict[contentIdx] = contentName
			print "\t%d) %s (type: %s)" % (contentIdx, contentName, contentType)
			contentIdx += 1

	print "\n\t(M) for Show Menu and (E) for Exit\n"

	selectedContent = raw_input("Select: ")
	selectedContent = selectedContent.lower()

	if selectedContent == "m" or selectedContent == "e":
		if selectedContent == "m":
			mainmenu()
		else:
			exit("Bye")

	contentName = dirContentDict[int(selectedContent)]
	print contentName

	print "\nActions:"
	if isfile(contentName):
		actionsDicts = {
			"A": ["Read", readingFiles],
			"B": ["Edit", editingFiles], 
			"C": ["Delete", removingContent],
			"D": ["Show Menu"],
			"E": ["Exit"]
		}
	else:
		actionsDicts = {
			"A": ["Rename", renamingContent], 
			"B": ["Delete", removingContent],
			"C": ["Show Menu"],
			"D": ["Exit"]
		}
	actionsList = ""
	for actKey in sorted(actionsDicts):
		actionsList += "  %s) %s" % (actKey, actionsDicts[actKey][0])
	print actionsList + "\n"
	selectedAct = raw_input("Select: ")
	if actionsDicts[selectedAct.upper()][0] == "Show Menu" or actionsDicts[selectedAct.upper()][0] == "Exit":
		if actionsDicts[selectedAct.upper()][0] == "Show Menu":
			mainmenu()
		else:
			exit("Bye")
	else:
		actionsDicts[selectedAct.upper()][1](contentName)

def readingFiles(name='notset'):
	inPath = dirname(realpath(__file__))
	#ask for file name
	filename = name if name != 'notset' else raw_input("Please enter the file name ? ")
	if isfile(inPath + "/" + filename) == False:
		print "%s is not a file!" % filename
		exit(0)
	print "%s Content:\n" % filename
	openFile = open(filename, "r")
	print openFile.read()
	print "\n"
	listContent()

def creatingFiles():
	print "Hint: Type M for back to Main Menu"
	filename = raw_input("Please type a file name (with extension): ")
	if filename.lower() == "m" or len(filename) < 1:
		mainmenu()
	filename = filename.replace(' ', '_')

	#check exists
	isExists = exists(filename)
	if isExists:
		print "sorry, %s is already exists" % filename
		exit(0)

	#open new file
	newfile = open(filename, "w")

	#ask for file content
	print "Contents of the file:"
	fileContent = raw_input()

	#write file content into file
	newfile.write(fileContent)

	#finallize file
	newfile.close()

	#show result message
	print "\nSuccess\n"
	listContent()

def creatingDirectories():
	print "Hint: Type M for back to Main Menu"
	directoryName = raw_input("Type new Directory name: ")
	if directoryName.lower() == "m" or len(directoryName) < 1:
		mainmenu()
	if exists(directoryName):
		print "%s is already exists!"
		creatingDirectories()

	os.makedirs(directoryName)
	print "\nSuccess\n"
	listContent()

def editingFiles(name="notset"):
	inPath = dirname(realpath(__file__))
	#ask for file name
	filename = name if name != "notset" else raw_input("Please enter the file/directory name ? ")
	
	message = "what do you want to do with %s ?" % filename
	actionsDicts = ['Rename', 'Edit Content'] if isfile(filename) else ['Rename']
	actionIdx = 1
	for act in actionsDicts:
		message += "\n\t%d) %s" % (actionIdx, act)
		actionIdx += 1
	message += "\nSelect: "
	action   = raw_input(message)
	action   = int(action) - 1
	actionLoader = [renamingContent, editingContent] if isfile(filename) else [renamingContent]
	actionLoader[action](filename)

def renamingContent(currentName):
	#rename content
	print "Current Name: %s" % currentName
	newName = raw_input("New Name: ")
	os.rename(currentName, newName)
	print "successfully rename %s to %s" % (currentName, newName)
	listContent()

def editingContent(filename):
	#edit content
	openFile = open(filename, "r")
	print "- %s content:\n" % filename
	print openFile.read()
	print "\n- New Content:\n"
	newContent = raw_input()
	openFile = open(filename, "w")
	openFile.truncate()
	openFile.write(newContent)
	openFile.close()
	print "\nSuccess\n"
	listContent()

def removingContent(name="notset"):

	inPath = dirname(realpath(__file__))
	#ask for file name
	contentName = name if name != "notset" else raw_input("Please enter the file/directory name ? ")

	if exists(contentName) == False:
		print "%s is not exists!" % contentName
		exit(1)

	contentType = "unknown"
	if isfile(contentName):
		contentType = "file"
	elif isdir(contentName):
		contentType = "directory"
	#confirm
	confMsg = "Are you sure that you want to remove %s (%s) ? (y/N) " % (contentName, contentType)
	confirm = raw_input(confMsg)
	confirm = confirm.lower()
	if confirm == "n" or confirm != "y":
		exit(0)
	else:
		if contentType == "file":
			os.remove(contentName)
		else:
			shutil.rmtree(contentName)
	print "\nSuccess\n"
	listContent()

def mainmenu():
	# let's generate the index list
	os.system("clear")
	print "Python %s" % platform.python_version()
	print "Start Python - Part %d: %s" % (1, 'FileSystems')

	#dictionary of index list; objects we used in javascript in python calls dictionaries
	indexDict = {
		'A': 'List Content',
		'B': 'Create File',
		'C': 'Create Directory',
		'D': 'Exit'
	}
	for dictIdx in sorted(indexDict):
		print "\t%s) %s" % (dictIdx, indexDict[dictIdx])

	#ask user to select one
	selectedIdx = raw_input("Please select index: ")
	selectedIdx = selectedIdx.upper()

	if selectedIdx == 'D':
		exit("Bye")

	#clear
	os.system("clear")

	#print title
	print "%s in Python\n" % indexDict[selectedIdx]

	#a switch-case for calling operations
	switchDicts = {
		'A': listContent,
		'B': creatingFiles,
		'C': creatingDirectories
	}
	switchDicts[selectedIdx]()

mainmenu()