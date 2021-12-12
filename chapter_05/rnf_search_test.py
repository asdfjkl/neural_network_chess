import keras
from common.game import Board
from mcts import Edge, Node, MCTS
import numpy as np
np.set_printoptions(precision=3, suppress=True)

model = keras.models.load_model("model_it10.keras")

mctsSearcher = MCTS(model)
g = Board()
g.setStartingPosition()
rootEdge = Edge(None, None)
rootEdge.N = 1
root = Node(g, rootEdge)
probs = mctsSearcher.search(root)
print(probs)
print(model.predict([g.toNetworkInput()])[0][0])