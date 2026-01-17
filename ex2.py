import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt


def create_gradient_image(height, width):
    """שאלה 1: יצירת תמונת גרדיאנט משחור ללבן"""
    img = np.zeros((height, width), dtype=np.uint8)
    for y in range(height):
        for x in range(width):
            img[y, x] = (x + y) * 255 // (width + height)
    return img


def brighten(img, b, func="np"):
    """שאלה 2: הוספת בהירות לכל הפיקסלים"""
    if func == "np":
        out = np.add(img, b)
    elif func == "cv2":
        out = cv2.add(img, b)
    else:
        raise ValueError("func must be 'np' or 'cv2'")
    return out


def test_brighten_twice(img):
    """שאלה 3: הפעלה כפולה והצגת הבדל"""
    np_img = brighten(brighten(img, 50, "np"), 50, "np")
    cv_img = brighten(brighten(img, 50, "cv2"), 50, "cv2")

    plt.figure("Brighten Test")
    plt.subplot(1, 3, 1)
    plt.title("Original")
    plt.imshow(img, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.title("NP twice")
    plt.imshow(np_img, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.title("CV2 twice")
    plt.imshow(cv_img, cmap='gray')
    plt.axis('off')

    plt.show()


def contrast(height, width, fg, bg):
    """שאלה 4: יצירת תמונה עם ניגודיות נמוכה"""
    img = np.full((height, width), bg, dtype=np.uint8)
    center = (width // 2, height // 2)
    radius = min(width, height) // 4
    cv2.circle(img, center, radius, fg, -1)
    return img


def normalize(img):
    """שאלה 5: נירמול תמונה למינימום 0 ומקסימום 255"""
    min_val = img.min()
    max_val = img.max()
    img_f = img.astype(np.float32)
    out = (img_f - min_val) * 255 / (max_val - min_val)
    out = np.clip(out, 0, 255).astype(np.uint8)
    return out


def test_pixel_change(img):
    """שאלה 6: שינוי פיקסל ובדיקת השפעה על normalization"""
    img2 = img.copy()
    img2[0, 0] = 0
    img2[0, 1] = 255
    norm = normalize(img2)
    return norm


def bw_and_histogram(path):
    """שאלה 7: המרת תמונה לשחור-לבן וחישוב היסטוגרמה"""
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    # המרה לשחור/לבן
    th = 128
    bw = np.where(img > th, 255, 0).astype(np.uint8)

    # חישוב היסטוגרמה ידנית
    hist = np.zeros(256, dtype=np.int32)
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            hist[img[y, x]] += 1

    # הצגת היסטוגרמה
    plt.figure("Histogram")
    plt.bar(range(256), hist)
    plt.title("Histogram")
    plt.show()

    return bw


def main():
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} image-filename")
        exit(-1)

    image_path = sys.argv[1]

    # שאלה 1
    gradient = create_gradient_image(255, 255)
    cv2.imwrite("gradient.png", gradient)

    # שאלה 2+3
    test_brighten_twice(gradient)

    # שאלה 4+5
    low_contrast = contrast(300, 300, fg=105, bg=100)
    normalized = normalize(low_contrast)

    # שאלה 6
    test_pixel_change(low_contrast)

    # שאלה 7
    bw_and_histogram(image_path)


if __name__ == "__main__":
    main()
