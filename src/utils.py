# Writing src/utils.py - Batch image loader utility
utils_code = '''import os
import glob
import cv2

def load_images_from_folder(folder_path):
    """
    Lê todas as imagens de um diretório em lote (batch).
    Suporta formatos .png, .jpg e .jpeg.
    """
    supported_extensions = ('*.png', '*.jpg', '*.jpeg', '*.PNG', '*.JPG', '*.JPEG')
    image_paths = []
    
    for ext in supported_extensions:
        image_paths.extend(glob.glob(os.path.join(folder_path, "**", ext), recursive=True))
        
    print(f"[INFO] Encontradas {len(image_paths)} imagens em: {folder_path}")
    return image_paths

def save_image(output_path, image):
    """
    Salva a imagem no caminho especificado criando diretórios se necessário.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cv2.imwrite(output_path, image)
'''

with open("computer_vision_project_sctech/src/utils.py", "w", encoding="utf-8") as f:
    f.write(utils_code)

# Writing src/pipeline.py - OpenCV Processing Pipeline
pipeline_code = '''import cv2
import numpy as np

def preprocess_image(image_path, target_size=(256, 256)):
    """
    Pipeline de pré-processamento OpenCV para inspeção visual de peças:
    1. Leitura
    2. Conversão para Escala de Cinza
    3. Suavização (Gaussian Blur)
    4. Limiarização Binarizada (Otsu Thresholding)
    5. Detecção de Bordas (Canny)
    6. Operações Morfológicas (Fechamento/Erosão)
    7. Redimensionamento Padrão
    """
    # 1. Leitura da Imagem
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Não foi possível ler a imagem no caminho: {image_path}")

    # 2. Conversão para Escala de Cinza (Grayscale)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 3. Suavização (Gaussian Blur) para redução de ruído
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # 4. Limiarização (Thresholding Otsu) para isolar a peça do fundo
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 5. Detecção de Bordas (Canny) para evidenciar ranhuras e defeitos
    edges = cv2.Canny(blurred, 50, 150)

    # 6. Refinamento Morfológico (Fechamento para eliminar falhas/ruídos pequenos)
    kernel = np.ones((3, 3), np.uint8)
    morphed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

    # 7. Redimensionamento Padronizado (256x256)
    resized = cv2.resize(morphed, target_size, interpolation=cv2.INTER_AREA)

    return resized
'''

with open("computer_vision_project_sctech/src/pipeline.py", "w", encoding="utf-8") as f:
    f.write(pipeline_code)