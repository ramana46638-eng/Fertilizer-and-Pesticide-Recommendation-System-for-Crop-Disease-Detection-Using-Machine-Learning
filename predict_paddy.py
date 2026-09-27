import numpy as np
import tensorflow as tf
import joblib


# Load SVM model
svm_model = joblib.load("models/paddy_svm.pkl")

# Load class names
class_names = joblib.load("models/paddy_classes.pkl")


# TensorFlow feature extractor
feature_model = tf.keras.applications.MobileNetV2(
    weights="imagenet",
    include_top=False,
    pooling="avg",
    input_shape=(128, 128, 3)
)


def predict_paddy(image_path):

    # Load image
    image = tf.keras.utils.load_img(
        image_path,
        target_size=(128, 128)
    )

    # Convert image to array
    image = tf.keras.utils.img_to_array(image)

    # Add batch dimension
    image = np.expand_dims(image, axis=0)

    # Preprocess
    image = tf.keras.applications.mobilenet_v2.preprocess_input(image)

    # Extract features
    features = feature_model.predict(
        image,
        verbose=0
    )

    # Predict
    prediction = svm_model.predict(features)[0]

    disease = class_names[prediction]

    # Confidence
    probabilities = svm_model.predict_proba(features)[0]
    confidence = max(probabilities) * 100

    return disease, round(confidence, 2)