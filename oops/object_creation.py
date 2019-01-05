class Calc:
	Counter = 0;
	def __init__(self, x, y):
		self.num1 = x
		self.num2 = y
		Calc.Counter += 1

	def sum(self):
		print("Sum of", self.num1, "and", self.num2, "is", self.num1 + self.num2)

	def diff(self):
		print("Diff of", self.num1, "and", self.num2, "is", self.num1 - self.num2)

	def __del__(self):
		Calc.Counter -= 1;

num1 = int(input("Enter first number "))
num2 = int(input("Enter second number "))
num3 = int(input("Enter first number "))
num4 = int(input("Enter second number "))

c1 = Calc(num1, num2)
c2 = Calc(num3, num4)

c1.sum()
c2.sum()

c1.diff()
c2.diff()

print("Total Clacs", Calc.Counter)

del c1

print("Total Clacs", Calc.Counter)