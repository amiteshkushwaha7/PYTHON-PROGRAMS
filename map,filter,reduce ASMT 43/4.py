def filter_int(element):
    if type(element)==int:
        return element
    
intValues = filter(filter_int, [2,2.2,"raman",5+3j,353,"this is a car",2345,234,765,676,7.5,7+7j])
for e in intValues:
    print(e,end=' ')