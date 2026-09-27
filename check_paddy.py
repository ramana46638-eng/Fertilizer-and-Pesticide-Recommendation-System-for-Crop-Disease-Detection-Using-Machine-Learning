from pathlib import Path

dataset_path = Path("dataset/paddy")

for folder in dataset_path.iterdir():
    if folder.is_dir():
        images = list(folder.glob("*.jpg"))
        images += list(folder.glob("*.jpeg"))
        images += list(folder.glob("*.png"))

        print(folder.name, ":", len(images), "images")