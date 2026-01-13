import sys
from PIL import Image, ImageOps


def show_rgb_channels(img):
    """שאלה 1: הצגת ערוצי RGB בנפרד"""
    r, g, b = img.split()

    red_img = Image.merge("RGB", (r, Image.new("L", r.size), Image.new("L", r.size)))
    green_img = Image.merge("RGB", (Image.new("L", g.size), g, Image.new("L", g.size)))
    blue_img = Image.merge("RGB", (Image.new("L", b.size), Image.new("L", b.size), b))

    red_img.show(title="Red Channel")
    green_img.show(title="Green Channel")
    blue_img.show(title="Blue Channel")


def grayscale_and_histogram(img):
    """שאלה 2: שחור-לבן, היסטוגרמה ומתיחה"""
    gray_img = img.convert("L")
    gray_img.show(title="Grayscale Image")

    histogram = gray_img.histogram()
    print("Grayscale Histogram:")
    print(histogram)

    stretched_img = ImageOps.autocontrast(gray_img)
    stretched_img.show(title="Stretched Grayscale Image")


def stretch_rgb_histogram(img):
    """שאלה 3: מתיחת היסטוגרמה לכל ערוץ צבע"""
    r, g, b = img.split()

    r_stretched = ImageOps.autocontrast(r)
    g_stretched = ImageOps.autocontrast(g)
    b_stretched = ImageOps.autocontrast(b)

    stretched_img = Image.merge("RGB", (r_stretched, g_stretched, b_stretched))
    stretched_img.show(title="Stretched RGB Image")


def main():
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} image-filename")
        exit(-1)

    image_path = sys.argv[1]
    img = Image.open(image_path)

    # שאלה 1
    show_rgb_channels(img)

    # שאלה 2
    grayscale_and_histogram(img)

    # שאלה 3
    stretch_rgb_histogram(img)


if __name__ == "__main__":
    main()