def check_progress():

	if len(skills_studied) == 0:
		progress = 0

	else:
		progress = (len(skills_studied)/len(skills)*100)

	return "Your progress is: {}%".format(progress)
