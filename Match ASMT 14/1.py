x = int(input("Enter a number "))
match x:
    case x if (x//100>0) and (x//100<10):
        print("It's is a three digits number")
    case x:
        print("It's is not a three digits number")