"""
#1
a3 = int(input())
a2 = int(input())
a1 = int(input())
b3 = int(input())
b2 = int(input())
b1 = int(input())
apples = a3 * 3 + a2 * 2 + a1
bananas = b3 * 3 + b2 * 2 + b1
if apples>bananas:
    print("A")
else:
    print("B")

#2
L = int(input())
numbers = []
characters = []
for questions in range(L):
    inp = input()
    index = inp.find(" ")
    numbers.append(inp[:index])
    characters.append(inp[index + 1:])

for integer in range(len(numbers)):
    numbers[integer] = int(numbers[integer])

print(numbers, characters)
for display in range(L):
    print(characters[display] * numbers[display])
"""
#3
def encode_line(line):
    encoded_line = ""
    count = 1
    for character in range(1, len(line)):
    
        if line[character] == line[character - 1]:
            count += 1
        else:
            encoded_line += str(count) + " " + line[character - 1] + " "
            count = 1

    encoded_line += str(count) + " " + line[-1] + " "

    return encoded_line

number_of_lines = int(input())

encoded_lines = []

for _ in range(number_of_lines):
    line = input()
    encoded_line = encode_line(line)
    encoded_lines.append(encoded_line)

for encoded_line in encoded_lines:
    print(encoded_line)

