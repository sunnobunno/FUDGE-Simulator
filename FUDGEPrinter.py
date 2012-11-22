#Imports
import xml.etree.ElementTree as ET

#Method for adding positive or negative prefixes to numbers
def DetermineIntPrefix(i):
	prefix = ''
	
	if i > 0:
		prefix = '+'
	
	return prefix


#Method to append items in an XML element to a list
def AppendXMLToList(xmlroot, elementchoice, list):
	for child in xmlroot.iter(elementchoice):
		i = 0
		for elements in child:
			list.append(child[i].text)
			i = i + 1

#Method to append items in an XML element to a dictionary
def AppendXMLToDict(xmlroot, elementchoice, dict):
	for child in xmlroot.iter(elementchoice):
		i = 0
		for elements in child:
			dict[str(child[i].tag)] = child[i].text
			i = i + 1

#Method to append a single item form an XML element to a single variable
#Obselete
def AppendXMLToItem(xmlroot, elementchoice, item):
	for child in xmlroot.iter('elementchoice'):
		item = child.text

FSkills = []            #List of skills for asking skill level
FPossibleSkills = []    #List of all possible outcomes (Skill level + dice roll)
FTitle = {}             #Titles
FPrompt = {}            #Promts
FError = {}             #Errors
FResultIdentifiers = {} #Identifiers for FPtintResult()

#Class that controlls all of the printing, given a language
class FPrinter:
	
	#Broken. Determines which language to write in
	def __init__(self, lang):
		self.language = lang
		
		#Check language
		if self.language == 'engl':
			tree = ET.parse('EngLang.xml')
			root = tree.getroot()
		
		#Apply langfile to lists and items
		AppendXMLToList(root, 'flistingskills', FSkills)	
		AppendXMLToList(root, 'fpossibleskills', FPossibleSkills)
		AppendXMLToDict(root, 'ftitle', FTitle)
		AppendXMLToDict(root, 'fprompt', FPrompt)
		AppendXMLToDict(root, 'ferror', FError)
		AppendXMLToDict(root, 'fresultidentifiers', FResultIdentifiers)
	
	
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
		result_description = FPossibleSkills[7 - result]
		
		print '%s: %s%d (%s)' % (result_type, prefix, result, result_description)