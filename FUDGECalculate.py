def DetermineSkillLevel(raw_skill_level):
	skill_level = (raw_skill_level * -1) + 5
	return skill_level

def DetermineTotalRoll(die_roll, skill_level):
	total_roll = die_roll + skill_level
	return int(total_roll)