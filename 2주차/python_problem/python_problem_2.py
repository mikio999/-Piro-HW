#student DB
student_data = {}

##############  menu 1
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
def Menu4():
  if not student_data:
      print("No student data!")
      return

  delete_name = input("Enter the name to delete:")
  if delete_name not in student_data:
      print("No Exist Name!")
  else:
      del student_data[delete_name]
      print(f"{delete_name} student information is deleted.")

#실행
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
      elif choice == "2" :
        Menu2()
      elif choice == "3" :
        Menu3()
      elif choice == "4" :
          Menu4()
      elif choice == "5" :
        print("Exit Program!")
        break
      else:
          print("Wrong number. Choose again.")
