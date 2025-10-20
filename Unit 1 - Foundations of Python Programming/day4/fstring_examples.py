age = 17
name = "Steve"

#String concatenation - joins strings using + and everything must be converted to a string
print(name + " is " + str(age) + " years old.") # cannot add a int to a string so use str(age)

print(f"{name} is {age} years old.")

sentence = name + " is " + str(age) + " years old."
print(sentence)

sentence2 = f"{name} is {age} years old."
print(sentence2)

print(23)