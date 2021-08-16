class Employee:
	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = "{}.{}@gmail.com".format(first, last)

#-------------------------------------------------------------

class Developer(Employee):
	raise_amt = 1.10

	def __init__(self, first, last, pay, language):
		super().__init__(first, last, pay)
# or... Employee.__init__(self, first, last, pay)
		self.language = language

#-------------------------------------------------------------

class Manager(Employee):
	def __init__(self, first, last, pay, employees = None):	# don't pass muteable obj as default arguments (list or dict)
		super().__init__(first, last, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_employee(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_employee(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print('-->', emp.first)

emp_1 = Employee("John", "Doe", 70000)

mg = Manager("Jon", "Jonson", 90000, [emp_1])

print(mg.email)
#isinstance, issubclass