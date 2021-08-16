class Employee:
	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = "{}.{}@gmail.com".format(first, last)

	@classmethod	# alternate constructor
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)

#		contructs object of class Employee
employee_str = 'John-Doe-70000'
emp_1 = Employee.from_string(employee_str)

