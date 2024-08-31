x = eval(input("Enter a data "))
match x:
    case x if type(x)==int:
        print("Monday")
    case x if type(x)==float:
        print("Tuesday")
    case x if type(x)==complex:
        print("Wednesday")
    case x if type(x)==bool:
        print("Thrusday")