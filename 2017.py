"""
#1
x = int(input())
y = int(input())
if x > 0 and y > 0:
    print("1")
elif x < 0 and y > 0:
    print("2")
elif x < 0 and y < 0:
    print("3")
else:
    print("4")

#2
N = int(input())
k = int(input())
sum = N
for x in range(k):
    N *= 10
    sum += N
print(sum)
"""
#3
def possible_to_move_or_not(initial_destination, final_destination, battery):

    one = two = 0

    a = initial_destination.split(" ")[0]
    b = initial_destination.split(" ")[1]
    c = final_destination.split(" ")[0]
    d = final_destination.split(" ")[1]     
                                            
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)

    
    if a > c:
        one = a - c
    else:
        one = c - a
    
    if b > d:
        two = b - d
    else:
        two = d - b

    required_energy = one + two
    
    if battery >= required_energy and (battery % required_energy) % 2 == 0:
        return "Y"
    else:
        return "N"


initial_destination = input()
final_destination = input()
battery = int(input())
print(possible_to_move_or_not(initial_destination, final_destination, battery))
