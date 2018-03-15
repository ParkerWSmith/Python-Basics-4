#Parker Smith
#1/30/2018
#CCIS 1505-02
#Program 4

#Count from 1 - 10 by 1
count = 1
while count <= 10:
    print ("Loop Counter =", count)
    count += 1
print()

#Count from 1 - 101 by 10
counter = 1
while counter <= 101:
    print("Loop Counter =", counter)
    counter += 10
print()

#Count backwards from 1000 - 0 by 100
ctDown = 1000
while ctDown >= 0:
    print("Loop Counter =", ctDown)
    ctDown -= 100
print()

#Create english word for user inputed number
strNum = input("Please enter a number from 1 - 10: ")
if strNum == "1":
    print("One")
elif strNum == "2":
    print("Two")
elif strNum == "3":
    print("Three")
elif strNum == "4":
    print("Four")
elif strNum == "5":
    print("Five")
elif strNum == "6":
    print("Six")
elif strNum == "7":
    print("Seven")
elif strNum == "8":
    print("Eight")
elif strNum == "9":
    print("Nine")
elif strNum == "10":
    print("Ten")
else:
    print("That is not a valid number.")

#Login with username and password
strName = input("Enter your username:")
strPass = input("Enter your password:")
if strName == "john doe" and strPass == "fopwpo":
    print("Login Successful!")
while strName != "john doe" or strPass != "fopwpo":
    print("Password or user name was incorrect, please try again.")
    strName = input("Enter your username:")
    strPass = input("Enter your password:")
if strName == "john doe" and strPass == "fopwpo":
    print("Login Successful!")
