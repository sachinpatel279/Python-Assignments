import numpy as np

# ------------------------------------------------------------
# Step 1: Create Feature Map
# ------------------------------------------------------------

feature_map = np.array([
    [3, 3, 3],
    [0, 0, 0],
    [-3, -3, -3]
])

print("\nOriginal Feature Map:")
print(feature_map)

# ------------------------------------------------------------
# Step 2: Apply ReLU Activation
# Rule:
# If value < 0, convert it to 0
# If value >= 0, keep it unchanged
# ------------------------------------------------------------

relu_output = np.maximum(0, feature_map)

print("\nFeature Map After ReLU:")
print(relu_output)

# ------------------------------------------------------------
# Step 3: Apply 2x2 Max Pooling
# Pool Size = 2x2
# Stride = 2
# ------------------------------------------------------------

pool_size = 2
stride = 2

rows, cols = relu_output.shape

output_rows = (rows - pool_size) // stride + 1
output_cols = (cols - pool_size) // stride + 1

max_pool_output = np.zeros(
    (output_rows, output_cols),
    dtype=int
)

for i in range(output_rows):
    for j in range(output_cols):

        # Extract 2x2 Region
        region = relu_output[
            i * stride : i * stride + pool_size,
            j * stride : j * stride + pool_size
        ]

        # Find Maximum Value
        max_value = np.max(region)

        # Store Maximum Value
        max_pool_output[i][j] = max_value

        print(f"\nPooling Region ({i}, {j}):")
        print(region)
        print("Maximum Value =", max_value)

# ------------------------------------------------------------
# Step 4: Display Final Output
# ------------------------------------------------------------

print("\nFeature Map After Max Pooling:")
print(max_pool_output)

# ------------------------------------------------------------
# Step 5: Display Dimensions
# ------------------------------------------------------------

print("\nOriginal Feature Map Size:", feature_map.shape)
print("After ReLU Size:", relu_output.shape)
print("After Max Pooling Size:", max_pool_output.shape)