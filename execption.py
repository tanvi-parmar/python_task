try:
    number1=int(input("enter a number: "))
    number2=int(input("enter another number: "))
    result=number1/number2

except ZeroDivisionError:
    print("you cannot devide by zero!")

except ValueError:
    print("please enter a valid number!")  

else:
    print("division successfull result is:",result) 

finally:
    print("this block always runs.")


try:
    my_list=[1,2,3]
    print(my_list[5])  

except IndexError:
    print("index is out of range!")

else:
    print("element found successfully!")

finally:
    print("program finished.")            
