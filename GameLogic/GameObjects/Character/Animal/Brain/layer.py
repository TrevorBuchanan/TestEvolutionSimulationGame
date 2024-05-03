import math
import random
import numpy as np


def activation_function(weighted_input):
    # np.clip to avoid overflow issues
    clipped_input = np.clip(weighted_input, -500, 500)
    return 1 / (1 + np.exp(-clipped_input))


class Layer:
    def __init__(self, input_amount, output_amount):
        self.numInputs = input_amount
        self.numOutputs = output_amount

        # Initialize weights and biases using NumPy
        self.weights = np.random.uniform(-1, 1, (input_amount, output_amount)) / np.sqrt(input_amount)
        self.biases = np.zeros(output_amount)

    def get_layer_outputs(self, inputs):
        """
        Get list of outputs after running inputs through weights and biases in layer and set layers inputs and outputs
        :param inputs: List (of length self.input_amount) of numbers
        :return: List of output numbers having run through layer and activation function
        """
        # Convert inputs to a numpy array if not already
        inputs = np.array(inputs)

        # Efficient matrix multiplication + bias addition
        weighted_input = np.dot(inputs, self.weights) + self.biases

        # Apply the activation function
        activated_outputs = activation_function(weighted_input)

        return activated_outputs
