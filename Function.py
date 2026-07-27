def display():
    print("Welcome to Python")
display()

print("Temp Statement")

display()

def studentInfo(rollno, stname, rank):
    print("Roll No: ", rollno )
    print("Name: ", stname)
    print("Rank: ", rank)


studentInfo(stname = "abc", rank= 1, rollno = "st-1")


def employeeData(empid, empname, salary = 30000.0):
    print("Employee ID: ", empid)
    print("Employee Name: ", empname)
    print("Salary : ", salary)


def employeeData(empid, empname, salary):
    print("Employee ID: ", empid)
    print("Employee Name: ", empname)
    print("Salary : ", salary)
employeeData("emp-1", "abc", 40000)


def data(*lst):
    print(lst)
data(10,20)
data(30,40,50)

def College_Info(**info):
    print(info)
College_Info(clg_name = "NGP", Dept = "CSE")

def calc():
    return 10 +20
res = calc()
print(res)

def bookInfo():
    return "B -1", "Complete Reference of Python", 1500.0
bookid, bookname, price = bookInfo()
print(bookid)
print(bookname)
print(price)