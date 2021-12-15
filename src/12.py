from collections import defaultdict
import helpers

Targets = list[str]
TargetsBySource = dict[str, Targets]
paths: TargetsBySource = defaultdict(list)

lc_caves = set()
for line in helpers.lines('../data/12_test.txt'):
    c1, c2 = line.split('-')
    for c in [c1, c2]:
        if c.islower() and c not in ['start', 'end']:
            lc_caves.add(c)
    paths[c1].append(c2)
    paths[c2].append(c1)

def search(path: list[str], visited: set[str], cave: str):
    global num_special_cave_visits
    if cave == 'end':
        print(two_visit_cave, ','.join(path))
        solutions.append(path)
    else:
        if cave.islower():
            visited.add(cave)
            if cave == two_visit_cave:
                num_special_cave_visits += 1
        for next_cave in paths[cave]:
            if next_cave not in visited or (
                    cave == two_visit_cave and num_special_cave_visits < 2):
                search(path + [next_cave], set(visited), next_cave)

solutions: list[list[str]] = []
for two_visit_cave in list(lc_caves) + [None]:
    num_special_cave_visits = 0
    search(['start'], set(), 'start')

ssl = list(set(','.join(s) for s in solutions))
ssl.sort()
print()
print('\n'.join(ssl))
print(len(ssl))
