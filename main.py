from functools import lru_cache


VALUES = tuple(range(1, 16))
ALL_MASK = (1 << len(VALUES)) - 1
FIXED_VALUE = 3
FIXED_INDEX = 3
ROW_COUNT = 5
VALUE_MASK = {value: 1 << (value - 1) for value in VALUES}


def row_mask(row):
    mask = 0
    for value in row:
        mask |= VALUE_MASK[value]
    return mask


@lru_cache(maxsize=None)
def compatible_rows(upper_row):
    upper_row = tuple(upper_row)

    if not upper_row:
        return tuple((value,) for value in VALUES)

    results = []

    def extend(prefix):
        position = len(prefix)
        if position == len(upper_row) + 1:
            results.append(tuple(prefix))
            return

        if position == 0:
            candidates = VALUES
        else:
            diff = upper_row[position - 1]
            previous = prefix[-1]
            candidates = (previous - diff, previous + diff)

        for candidate in candidates:
            if 1 <= candidate <= 15 and candidate not in prefix:
                prefix.append(candidate)
                extend(prefix)
                prefix.pop()

    extend([])
    return tuple(results)


def solve_from_row(current_row, used_mask):
    if len(current_row) == ROW_COUNT:
        if current_row[FIXED_INDEX] == FIXED_VALUE and used_mask == ALL_MASK:
            return [current_row]
        return None

    for next_row in compatible_rows(current_row):
        next_mask = row_mask(next_row)
        if next_mask & used_mask:
            continue
        if len(next_row) == ROW_COUNT and next_row[FIXED_INDEX] != FIXED_VALUE:
            continue

        solution = solve_from_row(next_row, used_mask | next_mask)
        if solution is not None:
            return [current_row] + solution

    return None


def solve_pyramid():
    top_values = sorted(VALUES, key=lambda value: len(compatible_rows((value,))))

    for top_value in top_values:
        solution = solve_from_row((top_value,), VALUE_MASK[top_value])
        if solution is not None:
            return solution

    return None


def print_pyramid(pyramid):
    width = len(" ".join(str(number) for number in VALUES))
    for row in pyramid:
        text = " ".join(str(number) for number in row)
        print(text.center(width))


def main():
    pyramid = solve_pyramid()
    if pyramid is None:
        print("No solution found")
        return

    print_pyramid(pyramid)


if __name__ == "__main__":
    main()