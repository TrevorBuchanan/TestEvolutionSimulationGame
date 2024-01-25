import math
import random


def activation_function(weighted_input):
    if weighted_input > 500:
        return 1
    if weighted_input < -500:
        return 0

    return 1 / (1 + (math.e ** -weighted_input))


class Layer:
    def __init__(self, input_amount, output_amount):
        # Layer input and output amount
        self.numInputs = input_amount
        self.numOutputs = output_amount

        # Activated_output (changed for each pass through)
        self.activated_outputs = [0 for _ in range(output_amount)]

        # Weights and biases
        self.weights = [[random.uniform(-1, 1) / (input_amount ** 0.5)
                         for _ in range(output_amount)] for _ in range(input_amount)]
        self.biases = [0 for _ in range(output_amount)]

    def get_layer_outputs(self, inputs):
        """
        Get list of outputs after running inputs through weights and biases in layer and set layers inputs and outputs
        :param inputs: List (of length self.input_amount) of numbers
        :return: List of output numbers having run through layer and activation function
        """
        for out_index in range(self.numOutputs):
            weighted_input = self.biases[out_index]
            for in_index in range(self.numInputs):
                weighted_input += inputs[in_index] * self.weights[in_index][out_index]
            self.activated_outputs[out_index] = activation_function(weighted_input)
        return self.activated_outputs
