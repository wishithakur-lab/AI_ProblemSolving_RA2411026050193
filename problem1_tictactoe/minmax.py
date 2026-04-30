nodes_explored = 0

def check_winner(board):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    
    for i,j,k in wins:
        if board[i] == board[j] == board[k] and board[i] != "":
            return board[i]
    return None

def minimax(board, isMax):
    global nodes_explored
    nodes_explored += 1

    winner = check_winner(board)
    if winner == "O": return 1
    if winner == "X": return -1
    if "" not in board: return 0

    if isMax:
        best = -100
        for i in range(9):
            if board[i] == "":
                board[i] = "O"
                best = max(best, minimax(board, False))
                board[i] = ""
        return best
    else:
        best = 100
        for i in range(9):
            if board[i] == "":
                board[i] = "X"
                best = min(best, minimax(board, True))
                board[i] = ""
        return best
