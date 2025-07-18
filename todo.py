my_list = []

def menu():
    while(True):
        print("Choose any of the Choices given below for your respective Job\n")
        print("1. Add your Task")
        print("2. Remove your Task")
        print("3. View your Task")
        print("4. Exit")

        option = input("Enter your option choosen from above options\n")
        
        match option :
            case "1":
                Add_Job()
            case "2":
                Remove_Job()
            case "3":
                View_Job()
            case "4":
                print("Exiting the Application")
                exit()
            case _:
                print("Invalid Option Choosen.Choose again\n")
            
def Add_Job():
    Job = input("Enter your Task")
    my_list.append({"Job": Job})
    print("Your Task is added to the List")

def Remove_Job():
    if len(my_list) == 0:
        print("You don't have any lists saved. Your List is Empty\n")
    else:
        search_index = int(input("Enter the Number of Tasks you want to remove: ")) - 1
        if 0 <= search_index < len(my_list):
            remove_task = my_list.pop(search_index)
            print(f"Task Removed: {remove_task}")
        else:
            print("Invalid Task Number\n")
        
def View_Job():
    print("Your Saved Lists\n")  
    if len(my_list) == 0:
        print("You don't have any lists saved\n")
    else:
        for index, Job in enumerate(my_list, 1): 
            print(f"{index}:{Job ['Job']}") 

if __name__ == "__main__":
    menu()