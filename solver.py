def slove(maze):
    down = len(maze)-1
    cross = len(maze[0])-1
    while True:
        not_change = True
        for i in range(1,down):
            for j in range(1,cross):
                k = maze[i][j]
                if k == '.':
                    if ((maze[i][j-1]=='#' or maze[i][j-1]=='b') and (maze[i-1][j]=='#' or maze[i-1][j]=='b') and (maze[i][j+1]=='#' or maze[i][j+1]=='b')):
                        maze[i][j] = 'b'
                        not_change = False
                    elif ((maze[i-1][j]=='#' or maze[i-1][j]=='b') and (maze[i][j+1]=='#' or maze[i][j+1]=='b') and (maze[i+1][j]=='#' or maze[i+1][j]=='b')):
                        maze[i][j] = 'b'
                        not_change = False
                    elif ((maze[i][j+1]=='#' or maze[i][j+1]=='b') and (maze[i+1][j]=='#' or maze[i+1][j]=='b') and (maze[i][j-1]=='#' or maze[i][j-1]=='b')):
                        maze[i][j] = 'b'
                        not_change = False
                    elif ((maze[i+1][j]=='#' or maze[i+1][j]=='b') and (maze[i][j-1]=='#' or maze[i][j-1]=='b') and (maze[i-1][j]=='#' or maze[i-1][j]=='b')):
                        maze[i][j] = 'b'
                        not_change = False
        if not_change:
            break
    return maze

def getCodinates(slove_maze):
    path =[]
    down = len(slove_maze)
    cross = len(slove_maze[0])
    for i in range(0,down):
        for j in range(0,cross):
            if slove_maze[i][j] == '.':
                path.append(i)
                path.append(j)
    print(path)