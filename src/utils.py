import os
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