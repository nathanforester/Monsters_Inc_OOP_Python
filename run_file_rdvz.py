from student_monster import *

# create new student object
student_1 = StudentMonster(name='bob', student_number='5555555', tax_number='111')

# add a skill to each of the students
# print(student_1.get_name())
# user_input = input('what new skill do you want to add? ')
# student_1.add_skill(user_input)


# create a course(initialise)
course_1 = Course(module_name='silly', start_date='11/03/1986')
user_input = input('enter a course name: ')
course_1.create_module_name(user_input)
print(course_1.get_module_name())



# append student object/instances to list of student attributes in one of the courses
user_input = input('add skill: ')
student_1.add_skill(user_input)
for student in student_1.get_skill():
    print(student_1.get_name() + ', ', course_1.get_module_name(), student_1.get_skill())
print(f'{student_1.get_name()} has {user_input} as a skill')



# xtra: get the list of students, iterate over it and print each of the student's names


