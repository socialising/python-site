##bonus
salary=int(input("enter salary:"))
time_of_service=int(input("enter time_of_service:"))
if time_of_service>10:  
  bonus=0.1*salary   
  print("net_bonus",bonus+salary) 
elif time_of_service>=6 and time_of_service<=10:
   bonus=0.08*salary
   print("net_bonus",bonus+salary) 
else:
   print("net_bonus",bonus+salary)
    