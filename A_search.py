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

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

queue = [(heuristic(start, goal), 0, start, [start])]
visited = set()

while queue:
    f, cost, (r, c), path = heapq.heappop(queue)

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

            new_cost = cost + 1
            h = heuristic((nr, nc), goal)
            new_f = new_cost + h

            heapq.heappush(
                queue,
                (new_f, new_cost, (nr, nc), path + [(nr, nc)])
            )