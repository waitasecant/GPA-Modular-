gradelist = ["O", "A", "B", "C", "D", "F"]

def read_marks(quiz, exam, assignment, project):
    if quiz > 20:
        global list
        list = []
        print("ERROR: Invalid Marks", int(quiz), "> 20")
    elif quiz < 0:
        list = []
        print("ERROR: Invalid Marks", int(quiz), "< 0")
    elif exam > 100:
        list = []
        print("ERROR: Invalid Marks", int(exam), "> 100")
    elif exam < 0:
        list = []
        print("ERROR: Invalid Marks", int(exam), "< 0")
    elif assignment > 100:
        list = []
        print("ERROR: Invalid Marks", int(assignment), "> 100")
    elif assignment < 0:
        list = []
        print("ERROR: Invalid Marks", int(assignment), "< 0")
    elif project >50:
        list = []
        print("ERROR: Invalid Marks", int(project), "> 50")
    elif project < 0:
        list = []
        print("ERROR: Invalid Marks", int(project), "< 0")
    else:
        list
        list = [quiz, exam, assignment, project]

def compute_gpa(quiz,exam,assignment,project):
    if list == [quiz,exam,assignment,project]:
        quiz = float(list[0])
        exam = float(list[1])
        assignment = float(list[2])
        project = float(list[3])
        global gpa
        gpa = ((float(quiz)/20)*0.15 + (float(exam)/100)*0.40 + (float(assignment)/100)*0.20 + (float(project)/50)*0.25)*10
        global gpa1
        gpa1 = round(gpa,2)
    else:
        pass

def assign_grade(gpa):
    global grade
    if int(gpa) == 10:
        grade = gradelist[0]
    elif 9 <= gpa < 10:
        grade = gradelist[1]
    elif 8 <= gpa < 9:
        grade = gradelist[2]
    elif 6.5 <= gpa < 8:
        grade = gradelist[3]
    elif 5 <= gpa < 6.5:
        grade = gradelist[4]
    else:
        grade = gradelist[5]        

def main():
    quiz = float(input())
    exam = float(input())
    assignment = float(input())
    project = float(input())
    gpa = ((float(quiz)/20)*0.15 + (float(exam)/100)*0.40 + (float(assignment)/100)*0.20 + (float(project)/50)*0.25)*10
    gradelist = ["O", "A", "B", "C", "D", "F"]
    read_marks(quiz, exam, assignment, project)
    compute_gpa(quiz, exam, assignment, project)
    assign_grade(gpa)

    if list == []:
        pass
    else:
        print("The GPA is", gpa1, end=",")
        print(" and the Grade is", grade)
    pass

if __name__ == "__main__":
    main()
