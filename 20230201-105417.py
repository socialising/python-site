#vote
nationality=input("Enter nationality:").lower()
age=int(input("Enter age:"))
if age>=18 and nationality=="Kenyan":
  print("eligible to vote")
else:
  print("not eligible to vote")
