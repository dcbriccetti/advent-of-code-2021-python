from collections import defaultdict
import helpers

Targets = list[str]
TargetsBySource = dict[str, Targets]
paths: TargetsBySource = defaultdict(list)

for line in helpers.lines('../data/12.txt'):
    s, e = line.split('-')
    paths[s].append(e)
    paths[e].append(s)

def dfs(path: list[str], visited: set[str], cave: str):
    if cave == 'end':
        solutions.append(path)
    else:
        if cave.islower():
            visited.add(cave)
        for next_cave in paths[cave]:
            if next_cave not in visited:
                dfs(path + [next_cave], set(visited), next_cave)

solutions: list[list[str]] = []
dfs(['start'], set(), 'start')
print(len(solutions))
