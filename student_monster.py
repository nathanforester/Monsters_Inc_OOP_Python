from course import *
from monsters import *


class StudentMonster(Monster):

    def __init__(self, name, tax_number, student_number, skill_list=[]):
        super().__init__(name=name, tax_number=tax_number, fur='')
        self.__student_number = student_number
        self.__skill_list = skill_list

    def get_student_number(self):
        return self.__student_number

    def set_student_number(self, new_student_number):
        self.__student_number = new_student_number
        return new_student_number

    def get_skill(self):
        return self.__skill_list

    def add_skill(self, new_skill):
        self.__skill_list.append(new_skill)
        return self.__skill_list


# student_1 = StudentMonster(name='bob', student_number='5555555', tax_number='111')
# print(student_1.get_name())
# user_input = input('what new skill do you want to add? ')
# student_1.add_skill(user_input)
# print(student_1.get_skill())




