import os
import numpy as np
import tensorflow as tf

from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

# -----------------------------
# 1. Dataset path
# -----------------------------
DATASET_PATH = Path("dataset/paddy")

# -----------------------------
# 2. Load image paths
# -----------------------------
images = []
labels = []

class_names = sorted([
    folder.name
    for folder in DATASET_PATH.iterdir()
    if folder.is_dir()
])

print("Classes:", class_names)

for label, class_name in enumerate(class_names):
    folder = DATASET_PATH / class_name

    for image_path in folder.iterdir():
        if image_path.suffix.lower() in [".jpg", ".jpeg", ".png"]:
            images.append(str(image_path))
            labels.append(label)

print("Total images:", len(images))

# -----------------------------
# 3. Train-test split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    images,
    labels,
    test_size=0.20,
    random_state=42,
    stratify=labels
)

print("Training images:", len(X_train))
print("Testing images:", len(X_test))

# -----------------------------
# 4. TensorFlow MobileNetV2
# -----------------------------
feature_model = tf.keras.applications.MobileNetV2(
    weights="imagenet",
    include_top=False,
    pooling="avg",
    input_shape=(128, 128, 3)
)

# -----------------------------
# 5. Feature extraction
# -----------------------------
def extract_features(image_paths):

    features = []

    for path in image_paths:

        image = tf.keras.utils.load_img(
            path,
            target_size=(128, 128)
        )

        image = tf.keras.utils.img_to_array(image)

        image = np.expand_dims(image, axis=0)

        image = tf.keras.applications.mobilenet_v2.preprocess_input(image)

        feature = feature_model.predict(
            image,
            verbose=0
        )

        features.append(feature[0])

    return np.array(features)


print("\nExtracting training features...")

X_train_features = extract_features(X_train)

print("Extracting testing features...")

X_test_features = extract_features(X_test)

print("Feature shape:", X_train_features.shape)

# -----------------------------
# 6. Train SVM
# -----------------------------
print("\nTraining SVM...")

svm_model = SVC(
    kernel="rbf",
    probability=True,
    random_state=42
)

svm_model.fit(
    X_train_features,
    y_train
)

# -----------------------------
# 7. Prediction
# -----------------------------
y_pred = svm_model.predict(X_test_features)

# -----------------------------
# 8. Evaluation
# -----------------------------
accuracy = accuracy_score(y_test, y_pred)

print("\n==============================")
print("PADDY DISEASE MODEL RESULTS")
print("==============================")

print("Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=class_names
    )
)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# -----------------------------
# 9. Save SVM model
# -----------------------------
os.makedirs("models", exist_ok=True)

joblib.dump(
    svm_model,
    "models/paddy_svm.pkl"
)

joblib.dump(
    class_names,
    "models/paddy_classes.pkl"
)

print("\nModel saved successfully!")
print("models/paddy_svm.pkl")
print("models/paddy_classes.pkl")