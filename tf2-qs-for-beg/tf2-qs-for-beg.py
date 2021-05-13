#!/usr/bin/env python
"""tensorflow 2 quickstart for beginners."""

# -->  Import TensorFlow into your program
from __future__ import absolute_import, division, print_function, unicode_literals

# Install TensorFlow

import tensorflow as tf
# <--  Import TensorFlow into your program

# --> hack against SSL: CERTIFICATE_VERIFY_FAILED
import ssl

# Don't know how to properly install ssl certificates for python
# .which causes this error:
# .urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED]
# .certificate verify failed: unable to get local issuer certificate (_ssl.c:1123)>
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context
# <-- hack against SSL: CERTIFICATE_VERIFY_FAILED

# Load and prepare the MNIST dataset
mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
# Convert the samples from integers to floating-point numbers
x_train, x_test = x_train / 255.0, x_test / 255.0

# Build the tf.keras.Sequential model by stacking layers
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10)
])

predictions = model(x_train[:1]).numpy()
tf.nn.softmax(predictions).numpy()
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
loss_fn(y_train[:1], predictions).numpy()

# Choose an optimizer and loss function for training
model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5)
# Evaluate the model
model.evaluate(x_test, y_test, verbose=2)

# If you want your model to return a probability,
# .you can wrap the trained model, and attach the softmax to it
probability_model = tf.keras.Sequential([
    model,
    tf.keras.layers.Softmax()
])
probability_model(x_test[:5])
