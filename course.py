from monsters import *


class Course(Monster):

    def __init__(self, list_of_students=[], module_name='', start_date=''):
        super().__init__('', '', '')
        self.__list_of_students = list_of_students
        self.__module_name = module_name
        self.__start_date = start_date

    def get_module_name(self):
        return self.__module_name

    def get_start_date(self):
        return self.__start_date

    def create_module_name(self, new_module_name):
        self.__module_name = new_module_name
        new_module_name = input('enter a course: ')
        return new_module_name

    def create_start_date(self, new_start_date):
        self.__start_date = new_start_date
        new_start_date = input('enter a start date: ')
        return new_start_date

# <<<<<<< HEAD
#     # def append_list_of_students(self, new_student, new_module_name):
#     #     self.__list_of_students = new_student
#     #     new_student = Monster()
#     #     new_student.get_name()
#     #     new_list = []
#     #     for new_student in new_list:
#     #         new_list.append(new_student)
#     #         return new_list + new_module_name
# =======
#     def append_list_of_students(self, new_student, new_module_name):
#         self.__list_of_students = new_student
#         new_student = Monster()
#         new_student.get_name()
#         new_list = []
#         for new_student in new_list:
#             new_list.append(new_student)
#             return new_list + new_module_name
# >>>>>>> 575ef60966b248f2da61214e9c39703ac753ed39
