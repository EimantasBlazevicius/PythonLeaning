

board = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']]
print(board)
location = input()
location = str(location)
player = 'X'

var1 = 0
var2 = 0

for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == location:
            var1 = i
            var2 = j
board[var1][var2] = player

print(board)
