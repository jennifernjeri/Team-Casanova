def get_skill_id():
    id = input("Enter id of skill:")
    return id

def get_skill_name():
    name = input("Enter name of skill:")
    return name
def add_skill():
    skill = {}
    skill_id = int(get_skill_id())
    skill_name = get_skill_name()
    skill = {skill_id:[skill_name, False]}
    return skill
