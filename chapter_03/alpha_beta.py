import chess

# P = 100
# N = 310
# B = 320
# R = 500
# Q = 900

# position table
pieceSquareTable = [
  [ -50,-40,-30,-30,-30,-30,-40,-50 ],
  [ -40,-20,  0,  0,  0,  0,-20,-40 ],
  [ -30,  0, 10, 15, 15, 10,  0,-30 ],
  [ -30,  5, 15, 20, 20, 15,  5,-30 ],
  [ -30,  0, 15, 20, 20, 15,  0,-30 ],
  [ -30,  5, 10, 15, 15, 10,  5,-30 ],
  [ -40,-20,  0,  5,  5,  0,-20,-40 ],
  [ -50,-40,-30,-30,-30,-30,-40,-50 ] ]


def eval(board):
    scoreWhite = 0
    scoreBlack = 0
    for i in range(0,8):
        for j in range(0,8):
            squareIJ = chess.square(i,j)
            pieceIJ = board.piece_at(squareIJ)
            if str(pieceIJ) == "P":
                scoreWhite += (100 + pieceSquareTable[i][j])
            if str(pieceIJ) == "N":
                scoreWhite += (310 + pieceSquareTable[i][j])
            if str(pieceIJ) == "B":
                scoreWhite += (320 + pieceSquareTable[i][j])
            if str(pieceIJ) == "R":
                scoreWhite += (500 + pieceSquareTable[i][j])
            if str(pieceIJ) == "Q":
                scoreWhite += (900 + pieceSquareTable[i][j])
            if str(pieceIJ) == "p":
                scoreBlack += (100 + pieceSquareTable[i][j])
            if str(pieceIJ) == "n":
                scoreBlack += (310 + pieceSquareTable[i][j])
            if str(pieceIJ) == "b":
                scoreBlack += (320 + pieceSquareTable[i][j])
            if str(pieceIJ) == "r":
                scoreBlack += (500 + pieceSquareTable[i][j])
            if str(pieceIJ) == "q":
                scoreBlack += (900 + pieceSquareTable[i][j])
    return scoreWhite - scoreBlack

"""
function alphabeta(node, depth, α, β, maximizingPlayer) is
    if depth = 0 or node is a terminal node then
        return the heuristic value of node
    if maximizingPlayer then
        value := −∞
        for each child of node do
            value := max(value, alphabeta(child, depth − 1, α, β, FALSE))
            α := max(α, value)
            if α ≥ β then
                break (* β cutoff *)
        return value
    else
        value := +∞
        for each child of node do
            value := min(value, alphabeta(child, depth − 1, α, β, TRUE))
            β := min(β, value)
            if β ≤ α then
                break (* α cutoff *)
        return value
"""

NODECOUNT = 0

def alphaBeta(board, depth, alpha, beta, maximize):
    global NODECOUNT
    if(board.is_checkmate()):
        if(board.turn == chess.WHITE):
            return -100000
        else:
            return 1000000
    if depth == 0:
        return eval(board)
    legals = board.legal_moves
    if(maximize):
        bestVal = -9999
        for move in legals:
            board.push(move)
            NODECOUNT += 1
            bestVal = max(bestVal, alphaBeta(board, depth-1, alpha, beta, (not maximize)))
            board.pop()
            alpha = max(alpha, bestVal)
            if alpha >= beta:
                return bestVal
        return bestVal
    else:
        bestVal = 9999
        for move in legals:
            board.push(move)
            NODECOUNT += 1
            bestVal = min(bestVal, alphaBeta(board, depth - 1, alpha, beta, (not maximize)))
            board.pop()
            beta = min(beta, bestVal)
            if beta <= alpha:
                return bestVal
        return bestVal


def getNextMove(depth, board, maximize):

    legals = board.legal_moves
    bestMove = None
    bestValue = -9999
    if(not maximize):
        bestValue = 9999
    for move in legals:
        board.push(move)
        value = alphaBeta(board, depth-1, -10000, 10000, (not maximize))
        board.pop()
        if maximize:
            if value > bestValue:
                bestValue = value
                bestMove = move
        else:
            if value < bestValue:
                bestValue = value
                bestMove = move
    return (bestMove, bestValue)



#board = chess.Board("rnbqkbnr/1p1p1pp1/2p4p/p3p1N1/2B1P3/8/PPPP1PPP/RNBQK2R w KQkq - 0 5")
board = chess.Board()

#print(getNextMove(4, board, True))
board.push_san("e4")
board.push_san("e5")
board.push_san("Qh5")
board.push_san("Nc6")
board.push_san("Bc4")
board.push_san("Nf6")
print(getNextMove(4, board, True))
print(NODECOUNT)


"""
print(board)
print("white, initial")
print(eval(board))

board.push(chess.Move.from_uci("g1f3"))
print("black initial")
print(eval(board))

board.push(chess.Move.from_uci("e7e5"))
print("white after e7e5")
print(eval(board))


board.push(chess.Move.from_uci("e2e4"))
print(eval(board))
"""