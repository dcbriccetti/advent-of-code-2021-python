def max_height(starting_dx: int, starting_dy: int, target_ranges: tuple[range, range]) -> int | None:
    dx, dy = starting_dx, starting_dy
    x, y = 0, 0
    max_height = None

    def slow_value(d: int) -> int:
        if d > 0:
            d -= 1
        elif d < 0:
            d += 1
        return d

    def not_too_far_right(): return x <= target_ranges[0][-1]
    def not_too_far_down(): return y >= target_ranges[1][0]
    def point_in_target(): return x in target_ranges[0] and y in target_ranges[1]

    while not_too_far_right() and not_too_far_down():
        x += dx
        dx = slow_value(dx)

        y += dy
        dy -= 1

        if max_height is None or y > max_height:
            max_height = y

        if point_in_target():
            return max_height

    return None

def solve() -> None:
    minx, maxx, miny, maxy = 20, 30, -10, -5  # Test
    # minx, maxx, miny, maxy = 79, 137, -176, -117 # My data
    target_ranges = range(minx, maxx + 1), range(miny, maxy + 1)
    best_max_height = 0
    best_dx = None
    best_dy = None
    num_wins = 0
    for dx in range(0, 500):
        for dy in range(-500, 500):
            height = max_height(dx, dy, target_ranges)
            if height is not None:
                num_wins += 1
                print(f'({dx}, {dy}), {height=}')
                if height > best_max_height:
                    best_max_height = height
                    best_dx = dx
                    best_dy = dy
    print(f'\nBest: ({best_dx}, {best_dy}), max height: {best_max_height}')
    print(f'{num_wins=}')

solve()
