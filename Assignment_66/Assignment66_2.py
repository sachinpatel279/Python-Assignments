import tensorflow as tf 
import numpy as np
import matplotlib.pyplot as plt

x = tf.linspace(-10, 10, 100)

sigmoid = tf.keras.activations.sigmoid(x)

relu = tf.keras.activations.relu(x)

tanh = tf.keras.activations.tanh(x)

plt.figure(figsize=(8, 4))

plt.plot(x.numpy(), sigmoid.numpy(), label='Sigmoid', color='blue')
plt.plot(x.numpy(), relu.numpy(), label='ReLU', color='green')
plt.plot(x.numpy(), tanh.numpy(), label='Tanh', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Activation Functions')
plt.legend()
plt.grid(True)
plt.show()