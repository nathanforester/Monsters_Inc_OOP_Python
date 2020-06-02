from course import *
from monsters import *


class StudentMonster(Monster):

    def __init__(self, student_number, skill_list):
        super().__init__(self, tax_number=student_number, fur='')
        self.__student_number = student_number
        self.__skill_list = skill_list

    def get_student_number(self):
        return self.__student_number
    
    def set_student_number(self, new_student_number):
        self.__student_number = new_student_number
        return new_student_number

    def get_skill(self):
        return self.__skill_list

    def add_skill(self, new_skill, new_student_number):
        self.__skill_list = new_skill
        new_skill = input('enter a scary skill, muahahahaha!: ')
        return new_skill + new_student_number









