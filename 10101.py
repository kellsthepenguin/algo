angles = []
isThereSameAngle = False

for _ in range(3):
    angle = int(input())
    if angle in angles:
        isThereSameAngle = True
    angles.append(angle)

if angles == [60, 60, 60]:
    print('Equilateral')
elif sum(angles) != 180:
    print('Error')
elif isThereSameAngle:
    print('Isosceles')
else:
    print('Scalene')
