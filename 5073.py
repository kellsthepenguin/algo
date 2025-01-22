while True:
    sides = list(map(int, input().split()))

    if sides == [0, 0, 0]:
        break
    
    copiedSides = sides.copy()
    maxSide = max(sides)
    copiedSides.remove(maxSide)
    if maxSide >= sum(copiedSides):
        print('Invalid')
    elif sides[0] == sides[1] and sides[0] == sides[2] and sides[1] == sides[2]:
        print('Equilateral')
    elif sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
        print('Isosceles')
    else:
        print('Scalene')
