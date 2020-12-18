mom_dict = {
  "name": "Karen",
  "age": 45,
  "gender": "female",
  "loves": "pizza"
}
dad_dict = {
    "name": "Mike",
    "age": 40,
    "gender": "male",
    "loves": "french fries"
}
daughter_dict = {
    "name": "Jessica",
    "age": 15,
    "gender": "female",
    "loves": "gymnastics"
}

family_dict = {
    "mom": mom_dict,
    "dad": dad_dict,
    "daughter": daughter_dict
}

print(family_dict)

#updated age of daughter
daughter_dict["age"] = 16


#print only age of daughter
print(daughter_dict["age"])