n = int(input())

layers = [1] # 각 레이어에 들어갈 수 있는 수
cnt = 1

while n > layers[-1]:
    layers.append(layers[-1] + cnt * 6)
    cnt = cnt + 1

print(cnt)
