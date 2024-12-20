#Global Variables
sem_gpas=[]
total_cred=[]
#Calculate SGPA
def cal_sgpa():
    print("***SGPA Calculation***")
    num = int(input("Enter number of subjects: "))
    names=[]
    for i in range(0,num):
        n=input(f"Enter the name of subject{i+1}: ")
        names.append(n)
    gsum = 0
    total = 0
    a = []
    b = []
    for i in range(0, num):
        grade = int(input(f"Enter points in {names[i]}: "))
        credit = float(input(f"Enter credits in {names[i]}: "))
        a.append(grade)
        b.append(credit)
        total = total + b[i]
    total_cred.append(total)
    for i in range(num):
        gsum = gsum + (a[i] * b[i])
        sgpa = gsum / total
    sem_gpas.append(sgpa)
    tsum=sum(total_cred)
    print(f"Your GPA in this semester is {sgpa:.2f}:")
    return sem_gpas,total_cred,tsum

#Calculate CGPA
def cal_cgpa():
    if len(sem_gpas)==0:
        print("***CGPA Calculation***")
        num = int(input("Enter number of semesters:"))
        a = []
        b = []
        gsum = 0
        total = 0
        for i in range(0, num):
            grade = float(input(f"Enter your GPA in semester {i + 1}:"))
            credit = float(input(f"Enter total number of credits in semester {i + 1}:"))
            a.append(grade)
            b.append(credit)
            total = total + b[i]
        for i in range(num):
            gsum = gsum + (a[i] * b[i])
            cgpa = gsum / total
        print(f"Your CGPA is {cgpa:.2f}:")
    else:
        gsum=0
        for i in range(0,len(sem_gpas)):
            gsum=gsum+(sem_gpas[i]*total_cred[i])
            cgpa=gsum/sum(total_cred)
        print(f"Your CGPA is {cgpa:.2f}:")
    return cgpa
def cal_sgpa_cgpa():
    print("***SGPA and CGPA calculation***")
    num=int(input("Enter number of semesters:"))
    for i in range(0,num):
        print(f"{i+1} Semester")
        cal_sgpa()
    cal_cgpa()
    return
#User Interface
print("Hi!What you neeed?")
print("Select:\n 1-CGPA Calculation\n 2-SGPA Calculation\n 3-Both CGPA and SGPA")
n = int(input("Enter your selection:"))
if n == 1:
    cal_cgpa()
elif n == 2:
    cal_sgpa()
elif n == 3:
    cal_sgpa_cgpa()
else:
    print("Invalid selection")