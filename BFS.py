from collections import deque

grid = [
    "S..#..",
    ".#.#..",
    ".#...#",
    "...#..",
    "#...#.",
    "...#.G"
]

start, goal = (0, 0), (5, 5)
queue = deque([(start, [start])])
visited = {start}

while queue:
    (r, c), path = queue.popleft()

    if (r, c) == goal:
        print("Path:", path)
        print("Steps:", len(path) - 1)
        break

    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        nr, nc = r + dr, c + dc

        if (0 <= nr < 6 and 0 <= nc < 6
                and grid[nr][nc] != '#'
                and (nr, nc) not in visited):

            visited.add((nr, nc))
            queue.append(((nr, nc), path + [(nr, nc)]))