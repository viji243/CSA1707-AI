def check_winner(board):
    lines = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b,c in lines:
        if board[a]==board[b]==board[c] and board[a] is not None:
            return board[a]
    if all(x is not None for x in board):
        return 'Draw'
    return None

def minimax(board, player, alpha=-math.inf, beta=math.inf):
    winner = check_winner(board)
    if winner=='X': return 1, None
    if winner=='O': return -1, None
    if winner=='Draw': return 0, None
    if player=='X':
        best_val = -math.inf; best_move=None
        for i in range(9):
            if board[i] is None:
                board[i]=player
                val,_ = minimax(board, 'O', alpha, beta)
                board[i]=None
                if val>best_val:
                    best_val=val; best_move=i
                alpha = max(alpha, val)
                if beta <= alpha: break
        return best_val, best_move
    else:
        best_val = math.inf; best_move=None
        for i in range(9):
            if board[i] is None:
                board[i]=player
                val,_ = minimax(board, 'X', alpha, beta)
                board[i]=None
                if val<best_val:
                    best_val=val; best_move=i
                beta = min(beta, val)
                if beta <= alpha: break
        return best_val, best_move
