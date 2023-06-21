import numpy as np

input_neurons = 2
output_neurons = 2
hidden_layer_neurons = 4
iterations = 6000

input = np.random.randint(1, 5, input_neurons)
output = np.array([1, 0])

hidden_weights = np.random.rand(input_neurons, hidden_layer_neurons)
output_weights = np.random.rand(hidden_layer_neurons, output_neurons)
hidden_bias = np.random.rand(1, hidden_layer_neurons)
output_bias = np.random.rand(1, output_neurons)


def sigmoid(li):
    return 1 / (1 + np.exp(-li))


def gradient(li):
    return li * (1 - li)


for i in range(iterations):
    hidden_layer = np.dot(input, hidden_weights)
    hidden_layer = sigmoid(hidden_bias + hidden_layer)

    output_layer = np.dot(hidden_layer, output_weights)
    output_layer = sigmoid(output_bias + output_layer)

    error = output - output_layer

    error_output = gradient(output_layer) * error
    error_hidden = gradient(hidden_layer) * np.dot(error_output, output_weights.T)

    gradient_hidden = np.dot(input.reshape(input_neurons, 1), error_hidden.reshape(1, hidden_layer_neurons))
    gradient_output = np.dot(hidden_layer.reshape(hidden_layer_neurons, 1), error_output.reshape(1, output_neurons))

    output_weights += gradient_output * 0.05
    hidden_weights += gradient_hidden * 0.05

    if i < 50 or i > iterations - 50:
        print(f'Iterations {i}: {error}\nOutput: {output_layer}')
