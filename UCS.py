import heapq

grid = [
    "S..#..",
    ".#.#..",
    ".#...#",
    "...#..",
    "#...#.",
    "...#.G"
]

start, goal = (0, 0), (5, 5)
queue = [(0, start, [start])]
visited = set()

while queue:
    cost, (r, c), path = heapq.heappop(queue)

    if (r, c) in visited:
        continue
    visited.add((r, c))

    if (r, c) == goal:
        print("Path:", path)
        print("Cost:", cost)
        break

    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        nr, nc = r + dr, c + dc

        if (0 <= nr < 6 and 0 <= nc < 6
                and grid[nr][nc] != '#'
                and (nr, nc) not in visited):

            heapq.heappush(
                queue,
                (cost + 1, (nr, nc), path + [(nr, nc)])
            )