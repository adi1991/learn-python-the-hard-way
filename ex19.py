def new_students(name, studentId):
	
	print "Whats id your name?", name
	print "What is your student number\n", studentId

	
new_students('aditya', 100815505)
	   
def new_student_record(Test1, Test2, Test3, Test4, Test5):

	print "Test1 marks", Test1
	print "Test2 marks", Test2
	print "Test3 marks", Test3
	print "Test4 marks", Test4
	print "Test5 marks", Test5

	Tot = Test1 + Test2 + Test3 + Test4 + Test5
	avg = Tot/5
	
	print "total", Tot
	print "average", avg
 
new_student_record(70, 80, 90, 67, 89)

