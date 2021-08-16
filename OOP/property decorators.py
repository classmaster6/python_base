class Employee:
	raise_amt = 1.04

	def __init__(self, first, last):
		self.first = first
		self.last = last

	@property    #turns methods into attributes (properties)
	def email(self):
		return f"{self.first}.{self.last}@gmail.com"

	@property
	def fullname(self):
		return f"{self.first} {self.last}"

	@fullname.setter   			 # allows global changing of attributes (self.first)
	def fullname(self, name):	 # activated when "instance.property = value"
		first, last = name.split(' ')
		self.first = first
		self.last = last

	@fullname.deleter    #has to be activated with 'del' operator
	def fullname(self):	
		print("deleter activated")
		self.first = None
		self.last = None


emp_1 = Employee('John', 'Smith')

emp_1.fullname = 'Bo Lil'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname

#self.first and last are now None