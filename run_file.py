
from course import *

test_monster = Monster(name='a', tax_number='2', fur='b')
print(test_monster)


print(test_monster.create_name(new_name=''))

from course import *
test_monster = Course()
print(test_monster.create_module_name(new_module_name=''), test_monster.create_start_date(new_start_date=''))

from student_monster import *
test_monster = StudentMonster(student_number='3', skill_list='evil')
print(test_monster.add_skill(new_skill=''))



