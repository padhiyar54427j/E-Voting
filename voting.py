studentl=input("Enter 1st student name:")
student2=input("Enter 2nd student name:")
stud1_votes=0
stud2_votes=0
voters_id=[101,102,103,104,105,106]
no_of_voters=len(voters_id)
print("number of voters: ", no_of_voters)
voted=[]
while True:
    if voters_id==[]:
        print("voting is over")
        if stud1_votes>stud2_votes:
            print(f"{studentl} won the election with {stud1_votes}")
        elif stud2_votes>stud1_votes:
            print(f"{student2}won the election with {stud2_votes}")
        elif stud1_votes==stud2_votes:
            print("tied!!!")
        break

    else:
        voter=int(input("Enter Your ID: "))
        if voter in voted:
            print("Your already voted")
        else:
            if voter in voters_id:
                print(f"1.{studentl}\n2.{student2}")
                choice = int(input("Enter Your Choice: "))
                if choice==1:
                    stud1_votes+=1
                    print(f"you voted {studentl} ")
                elif choice==2:
                    stud2_votes+=1
                    print(f"you voted {student2} ")
                voters_id.remove(voter)
                voted.append(voter)
            else:
                print("You are not allowed to vote")
