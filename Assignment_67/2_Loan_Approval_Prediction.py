
# Import required libraries
import numpy as np
import tensorflow as tf

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Create dataset
X = np.array([
    [25000, 600, 200000, 10000, 0],
    [40000, 700, 300000, 8000, 1],
    [60000, 750, 500000, 12000, 1],
    [20000, 550, 150000, 15000, 0],
    [80000, 800, 700000, 10000, 1],
    [35000, 650, 250000, 9000, 1],
    [18000, 500, 100000, 12000, 0],
    [90000, 850, 800000, 15000, 1],
    [30000, 580, 200000, 14000, 0],
    [70000, 780, 600000, 10000, 1]
], dtype=float)

# Set random seed
np.random.seed(42)
tf.random.set_seed(42)

y = np.array([0, 1, 1, 0, 1, 1, 0, 1, 0, 1])

# Clean the dataset
print("Missing values:", np.isnan(X).sum())

# Split dataset
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=42, stratify=y)

# Apply StandardScaler
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create FNN model
model = tf.keras.Sequential([
    tf.keras.Input(shape=(5,)),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Display model architecture
model.summary()

# Compile model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Train model
model.fit(X_train, y_train, epochs=100, batch_size=2, verbose=0)

print("\nModel training completed!")

# Evaluate model
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)

print("\nTest Loss:", loss)
print("Test Accuracy:", accuracy * 100, "%")

# Predict test data
y_pred_prob = model.predict(X_test, verbose=0)

y_pred = (y_pred_prob >= 0.5).astype(int).flatten()

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# Predict new applicant
new_applicant = np.array([[55000, 720, 400000, 10000, 1]])

# Apply scaling
new_applicant_scaled = scaler.transform(new_applicant)

# Make prediction
prediction = model.predict(new_applicant_scaled, verbose=0)[0][0]

print("\nNew Applicant Prediction:")

if prediction >= 0.5:
    print("Prediction: Loan Approved")
else:
    print("Prediction: Loan Rejected")

print("Approval Probability:", prediction)