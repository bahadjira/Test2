num = int(input ("Enter a number: "))
mod = num % 2
if mod > 0 :
    print ("this is an odd number")
else:
    print ("This is an Even number")
    if num % 4 == 0:
        print (num, "is a multiple of 4")
    else:
        print (num, "does not divide evenly by 4")


