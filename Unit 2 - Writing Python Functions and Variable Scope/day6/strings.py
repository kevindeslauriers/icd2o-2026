# str1 = "hello"
# str2 = "alpha"
# str3 = "bet"
# str4 = "alphabet"

# print(len(str1))    # len() is the number of characters in a string
# print(len(str4))    # the len() is one more than the largest positive index
# print(len("Ryan"))  # len() is 4 largest positive index is 3
# print(len("Enzo"))  # len() is 4 largest positive index is 3

# print(str4[3])      # h - select a character using str[n] where n is an index
# print(str4[-5])     # h

# print("hello"[2])   # first l
# print("hello"[-3])  # first l

# # print("hello"[100])           # IndexError: string index out of range
# # print("hello"[len("hello")])    # IndexError: string index out of range ---> because "hello"[5] biggest incex is 4


# #[start:end:step]

# print(str4[2:5])    # "pha" 2 is inclusive and 5 is exclusive

# print("Enzo"[2:4])  #"zo" 2 inclusive and 4 exclusive which means indexes 2 to 3 inclusive

# print("alphabet"[5:8])  # "bet"
# print("alphabet"[-3:8]) # "bet"
# print("alphabet"[-3:])  # "bet"
# print("alphabet"[5:])   # "bet"

# print("0123456789"[0:10:2]) # "02468" skips every other one - step of 2
# print("0123456789"[0:10:3]) # step of 4 "0369"

# print("0123456789"[-1:-11:-1]) # "9876543210" --> steps backwards

# print("alphabet"[::2])      # starts at 0 and goes to the end and steps 2

# print("alphabet"[2::2])

# code = "ICS-4U"
# print(code[1::2])

def mystery(name, width):
    return f"{name:^{width}}"
print(mystery("he",10))

