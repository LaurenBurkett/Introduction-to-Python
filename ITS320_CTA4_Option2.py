# user inputs 5 floating-point grades 
# average calculated 
# min calculated
# max calculated 
# user prompted to run program again : y / n 
# if n - exits program / if y program runs again 
user_input = 'y'
while user_input == 'y': 
    print('Please enter 5 grades:')
    grade_1 = float(input())
    grade_2 = float(input())
    grade_3 = float(input())
    grade_4 = float(input())
    grade_5 = float(input())
    grade_list = [grade_1, grade_2, grade_3, grade_4, grade_5]
    average_var = sum(grade_list) / 5
    print('Grade average:', average_var)
    grade_min = min(grade_list)
    print('Grade minimum:', grade_min)
    grade_max = max(grade_list)
    print('Grade maximum:', grade_max)
    print('Would you like to run the program again? y/n')
    user_input = input()    
print('Goodbye.')