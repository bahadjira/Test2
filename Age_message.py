from datetime import date

name = input("Enter your name ")
while True:
    try:
        age = int (input("Enter your age "))
    except:
        print("Please enter a number ")
        continue
    break
yr = date.today ().year + 100 - age
str1 = "You will turn 100 in the year "
num = int(input("enter a number "))
print((str1, yr)*num)

