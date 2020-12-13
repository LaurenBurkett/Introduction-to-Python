def concatstring (String1, String2, String3):
    var_reverse = String3 + String2 + String1 
    print(var_reverse)
    return var_reverse

String1 = input('Please supply a string: ')
String2 = input('Please supply a string: ')
String3 = input('Please supply a string: ')

concatstring(String1, String2, String3)