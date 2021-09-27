from HexapawnZero.common.game import Board
from HexapawnZero.minimax.minimax import minimax
import copy
import numpy as np

def getBestMoveRes(board):
    bestMove = None
    bestVal = 1000000000
    if(board.turn == board.WHITE):
        bestVal = -1000000000
    for m in board.generateMoves():
        tmp = copy.deepcopy(board)
        tmp.applyMove(m)
        mVal = minimax(tmp, 30, tmp.turn == board.WHITE)
        if(board.turn == board.WHITE and mVal > bestVal):
            bestVal = mVal
            bestMove = m
        if(board.turn == board.BLACK and mVal < bestVal):
            bestVal = mVal
            bestMove = m
    return bestMove, bestVal

positions = []
moveProbs = []
outcomes = []

terminals = []

def visitNodes(board):
    term, _ = board.isTerminal()
    if(term):
        terminals.append(1)
        return
    else:
        bestMove, bestVal = getBestMoveRes(board)
        positions.append(board.toNetworkInput())
        moveProb = [ 0 for x in range(0,28) ]
        idx = board.getNetworkOutputIndex(bestMove)
        moveProb[idx] = 1
        moveProbs.append(moveProb)
        if(bestVal > 0):
            outcomes.append(1)
        if(bestVal == 0):
            outcomes.append(0)
        if(bestVal < 0):
            outcomes.append(-1)
        for m in board.generateMoves():
            next = copy.deepcopy(board)
            next.applyMove(m)
            visitNodes(next)

board = Board()
board.setStartingPosition()
visitNodes(board)

np.save("positions", np.array(positions))
np.save("moveprobs", np.array(moveProbs))
np.save("outcomes", np.array(outcomes))
