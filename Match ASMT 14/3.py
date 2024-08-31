print("1.Odd-Even","2.Positive-Non-Positive","3.Simple Interest","4.Roots of quadratic equation",sep='\n')
choice = int(input("Enter your choice "))
match choice:
    case 1:
        x = int(input("Enter a number "))
        print("Even" if x%2==0 else "Odd")
    case 2:
        x = int(input("Enter a number "))
        if x>0:
            print("Positive")
        elif x==0:
            print(0)
        else:
            print("Non-Positive")
    case 3:
        print("Enter principle, rate and time ")
        p = int(input())
        r = float(input())
        t = int(input())

        si = (p*r*t)/100
        print(si)
    case 4:
        print("Enter three numbers ")
        a = int(input())
        b = int(input())
        c = int(input())

        if ((b**2) - (4*a*c)) > 0:
            print("Real roots")
        elif ((b**2) - (4*a*c)) == 0:
            print("Imaginary roots")
        else:
            print("Distinct roots")
    case _:
        print("Invalid choice")