import copy

def minimax(board, depth, maximize):
    isTerminal, winner = board.isTerminal()
    if(isTerminal):
        if(winner == board.WHITE):
            return 1000
        if(winner == board.BLACK):
            return -1000
        if(winner == board.DRAW):
            return 0
    moves = board.generateMoves()
    if(maximize):
        bestVal = -999999999999
        for move in moves:
            next = copy.deepcopy(board)
            next.applyMove(move)
            bestVal = max(bestVal, minimax(next, depth - 1, (not maximize)))
        return bestVal
    else:
        bestVal = 9999999999999
        for move in moves:
            next = copy.deepcopy(board)
            next.applyMove(move)
            bestVal = min(bestVal, minimax(next, depth - 1, (not maximize)))
        return bestVal