task=[]
while True:
     print("\n 1.Add task \n 2.Show task \n 3.Mark task as done \n 4.Status of Task \n 5.Exit\n")
     choice=int(input("Enter your choice:")) 
     if choice==1:
         my_list=input("Enter the task :")
         print(end="")
         print("Task added")
         task.append(my_list)
     elif choice==2:
         print()
         print("The Task is -")
         for a in task:
             print(a)
     elif choice==3:
         for b in task:
              c=str(input(f"{b} - Have you completed the Task (Yes/No) :"))
              if c.lower()=="Yes":
                 print(f"{b} : {c},Good!")
              elif c.lower()=="No":
                 print(f"{b} : {c},Please do the Task")     
     elif choice==4:
         print("Exit")
         break
            
             
    
         
