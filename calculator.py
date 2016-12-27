letters = ['A', 'B','C', 'D', 'F']

def createGradeScale():
	grades = {}
	gpa = 4.00

	#Create Grade Point Scale
	for i in range(len(letters)):
		if letters[i] != 'F':
			grades[letters[i] + '+'] = round(gpa, 2)
			if letters[i] == 'A':
				grades[letters[i]] = round(gpa, 2)
			else:
				gpa -= .33
				grades[letters[i]] = round(gpa, 2)
			gpa -= .33
			grades[letters[i] + '-'] = round(gpa, 2)
		else:
			grades[letters[i]] = 0.00
		gpa -= .34
	return grades

#Get letter grade and hour of a class
def getGrade(grades):
	grade = raw_input('What is the grade you got: ').upper()
	hours = input('What is the credit hour for this class: ')
	grades.append([grade, hours])

#Calculate semester GPA
def calcGPA(grades, scale):
	totalHrs = 0
	totalQP = 0
	for i in range(len(grades)):
		#Letter, Hour
		letter = grades[i][0]
		hrs = grades[i][1]

		#Add to total 
		totalHrs += hrs
		totalQP += scale[letter] * hrs
	return round(totalQP/totalHrs, 2), totalHrs

def calcTotalGPA(currGPA, currHrs, semGPA, semHrs):
	currQP = currGPA * currHrs
	semQP = semGPA * semHrs
	return round((currQP + semQP)/(currHrs + semHrs), 2)
		
def main():
	scale = createGradeScale()
	grades = []
	classes = input('Number of classes: ')
	for i in range(classes):
		getGrade(grades)
	print ''
	gpa, hours = calcGPA(grades, scale)
	print 'Semester GPA: ' + str(gpa)
	total = raw_input('Do you want cumulative GPA (y/n): ')
	if total == 'y':
		print 'Cumulative GPA ' + str(calcTotalGPA(input('Current GPA: '), input('Total Hours: '), gpa, hours))

if __name__ == "__main__":main()