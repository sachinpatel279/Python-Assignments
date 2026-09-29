
import math

value = 3
weight = 0.5
bias = 1.0

target = 1
learning_rate = 0.1

# sigmoid activation function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# calculate the predicted value using the sigmoid function
weighted_sum = (value * weight) + bias
predicted = sigmoid(weighted_sum)

#calculate error
error = target - predicted

# Store old weight
old_weight = weight

# calculate gradient
gradient = (predicted - target) * predicted * (1 - predicted) * value

# update weight using gradient descent
weight = weight - learning_rate * gradient

#update bias
bias_gradient = (predicted - target) * predicted * (1 - predicted)
bias = bias - learning_rate * bias_gradient

print("Old Weight:", old_weight)
print("Updated Weight:", weight)
print("Updated Bias:", bias)
