"""
#1
d = int(input("Enter tine length: "))
m = int(input("Enter tine length: "))



    QUESTION 2 NOT DONE





#2
lower_bound = int(input("Enter the lower bound of the interval:\n"))
upper_bound = int(input("Enter the upper bound of the interval:\n"))


rotatable_numbers = 0
special_numbers = [1, 6, 8, 9]
numbers = []

for number in range(lower_bound, upper_bound + 1):
    numbers.append(number)
    
for character in range(lower_bound, upper_bound + 1):
    #length = len(numbers[character])
    count=0
    while(numbers[character]>0):
        count=count+1
        numbers[character]=numbers[character]//10
    for char_iterations in range(count):
        if numbers[character[char_iterations]] in special_numbers:
            rotatable_numbers += 1

print(f"The number of rotatable numbers is:\n{rotatable_numbers}")
print(numbers)
"""
