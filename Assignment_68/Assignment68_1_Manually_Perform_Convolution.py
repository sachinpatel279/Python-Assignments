import numpy as np

# ------------------------------------------------------------
# Step 1: Create 5x5 Grayscale Image
# ------------------------------------------------------------

image = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
])

print("\nOriginal 5x5 Image:")
print(image)

# ------------------------------------------------------------
# Step 2: Create 3x3 Kernel for Edge Detection
# ------------------------------------------------------------

kernel = np.array([
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
])

print("\n3x3 Kernel:")
print(kernel)

# ------------------------------------------------------------
# Step 3: Calculate Output Dimensions
# ------------------------------------------------------------

image_size = image.shape[0]
kernel_size = kernel.shape[0]

output_size = image_size - kernel_size + 1

print("\nOutput Size:", output_size, "x", output_size)

# Initialize Feature Map
feature_map = np.zeros((output_size, output_size), dtype=int)

# ------------------------------------------------------------
# Step 4: Perform Convolution Operation
# ------------------------------------------------------------

print("\n========== Convolution Calculations ==========")

for i in range(output_size):
    for j in range(output_size):

        # Extract 3x3 Region
        region = image[i:i+kernel_size, j:j+kernel_size]

        # Multiply and Sum
        result = np.sum(region * kernel)

        # Store Result in Feature Map
        feature_map[i][j] = result

        # Display Current Region
        print(f"\nRegion at Position ({i}, {j}):")
        print(region)

        print("\nKernel:")
        print(kernel)

        # Display Calculation
        print("\nCalculation:")

        for m in range(kernel_size):
            for n in range(kernel_size):

                print(f"{region[m][n]} * {kernel[m][n]}", end="")

                if m != kernel_size - 1 or n != kernel_size - 1:
                    print(" + ", end="")

            print()

        print("Output =", result)

# ------------------------------------------------------------
# Step 5: Display Final Feature Map
# ------------------------------------------------------------

print("\n------------- Final Feature Map -------------")
print(feature_map)
