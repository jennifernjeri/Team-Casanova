class Skills(object):

	def __init__(self):
		self.skill = {}

	def add_skill(self):
		id = int(input("Enter id of skill:"))
		name = input("Enter name of skill:")
		self.skill.update({'id': id, 'value': name})

	def view_skill(self):
		print "Your skills are:" 
		print self.skill

skills = Skills()
skills.add_skill()
skills.view_skill()

