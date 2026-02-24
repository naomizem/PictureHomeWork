import sys
import cv2
import numpy as np

# ---------- RGB -> HSV (manual) ----------
def rgb_to_hsv_manual(R, G, B):
    r = R / 255.0
    g = G / 255.0
    b = B / 255.0

    cmax = max(r, g, b)
    cmin = min(r, g, b)
    delta = cmax - cmin

    if delta == 0:
        H = 0
    elif cmax == r:
        H = 60 * (((g - b) / delta) % 6)
    elif cmax == g:
        H = 60 * (((b - r) / delta) + 2)
    else:
        H = 60 * (((r - g) / delta) + 4)

    if cmax == 0:
        S = 0
    else:
        S = delta / cmax

    V = cmax
    return H, S, V

# ---------- RGB -> HSL (manual) ----------
def rgb_to_hsl_manual(R, G, B):
    r = R / 255.0
    g = G / 255.0
    b = B / 255.0

    cmax = max(r, g, b)
    cmin = min(r, g, b)
    delta = cmax - cmin

    L = (cmax + cmin) / 2.0

    if delta == 0:
        H = 0
        S = 0
    else:
        S = delta / (1 - abs(2 * L - 1))
        if cmax == r:
            H = 60 * (((g - b) / delta) % 6)
        elif cmax == g:
            H = 60 * (((b - r) / delta) + 2)
        else:
            H = 60 * (((r - g) / delta) + 4)

    return H, S, L

# ---------- RGB -> YCrCb (manual) ----------
def rgb_to_ycrcb_manual(R, G, B):
    Y  = 0.299 * R + 0.587 * G + 0.114 * B
    Cr = (R - Y) * 0.713 + 128
    Cb = (B - Y) * 0.564 + 128
    return Y, Cr, Cb

# ---------- MAIN ----------
if len(sys.argv) != 4:
    print("Usage: python color_models.py R G B")
    sys.exit()

R = int(sys.argv[1])
G = int(sys.argv[2])
B = int(sys.argv[3])

print("Input RGB:", R, G, B)

# Manual calculations
hsv_m = rgb_to_hsv_manual(R, G, B)
hsl_m = rgb_to_hsl_manual(R, G, B)
ycc_m = rgb_to_ycrcb_manual(R, G, B)

print("\nManual results:")
print("HSV:", hsv_m)
print("HSL:", hsl_m)
print("YCrCb:", ycc_m)

# OpenCV calculations
pixel = np.uint8([[[B, G, R]]])

hsv_cv = cv2.cvtColor(pixel, cv2.COLOR_BGR2HSV)[0][0]
hsl_cv = cv2.cvtColor(pixel, cv2.COLOR_BGR2HLS)[0][0]
ycc_cv = cv2.cvtColor(pixel, cv2.COLOR_BGR2YCrCb)[0][0]

print("\nOpenCV results:")
print("HSV:", hsv_cv)
print("HSL:", hsl_cv)
print("YCrCb:", ycc_cv)

print("\nNote:")
print("OpenCV uses different ranges and integer rounding, so small differences are normal.")