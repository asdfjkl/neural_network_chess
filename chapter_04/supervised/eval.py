import keras
from HexapawnZero.common.game import Board
import random
import numpy as np

model = keras.models.load_model("supervised_model.keras")
# Rand vs Supervised Network: 0.0/0.0/1.0
# Rand vs Rand Network: 0.59/0.0/0.41

# model = keras.models.load_model("../common/random_model.keras")
# Rand vs Supervised Network: 0.3/0.46/0.24
# Rand vs Rand Network: 0.37/0.36/0.27

def fst(a):
    return a[0]

# white == random player
# black == network
def rand_vs_net(board):
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
    #if(winner != Board.WHITE):
    #    print(record)
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
draws = 0
for i in range(0,100):
    board = Board()
    board.setStartingPosition()
    moves = board.generateMoves()
    m = moves[random.randint(0, len(moves)-1)]
    board.applyMove(m)
    winner = rand_vs_net(board)
    if(winner == Board.WHITE):
        whiteWins += 1
    if(winner == Board.BLACK):
        blackWins += 1
    if(winner == Board.DRAW):
        draws += 1
all = whiteWins + blackWins + draws
print("Rand vs Supervised Network: "+str(whiteWins/all) +"/"+str(draws/all)+ "/"+str(blackWins/all))


whiteWins = 0
blackWins = 0
draws = 0
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
    if(winner == Board.DRAW):
        draws += 1
all = whiteWins + blackWins + draws
print("Rand vs Rand Network: "+str(whiteWins/all) +"/"+str(draws/all)+ "/"+str(blackWins/all))