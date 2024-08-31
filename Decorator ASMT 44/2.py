def deco_function(dup_print_message):
    def greeting():
        print("Happy New Year")
        dup_print_message()
    return greeting

@deco_function
def print_message():
    print("This is the end of the program")

print_message()    