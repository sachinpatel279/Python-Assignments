
# ------------------------------------------------------------
# Assignment 3: Flatten Layer and Fully Connected Layer
# Convert 2D Matrix into 1D Vector
# Calculate Final Output Manually
# ------------------------------------------------------------

import numpy as np

# ------------------------------------------------------------
# Step 1: Create 2D Matrix
# ------------------------------------------------------------

matrix = np.array([
    [6, 4],
    [8, 6]
])

print("\nOriginal 2D Matrix:")
print(matrix)

# ------------------------------------------------------------
# Step 2: Apply Flatten Layer
# Convert 2D Matrix into 1D Vector
# ------------------------------------------------------------

flatten_output = matrix.flatten()

print("\nFlatten Output:")
print(flatten_output)

# ------------------------------------------------------------
# Step 3: Define Fully Connected Layer Weights and Bias
# ------------------------------------------------------------

weights = np.array([0.2, 0.3, 0.4, 0.1])
bias = 0.5

print("\nWeights:")
print(weights)

print("\nBias:")
print(bias)

# ------------------------------------------------------------
# Step 4: Calculate Fully Connected Layer Output
# Output = (Input * Weights) + Bias
# ------------------------------------------------------------

multiplication = flatten_output * weights

print("\nMultiplication:")
print(multiplication)

weighted_sum = np.sum(multiplication)

print("\nWeighted Sum:")
print(weighted_sum)

final_output = weighted_sum + bias

print("\nFinal Output:")
print(final_output)

# ------------------------------------------------------------
# Step 5: Display Final Result
# ------------------------------------------------------------

print("\n------------- Final Result -------------")
print("Original Matrix:")
print(matrix)

print("Flatten Vector:", flatten_output)
print("Fully Connected Layer Output:", final_output)