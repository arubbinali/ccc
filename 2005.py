"""
#1
print("Number of daytime minutes?")
d = int(input())
print("Number of evening minutes?")
e = int(input())
print("Number of weekend minutes?")
w = int(input())

if d >= 100:
    d = d - 100

acents = 0
bcents = 0

                #Plan a
acents = (d*25)+(e*15)+(w*20)
print(acents)

                #Plan b
d = 0
if d >= 250:
    d = d - 250
bcents = (d*45)+(e*35)+(w*25)


acents = str(acents)
bcents = str(bcents)

print("Plan A costs",acents + ".")
print("Plan B costs",bcents + ".")

acents = int(acents)
bcents = int(bcents)

if acents < bcents:
    print("Plan A is cheapest.")
elif bcents < acents:
    print("Plane B is cheapest.")
else:
    print("Plan A and B are the same price.")

#2
instructions = []
while True:
    instruction = input()
    if instruction == "SCHOOL":
        break
    instructions.append(instruction)

instructions.reverse()
opposite_instructions = []

for instruction in instructions:
    if instruction != "R" and instruction != "L":
        opposite_instructions.append(f"Turn LEFT onto {instruction} street.")

opposite_instructions.append("Turn LEFT into your HOME.")

for instruction in opposite_instructions:
    print(instruction)
"""
    
