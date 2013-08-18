global d
global c
global path_down
global path_cross

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

def re_arrange(i):
    global c
    global d
    d = path_down[i]
    c = path_cross[i]
    path_down.pop(i)
    path_cross.pop(i)


def arrange(start):
    path = []
    global c
    global d
    global path_cross
    global path_down
    d = start[0]
    c = start[1]
    while len(path_cross) != 0 :
        for i in range(0,len(path_cross)):
            if ((d+1)== path_down[i]) and (c == path_cross[i]) :
                print ("down ")
                re_arrange(i)
                break
            elif ((d-1)== path_down[i]) and (c == path_cross[i]) :
                print ("up ")
                re_arrange(i)
                break
            elif (d == path_down[i]) and ((c+1) == path_cross[i]):
                print("right ")
                re_arrange(i)
                break
            elif (d == path_down[i]) and ((c-1) == path_cross[i]):
                print("left ")
                re_arrange(i)
                break

def getCodinates(slove_maze):
    global path_cross
    global path_down
    path_down =[]
    path_cross =[]
    start = []
    down = len(slove_maze)
    cross = len(slove_maze[0])
    for i in range(0,down):
        for j in range(0,cross):
            if slove_maze[i][j] == '.':
                path_down.append(i)
                path_cross.append(j)
            elif slove_maze[i][j] == 's':
                start.append(i)
                start.append(j)
    arrange(start)
    #print(path_down)
    #print(path_cross)
    #print(start)