#Imports
import FUDGEPrinter
import FUDGEDice
from FUDGEDice import *
import FUDGECalculate

#Used variables
loop = 1            # (int) Loop variable
raw_skill_level = 0 # (int) Value between 1 and 9 that's entered when selecting skill level
skill_level = 0     # (int) Translated raw_skill_level onto a -4 to +4 spectrum; used to get total_roll
dice_roll = 0       # (int) Value between -3 and +3 that is used to get total_roll
total_roll = 0      # (int) Value between -7 and +7 that is skill_level + dice_roll

#Objects
printer = FUDGEPrinter.FPrinter('engl')
dice = FDice()

#Skip starting line
printer.FSkipLine()

#Welcome
printer.FPrintItem(FTitle)  #Welcome Title
printer.FSkipLine()
printer.FPrintList(FSkills) #Display Skill List

#Get Skill Level
printer.FSkipLine()
loop = 1
while loop == 1:
	printer.FPrintItem(FPrompt)
	raw_skill_level = int(raw_input('> '))           #Ask for input on skill level
	#Checking for valid choice
	if raw_skill_level > 0 and raw_skill_level < 10: #If between 0 and 10, continue
		loop = 0
	else:                                            #If not between 0 and 10, try again
		printer.FSkipLine()
		printer.PrintItem(FError['SkillChoice'])
		printer.FSkipLine()
		loop = 1
		
#Process skill level into true skill level
skill_level = int(FUDGECalculate.DetermineSkillLevel(raw_skill_level))

#Get dice roll
dice_roll = int(dice.Roll())

#Display skill level and dice roll
printer.FSkipLine()
printer.FPrintResult(FIdentifier['Skill Level'], skill_level) #Print skill level
printer.FPrintResult(FIdentifier['Roll'], dice_roll)          #Print dice roll

#Process total roll (Dice roll + skill level)
total_roll = FUDGECalculate.DetermineTotalRoll(dice_roll, skill_level)

printer.FSkipLine()
printer.FPrintResult(FIdentifier['Roll + Skill Level'], total_roll) #Display total roll (Dice roll + skill level)
printer.FSkipLine()