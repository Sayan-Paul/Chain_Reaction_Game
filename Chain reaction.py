#################################################################
### Chain Reactor Game Demo For Technites                       #
###                                                             #
#################################################################

grid=[[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
      [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
      [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
      [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
      [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
      [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
      [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
      [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
      [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
      ]

free_dir_grid=[
                [2,3,3,3,3,3,3,2],
                [3,4,4,4,4,4,4,3],
                [3,4,4,4,4,4,4,3],
                [3,4,4,4,4,4,4,3],
                [3,4,4,4,4,4,4,3],
                [3,4,4,4,4,4,4,3],
                [3,4,4,4,4,4,4,3],
                [2,3,3,3,3,3,3,2]
    ]

def display():
    "Display the whole game grid"
    global grid
    print "Game Grid"
    for i in range(8):
        for j in range(8):
            if grid[i][j][0]==0 and grid[i][j][1]==0:
                print "_",
            else:
                if grid[i][j][1]==0:
                    print grid[i][j][0]*"R",
                else:
                    print grid[i][j][1]*"G",
        print
    print

def winner():
    "Check if any player won the game"
    global grid
    sg=0
    sr=0
    for i in range(8):
        for j in range(8):
            sr+=grid[i][j][0]
            sg+=grid[i][j][1]
            if sr*sg>0:
                return 0
    return 1

def chain_reaction(i,j,p,t=0):
    "Splits the current cell elements to neighbouring elements"
    if i<0 or i>7 or j<0 or j>7:
        return
    global grid
    if t==0:
        grid[i][j][p]=0
    else:
        grid[i][j][p]+=1
        grid[i][j][(p+1)%2]=0
    if grid[i][j][p]==free_dir_grid[i][j]:
        chain_reaction(i,j,p)
    if t==0:
        chain_reaction(i-1,j,p,1)
        chain_reaction(i,j-1,p,1)
        chain_reaction(i,j+1,p,1)
        chain_reaction(i+1,j,p,1)
    
        
if __name__=="__main__":
    i=0
    player=["Red","Green"]
    turns=0
    print "Welcome to chain reation game"
    display()
    while True:
        x,y=map(int,raw_input("It's player "+player[i]+"'s move: ").split())
        if x<0 or y<0:
            break
        if x>7 or y>7:
            print "Invalid cell "
            continue
        if grid[x][y][(i+1)%2]!=0: #if opponent has already occupied the cell
            print "Try other cell "
            continue
        grid[x][y][i]+=1
        display()
        if grid[x][y][i]==free_dir_grid[x][y]: #Cell needs to be split
            chain_reaction(x,y,i)
            display()
        if turns==2:
            if winner():        #Check if any player won
                print player[i]+ " won the game"
                break
        if turns<2:
            turns+=1
        #Change player in next turn
        i+=1
        i%=2
        
        
