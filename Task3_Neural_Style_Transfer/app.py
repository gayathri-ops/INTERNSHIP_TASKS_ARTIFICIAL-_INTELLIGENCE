import tensorflow as tf
import tensorflow_hub as hub
from PIL import Image
import numpy as np

def load_image(path):
    img = Image.open(path)
    img = img.resize((512, 512))
    img = np.array(img) / 255.0
    img = img.astype(np.float32)
    img = img[np.newaxis, :]
    return tf.constant(img)

content_image = load_image("content.jpg")
style_image = load_image("style.jpg")

model = hub.load(
    "https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2"
)

stylized_image = model(content_image, style_image)[0]

output = tf.squeeze(stylized_image).numpy()
output = (output * 255).astype(np.uint8)

Image.fromarray(output).save("output.jpg")

print("Style transfer completed!")
print("Output saved as output.jpg")