# WORK IN PROCESS

n, m = map(int, input().split())
grid = []
turns = 0

for _ in range(n):
    pixels = list(input())
    grid.append(pixels)

commands = list(input())
player = None
objs = {}
num_monster = 0
num_item_box = 0
boss_rc = (0, 0)

class Player:
    def __init__(self, r, c):
        self.hp = 20
        self.max_hp = 20
        self.atk = 2
        self.dfn = 2 # defense
        self.exp = 0
        self.need_xp = 5
        self.lvl = 1
        self.armor = 0 # 방어구
        self.weapon = 0 # 무기
        self.acc = [] # 장신구
        self.r = r
        self.c = c

    def move(self, direction): # main logic 움직이면 grid에도 반영
        global turns
        to = (0, 0)
        turns += 1
        if direction == 'L':
            to = (self.r, self.c - 1)
        elif direction == 'R':
            to = (self.r, self.c + 1)
        elif direction == 'U':
            to = (self.r - 1, self.c)
        elif direction == 'D':
            to = (self.r + 1, self.c)
        
        if to[0] > n or to[1] > m or to[0] < 1 or to[1] < 1 or grid[to[0]-1][to[1]-1] == "#":
            if not (self.r, self.c) in objs: return
            if isinstance(objs[(self.r, self.c)], SpikeTrap):
                self.hp =- 5
                if self.hp < 0:
                    self.end(False, 'SPIKE TRAP')
                    return
            return
        
        thing = grid[to[0]-1][to[1]-1]

        if thing == "B":
            print(objs)
            item = objs[(to[0], to[1])]
            if item.type == "W":
                self.weapon = item.arg
            elif item.type == "A":
                self.armor = item.arg
            elif item.type == "O":
                if item.arg not in self.acc and len(self.acc) <= 3:
                    self.acc.append(item.arg)
        elif thing == "&" or thing == "M":
            monster = objs[(to[0], to[1])]
            playerPower = max(1, self.atk + self.weapon - monster.dfn)
            monsterPower = max(1, monster.atk - (self.dfn + self.armor))
            isPlayerAttack = True
            while self.hp > 0 and monster.hp > 0:
                if isPlayerAttack:
                    monster.hp -= playerPower
                else:
                    player.hp -= monsterPower

            if self.hp < 0:
                self.end(False, monster.name) # exit
                return
            elif monster.hp < 0:
                self.expup(monster.exp)
                if monster.isBoss:
                    self.end(True, None)
        
        if thing == "B" or thing == "&" or thing == "M":
            del objs[(to[0], to[1])]

        if not (to[0], to[1]) in objs: return
        if isinstance(objs[(to[0], to[1])], SpikeTrap):
            self.hp =- 5
            if self.hp < 0:
                self.end(False, 'SPIKE TRAP')
        
        grid[to[0]-1][to[1]-1] = '@'
        self.r = to[0]
        self.c = to[1]

    def expup(self, exp):
        self.exp += exp

        if self.exp >= self.need_xp:
            self.exp = 0
            self.lvl += 1
            self.need_xp = 5 * self.lvl
    
    def end(self, win, by):
        for lines in grid:
            for pixel in lines:
                print(pixel, end='')
            print()
        print('Passed Turns : ' + turns)
        print('LV : ' + self.lvl)
        if self.hp < 0: self.hp = 0
        print('HP : ' + self.hp + '/' + self.max_hp)
        print('ATT : ' + self.atk + '+' + self.weapon)
        print('DEF : ' + self.exp + '|' + self.need_xp) 
        if win:
            print('YOU WIN!')
        elif by == None:
            print('Press any key to continue.')
        else:
            print('YOU HAVE BEEN KILLED BY ' + by + '..')
        exit()



class Monster:
    def __init__(self, name, atk, dfn, max_health, exp, isBoss):
        self.name = name
        self.atk = atk
        self.dfn = dfn
        self.hp = max_health
        self.max_health = max_health
        self.exp = exp
        self.isBoss = isBoss

    def reset(self): # called when reincarnation used
        self.hp = self.max_health

class Item:
    def __init__(self, type, arg): # arg는 공격력 또는 방어력 또는 효과
        self.type = type
        self.arg = arg

class SpikeTrap:
    def __init__(self):
        pass

def int_or_skip(value):
    try:
        int(value)
    except ValueError:
        return value
    return int(value)

for r, line in enumerate(grid):
    for c, pixel in enumerate(line):
        if pixel == "B":
            num_item_box += 1
        elif pixel == "&":
            num_monster += 1
        elif pixel == "M":
            num_monster += 1
            boss_rc = (r + 1, c + 1)
        elif pixel == "^":
            objs[(r + 1, c + 1)] = SpikeTrap()
        elif pixel == "@":
            player = Player(r + 1, c + 1)

for _ in range(num_monster):
    r, c, s, w, a, h, e = map(int_or_skip, input().split())
    
    objs[(r, c)] = Monster(s, w, a, h, e, True if boss_rc == (r, c) else False)

for _ in range(num_item_box):
    r, c, t, arg = map(int_or_skip, input().split())
    print("ITEM", r,c)
    objs[(r, c)] = Item(t, int_or_skip(arg))

for command in commands:
    player.move(command)