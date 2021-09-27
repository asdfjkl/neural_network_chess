import random
import chess
import math

random.seed(42)

PLAYER = chess.WHITE
OPPONENT = chess.BLACK

class TreeNode():

    def __init__(self, board):
        self.M = 0
        self.V = 0
        self.visitedMovesAndNodes = []
        self.nonVisitedLegalMoves = []
        self.board = board
        self.parent = None
        for m in self.board.legal_moves:
            self.nonVisitedLegalMoves.append(m)

    def isMCTSLeafNode(self):
        return len(self.nonVisitedLegalMoves) != 0

    def isTerminalNode(self):
        return len(self.nonVisitedLegalMoves) == 0 and len(self.visitedMovesAndNodes) == 0

def uctValue(node, parent):
    val = (node.M/node.V) + 1.4142 * math.sqrt(math.log(parent.V) / node.V)
    #print(val)
    return val

def select(node):
    if(node.isMCTSLeafNode() or node.isTerminalNode()):
        return node
    else:
        #print(node.board)
        #print(node.visitedMovesAndNodes)
        #print(node.nonVisitedLegalMoves)
        maxUctChild = None
        maxUctValue = -1000000.
        for move, child in node.visitedMovesAndNodes:
            uctValChild = uctValue(child, node)
            if(uctValChild > maxUctValue):
                maxUctChild = child
                maxUctValue = uctValChild
        if(maxUctChild == None):
            raise ValueError("could not identify child with best uct value")
        else:
            return select(maxUctChild)

def expand(node):
    moveToExpand = node.nonVisitedLegalMoves.pop()
    board = node.board.copy()
    board.push(moveToExpand)
    childNode = TreeNode(board)
    childNode.parent = node
    node.visitedMovesAndNodes.append((moveToExpand, childNode))
    return childNode

def simulate(node):
    board = node.board.copy()
    while(board.outcome(claim_draw = True) == None):
        ls = []
        for m in board.legal_moves:
            ls.append(m)
        move = random.choice(ls)
        board.push(move)
    #print("---------------start-----------")
    #print(board)
    payout = 0.5
    o = board.outcome(claim_draw = True)
    #print("winner: " + str(o.winner))
    #print()
    if(o.winner == PLAYER):
        payout = 1
    if(o.winner == OPPONENT):
        payout = 0.5
    if(o.winner == None):
        payout = 0

    return payout

def backpropagate(node, payout):
    #node.M = ((node.M * node.V) + payout) / (node.V + 1)
    node.M = node.M + payout
    node.V = node.V + 1
    # not at the root node yet
    if(node.parent != None):
        return backpropagate(node.parent, payout)


import chess

board = chess.Board()

"""
board.push_uci("e2e4")
board.push_uci("e7e5")
board.push_uci("f1c4")
board.push_uci("d7d6")
board.push_uci("d1h5")
board.push_uci("g8f6")
"""

board.push_uci("e2e4")
board.push_uci("e7e6")
board.push_uci("d2d4")
board.push_uci("d7d5")
board.push_uci("b1c3")
board.push_uci("g8f6")
board.push_uci("e4e5")
board.push_uci("f6d7")
board.push_uci("g1f3")
board.push_uci("f8b4")
board.push_uci("f1d3")
board.push_uci("e8g8")

root = TreeNode(board)

print(len(root.nonVisitedLegalMoves))

for i in range(0,5000):
    if(i%10 == 0):
        print(i)
    if(i%100 == 0):
        for move, child in root.visitedMovesAndNodes:
            print("move: "+str(move)+" "+str(child.M)+ ", "+str(child.V))
    node = select(root)
    # if the selected node is a terminal, we cannot expand
    # any child node. in this case, count this as a win/draw/loss
    if(not node.isTerminalNode()):
        node = expand(node)
    payout = simulate(node)
    backpropagate(node, payout)

print(root.M)
print(root.V)

for move, child in root.visitedMovesAndNodes:
    print("move: "+str(move)+" "+str(child.M)+ ", "+str(child.V))

