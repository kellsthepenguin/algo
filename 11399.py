n = int(input())
p = list(map(int, input().split()))
p_dict = {}

for i, p_i in enumerate(p):
    p_dict[i + 1] = p_i

sorted_p_dict = dict(sorted(p_dict.items(), key=lambda x: x[1]))
time = 0

for man, time1 in sorted_p_dict.items():
    time += sum(list(sorted_p_dict.values())[:man - 1]) + time1

print(time)
