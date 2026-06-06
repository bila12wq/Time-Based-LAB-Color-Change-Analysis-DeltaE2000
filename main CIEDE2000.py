import cv2
import numpy as np
from skimage import color
from skimage.color import deltaE_ciede2000

# ===== Load images =====
image1 = cv2.imread(r"C:\Users\bilal\Downloads\before.png")   # Before image
image2 = cv2.imread(r"C:\Users\bilal\Downloads\after.png")    # After image

if image1 is None or image2 is None:
    print("Error: Could not load images")
    exit()

# ===== Resize images to same size =====
image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

# ===== Combine images side by side =====
combined = np.hstack((image1, image2))
display = combined.copy()

# ===== Convert RGB → LAB =====
def rgb_to_lab(r, g, b):
    rgb = np.array([[[r, g, b]]]) / 255.0
    lab = color.rgb2lab(rgb)
    return lab[0][0]

# ===== Extract region color =====
def get_region_rgb(image, x, y, size=7):
    h, w, _ = image.shape

    x1 = max(0, x - size)
    x2 = min(w, x + size)
    y1 = max(0, y - size)
    y2 = min(h, y + size)

    region = image[y1:y2, x1:x2]
    pixels = region.reshape(-1, 3)

    # median for stability
    b, g, r = np.median(pixels, axis=0)

    return int(r), int(g), int(b)

# ===== ΔE interpretation =====
def interpret_deltaE(delta_e):
    if delta_e < 1:
        return "No significant difference"
    elif delta_e < 3:
        return "Noticeable but acceptable"
    else:
        return "Noticeable and not acceptable"

# ===== Mouse click event =====
def click_event(event, x, y, flags, param):
    global display

    if event == cv2.EVENT_LBUTTONDOWN:

        width = image1.shape[1]

        # ---- Extract from both images ----
        r1, g1, b1 = get_region_rgb(image1, x, y)
        r2, g2, b2 = get_region_rgb(image2, x, y)

        lab1 = rgb_to_lab(r1, g1, b1)
        lab2 = rgb_to_lab(r2, g2, b2)

        lab1_arr = np.array([lab1])
        lab2_arr = np.array([lab2])

        delta_e = deltaE_ciede2000(lab1_arr, lab2_arr)[0]
        interpretation = interpret_deltaE(delta_e)

        # ---- Print results ----
        print("\nPoint:", (x, y))
        print(f"Before: L={lab1[0]:.2f}, a={lab1[1]:.2f}, b={lab1[2]:.2f}")
        print(f"After : L={lab2[0]:.2f}, a={lab2[1]:.2f}, b={lab2[2]:.2f}")
        print(f"ΔE2000 = {delta_e:.2f} → {interpretation}")

        # ---- Reset display ----
        display = combined.copy()

        size = 7

        # ---- LEFT IMAGE (before) ----
        cv2.rectangle(display,
                      (x - size, y - size),
                      (x + size, y + size),
                      (0, 255, 0), 2)

        cv2.circle(display, (x, y), 5, (0, 0, 255), -1)

        # ---- RIGHT IMAGE (after) ----
        x2 = x + width

        cv2.rectangle(display,
                      (x2 - size, y - size),
                      (x2 + size, y + size),
                      (0, 255, 0), 2)

        cv2.circle(display, (x2, y), 5, (0, 0, 255), -1)

        # ---- Connect points ----
        cv2.line(display, (x, y), (x2, y), (255, 0, 0), 1)

        # ---- Show ΔE text ----
        text = f"dE = {delta_e:.2f}"
        cv2.putText(display, text,
                    (x + 10, y + 25),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (255, 255, 255),
                    2)

        cv2.imshow("DeltaE Analyzer", display)


# ===== Run app =====
cv2.imshow("DeltaE Analyzer", display)
cv2.setMouseCallback("DeltaE Analyzer", click_event)

print("Click on the LEFT image to compare color change")

cv2.waitKey(0)
cv2.destroyAllWindows()
