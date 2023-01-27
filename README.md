# Python_Assignment

1. Taken n(rows) and m(columns) from the user as input and created a 2D matrix using lists.
2. For the mention problem traverse the 4 borders of the matrix and when we encounter 'O', we call DFS(Depth First Search).
3. In the DFS function, if our iterater (i,j) reaches out of bounds or we encounter 'X', simply return from it. Else change the current value to a flag value say 'A' in our case and apply DFS in all 4 adjacent sides.
4. Traverse the whole matrix and change all 'O' to 'X' and all 'A' to 'O' and we get our desired output.
