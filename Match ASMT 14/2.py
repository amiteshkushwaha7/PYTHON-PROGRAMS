x = int(input("Enter a number "))
match x:
    case x if x>0:
        print("It's a positive number")
    case x if x==0:
        print("It's",0)
    case x if x<0:
        print("It's a negative number")