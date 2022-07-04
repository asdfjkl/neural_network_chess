This contains the source code for the Hexapawn example of Chapter 5.

Execute the files as follows:

- create a command prompt and change to the this directory:

# generate training data for supervised learning 
# by solving the game with minimax
python mnx_generateTrainingData.py

# train the network with supervised learning from the data
# that was created using minimax search
python sup_network.py

# evaluate the supervised network 
python sup_eval.py

# train the network using reinforcement learning
# using MCTS, i.e. in "AlphaZero-style"
python rnf_train.py

# evaluate the network that was trained 
# by reinforcement learning
python rnf_eval.py

