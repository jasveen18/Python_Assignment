# Function to apply DFS on the elements at border and with char 'O' and adjacent to it
# Then changing the elements to a different value
def dfs(i,j,n,m,board):

    #Checking boundry condition
    if(i<0 or j<0 or i>=n or j>=m or board[i][j]!='O'):
        return

    board[i][j]='A'
    
    # DFS in all four directions
    dfs(i+1,j,n,m,board)
    dfs(i-1,j,n,m,board)
    dfs(i,j-1,n,m,board)
    dfs(i,j+1,n,m,board)    



# Taking the row and column input
n=int(input("Enter number of rows: ", ))
m=int(input("Enter number of columns: ", ))

board=[[] for i in range(n)]

# Taking the input of matrix
print("Enter the elements of matrix: ", )

for i in range(0,n):
    for j in range(0,m):
        str=input()
        board[i].append(str)


# DFS on first and last column
for i in range(0,n):
    dfs(i,0,n,m,board)
    dfs(i,m-1,n,m,board)

# DFS on first and last row
for j in range(0,m):
    dfs(0,j,n,m,board)
    dfs(n-1,j,n,m,board)    


# Changing the flag value 
for i in range(0,n):
    for j in range(0,m):
        if(board[i][j]=='O'):
            board[i][j]='X'

        elif(board[i][j]=='A'):
            board[i][j]='O'                


# Printing the output board
print(board)
        
        