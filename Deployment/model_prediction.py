# model_prediction.py

import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

# Load the model
model_final = load_model('model_func.keras')

# Define class labels
class_labels = ['cloudy', 'foggy', 'rainy', 'shine', 'sunrise']

# Function to preprocess the image
def preprocess_image(image):
    # Resize the image to match the expected input shape of the model
    image = image.resize((400, 400))
    # Convert image to numpy array
    image = np.array(image)
    # Normalize the image
    image = image / 255.0
    return image

# Function to make predictions
def predict(image):
    image = preprocess_image(image)
    image_array = np.expand_dims(image, axis=0)
    predictions = model_final.predict(image_array)
    predicted_class_index = np.argmax(predictions)
    predicted_class_label = class_labels[predicted_class_index]
    return predicted_class_label

def run_model_prediction():
    st.title('Prediction')
    st.write("Upload an image for classification:")

    # Allow user to upload an image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Predict the class of the uploaded image
        prediction = predict(image)
        st.write(f'Predicted Class: {prediction}')
