#Imports
import FUDGEPrinter
from FUDGEPrinter import *
import FUDGEDice
from FUDGEDice import *
import FUDGECalculate

#Used variables
loop = 1            # (int) Loop variable. 1 = true, 0 = false
raw_skill_level = 0 # (int) Value between 1 and 9 that's entered when selecting skill level
skill_level = 0     # (int) Translated raw_skill_level onto a -4 to +4 spectrum; used to get total_roll
dice_roll = 0       # (int) Value between -3 and +3 that is used to get total_roll
total_roll = 0      # (int) Value between -7 and +7 that is skill_level + dice_roll
lang_choice = 0      # (int) Value between 1 and 2 that determines language choice

#Objects
defprinter = FPrinter('engl')
dice = FDice()

#Skip starting line
defprinter.FSkipLine()

#Welcome
defprinter.FPrintItem(FTitle['fmaintitle'])  #Welcome Title

#Ask language
defprinter.FSkipLine()
defprinter.FPrintList(Flanguages)

#Language asking loop
loop = 1
while loop == 1:
	defprinter.FSkipLine()
	defprinter.FPrintItem(FPrompt['languageprompt'])
	lang_choice = int(raw_input('> '))
	
	#Check for valid choice
	if langchoice > 0 and langchoice < 3:
		loop = 0
	else:
		defprinter.FSkipLine()
		defprinter.FPrintItem(Ferror['choiceerror'])
		loop = 1

if langchoice == 'eng':
	printer = FUDGEPrinter.FPrinter('eng')
elif langchoice == 'frn':
	printer = FUDGEPrinter.FPrinter('frn')
else:
	pass

printer.FSkipLine()
printer.FPrintList(FSkills) #Display Skill List

#Skill level asking loop
printer.FSkipLine()
loop = 1
while loop == 1:
	printer.FPrintItem(FPrompt['skillprompt'])
	raw_skill_level = int(raw_input('> '))           #Ask for input on skill level
	#Checking for valid choice
	if raw_skill_level > 0 and raw_skill_level < 10: #If between 0 and 10, continue
		loop = 0
	else:                                            #If not between 0 and 10, try again
		printer.FSkipLine()
		printer.FPrintItem(FError['choiceerror'])
		loop = 1
		
#Process skill level into true skill level
skill_level = int(FUDGECalculate.DetermineSkillLevel(raw_skill_level))

#Get dice roll
dice_roll = int(dice.Roll())

#Display skill level and dice roll
printer.FSkipLine()
printer.FPrintResult(FResultIdentifiers['skilllevel'], skill_level) #Print skill level
printer.FPrintResult(FResultIdentifiers['roll'], dice_roll)          #Print dice roll

#Process total roll (Dice roll + skill level)
total_roll = FUDGECalculate.DetermineTotalRoll(dice_roll, skill_level)

printer.FSkipLine()
printer.FPrintResult(FResultIdentifiers['totalroll'], total_roll) #Display total roll (Dice roll + skill level)
printer.FSkipLine()