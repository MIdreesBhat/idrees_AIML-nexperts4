print("----members SMS libarary ASSEMBLE----")


# welcome functionality
def welcome_message(): # method
    return "------- Welcome to the School Management System Portal -------"


# school member ---> head of deptt, instructor, office workers, non teaching 
class SchoolMember:

    # class variables
    school_name = "Nexperts School of Engineering"

    def __init__(self, name, role):
        self.name = name
        self.role = role
    
    def get_info(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"School: {self.school_name}")

# inheritance
class Instructor(SchoolMember): # child class of school member
    def __init__(self, name, role, subjects):
        super().__init__(name, role) # used to build relationship with parent class or template
        self.subjects = subjects



