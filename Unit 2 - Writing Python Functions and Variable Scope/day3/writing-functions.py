import math

def printMessage():
    print("Welcome to ICD2O!")

def subtract(num1, num2):
    answer = num1 - num2
    return answer

# printMessage()
# print(subtract(4,2))
# result = subtract(5,6)

# print(result)

# x = int(input("Enter a number: "))
# y = int(input("Enter a number: "))
# print(subtract(x,y))

def greet(name):
    return f"Hello, {name}!"

print(greet("Steve"))

def cube(num):
    return num**3

print(cube(5))

def area_rectangle(length, width):
    return length*width

print(area_rectangle(3,2))

def format_pi(decimals):
    return f"{math.pi:.{decimals}f}"

print(format_pi(3))

def seconds(hours):
    return hours*60

def def_pay(hours, rate):
    return f"Pay: ${hours*rate}.2f"

def total_with_tax(price, tax_rate):
    return f"Total: ${(price*tax_rate + price):.2f}"

def total_with_tax_v2(price, tax_rate):
    return price*tax_rate + price


print(total_with_tax(15,0.15))
print(f"Total: ${total_with_tax_v2(15,0.15):.2f}")



