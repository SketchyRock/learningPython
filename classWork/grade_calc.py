"""Program calculates weighted grade average.

Author: Enzo Hins
Version: 9/3/2025
"""

name = input("Name: ")
homework_avg = float(input("Homework Avg: " ))
test_avg = float(input("Test Avg: "))
lab_avg = float(input("Lab Avg: "))
course = input("Course: ")
weighted_total = 0

if course not in ("CT201", "CT222", "CT301"):
	print("COURSE - no such course")
else:
	if course == "CT201":
		weighted_total = (homework_avg*0.3) + (test_avg * 0.5) + (lab_avg * 0.2)
		print(f"Final grade for {name} in {course} is {weighted_total:.2f}")
	elif course == "CT222":
		weighted_total = (homework_avg*0.45) + (test_avg * 0.4) + (lab_avg * 0.15)
		print(f"Final grade for {name} in {course} is {weighted_total:.2f}")
	else:
		weighted_total = (homework_avg*0.2) + (test_avg * 0.25) + (lab_avg * 0.55)
		print(f"Final grade for {name} in {course} is {weighted_total:.2f}")
