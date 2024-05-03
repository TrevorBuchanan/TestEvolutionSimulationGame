from GameLogic.GameObjects.Character.Animal.Brain.layer import Layer
import numpy as np


class NeuralNet:
    def __init__(self, layer_sizes, min_max_inputs):
        """
        List of layers
        :param layer_sizes: List of integers for each layer size (all must be positive and non-zero)
        :param min_max_inputs: List of tuples holding minimum and maximum values for each initial input node
        """
        self.layers = [Layer(layer_sizes[i], layer_sizes[i + 1]) for i in range(len(layer_sizes) - 1)]
        self.min_max_inputs = np.array(min_max_inputs)

    def normalize_inputs(self, inputs):
        """
        Normalizes input to workable range
        :param inputs: List of inputs
        :return: Normalized (scaled) inputs
        """
        inputs = np.array(inputs, dtype=np.float64)
        min_vals = self.min_max_inputs[:, 0]
        max_vals = self.min_max_inputs[:, 1]
        return (inputs - min_vals) / (max_vals - min_vals)

    def get_outputs(self, inputs):
        """
        Runs inputs through all layers in the neural network
        :param inputs: List of inputs (Must be same size as first layer in the neural network)
        :return: List of outputs from neural network
        """
        inputs = self.normalize_inputs(inputs)
        for layer in self.layers:
            inputs = layer.get_layer_outputs(inputs)
        return inputs

    # def learn(self, training_data, learn_rate):
    #    pass
