f1=open("one.txt","r")
data1=f1.read()
f1.close()
f2=open("two.txt","r")
data2=f2.read()
f2.close()

merged=open("merged.txt","w")
merged.write(data1)
merged.write("\n")
merged.write(data2)
merged.close()

print("Files merged into merged.txt")