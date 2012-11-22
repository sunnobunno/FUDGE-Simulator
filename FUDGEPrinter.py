import FLangEng

#Class that controlls all of the printing, given a language
class FPrinter:
	
	#Broken. Determines which language to write in
	def __init__(self, lang):
		self.language = lang
		
		if self.language == 'engl':
			flang = FLangEng
	
	#Method for adding positive or negative prefixes to numbers
	def DetermineIntPrefix(self, i):
		prefix = ''
		
		if i > 0:
			prefix = '+'
		
		return prefix
	
	# Print a numbered list
	def FPrintList(self, list):
		flist = flang.list
		i = 1
		for item in flist:
			print '%d: %s' % (i, item)
			i = i + 1
	
	#Print a single string or other variable
	def FPrintItem(self, item):
		fitem = flang.item
		print fitem
	
	#Skip line
	def FSkipLine(self):
		print ''
	
	#Print result
	def FPrintResult(self, result_type, result):
		prefix = DetermineIntPrefix(result)
		result_description = FPossibleSkills[7 - result]
		
		print '%s: %s%d (%s)' % (result_type, prefix, result, result_description)
	
	def FPrintSkill(self, skill):
		prefix = DetermineIntPrefix(skill)
		
		print 'Skill level: %s%d' % (prefix, skill)
	
	def FPrintRoll(self, roll):
		prefix = DetermineIntPrefix(roll)
		
		print 'Roll: %s%d' % (prefix, roll)
	
	def FPrintTotalRoll(self, totalroll):
		prefix = DetermineIntPrefix(totalroll)
		
		print 'Roll + Skill Level: %s%d' % (prefix, totalroll)