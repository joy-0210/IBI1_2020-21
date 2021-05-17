#create class
class Student:
    
    #instialize
    def __inti__(self):
        self.first_name = None
        self.last_name = None
        self.progamme = None
        
    #input the imformation
    def set_first_name(self,first_name):
        self.first_name=first_name
    def set_last_name(self,last_name):
        self.last_name=last_name
    def set_programme(self,programme):
        self.programme=programme

    #output the data
    def print_information(self):
        print("The student's name is "+self.first_name+" "+self.last_name+". His/Her undergraduate programme is "+self.programme)

#give an example
    
test = Student()
test.set_first_name("Yue")
test.set_last_name("Jin")
test.set_programme("BMS")
test.print_information()
    
        
        
