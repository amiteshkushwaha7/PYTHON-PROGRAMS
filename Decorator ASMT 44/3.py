def deco_function(dup_print_message):
    def greetint():
        dup_print_message()
    return greetint

@deco_function
def print_message():
    print("Good Bye")
    
print_message()