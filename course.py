from monsters import *


class Course(Monster):

    def __init__(self, module_name, start_date, list_of_students=[]):
        super().__init__(name='', tax_number='', fur='')
        self.list_of_students = list_of_students
        self.__module_name = module_name
        self.__start_date = start_date

    def get_module_name(self):
        return self.__module_name

    def get_start_date(self):
        return self.__start_date

    def create_module_name(self, new_module_name):
        self.__module_name = new_module_name
        return new_module_name

    def create_start_date(self, new_start_date, new_module_name):
        self.__start_date = new_start_date
        return new_start_date + new_module_name

    def get_list_of_students(self, student):
        return self.__list_of_students.append(student)

    def get_student(self):
        return ', '.join(self.__get_names())

    def __get_names(self):
        all_students = []
        for student in self.list_of_students:
            all_students.append(student.get_name())
        return all_students

