def minimax(board, player):
    win = winner(board)
    if win == AI: return (1, None)
    if win == HUMAN: return (-1, None)
    moves = available_moves(board)
    if not moves: return (0, None)

    if player == AI:
        best = (-math.inf, None)
        for m in moves:
            board[m] = AI
            score,_ = minimax(board, HUMAN)
            board[m] = EMPTY
            if score > best[0]: best = (score, m)
        return best
    else:
        best = (math.inf, None)
        for m in moves:
            board[m] = HUMAN
            score,_ = minimax(board, AI)
            board[m] = EMPTY
            if score < best[0]: best = (score, m)
        return best
