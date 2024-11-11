#object oriented programe
# it includes classes
#classes have objects
#ojects have propertities
#all ojects were intanciated meaning they were enrolled 
#objects have methords and those are the things we want an
#  object to do such as attendance , regestering etc

#creating classes
#syntax:
#Cohort class #a class name starts with  a capital latter and always singular 


#ie;
#class Cohort_four:
    # name
    # discription
    # start_date
    # end_date

#with in a constractor;
#add constactor for the cohort class
#answers
class Cohort_four:
    def __init__(person,student_name,student_reg_no,student_marks):
        person.student_name = student_name
        person.student_reg_no = student_reg_no
        person.student_marks =student_marks
result = Cohort_four("latifah","2024/DSC/0070/SS","80")
print(f"The student name is {result.student_name}")
print(f"The student registration number is {result.student_reg_no}")
print(f"The student mark is {result.student_marks}")


#add the method to the class that prints the cohort name ,and the 
#total number of students 
#answers
class cohort:
    def __init__(self,cohort_name,total_no_of_students):
        self.cohort_name = cohort_name
        self.total_no_of_students = total_no_of_students
    def myfunc(self):
        print(f"The cohort name is {self.cohort_name}")
        print(f"The total number of students is {self.total_no_of_students}")
results = cohort("Cohort_iv","40")
results.myfunc()

#create a new instance of the cohort class 
#name
#description
#start_date
#end_date
#total_student
#answers
class COHORT:
    def __init__(self,name,description,start_date,end_date,total_students):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.total_students = total_students
cohort_v = COHORT("Cohort five"," Degree in ICT","20th/08/2026","31st/10/2029","130")
print(f"The cohort name is {cohort_v.name}")
print(f"The description is {cohort_v.description}")
print(f"The start date is {cohort_v.start_date}")
print(f"The end date is {cohort_v.end_date}")
print(f"The total students should be {cohort_v.total_students}")
    