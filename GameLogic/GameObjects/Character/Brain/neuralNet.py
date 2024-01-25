from GameLogic.GameObjects.Character.Brain.layer import Layer


class NeuralNet:

    def __init__(self, layer_sizes, min_max_inputs):
        """
        List of layers
        :param layer_sizes: List of integers for each layer size (all must be positive and non-zero)
        :param min_max_inputs: List of tuples holding minimum and maximum values for each initial input node
        """
        self.layers = self.create_layers(layer_sizes)
        self.min_max_inputs = min_max_inputs

    @staticmethod
    def create_layers(layer_sizes):
        """
        Creates layers according to layer sizes
        :param layer_sizes: List of integers defining the layer sizes
        :return: A List of Layers
        """
        layers = []
        # Loop through layers and add layer to layers list
        for i in range(len(layer_sizes) - 1):
            layers.append(Layer(layer_sizes[i], layer_sizes[i + 1]))
        return layers

    def normalize_inputs(self, inputs):
        """
        Normalizes input to workable range
        :param inputs: List of inputs
        :return: Normalized (scaled) inputs
        """
        normalized_inputs = []
        # Loop through each value and normalize inputs to between 0 and 1
        for input_node_val, min_max in zip(inputs, self.min_max_inputs):
            if isinstance(input_node_val, bool):
                if input_node_val:
                    normalized_inputs.append(1.0)
                else:
                    normalized_inputs.append(0.0)
            else:
                normalized = (input_node_val - min_max[0]) / (min_max[1] - min_max[0])
                normalized_inputs.append(normalized)
        return normalized_inputs

    def get_outputs(self, inputs):
        """
        Runs inputs through all layers in the neural network
        :param inputs: List of inputs (Must be same size as first layer in the neural network)
        :return: List of outputs from neural network
        """
        inputs = self.normalize_inputs(inputs)
        if self.layers[0].numInputs == len(inputs):
            # Forward propagate through network
            for one_layer in self.layers:
                inputs = one_layer.get_layer_outputs(inputs)
        else:
            raise Exception("Incorrectly sized input for neural network")
        return inputs

    # def learn(self, training_data, learn_rate):
    #    pass
