def add(a,b):
    print("a=",a)
    print("b=",b)
    return a+b
result=add(2,5)
print("sum=",result)

def student_info(name,roll,marks):
    print("Name :",name)
    print("Roll No :",roll)
    print("Marks :",marks)
student_info("Ravi",101,85)

def simple_interest(p,r,n):
    si=(p*r*n)/100
    print("simle interest :",si)
simple_interest(10000,2,2)
simple_interest(50000,1.2,3)

def ar_circle(r):
    a_circle=3.14*r*r
    print("area of circle=",a_circle)
ar_circle(1.5)
ar_circle(4)

def check_value(no):
    if(no>0):
        print("positive")
    elif(no<0):
        print("negative")
    else:
        print("zero")
check_value(0)
check_value(90)
check_value(-2)

def odd_even(no):
    if(no%2==0):
        print(f"value {no} is even")
    else:
        print(f"value {no} is odd")
odd_even(50)
odd_even(15)

def addition(a,b):
    add=a+b
    print("Addition of two values=",add)
addition(50,10.5)
addition(100,200)

def student_info(name,age,city):
    print("Name :",name)
    print("Age :",age)
    print("City :",city)
student_info(age=18,city="rajkot",name="ravi")

def display(a,b,c):
    print("a=",a)
    print("b=",b)
    print("c=",c)
display(a=1,c=8,b=6)

def simple_interest(p:float,r:int,t:float):
    si=(p,r,t)/100
    print("simple interest=",si)
simple_interest(p=10000,t=2,r=1.5)
simple_interest(t=1.5,p=15000,r=2)
