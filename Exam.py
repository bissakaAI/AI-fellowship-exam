#QUESTION 1
#adding 
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
    
print(("==" * 20).center(100) )
print("WELCOME TO THE CALCULATOR PROGRAM".center(100))
print(("==" * 20).center(100) )
while True:
    try:
        first_no = float(input("please input frist number: "))
        second_no = float(input("please input second number: "))
        choice= input("Choose from the option below \n1. to add (+)\n2. to subtract (-)\n3. to multiply (*)\n4. to divide (/)\n'exit' to quit:")
        if choice=="1":
            x=add(first_no,second_no)
            print(f"Result: {x}")

        elif choice=="2":
            x=subtract(first_no,second_no)
            print(f"Result: {x}")

        elif choice=="3":
            x=multiply(first_no,second_no)
            print(f"Result: {x}")

        elif choice=="4":
            x=divide(first_no,second_no)
            print(f"Result: {x}")

        elif choice =="exit":
            print("Exiting calculator... Goodbye!")
            break
    except ZeroDivisionError:
        print("you cant devide by zero (0)")
    except ValueError:
        print("Invalid Input")

    except Exception as e:
        print("Error: ",e)






#QUESTION 2

while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    if user_input == "exit":
        print("Goodbye!")
        break        # break out of loop
    
    num = int(user_input)   # convert to integer
    
    if num % 2 == 0:
        print("The number is Even")
    else:
        print("The number is odd")







#QUESTION 3

while True:
    age = input("Enter your age (or type exit to quit): ")
    if age == "exit":
        print("Goodbye!")
        break

    try:
        if int(age) >= 18:
            print("You can vote")
        else:
            print("You cannot vote")
    except:
        print("Invalid input")