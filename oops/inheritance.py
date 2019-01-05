class Student:
	Marks = 80;
	def print_marks(self):
		print("Marks: ", Student.Marks);

class SportsStudent (Student):
	Marks = 5;
	def print_total_marks(self):
		print("Total Marks", SportsStudent.Marks + Student.Marks);



s = SportsStudent();
s.print_marks();
s.print_total_marks();

s2 = Student();
s2.print_marks();