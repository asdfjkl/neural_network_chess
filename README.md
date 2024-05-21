# Neural Networks For Chess

![cover](https://raw.githubusercontent.com/asdfjkl/neural_network_chess/main/cover_single_graphic.png?token=AADBBS6WSERHTN4OIH7GGP3BKLJWE)

# Free Book

- Grab your free PDF copy [HERE](https://github.com/asdfjkl/neural_network_chess/releases)
- Buy a printed copy at [HERE](https://www.amazon.de/dp/B09HFXFSBV) or [HERE](https://www.amazon.com/-/de/dp/B09HFXFSBV/)

Donations are welcome: 

[![paypal](https://www.paypalobjects.com/en_US/DK/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/donate?hosted_button_id=9K2JDF5YBDZT6)

If you like the book, a review on [Amazon](https://www.amazon.de/dp/B09HFXFSBV) is also highly appreciated.

# Contact

- You can contact me via firstname <-> dot <-> lastname <-> outlook <-> com
- Please don't write to random strangers with the name "Dominik Klein" :-)

# Contents

AlphaZero, Leela Chess Zero and Stockfish NNUE revolutionized Computer Chess. This book 
gives a complete introduction into the technical inner workings of such engines. 

The book is split into four main chapters - excluding chapter 1 (introduction) and chapter 6 (conclusion):

- Chapter 2 introduces neural networks and covers all the basic building blocks that 
are used to build deep networks such as those used by AlphaZero. Contents include the perceptron, back-propagation and gradient descent, classification, regression, multilayer perceptron, vectorization techniques, convolutional networks, squeeze and excitation networks, fully connected networks, batch normalization and rectified linear units, residual layers, overfitting and underfitting.

- Chapter 3 introduces classical search techniques used for chess engines as well as those used by AlphaZero. Contents include minimax, alpha-beta search, and Monte Carlo tree search.
  
- Chapter 4 shows how modern chess engines are designed. Aside from the ground-breaking AlphaGo, AlphaGo Zero and AlphaZero we cover Leela Chess Zero, Fat Fritz, Fat Fritz 2 and Efficiently Updatable Neural Networks (NNUE) as well as Maia.

- Chapter 5 is about implementing a miniaturized AlphaZero. Hexapawn, a minimalistic version of chess, is used as an example for that. Hexapawn is solved by minimax search and training positions for supervised learning are generated. Then as a comparison, an AlphaZero-like training loop is implemented where training is done via self-play combined with reinforcement learning. Finally, AlphaZero-like training and supervised training are compared.

# Source Code

Just clone this repository or directly browse the files. You will find here all sources of the examples of the book.

Several users contacted me as they have problems setting up their python environment. I highly suggest to use Ubuntu 20.04. The examples do not require much computation power, i.e. you can also install a virtual machine. First install `git`, then install `numpy` and `pip` via `apt`, and finally install `TensorFlow`, `scikit-image`, `matplotlib`, `python-chess`, `tqdm` via `pip`. You can do so by opening a terminal and running the following commands.

````
sudo apt install python3 git python3-numpy python3-pip
pip3 install --user --upgrade TensorFlow
pip3 install --user --upgrade scikit-image
pip3 install --user --upgrade matplotlib
pip3 install --user --upgrade python-chess
pip3 install --user --upgrade tqdm
git clone https://github.com/asdfjkl/neural_network_chess.git
````
Note: The examples on the book use [keras](https://keras.io/) with [tensorflow](https://www.tensorflow.org) as the backend. For those who prefer pytorch, there is port for Chapter 5 [here](https://github.com/ppeloton/neural_network_chess_pytorch)

# About

During COVID, I worked a lot from home and saved approximately 1.5 hours of commuting time each day. I decided to use that time to do something useful (?) and wrote a book about computer chess. In the end I decided to release the book for free.

# Profits

To be completely transparent, here is what I make from every paper copy sold on Amazon. The book retails for $16.95 (about 15 Euro).

- printing costs $4.04
- Amazon takes $6.78
- my royalties are $6.13

# Errata

If you find mistakes, please report them [here](https://github.com/asdfjkl/neural_network_chess/issues/1) - your help is appreciated!
