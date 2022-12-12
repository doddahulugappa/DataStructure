# A Python program to demonstrate
# inheritance


# Base class or Parent class
class Child:

	# Constructor
	def __init__(self, name):
		self.name = name

	# To get name
	def getName(self):
		return self.name

	# To check if this person is student
	def isStudent(self):
		return False

# Derived class or Child class
class Student(Child):

	# True is returned
	def isStudent(self):
		return True


# Driver code
# An Object of Child
std = Child("Ram")
print(std.getName(), std.isStudent())

# An Object of Student
std = Student("Shivam")
print(std.getName(), std.isStudent())


# Python program to demonstrate
# single inheritance


# Base class
class Parent:
	def func1(self):
		print("This function is in parent class.")

# Derived class
class Child(Parent):
	def func2(self):
		print("This function is in child class.")

# Driver's code
object = Child()
object.func1()
object.func2()

# Python program to demonstrate
# multiple inheritance


# Base class1
class Mother:
	mothername = ""
	def mother(self):
		print(self.mothername)

# Base class2
class Father:
	fathername = ""
	def father(self):
		print(self.fathername)

# Derived class
class Son(Mother, Father):
	def parents(self):
		print("Father :", self.fathername)
		print("Mother :", self.mothername)

# Driver's code
m1 = Mother()
m1.mothername = "Pakkeramma"
m1.mother()
f1 = Father()
f1.fathername = "Eranna"
f1.father()

s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()

