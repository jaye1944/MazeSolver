import solver
global st_end

#cerate 1 and last row
def pad_st_end(row):
    global st_end
    st_end = []
    for i in range(0,len(row)+2):
        st_end.append('#')
    #print(st_end)

#create  padding
def padding(maz_e):
    padded_maze =[]
    padded_maze.append(st_end)
    temp_row = []
    for row in maz_e:
        temp_row.append('#')
        for i in row:
            temp_row.append(i)
        temp_row.append('#')
        padded_maze.append(temp_row)
        temp_row = []
    padded_maze.append(st_end)
    return padded_maze

#print file
def printer(maze):
    for i in maze:
        print(' '.join(i))

#remove padding
def remover(maz_e):
    maz_e.remove(maz_e[0])
    maz_e.remove(maz_e[len(maz_e)-1])
    return maz_e

#open file
def read(name):
    fo = open(name, "r")
    all =[]
    row =[]
    while True:
        k = fo.read(1)
        if k == '\n':
            if(len(row)!=0):
                all.append(row)
                row=[]
        elif not k:
            if(len(row)!=0):
                all.append(row)
            fo.close()
            break
        else:
            row.append(k)
    pad_st_end(all[0])
    return all
maze = read("maze.txt")
r_maze = remover(solver.slove(padding(maze)))
#print(maze)
#print(len(all))
#printer(maze)

#print("ppppppppppppppppppppppp")
printer(r_maze)
