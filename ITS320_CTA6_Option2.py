import itertools

user_list1 = [int(item) for item in input("Please enter the list items (Example: '1 2 3'): ").split()] 
user_list2 = [int(item) for item in input("Please enter the list items (Example: '1 2 3') : ").split()] 
list3 = [user_list1, user_list2]
list4 = []
for element in itertools.product(*list3):
    list4.append(element)
print(list4)