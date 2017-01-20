def ViewSkillsNotStudied():

	skills = arr1
	skillsstudied = arr2

	if arr1 == arr2:

		print("You have studied all skills")

	elif arr1 != arr2:

		x = set(arr1)
		y = set(arr2)
		z = x-y
		
		return list(z)
