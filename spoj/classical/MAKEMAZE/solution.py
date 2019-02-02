def openings(maze):
    o = []
    m = len(maze)
    n = len(maze[0])
    for i in range(0, m):
        if maze[i][0] == 0:
            o.append((i, 0))
        
        if n > 1 and maze[i][n-1] == 0:
            o.append((i, n-1))
    
    for j in range(1, n-1):
        if maze[0][j] == 0:
            o.append((0, j))
        if m > 1 and maze[m-1][j] == 0:
            o.append((m-1, j))
    return o

# o is a list of tuples
# first tuple indicates starting position of maze
# second tuple indicates ending position of maze
dy = [-1, 0, 1, 0]
dx = [ 0, 1, 0, -1]

from queue import Queue
def valid_based_on_bfs(maze):
    o = openings(maze)
    if len(o) != 2:
        return False
    
    m = len(maze)
    n = len(maze[0])
    
    p = o[0]
    maze[p[0]][p[1]] = 2
    work = Queue()
    work.put(p)
    while not work.empty():
        temp = work.get()
        y = temp[0]
        x = temp[1]
        for k in range(0, 4):
            nx = dx[k] + x
            ny = dy[k] + y
            if ny < 0 or ny > m-1 or nx < 0 or nx > n-1:
                continue
            if maze[ny][nx] != 0:
                continue
            
            maze[ny][nx] = 2
            q = (ny, nx)
            
            # Reached end of maze
            if q == o[1]:
                return True
            
            work.put(q)
            
    return maze[o[1][0]][o[1][1]]

def valid(maze):
    return valid_based_on_bfs(maze)
    
def main():
    
    for _ in range(0, int(input())):
        m, n = [int(tok) for tok in input().split()]
        maze = [[0 for i in range(n)] for j in range(m)]

        for i in range(0, m):
            row = input()
            for j, c in enumerate(row):
                if c == '#':
                    maze[i][j] = 1

        if valid(maze):
            print("valid")
        else:
            print("invalid")

main()

