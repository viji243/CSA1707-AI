def alphabeta(board, player, alpha=-math.inf, beta=math.inf):
    win = winner(board)
    if win == AI: return (1, None)
    if win == HUMAN: return (-1, None)
    moves = available_moves(board)
    if not moves: return (0, None)

    if player == AI:
        best = (-math.inf, None)
        for m in moves:
            board[m] = AI
            score,_ = alphabeta(board, HUMAN, alpha, beta)
            board[m] = EMPTY
            if score > best[0]: best = (score, m)
            alpha = max(alpha, best[0])
            if beta <= alpha: break
        return best
    else:
        best = (math.inf, None)
        for m in moves:
            board[m] = HUMAN
            score,_ = alphabeta(board, AI, alpha, beta)
            board[m] = EMPTY
            if score < best[0]: best = (score, m)
            beta = min(beta, best[0])
            if beta <= alpha: break
        return best
