import keras
from common.game import Board
import random
import numpy as np

model = keras.models.load_model("model_it10.keras")
#model = keras.models.load_model("common/random_model.keras")

def fst(a):
    return a[0]

# white == random player
# black == network
def net_vs_rand(board):
    record = []
    while(not fst(board.isTerminal())):
        if(board.turn == Board.WHITE):
            moves = board.generateMoves()
            m = moves[random.randint(0, len(moves)-1)]
            board.applyMove(m)
            record.append(m)
            continue
        else:
            q = model.predict(np.array([board.toNetworkInput()]))
            masked_output = [ 0 for x in range(0,28)]
            for m in board.generateMoves():
                m_idx = board.getNetworkOutputIndex(m)
                masked_output[m_idx] = q[0][0][m_idx]
            best_idx = np.argmax(masked_output)
            sel_move = None
            for m in board.generateMoves():
                m_idx = board.getNetworkOutputIndex(m)
                if(best_idx == m_idx):
                    sel_move = m
            board.applyMove(sel_move)
            record.append(sel_move)
            continue
    terminal, winner = board.isTerminal()
    return winner

# white random player
# black random player
def rand_vs_rand(board):
    while(not fst(board.isTerminal())):
        moves = board.generateMoves()
        m = moves[random.randint(0, len(moves)-1)]
        board.applyMove(m)
        continue
    terminal, winner = board.isTerminal()
    return winner


whiteWins = 0
blackWins = 0

for i in range(0,100):
    board = Board()
    board.setStartingPosition()
    moves = board.generateMoves()
    m = moves[random.randint(0, len(moves)-1)]
    board.applyMove(m)
    winner = net_vs_rand(board)
    if(winner == Board.WHITE):
        whiteWins += 1
    if(winner == Board.BLACK):
        blackWins += 1

all = whiteWins + blackWins
print("Rand Network vs Reinforcement: "+str(whiteWins/all) + "/"+str(blackWins/all))


whiteWins = 0
blackWins = 0

for i in range(0,100):
    board = Board()
    board.setStartingPosition()
    moves = board.generateMoves()
    m = moves[random.randint(0, len(moves)-1)]
    board.applyMove(m)
    winner = rand_vs_rand(board)
    if(winner == Board.WHITE):
        whiteWins += 1
    if(winner == Board.BLACK):
        blackWins += 1

all = whiteWins + blackWins
print("Rand vs Rand Network: "+str(whiteWins/all) + "/"+str(blackWins/all))