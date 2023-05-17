import math
import random

# our network:
#
#  x0 ---w0---|
#  x1 ---w1---v--sigmoid->
#  x2 ---w2---|
#
# where x0 = 1 is the bias

# the weights of the first (and only) layer
weights = [ 1., 2., 3.]
# the output node
v = 0.

# sigmoid function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def forward_pass(inputs):
    # v = 1 * w0 + x1 * w1 + x2 * w2
    v_ = 1 * weights[0] + inputs[0] * weights[1] + inputs[1] * weights[2]
    return sigmoid(v_)

def error_func(x,y):
    return (x-y) ** 2

def total_error(train_data):
    # to measure the total error, we
    # sum up over all training examples
    # and take the mean of the squared errors
    err = 0.
    for train_in, train_res in train_data:
        net_out = forward_pass(train_in)
        err += error_func(train_res, net_out)
    return err / len(train_data)

# training data for AND
# ([x1, x2], expected result)
train_data_and = [
    ([ 0, 0 ], 0.),
    ([ 0, 1 ], 0.),
    ([ 1, 0 ], 0.),
    ([ 1, 1 ], 1.)
]

# current network outputs and error value for the example (1,0)
out = forward_pass(train_data_and[2][0])
print("network output for (1,0)")
print(out)
print("error value for (1,0)")
print(error_func(out, train_data_and[2][1]))

# current network outputs and error value for the example (1,1)
out = forward_pass(train_data_and[3][0])
print("network output for (1,1)")
print(out)
print("error value for (1,1)")
print(error_func(out, train_data_and[3][1]))

def train_by_gradient_descent(train_data):
    train_in, train_res = train_data

    # first calculate the network output for the example
    net_out = forward_pass(train_in)

    # we now need to update the weights w0 (=bias weight), w1 and w2
    # i.e. we have to compute the partial derivatives using the chain rule
    # a) ∂_err/ ∂_w0 = ∂_err/ ∂_out * ∂_out/ ∂_net *  ∂_net/ ∂_w0
    # b) ∂_err/ ∂_w1 = ∂_err/ ∂_out * ∂_out/ ∂_net *  ∂_net/ ∂_w1
    # c) ∂_err/ ∂_w2 = ∂_err/ ∂_out * ∂_out/ ∂_net *  ∂_net/ ∂_w2

    # ∂_err/ ∂_out = 2 * ((train_res - net_out) ** (2 - 1)) * -1
    #                technically we can define the error function as 1/2 * error_func
    #                so that the 2 cancels out when computing the derivative, but let's
    #                keep it here for fun
    err_out = -2*(train_res - net_out)

    # ∂_out/ ∂_net = out * (1 - out)
    out_net = net_out * (1 - net_out)

    # ∂_net/ ∂_w0 = x0 = 1
    # ∂_net/ ∂_w1 = x1
    # ∂_net/ ∂_w2 = x2
    net_w0 = 1
    net_w1 = train_in[0]
    net_w2 = train_in[1]

    # multiply to get the actual derivatives
    total_w0 = err_out * out_net * net_w0
    total_w1 = err_out * out_net * net_w1
    total_w2 = err_out * out_net * net_w2

    # update the weights, let's use a learning rate of 0.5
    nu = 0.5
    weights[0] = weights[0] - nu * total_w0
    weights[1] = weights[1] - nu * total_w1
    weights[2] = weights[2] - nu * total_w2

# let's train out network a few times on the four training data
for i in range(0,100):

    train_example = train_data_and[random.randint(0, 3)]
    train_by_gradient_descent(train_example)
    print("total error:")
    print(total_error(train_data_and))

print("learned weights:")
print(weights)

# current network outputs and error value for the example (1,0)
out = forward_pass(train_data_and[2][0])
print("network output for (1,0)")
print(out)
print("error value for (1,0)")
print(error_func(out, train_data_and[2][1]))

# current network outputs and error value for the example (1,1)
out = forward_pass(train_data_and[3][0])
print("network output for (1,1)")
print(out)
print("error value for (1,1)")
print(error_func(out, train_data_and[3][1]))