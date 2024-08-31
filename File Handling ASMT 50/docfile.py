def file_to_dict(file): 
    data_dict = {}
    f=open(file,"r")
    
    for line in f:
        line = line.strip()
        
        name,age = line.split(',')
        age = int(age)
        
        data_dict[name] = age
        
    return data_dict

print(file_to_dict("name_age.txt"))
        