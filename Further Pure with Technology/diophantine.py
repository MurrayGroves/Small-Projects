# Find values of x and y for ax + by = c
def diophantine(a, b, c):
    solutions = []
    for x in range(0, c+1, a):
        for y in range(0, c+1, b):
            if x + y == c:
                solutions.append((x//a, y//b))

            elif x + y > c:
                break
                
    return solutions


print(diophantine(2, 3, 54))
