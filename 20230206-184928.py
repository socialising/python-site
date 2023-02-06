#average
subject1=int(input("enter subject1:"))
subject2=int(input("enter subject2:"))
subject3=int(input("enter subject3:"))
average=(subject1+subject2+subject3)/3
print("average", average)
if average>=70 and average<100:
   print("Grade A")
elif average>=60 and average<69:
   print("Grade B")
elif average>=50 and average<59:
   print("Grade C")
elif average>=40and average<49:
   print("Grade D")
else:
   print("fail")
    