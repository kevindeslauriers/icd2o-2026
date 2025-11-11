age = 15
print(age >= 16)         # False

temp_c = -2
print(temp_c <= 0)       # True

speed = 72
limit = 80
print(speed > limit)     # False

length = 19.9
target = 20.0
print(length != target)     # True length is not equals to target

username = "Admin"
print(username.lower() == "admin")  # True

msg = "System OK"
print("ok" in msg.lower())  # True

password = "secret42"
print(len(password) >= 8)   # True (8 >= 8)

word = "preheating"
print(word[:3].lower() == "pre")  # starts with    # True
print(word[-3:].lower() == "ing") # ends with      # True

title = "The Hobbit"
print(title[:3].lower() == "the")       # true

name = "maria"
print(name != "" and name[0].lower() < "m")  # alphabet check (guard empty)
# short circuit
