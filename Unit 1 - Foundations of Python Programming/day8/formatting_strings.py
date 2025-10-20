number = 42
print(f"|{number}|")     #|42|
print(f"|{number:>5}|")  #|   42| width of 5 right aligned
print(f"|{number:<5}|")  #|42   | width of 5 left aligned
print(f"|{number:^5}|")  #| 42  | center of 5 left aligned
print(f"|{number:^10}|") #|    42    |


value = 123.456789
print(f"{value}")
print(f"{value:.2f}")   #123.46
print(f"{value:.3f}")   #123.457

value = 7.5
print(f"{value:.2f}")

percentage = 15/17
print(f"{percentage:.3%}")


cost = 5.67

print(f"The cost is ${cost:.2f}")
