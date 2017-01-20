# from tabulate import tabulate
class Skills(object):
	def __init__(self):
		self.skill = {}

	def get_skill_id(self):
	    id = int(input("Enter id of skill:"))
	    return id

	def get_skill_name(self):
	    name = input("Enter name of skill:")
	    return name

	def add_skill(self):
	    self.skill.update({'id': get_skill_id(), 'value': get_skill_name()})

	def view_skill(self):
		return self.skill


