
from course import *

test_monster_a = Monster(name='a', tax_number='2', fur='b')
print(test_monster_a)




from course import *
test_monster_b = Course('blah', 'blah')
print(test_monster_b.create_module_name(new_module_name=''), test_monster_b.create_start_date(new_start_date='', new_module_name=''))

from student_monster import *
test_monster = StudentMonster(name='bob', tax_number=5, student_number=3, skill_list='evil')
print(test_monster_a.tax_number(new_tax_number='', new_name=''))



student_1 = StudentMonster(name='bob', student_number='5555555', tax_number='111')
print(student_1.get_name())
user_input = input('what new skill do you want to add? ')
student_1.add_skill(user_input)
print(student_1.get_skill())

from course import *

student_1 = Course('bob', 555, 'brown')
user_input = input('please enter a name: ')
student_1.get_names(user_input)
print(student_1.get_name())


