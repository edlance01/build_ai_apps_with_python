import matplotlib.pyplot as plt
import keras


(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# View a single image
plt.imshow(x_train[0], cmap="gray")
plt.title(f"Label: {y_train[0]}")
plt.show()

# View a grid of 25 images
fig, axes = plt.subplots(5, 5, figsize=(8, 8))
for i, ax in enumerate(axes.flat):
    ax.imshow(x_train[i], cmap="gray")
    ax.set_title(f"{y_train[i]}")
    ax.axis("off")
plt.tight_layout()
plt.show()
