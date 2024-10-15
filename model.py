import math
import random

class Layer:
    num_of_layers = 0
    def __init__(self, input_size, output_size, name="Layer" + str(num_of_layers)):
        Layer.num_of_layers += 1
        self.weights = [[random.random() for x in range(output_size)] for y in range(input_size)]
        self.input_size = input_size
        self.output_size = output_size
        self.last_forward_input = []
        self.last_forward_out = []
        self.delta = [0 for i in range(input_size)]

    def forward(self, data):
        if len(data) != len(self.weights):
            assert "Wrong input size"

        out_percept = [[data[i] * self.weights[i][j] for i in range(self.input_size)] for j in range(self.output_size)]
        out = [sum(out_percept[i]) for i in range(self.output_size)]
        self.last_forward_input = data
        self.last_forward_out = data
        return out

    def backward(self, input):
        for i in range(self.input_size):
            y_k = self.last_forward_out[i]
            summ = sum([input[j] * self.weights[i][j] for j in range(self.output_size)])
            self.delta[i] = y_k * (1 - y_k) * summ

        return self.delta

    def step(self, delta, alpha):
        for output in range(self.output_size):
            for input in range(self.input_size):
                self.weights[input][output] += alpha * delta[output] * self.last_forward_input[input]
        return self.delta



def activation_sigmoid(layer):
    return [1/(1 + (math.e ** (-x))) for x in layer]

def find_loss(out_wait, out_actual):
    return sum([abs(out_wait[i] - out_actual[i]) for i in range(len(out_wait))])/2

class Model:
    def __init__(self, num_layers, layers_with, lr):
        super().__init__()

        self.num_layers = num_layers
        self.layers = []
        self.lr = lr
        self.last_result = None

        for i in range(num_layers + 1):
            if i == 0:
                self.layers.append(Layer(7 * 7, layers_with[i]))
            elif i == num_layers:
                self.layers.append((Layer(layers_with[i - 1], 3)))
            else:
                self.layers.append((Layer(layers_with[i - 1], layers_with[i])))

    def forward(self, data):
        tmp = data
        for layer in self.layers:
            tmp = activation_sigmoid(layer.forward(tmp))
        self.last_result = tmp
        return tmp

    def backward(self, expected, e):
        alpha = 2 * abs(e) / 3
        tmp = [0, 0, 0]

        for i in range(3):
            t = expected[i]
            y = self.last_result[i]
            tmp[i] = y * (1 - y) * (t - y)

        for layer in reversed(self.layers):
            tmp = layer.backward(tmp)

        for layer in self.layers:
            tmp = layer.step(tmp, alpha)
