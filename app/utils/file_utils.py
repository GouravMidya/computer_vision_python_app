import cv2

def load_image(file_path):
    # Load image from file path
    img = cv2.imread(file_path)
    return img

def save_image(file_path, img):
    # Save image to file path
    cv2.imwrite(file_path, img)