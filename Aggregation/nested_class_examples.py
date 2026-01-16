class Company :
    class Employee: 
        def __init__(self,name,position):
            self.name = name 
            self.position = position
        def get_details(self):
            return [f" {self.name}{self.position}"] 
    def __init__(self, company_name):
        self.company_name = company_name 
        self.employees = []
    def add_employees(self, name, position):
        new_employee = self.Employee(name,position )
    def list_employees (self):
        return [f"{self.name }{}"] 

company= Company ("SharkNinja")
company.add_employees("Ria Mendes", "Control Systems Engineer")
company.list_employees()
print(company.company_name)