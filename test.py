from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
class Name(Field):
    def __init__(self, value):
        super().__init__(value)
        self.name_value = self.value

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.phone_number = self.validate_phone()

    def validate_phone(self):
        if self.value.isdigit() and len(self.value) == 10:  
            return self.value
        else:
            raise Exception("The phone format is not correct.")  
        

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        
    def add_phone(self, phone):
        number = Phone(phone)
        self.phones.append(number)

    def remove_phone(self, phone):
        for idx, phone_num in enumerate(self.phones):
            if phone_num.value == phone:
                del self.phones[idx]
                return f"The phone {phone} has been removed."
        return f"The phone has not been found."
        

    def edit_phone(self, old_phone, new_phone):
        for phone_num in self.phones:
            if phone_num.value == old_phone:
                phone_num.value == new_phone
                return f"Phone number {old_phone} updated to {new_phone} for contact {self.name.value}"
        return f"Phone number {old_phone} has not been found."

    def find_phone(self, phone):
        for phone_num in self.phones:
            if phone_num.value == phone:
                return f"Phone number {phone} found for the contact {self.name.value}"
        return f"Phone number {phone} hasn't been found for the contact {self.name.value}"

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"




class AddressBook(UserDict):
    def __init__(self):
        self.data = UserDict()
        self.name = None
    

"""
functions to add

    def birthdays(self, birthday):
        return #list of birthdays

    def show_birthday(self, contact):
        if in book:
            return # birthday contact 
        
        """
        


 
    
    


fedir = Record("Fedir")
fedir.add_phone("0987654321")
print(fedir)
fedir.remove_phone("0987654321")
print(fedir)
 
