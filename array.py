#1.int array
from array import array
arr=array('i',[10,20,30,40])
print(arr)


#len()-number of elements
from array import array
arr=array('i',[10,20,30,40])
print(len(arr))

#append()
arr=array('i',[10,20,30])
arr.append(40)
print(arr)

#insert(pos,x)
arr=array('i',[10,20,40])
arr.insert(2,30)
print(arr)

#remove(x)
arr=array('i',[10,20,30,20,40])
arr.remove(20)
print(arr)

#pop()
arr=array('i'[10,20,30,40])
x = arr.pop()
print("removed: ",x)
print(arr)

#index(x)
from array import array
arr=array('i',[10,20,30,40])
print(arr.index(30))

#count(x)
from array import array
arr=array('i',[10,20,30,20,40])
print(arr.count(20))

#reverse()
from array import array
arr=array('i',[10,20,30,40])
arr.reverse()
print(arr)

#positive index
from array import array 
arr=array('i',[10,20,30,40,50])
print(arr[0])
print(arr[2])
print(arr[4])

#negative index
from array import array
arr=array('i',[10,20,30,40,50])
print(arr[-1])
print(arr[-2])
print(arr[-5])

#modifying elements
from array import array
arr=array('i',[10,20,30,40,50])
arr[2]=35
print(arr)

#indexx error
from array import array
arr=array('i',[10,20,30])
print(arr[5])

#basic slice
from array import array
arr=array('i',[10,20,30,40,50])
print(arr[1:4])
print(arr[:3])
print(arr[2:])
print(arr[:])

#slicing with step
from array import array 
arr=array('i',[10,20,30,40,50,60,70,80])
print(arr[::2])
print(arr[1::2])
print(arr[::3])

#negative slicing
from array import array 
arr=array('i',[10,20,30,40,50])
print(arr[-4:-1])
print(arr[-3:])
print(arr[:-2])

#reverse array
from array import array
arr=array('i',[10,20,30,40,50])
print(arr[::-1])

#modifyiyng slices
from array import array
arr=array('i',[10,20,30,40,50])
arr[1:4]=array('i',[25,35,45])
print(arr)