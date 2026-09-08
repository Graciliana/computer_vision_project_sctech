import cv2
import numpy as np

def preprocess_image(image_path, target_size=(256, 256)):
    """
    Pipeline OpenCV: Grayscale, Blur, Otsu, Canny, Morfologia e Resize.
    """
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Não foi possível ler a imagem no caminho: {image_path}")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    edges = cv2.Canny(blurred, 50, 150)

    kernel = np.ones((3, 3), np.uint8)
    morphed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
    resized = cv2.resize(morphed, target_size, interpolation=cv2.INTER_AREA)

    return resized