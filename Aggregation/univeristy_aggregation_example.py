class University:
    def __init__(self,name):
        self.name = name 
        self.student= []
    def add_students(self, student):
        self.student.append(student)
    def remove_students(self,student):
        self.student.remove(student)
    def list_students(self):
        return [f"{student.name} with id {student.id}" for student in self.student]

         
class Student:
     def __init__(self,name,id):
          self.name = name 
          self.id= id 
university = University ("Northeastern Univ")
student1= Student("Kavya" , 231)
student2 = Student("Ria", 455)
student3= Student ("Sai", 544)

university.add_students(student1)
university.add_students(student2)
university.add_students(student3)
university.remove_students(student1)
print(university.list_students())