
# joining of strings

# 1. String Concatenation use of + to join strings
first_name = "Erikah"
last_name = "Testimony"
full_name = first_name + " "+ last_name
sentence_1 = "My name is "  + full_name
age = 14
sentence_2= sentence_1 + " and I am " + str(age) + " years old" # we typecasted age into str fro int before it can work.
print(sentence_1)
print(sentence_2)


# 2. String Interpolation or the use of f-string
sentence_3 = f"My name is {full_name} and I am {age} years old" 
print(sentence_3)




