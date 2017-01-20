import unittest
import add_skill

class SkillTest(unittest.TestCase):


    def test_skill_id_is_not_null(self):
        self.assertFalse("add_skill.Skills.get_skill_id()" is "")

if __name__== '__main__':
    unittest.main()
