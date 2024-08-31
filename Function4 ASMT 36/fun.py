# def remove_duplicate(user_list):
#     i=0
#     while i<len(user_list):
#         j=i+1
#         while j<len(user_list):
#             if user_list[i]==user_list[j]:
#                 del user_list[j]
#             j+=1
#         i+=1
#     return user_list

# def count_frequency(user_list):
#     user_list.sort()
#     list_dict = dict()

#     i=0
#     while i<len(user_list):
#         j=i
#         cnt=0
#         while j<len(user_list):
#             if user_list[i]==user_list[j]:
#                 cnt+=1
#             else:
#                 break
#             j+=1
#         list_dict[user_list[i]]=cnt
#         i=j
    
#     return list_dict

def find_numbers(lst):
    temp = []
    for i in lst:
        if type(eval(i))==int or type(eval(i))==float:
            temp.append(lst[i])
    print(temp)
    # return temp

# def check_List(lst1, lst2):
#     lst1.sort()
#     lst2.sort()
#     if len(lst1)==len(lst2):
#         i=0
#         while i<len(lst1):
#             if lst1[i]!=lst2[i]:
#                 return False
#             i+=1
#         return True
#     return False

# def find_longest_subsequence(lst):
#     i=0
#     temp1 = []
#     longest = []
    
#     while i<len(lst):
#         if (i+1)<len(lst) and lst[i]<lst[i+1]:
#             temp1.append(lst[i])
#         else:
#             temp1.append(lst[i])
            
#             if len(temp1) > len(longest):
#                 longest = temp1
#             temp1 = []
#         i+=1
#     return longest


# # Q-1
# user_input = input("Enter list elements seperated by spaces: ")
# user_list = user_input.split()
# user_list = remove_duplicate(user_list)
# print(user_list)

# # Q-2
# user_input = input("Enter list elements seperated by space: ")
# user_list = user_input.split()
# print(count_frequency(user_list))


# # Q-3
user_input = input("Enter list elements seperated by space: ")
user_list = list(user_input)
print(user_list)
find_numbers(user_list)
# print(find_numbers(user_list))

# # Q-4
# sample_list = [1,2,1,3,4,5,2]
# print(find_longest_subsequence(sample_list))

# Q-5
# l1 = [1,2,3,4,5,6]
# l2 = [1,4,3,5,2,6]
# print(check_List(l1,l2))