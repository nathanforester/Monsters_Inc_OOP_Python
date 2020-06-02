
from course import *

test_monster_a = Monster(name='a', tax_number='2', fur='b')
print(test_monster_a)


print(test_monster_a.create_name(new_name=''))

from course import *
test_monster_b = Course()
print(test_monster_b.create_module_name(new_module_name=''), test_monster_b.create_start_date(new_start_date=''))

from student_monster import *
test_monster = StudentMonster(student_number='3', skill_list='evil')
print(test_monster_a.tax_number(new_tax_number='', new_name=''), test_monster.add_skill(new_skill='', new_student_number=''))

print(test_monster_a.create_name(new_name=''), test_monster_b.create_module_name(new_module_name=''))



