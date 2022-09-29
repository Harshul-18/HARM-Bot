import numpy as np
import matplotlib.pyplot as plt
import pafy
from keras.models import load_model
from PIL import Image, ImageOps
import requests
from skimage import io
from io import BytesIO

def predictCategoryFor(url):

    # Loading the saved model
    model = load_model('model.h5')

    video_url = url

    video = pafy.new(video_url)
    thumbnail_url = video.bigthumbhd
    response = requests.get(thumbnail_url)
    image = Image.open(BytesIO(response.content))

    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array

    prediction = model.predict(data)

    prediction = [100 * (prediction[0][0]-0.03), 100 * (prediction[0][1]+0.03)]

    category = ["Educational", "Non Educational"]
    percentage = prediction

    # plt.bar(
    #     category,
    #     percentage,
    #     color=("orange", "blue"),
    # )
    # plt.show()

    if prediction[0] >= 0.5:
        return "HARM Bot predicts that this video is educational."
    else:
        return "HARM Bot predicts that this is not an educational video."

# predictCategoryFor(url="https://www.youtube.com/watch?v=2_ZbslLnshw")