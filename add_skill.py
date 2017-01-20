# from tabulate import tabulate
def get_skill_id():
    id = int(input("Enter id of skill:"))
    return id

def get_skill_name():
    name = input("Enter name of skill:")
    return name
def add_skill():
    skill = {}
    skill.update({'id': get_skill_id(), 'value': get_skill_name()})
    return skill

print add_skill()
