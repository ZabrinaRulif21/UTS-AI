import numpy as np

inputs = [3.2, 3.4, 3.6, 3.8, 4.0, 4.2, 4.4, 4.6, 4.8, 5.0]
weights = [
    [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 2.0],
    [2.3, 1.3, 3.3, 4.3, 5.3, 7.3, 6.3, 9.3, 8.3, 0.3],
    [1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0],
    [2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0],
    [0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.5, 1.7, 1.9],
]

biases = [0.4, 1.3, 2.3, 3.5, 6.1]

outputs = np.dot(weights, inputs) + biases
print(outputs)