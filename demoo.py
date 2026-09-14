
#a = int(input("Enter a number:"))
#print('The number is odd:',a%2!=0)

#Write a program to print age in days
#a  =  int(input("Enter your age:"))
#print(f" {a} years = {a*365} days ")

#Write a Program to convert minutes into hours and 
#minutes = int(input("Enter minutes:"))
#print(f" {minutes} is {minutes//60} hours {minutes%60} minutes")

#write a program to extract last digit of an number
#no = int(input("Enter a number:"))
#print(f" {no} : last digit is {no%10} ")
#or
#no = input("Enter a number:")
#print(f" {no} : last digit is {no[-1]} ")

#write a program to check if a person is eligible for discount the criteria is he must be a student and age mst be below 21
#role = input("Enter your role(student/teacher):")
#age = int(input("Enter your age:"))
#print(f" Eligible: {age<21 and role == 'student'}")

#write a program to swap two numbers without 3rd variable and using arithmatic operations
#a = 23
#b = 45
#print(f"before swap: {a}= 10 ")
#Yashashreeparab 
#xyz
#okp

#11/9
#Conditional statements
#is_raining = False
#if is_raining:
#    print("raining outside")
#else :
#    print("not raining")

#age = int(input("Enter your age:"))
#if age<=18 :
#    print("Not Eligible for voting")
#else :
#    print("Eligible for voting")


#n=int(input("Enter a number:"))
#if n==1:
#     print("Sunday")
#elif n==2:
#   print("Monday")
#elif n==3:
#    print("Tuesday")
#elif n==4:
#    print("Wednesday")
##elif n==5:
#    print("Thursday")
#elif n==6:
 #   print("Friday")
#elif n==7:
 #   print("Saturday")
#else:
 #   print("Invalid number")


#age = 20
#has_id = True
#if age >= 18:
#    if has_id:
#        print("Entry allowed")
#    else:
#        print("Id required")
#else:
#    print("Underage")

#MATCH CASE
#day = int(input("Enter the day number:"))

#match day:
#    case 1:
#        print("Monday")
#    case 2:
#        print("Tuesday")
#    case 3:
#        print("Wednesday")
#    case 4:
 #       print("Thursday")
  #  case 5:
   #     print("friday")
   # case 6:
   #     print("saturday")
   # case 7:
   #     print("sunday")
   # case _:
   #     print("invalid number")

#odd even
#n = int(input("Enter a number:"))
#if n%2==0 :
#    print("The number is even")
#else:
#    print("Number is odd")


#age = int(input("Enter age:"))
#price = 500
#if age<12 :
#    print("10% Discount Applies | Ticket price =", (price)-(price*10/100))
#else :
#   print("Discount does not apply | Ticket price=",age)


#marks above 90 o grade 80 pl a+ till f
#marks = int(input("Enter marks:"))
#if marks>=90 and marks<100 :
#    print("Grade:O")
#elif marks>=80 and marks<=90 :
#    print("Grade:A")
#elif marks>65 and marks<=80 :
#    print("Grade:B")
#elif marks<=35 and marks>=0:
#    print("Grade:C|failed")
#else :
#    print("Invalid marks")

#check positiove negative
#no= int(input("Enter a number:"))
#if no<0 :
#    print("Number is negative")
#elif no>0:
#    print("Number is positive")
#else:
#    print("Number is 0")


#a= int(input("Enter first number:"))
#b = int(input("Enter second number:"))
#c = int(input("ENter third number:"))

#if a>=b and a>=c:
 #   print(a)

#elif b>=a and b>=c:
#    print(b)

#elif a==b==c:
#    print(a)

#else:
#    print(c)

#year = int(input("Enter year:"))
#if year%4==0:
#    print("Leap year")
#else:
#    print("Not leap year")

#calculator
#a=int(input("Enter first no-"))
#b=int(input("Enter second no-"))
#choice=int(input(("1-addition\n2-subtraction\n3-multiplication\n4-division\nEnter your choice:")))

#match choice:
#    case 1: 
#            print("addition=",a+b)

#    case 2: 
#            print("Subtraction=",a-b)

#    case 3: 
#            print("Multiplication=",a*b)

#    case 4: 
#              if b==0:
#                print("Division by 0 not possible")
#              else:
#                print("Division=",a/b)

#   case _: print("invalid choice")

#HOMEWORK 11/9/26

#Q1 Traffic Signal: Red -> "Stop"
#   Yellow -> "Get Ready"
#   Green -> "Go"  Handle invalid colors

#color = input("Enter a color:").lower()
#if color == 'red':
#    print("Stop")

#elif color == 'yellow':
#    print("Get ready")

#elif color == 'green':
#    print("Go")

#else:
#    print("Invalid color")

#Q2 ATM Menus
#balance = 10000
#print("1 - Check balance\n2 - Deposit\n3 - Withdraw\n4 - Exit\n")
#n = int(input("Enter your choice:"))
#match n:
#    case 1:
#        print("Your account balance is:",balance)

#    case 2:
#        deposit = int(input(print("Enter the amount you want to deposit:")))
#        balance = balance + deposit
#        print("Deposit done, your balance is:",balance)
#
#    case 3: 
#        withdraw = int(input("Enter the amount you want to withdraw:"))
#        if withdraw > balance :
#            print("Insufficient Balance")
#
#        else :
#            balance = balance - withdraw
#            print("Withdraw done, your balance is:",balance)
#
#    case 4:
#        print("Thankyou for using this ATM")

#    case _:
#        print("Invalid Choice")


#Q3 Rock paper scissors
player1 = input("Player 1 - Enter rock, paper or scissors: ").lower()
player2 = input("Player 2 - Enter rock, paper or scissors: ").lower()

if player1 == player2:
    print("It's a tie!")

elif player1 == "rock" and player2 == "scissors":
    print("Player 1 wins!")

elif player1 == "paper" and player2 == "rock":
    print("Player 1 wins!")

elif player1 == "scissors" and player2 == "paper":
    print("Player 1 wins!")

elif player1 in ["rock", "paper", "scissors"] and player2 in ["rock", "paper", "scissors"]:
    print("Player 2 wins!")

else:
    print("Invalid choice")