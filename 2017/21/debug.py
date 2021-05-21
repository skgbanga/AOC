s = """
.#.
..#
###
"""

mat = [line for line in s.splitlines() if line]

for row in mat:
    print("".join(row))
