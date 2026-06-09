# Absolute Castle (Pyramid Puzzle)

This folder contains a Python solver for the Jane Street puzzle Absolute Castle.

## How this code works

The solver builds the pyramid row by row using depth-first search with pruning.

1. It represents values 1 through 15 and tracks which values are already used.
2. For each row, it generates all compatible next rows that satisfy the adjacent-difference rule.
3. It uses caching for compatible-row generation so repeated row shapes are computed once.
4. It uses a bitmask to quickly reject rows that reuse numbers already placed in the pyramid.
5. It enforces the fixed condition that the middle value of the 5-number base row is 3.
6. It stops as soon as a full valid pyramid is found and prints it centered.

## Main functions

- row_mask: converts a row into a bitmask of used values.
- compatible_rows: generates valid child rows from an upper row.
- solve_from_row: recursive backtracking search.
- solve_pyramid: tries top-row starts in a heuristic order.
- print_pyramid: prints the final layout.

Run with:

python main.py
