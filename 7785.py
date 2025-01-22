n = int(input())
company = set()

for _ in range(n):
    name, el = input().split()
    if el == "enter":
        company.add(name)
    else:
        company.remove(name)

c = reversed(sorted(list(company)))

for name in c:
    print(name)
