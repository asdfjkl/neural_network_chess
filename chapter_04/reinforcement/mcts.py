import copy
import numpy as np
import math
from HexapawnZero.common.game import Board
import random

class Edge():
    def __init__(self, move, parentNode):
        self.parentNode = parentNode
        self.move = move
        self.N = 0
        self.W = 0
        self.Q = 0
        self.P = 0

class Node():
    def __init__(self, board, parentEdge):
        self.board = board
        self.parentEdge = parentEdge
        self.childEdgeNode = []

    def expand(self, network):
        moves = self.board.generateMoves()
        for m in moves:
            child_board = copy.deepcopy(self.board)
            child_board.applyMove(m)
            child_edge = Edge(m, self)
            childNode = Node(child_board, child_edge)
            self.childEdgeNode.append((child_edge,childNode))
        q = network.predict(np.array([self.board.toNetworkInput()]))
        prob_sum = 0.
        for (edge,_) in self.childEdgeNode:
            m_idx = self.board.getNetworkOutputIndex(edge.move)
            edge.P = q[0][0][m_idx]
            prob_sum += edge.P
        for edge,_ in self.childEdgeNode:
            edge.P /= prob_sum
        v = q[1][0][0]
        return v

    def isLeaf(self):
        return self.childEdgeNode == []

class MCTS():

    def __init__(self, network):
        self.network = network
        self.rootNode = None
        self.tau = 1.0
        self.c_puct = 1.0

    def uctValue(self, edge, parentN):
        return self.c_puct * edge.P * (math.sqrt(parentN) / (1+edge.N))

    def select(self, node):
        if(node.isLeaf()):
            return node
        else:
            maxUctChild = None
            maxUctValue = -100000000.
            for edge, child_node in node.childEdgeNode:
                uctVal = self.uctValue(edge, edge.parentNode.parentEdge.N)
                val = edge.Q
                if(edge.parentNode.board.turn == Board.BLACK):
                    val = -edge.Q
                uctValChild = val + uctVal
                if(uctValChild > maxUctValue):
                    maxUctChild = child_node
                    maxUctValue = uctValChild
            allBestChilds = []
            for edge, child_node in node.childEdgeNode:
                uctVal = self.uctValue(edge, edge.parentNode.parentEdge.N)
                val = edge.Q
                if(edge.parentNode.board.turn == Board.BLACK):
                    val = -edge.Q
                uctValChild = val + uctVal
                if(uctValChild == maxUctValue):
                    allBestChilds.append(child_node)
            if(maxUctChild == None):
                raise ValueError("could not identify child with best uct value")
            else:
                if(len(allBestChilds) > 1):
                    idx = random.randint(0, len(allBestChilds)-1)
                    return self.select(allBestChilds[idx])
                else:
                    return self.select(maxUctChild)

    def expandAndEvaluate(self, node):
        terminal, winner = node.board.isTerminal()
        if(terminal == True):
            v = 0.0
            if(winner == Board.WHITE):
                v = 1.0
            if(winner == Board.BLACK):
                v = -1.0
            if(winner == Board.DRAW):
                v = 0.0
            self.backup(v, node.parentEdge)
            return
        v = node.expand(self.network)
        self.backup(v, node.parentEdge)

    def backup(self, v, edge):
        edge.N += 1
        edge.W = edge.W + v
        edge.Q = edge.W / edge.N
        if(edge.parentNode != None):
            if(edge.parentNode.parentEdge != None):
                self.backup(v, edge.parentNode.parentEdge)

    def search(self, rootNode):
        self.rootNode = rootNode
        _ = self.rootNode.expand(self.network)
        for i in range(0,100):
            selected_node = self.select(rootNode)
            self.expandAndEvaluate(selected_node)
        N_sum = 0
        moveProbs = []
        for edge, _ in rootNode.childEdgeNode:
            N_sum += edge.N
        for (edge, node) in rootNode.childEdgeNode:
            prob = (edge.N ** (1 / self.tau)) / ((N_sum) ** (1/self.tau))
            moveProbs.append((edge.move, prob, edge.N, edge.Q))
        return moveProbs

