dials = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

word = input()
time = 0

for letter in list(word):
    time += 3 + dials.index(next(x for x in dials if letter in x))

print(time)
