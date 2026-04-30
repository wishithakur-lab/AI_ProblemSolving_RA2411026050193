nodes_explored_ab = 0

def alphabeta(board, alpha, beta, isMax):
    global nodes_explored_ab
    nodes_explored_ab += 1

    from minimax import check_winner

    winner = check_winner(board)
    if winner == "O": return 1
    if winner == "X": return -1
    if "" not in board: return 0

    if isMax:
        best = -100
        for i in range(9):
            if board[i] == "":
                board[i] = "O"
                val = alphabeta(board, alpha, beta, False)
                board[i] = ""
                best = max(best, val)
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
        return best
    else:
        best = 100
        for i in range(9):
            if board[i] == "":
                board[i] = "X"
                val = alphabeta(board, alpha, beta, True)
                board[i] = ""
                best = min(best, val)
                beta = min(beta, best)
                if beta <= alpha:
                    break
        return best
