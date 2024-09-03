#1
P = int(input())
C = int(input())
F = 50*P - 10*C
if P > C:
    F = F + 500
print(F)

#2
N = int(input())
spice = 0
for x in range(N):
    pepper = input()
    if pepper == "Poblano":
        spice += 1500
    if pepper == "Mirasol":
        spice += 6000
    if pepper == "Serrano":
        spice += 15500
    if pepper == "Cayenne":
        spice += 40000
    if pepper == "Thai":
        spice += 75000
    if pepper == "Habanero":
        spice += 125000
print(spice)

#3
n = int(input())

availability = [0] * 5
print(availability)

for _ in range(n):
    person_availability = input()
    for i, day in enumerate(person_availability):
        if day == 'Y':
            availability[i] += 1
    print(availability)

max_people = max(availability)

output = [str(i+1) for i, num_people in enumerate(availability) if num_people == max_people]
print(','.join(output))

#4