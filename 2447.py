n = int(input())

def s(n):
    if n == 1:
        return ['*']
    stars = s(n // 3)
    r = []

    for star in stars:
        r.append(star * 3)
    
    for star in stars:
        r.append(star + ' ' * (n // 3) + star)
    
    for star in stars:
        r.append(star * 3)
    
    return r

print('\n'.join(s(n)))
