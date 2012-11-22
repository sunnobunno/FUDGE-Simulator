def DetermineIntPrefix(i): #Method for adding positive or negative prefixes to numbers
	prefix = ""
	
	if i > 0:
		prefix = "+"
	
	return prefix

#Class for printing everything
class FPrinter(object):
	
	# Print a numbered list
	def FPrintList(self, list):
		i = 1
		for item in list:
			print "%d: %s" % (i, item)
			i = i + 1
	
	#Print a single string or other variable
	def FPrintItem(self, item):
		print item
	
	#Skip line
	def FSkipLine(self):
		print ""
	
	#Print result
	def FPrintResult(self, result_type, result):
		prefix = DetermineIntPrefix(result)
		result_description = FSkillsPure[7 - result]
		
		print "%s: %s%d (%s)" % (result_type, prefix, result, result_description)
	
	def FPrintSkill(self, skill):
		prefix = DetermineIntPrefix(skill)
		
		print "Skill level: %s%d" % (prefix, skill)
	
	def FPrintRoll(self, roll):
		prefix = DetermineIntPrefix(roll)
		
		print "Roll: %s%d" % (prefix, roll)
	
	def FPrintTotalRoll(self, totalroll):
		prefix = DetermineIntPrefix(totalroll)
	
		print "Roll + Skill Level: %s%d" % (prefix, totalroll)

FSkills = ["Legendary (+4)",
	"Superb    (+3)",
	"Great     (+2)",
	"Fair      (+1)",
	"Average   (+0)",
	"Poor      (-1)",
	"Mediocre  (-2)",
	"Terrible  (-3)",
	"Pathetic  (-4)"]

FPossibleSkills = ["Legendary",
	"Legendary",
	"Legendary",
	"Legendary",
	"Superb",
	"Great",
	"Fair",
	"Average",
	"Poor",
	"Mediocre",
	"Terrible",
	"Pathetic",
	"Pathetic",
	"Pathetic",
	"Pathetic"]

FTitle = "------- FUDGE Resolution Simulator -------"

FPrompt = "Enter corresponding skill number"

FError = {"SkillChoice" : "Please input a valid selection"}

FIdentifier = {"Skill Level" : "Skill Level",
	"Roll" : "Roll",
	"Roll + Skill Level" : "Roll + Skill Level"}