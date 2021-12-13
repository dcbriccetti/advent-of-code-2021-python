from helpers import create_grid, neighbor_coords

Flashes = set[tuple[int, int]]
levels = create_grid('../data/11.txt')
nr, nc = levels.shape
num_octopuses = nr * nc

def step() -> int:
    def over_nines():
        return [(r, c) for r in range(nr) for c in range(nc) if levels[r, c] > 9]

    def increase_all_energy_levels():
        for r in range(nr):
            for c in range(nc):
                levels[r, c] += 1

    def flash_until_no_more(flashes):
        while True:
            if needing_flash_coord_pairs := over_nines():
                for r, c in needing_flash_coord_pairs:
                    flashes.add((r, c))
                    flash(r, c)
            else:
                break

    def reset_over_nines():
        for r, c in over_nines():
            levels[r, c] = 0

    def reset_flashed(flashes):
        for fr, fc in flashes:
            levels[fr, fc] = 0

    flashes: Flashes = set()
    increase_all_energy_levels()
    flash_until_no_more(flashes)
    reset_over_nines()
    reset_flashed(flashes)
    return len(flashes)

def flash(r: int, c: int) -> None:
    'Increase the energy level of adjacent octopuses, and reset the level of this one'
    for nr, nc in neighbor_coords(levels.shape, r, c):
        levels[nr, nc] += 1
    levels[r, c] = 0

def part1() -> int:
    steps = 100
    num_flashes = sum(step() for _ in range(steps))
    print(f'{num_flashes:,} flashes after {steps} steps')
    return num_flashes

def part2() -> int:
    num_flashes = None
    step_num = 0
    while num_flashes != num_octopuses:
        step_num += 1
        num_flashes = step()
    print(f'All octopuses flashed at step {step_num}')
    return step_num

part1()
part2()
