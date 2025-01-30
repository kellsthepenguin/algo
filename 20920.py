from collections import defaultdict
import sys

input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, open(0).read().rstrip().split())
words = []

occurrences = defaultdict(lambda: 0)

for i in range(n):
    word = open(0).read().rstrip()
    if len(word) < m:
        continue
    occurrences[word] += 1
    words.append(word)

words.sort(key=lambda x: (-occurrences[x], -len(x), x))
s_words = list(dict.fromkeys(words))

print(' '.join(map(str, s_words)) + '\n')
