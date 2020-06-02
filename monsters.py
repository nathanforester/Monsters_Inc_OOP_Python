
class Monster:

    def __init__(self, name, tax_number, fur):
        self.__name = str(name)
        self.__tax_number = tax_number
        self.fur = fur

    def get_name(self):
        return self.__name

    def create_name(self, new_name):
        self.__name = new_name
        return new_name

    def get_tax_number(self):
        return self.__tax_number

    def tax_number(self, new_tax_number, new_name):
        self.__tax_number = new_tax_number
        return new_tax_number + new_name




