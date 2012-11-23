#Imports
import FUDGEPrinter
import DefaultFPrinter
import FUDGEDice
import FUDGECalculate

#Used variables
loop = 1            # (int) Loop variable. 1 = true, 0 = false
raw_skill_level = 0 # (int) Value between 1 and 9 that's entered when selecting skill level
skill_level = 0     # (int) Translated raw_skill_level onto a -4 to +4 spectrum; used to get total_roll
dice_roll = 0       # (int) Value between -3 and +3 that is used to get total_roll
total_roll = 0      # (int) Value between -7 and +7 that is skill_level + dice_roll
lang_choice = 0      # (int) Value between 1 and 2 that determines language choice

#Objects
defprinter = DefaultFPrinter.DefPrinter('engl')
dice = FUDGEDice.FDice()

#Skip starting line
defprinter.FSkipLine()

#Welcome
defprinter.FPrintItem(DefaultFPrinter.FTitle['fmaintitle'])  #Welcome Title

#Language asking loop
loop = 1
while loop == 1:
	defprinter.FSkipLine()
	defprinter.FPrintList(DefaultFPrinter.FLanguages)
	defprinter.FSkipLine()
	defprinter.FPrintItem(DefaultFPrinter.FPrompt['languageprompt'])
	lang_choice = int(raw_input('> '))
	
	#Check for valid choice
	if lang_choice > 0 and lang_choice < 3:
		loop = 0
	else:
		defprinter.FSkipLine()
		defprinter.FPrintItem(DefaultFPrinter.FError['choiceerror'])
		loop = 1

if lang_choice == 1:  #Englsih (1)
	printer = FUDGEPrinter.FPrinter('eng')
elif lang_choice == 2:  #French (2)
	printer = FUDGEPrinter.FPrinter('frn')
else:
	pass

del defprinter

#Skill level asking loop
loop = 1
while loop == 1:
	printer.FSkipLine()
	printer.FPrintList(FUDGEPrinter.FSkills) #Display Skill List
	printer.FSkipLine()
	printer.FPrintItem(FUDGEPrinter.FPrompt['skillprompt'])
	raw_skill_level = int(raw_input('> '))           #Ask for input on skill level
	#Checking for valid choice
	if raw_skill_level > 0 and raw_skill_level < 10: #If between 0 and 10, continue
		loop = 0
	else:                                            #If not between 0 and 10, try again
		printer.FSkipLine()
		printer.FPrintItem(FUDGEPrinter.FError['choiceerror'])
		loop = 1
		
#Process skill level into true skill level
skill_level = int(FUDGECalculate.DetermineSkillLevel(raw_skill_level))

#Get dice roll
dice_roll = int(dice.Roll())

#Display skill level and dice roll
printer.FSkipLine()
printer.FPrintResult(FUDGEPrinter.FResultIdentifiers['skilllevel'], skill_level) #Print skill level
printer.FPrintResult(FUDGEPrinter.FResultIdentifiers['roll'], dice_roll)          #Print dice roll

#Process total roll (Dice roll + skill level)
total_roll = FUDGECalculate.DetermineTotalRoll(dice_roll, skill_level)

printer.FSkipLine()
printer.FPrintResult(FUDGEPrinter.FResultIdentifiers['totalroll'], total_roll) #Display total roll (Dice roll + skill level)
printer.FSkipLine()