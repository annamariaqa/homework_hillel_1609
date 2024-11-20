class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary):
        Employee.__init__(self, name, salary)
        self.department = 'IT'

class Developer(Employee):
    def __init__(self, name, salary):
        Employee.__init__(self, name, salary)
        self.programming_language = 'Python'

class TeamLead(Manager, Developer):
    def __init__(self, name, salary):
        Manager.__init__(self, name, salary)
        Developer.__init__(self, name, salary)
        self.team_size = 8

team_lead_john = TeamLead('John','7k')
print(team_lead_john.name)
print(team_lead_john.salary)
print(team_lead_john.department)   
print(team_lead_john.team_size)
print(team_lead_john.programming_language)