#함수 이름은 변경 가능합니다.
student_data = {}
##############  menu 1
# def Menu1(#매개변수가 필요한지 판단 후 코딩할 것) :
    #사전에 학생 정보 저장하는 코딩 
def Menu1():
    while True:
        try:
            name, mid_score, final_score = input("Enter (name, mid-score, final-score) :").split()

            if name in student_data:
                print("Student information already exists!")
            elif not mid_score.isdigit() or not final_score.isdigit():
                print("Score is not a positive integer!")
            else:
                student_data[name] = {"mid_score": int(mid_score), "final_score": int(final_score)}
                print(f"{name} student information successfully saved!")
                break

        except ValueError:
            print("Please enter all three data: name, mid-score, final-score")

##############  menu 2
# def Menu2(#매개변수가 필요한지 판단 후 코딩할 것) :
    #학점 부여 하는 코딩
def Menu2():
    if not student_data:
        print("No student data!")
        return
    
    for name in student_data:
        if "grade" not in student_data[name]:
            mid_score = student_data[name]["mid_score"]
            final_score = student_data[name]["final_score"]
            average = (mid_score + final_score)/2
            if average >= 90:
                grade = "A"
            elif average >= 80:
                grade = "B"
            elif average >= 70:
                grade = "C"
            else:
                grade = "D"
            student_data[name]["grade"] = grade
    print(student_data)
        

##############  menu 3
# def Menu3(#매개변수가 필요한지 판단 후 코딩할 것) :
    #출력 코딩
def Menu3():
    if not student_data:
        print("No student data!")
    else:
        all_grades_assigned = True
        for name in student_data:
            if "grade" not in student_data[name]:
                all_grades_assigned = False
                break
        
        if not all_grades_assigned:
            print("There is a student who didn't get grade")
        else:
            print("----------------------------")
            print("name     mid   final   grade")
            print("----------------------------")
            for name in student_data:
                mid_score = student_data[name]["mid_score"]
                final_score = student_data[name]["final_score"]
                grade = student_data[name]["grade"]
                print(f"{name}    {mid_score}     {final_score}     {grade}")

##############  menu 4
# def Menu4(#매개변수가 필요한지 판단 후 코딩할 것):
    #학생 정보 삭제하는 코딩

#학생 정보를 저장할 변수 초기화
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
      choice = input("Choose menu 1, 2, 3, 4, 5 : ")
      if choice == "1":
          Menu1()
      
        #학생 정보 입력받기
        #예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
        #예외사항이 아닌 입력인 경우 1번 함수 호출 

      elif choice == "2" :
        Menu2()
      elif choice == "3" :
        Menu3()
    #     #예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
    #     #예외사항이 아닌 경우 3번 함수 호출

    # elif choice == "4" :
    #     #예외사항 처리(저장된 학생 정보의 유무)
    #     #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
    #     #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
    #     #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력

      elif choice == "5" :
        print("Exit Program!")
        break

      else:
          print("Wrong number. Choose again.")
