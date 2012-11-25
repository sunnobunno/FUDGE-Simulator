#Imports
import xml.etree.ElementTree as ET
import XMLParse
from XMLParse import *

#Method for adding positive or negative prefixes to numbers
def DetermineIntPrefix(i):
	prefix = ''
	
	if i > 0:
		prefix = '+'
	
	return prefix

FSkills = []            #List of skills for asking skill level
FPossibleSkills = []    #List of all possible outcomes (Skill level + dice roll)
FTitle = {}             #Titles
FPrompt = {}            #Promts
FError = {}             #Errors
FResultIdentifiers = {} #Identifiers for FPtintResult()
FLanguages = []         #Language names

#Class that controlls all of the printing, given a language
class FPrinter:
	
	#Determines which language to write in
	def __init__(self, lang):
		self.lang = lang
		
		self.tree = ET.parse('EngLang.xml')
		self.root = self.tree.getroot()
		
		#Check language
		#English
		if self.lang == 'eng':
			self.tree = ET.parse('EngLang.xml')
			self.root = self.tree.getroot()
		#French
		elif self.lang == 'frn':
			self.tree = ET.parse('FrnLang.xml')
			self.root = self.tree.getroot()
		#--Filler--
		else:
			pass
		
		#Apply langfile to lists and items
		AppendXMLToList(self.root, 'flistingskills', FSkills)	
		AppendXMLToList(self.root, 'fpossibleskills', FPossibleSkills)
		AppendXMLToDict(self.root, 'ftitle', FTitle)
		AppendXMLToDict(self.root, 'fprompt', FPrompt)
		AppendXMLToDict(self.root, 'ferror', FError)
		AppendXMLToDict(self.root, 'fresultidentifiers', FResultIdentifiers)
		AppendXMLToList(self.root, 'flanguages', FLanguages)
	
	# Print a numbered list
	def FPrintList(self, list):
		i = 1
		for item in list:
			print '%d: %s' % (i, item)
			i = i + 1
	
	#Print a single string or other variable
	def FPrintItem(self, item):
		print item
	
	#Skip line
	def FSkipLine(self):
		print ''
	
	#Print result
	def FPrintResult(self, result_type, result):
		prefix = DetermineIntPrefix(result)
		result_description = FPossibleSkills[6 - result]
		
		print '%s: %s%d (%s)' % (result_type, prefix, result, result_description)