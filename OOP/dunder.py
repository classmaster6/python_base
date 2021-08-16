class Employee:
	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = "{}.{}@gmail.com".format(first, last)

#__repr__ (other devs, debugging/logging), __str__(readable)
	
	def __repr__(self):
		return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

	def __str__(self):
		return "{} {} - {}".format(self.first, self.last, self.email)

# print(emp_1) --> defaults to str and then repr
# print(repr(emp_1))
# print(str(emp_1))

	def __add__(self, other):
		return self.pay + other.pay

	def __len__(self):
		return len(self.first)

emp_1 = Employee("John", "Doe", 50000)
emp_2 = Employee("Jam", "Soe", 60000)


print(emp_1 + emp_2)

print(int.__add__(1, 2))

print(str.__add__('a', 'b'))

print(len(emp_1))