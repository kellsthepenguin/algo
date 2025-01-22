n = int(input())
c = 0

for i in range(n):
    word = input()
    if list(word) == sorted(word, key=word.find):
        c += 1

print(c)
