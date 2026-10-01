import numpy as np
import tensorflow as tf 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix,accuracy_score

# create dataset
X = np.array([
[25, 500, 12, 1, 2],
[30, 700, 24, 0, 1],
[45, 1200, 6, 5, 8],
[50, 1500, 5, 6, 10],
[28, 600, 18, 1, 1],
[35, 800, 30, 0, 0],
[48, 1400, 4, 7, 9],
[52, 1600, 3, 8, 12],
[27, 550, 20, 0, 1],
[42, 1300, 8, 4, 7]
])

y = np.array([0, 0, 1, 1, 0, 0, 1, 1, 0, 1])

# Clean the dataset
print("Missing values:", np.isnan(X).sum())

# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Apply StandardScaler
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create Feed Forward Neural Network
model = tf.keras.Sequential([
    tf.keras.Input(shape=(5,)),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Display model architecture
model.summary()

# Compile the model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Train the model
model.fit(
    X_train,
    y_train,
    epochs=100,
    batch_size=2,
    verbose=0
)

print("\nModel training completed!")

# Evaluate the model
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

# Predict a new customer
new_customer = np.array([[46, 1450, 5, 6, 9]])

# Apply the same scaler
new_customer_scaled = scaler.transform(new_customer)

# Make prediction
prediction = model.predict(new_customer_scaled, verbose=0)[0][0]

print("\nNew Customer Prediction:")

if prediction >= 0.5:
    print("Prediction: Customer may leave")
else:
    print("Prediction: Customer will stay")

print("Churn Probability:", prediction)