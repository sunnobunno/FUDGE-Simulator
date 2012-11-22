#Imports
import FUDGEPrinter
from FUDGEPrinter import *
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
dice = FDice()

#Skip starting line
FSkipLine()

#Welcome
FPrintItem(FTitle)  #Welcome Title
FSkipLine()
FPrintList(FSkills) #Display Skill List

#Get Skill Level
FSkipLine()
loop = 1
while loop == 1:
	FPrintItem(FPrompt)
	raw_skill_level = int(raw_input("> "))           #Ask for input on skill level
	#Checking for valid choice
	if raw_skill_level > 0 and raw_skill_level < 10: #If between 0 and 10, continue
		loop = 0
	else:                                            #If not between 0 and 10, try again
		FSkipLine()
		PrintItem(FError["SkillChoice"])
		FSkipLine()
		loop = 1
		
#Process skill level into true skill level
skill_level = int(FUDGECalculate.DetermineSkillLevel(raw_skill_level))

#Get dice roll
dice_roll = int(dice.Roll())

#Display skill level and dice roll
FSkipLine()
FPrintResult(FIdentifier["Skill Level"], skill_level) #Print skill level
FPrintResult(FIdentifier["Roll"], dice_roll)          #Print dice roll

#Process total roll (Dice roll + skill level)
total_roll = FUDGECalculate.DetermineTotalRoll(dice_roll, skill_level)

FSkipLine()
FPrintResult(FIdentifier["Roll + Skill Level"], total_roll) #Display total roll (Dice roll + skill level)
FSkipLine()