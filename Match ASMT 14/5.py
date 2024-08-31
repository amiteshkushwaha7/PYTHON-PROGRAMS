x = input("Enter a string ")
match x:
    case x if x in "My":
        print("one")
    case x if x in "SirG":
        print("two")
    case x if x in "Education":
        print("three")
    case _:
        print("invalid string")
