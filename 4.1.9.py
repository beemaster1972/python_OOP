class Layer:

    def __init__(self):
        self.next_layer = None
        self.name = 'Layer'

    def __call__(self, next_layer):
        self.next_layer = next_layer
        return self.next_layer

    def __repr__(self):
        params = [str(val) for key, val in self.__dict__.items() if key not in ['name', 'next_layer']]
        return f'{self.name}({",".join(params)})'


class Input(Layer):

    def __init__(self, inputs):
        super().__init__()
        self.name = 'Input'
        self.inputs = inputs


class Dense(Layer):

    def __init__(self, inputs, outputs, activation):
        super().__init__()
        self.name = 'Dense'
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation


class NetworkIterator(Layer):

    def __init__(self, top):
        self.layer = Layer()
        self.layer.next_layer = self.layer(top)

    def __iter__(self):
        return self

    def __next__(self):
        self.layer = self.layer.next_layer
        if self.layer is None:
            raise StopIteration
        return self.layer



if __name__ == '__main__':
    network = Input(128)
    layer = network(Dense(network.inputs, 1024, 'linear'))
    layer = layer(Dense(layer.inputs, 10, 'softmax'))
    for x in NetworkIterator(network):
        print(x)