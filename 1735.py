from fractions import Fraction
a, b = map(int, input().split())
c, d = map(int, input().split())

ratio = (Fraction(a, b) + Fraction(c, d)).as_integer_ratio()

print(ratio[0], ratio[1])
