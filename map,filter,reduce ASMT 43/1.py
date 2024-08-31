def find_vowels(string):
    i = 0
    seperate_charaters = []
    while i<len(string):
        seperate_charaters.append(string[i])
        i+=1 
    
    vowels = "aeiouAEIOU"
    cnt=0
    for e in seperate_charaters:
        if e in vowels:
            cnt+=1
    return cnt

vowels_list = map(find_vowels, ["this is a car","how are you","what is your name?","i am happy"])
for e in vowels_list:
    print(e,end=' ')