# Author: Yanling Wang yuw17@psu.edu
def getGradePoint(letter):
  """
  Given a letter grade, translate it into a gradepoint value between 0.0 and 4.0
  YOU MUST USE if/elif/../else structure to implement this function.
  YOU CAN NOT use any features/data structure we haven't learned in the class,
  including but not limited to list, dictionary and tuples.
  """
"""  
gl = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'D', 'F']
gl2 = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'D', 'F']
gl3 = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'D', 'F']
"""
  if letter == "A":
    gp = 4.0
  elif letter == "A-":
    gp = 3.67
  elif letter == "B+":
    gp = 3.33
  elif letter == "B":
    gp = 3.0
  elif letter == "B-":
    gp = 2.67
  elif letter == "C+":
    gp = 2.33
  elif letter == "C":
    gp = 2.0
  elif letter == "D":
    gp = 1.0
  else:
   gp = 0.0
  float gp  
  return gp  

def run():
  """
  Use either a while-loop or a for-loop to make your code for getting three separate
  courses' letter grade and credit info. And calculate the final GPA.
  YOU CAN NOT use any features/data structures we haven't learned in the class,
  including but not limited to list, dictionary, and tuples.
  """
ask = input("Enter your course 1 letter grade: ")
cred = input("Enter your course 1 credit: ")
for x in gl:
	if ask == "A":
		gp = 4.0
	elif ask == "A-":
		gp = 3.67
	elif ask == "B+":
		gp = 3.33
	elif ask == "B":
		gp = 3.0
	elif ask == "B-":
		gp = 2.67
	elif ask == "C+":
		gp = 2.33
	elif ask == "C":
		gp = 2.0
	elif ask == "D":
		gp = 1.0
	else:
		gp = 0.0
print(f"Grade point for course 1 is: {gp}")

ask2 = input("Enter your course 2 letter grade: ")
cred2 = input("Enter your course 2 credit: ")

for x in gl2:
	if ask2 == "A":
		gp2 = 4.0
	elif ask2 == "A-":
		gp2 = 3.67
	elif ask2 == "B+":
		gp2 = 3.33
	elif ask2 == "B":
		gp2 = 3.0
	elif ask2 == "B-":
		gp2 = 2.67
	elif ask2 == "C+":
		gp2 = 2.33
	elif ask2 == "C":
		gp2 = 2.0
	elif ask2 == "D":
		gp2 = 1.0
	else:
		gp2 = 0.0
print(f"Grade point for course 2 is: {gp2}")

ask3 = input("Enter your course 3 letter grade: ")
cred3 = input("Enter your course 3 credit: ")

for x in gl3:
	if ask3 == "A":
		gp3 = 4.0
	elif ask3 == "A-":
		gp3 = 3.67
	elif ask3 == "B+":
		gp3 = 3.33
	elif ask3 == "B":
		gp3 = 3.0
	elif ask3 == "B-":
		gp3 = 2.67
	elif ask3 == "C+":
		gp3 = 2.33
	elif ask3 == "C":
		gp3 = 2.0
	elif ask3 == "D":
		gp3 = 1.0
	else:
		gp3 = 0.0
print(f"Grade point for course 3 is: {gp3}")

gpa = (float(gp)*float(cred) + (float(gp2))*(float(cred2)) + (float(gp3))*(float(cred3)))/ (float(cred))+(float(cred2))+(float(cred3))
print(f"Your GPA is: {gpa}")


if __name__ == "__main__":
  run()
