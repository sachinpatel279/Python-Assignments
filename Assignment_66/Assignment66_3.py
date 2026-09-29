import math

# Actual and predicted values
actual = [3, -0.5, 2, 7]
predicted = [2.5, 0.0, 2, 8]    

# Calculate Mean Squared Error (MSE)
def mean_squared_error(actual, predicted):
    total_error = 0

    for i in range(len(actual)):
        error = actual[i] - predicted[i]
        total_error += error ** 2
        mse = total_error / len(actual)
    return mse

# Binary Cross-Entropy 
def binary_cross_entropy(actual, predicted):
    total_loss = 0
    epsilon = 1e-15

    for i in range(len(actual)):
        p = max(epsilon, min(1 - epsilon, predicted[i]))

        loss = -(actual[i] * math.log(p) +
                 (1 - actual[i]) * math.log(1 - p))

        total_loss += loss
        bce = total_loss / len(actual)
    return bce

#calculate losses
mse = mean_squared_error(actual, predicted)
bce = binary_cross_entropy(actual, predicted)

print("Mean Squared Error (MSE) :", mse)
print("Binary Cross-Entropy (BCE) :", bce)
