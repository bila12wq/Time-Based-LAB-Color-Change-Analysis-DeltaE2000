# Time-Based LAB Color Change Analysis (ΔE2000)

Interactive Python tool for analyzing perceptual color changes between two images using LAB color space and ΔE2000.

---

##  Overview
This project measures how colors change over time by comparing two images (before and after).  
It extracts LAB color values from the same region in both images and computes the **ΔE2000 color difference**, which represents how noticeable the change is to the human eye.

---

## What This Project Does
- Extracts LAB color values from two images  
- Uses region-based sampling for stable and accurate results  
- Computes ΔE2000 for perceptual color difference  
- Provides interpretation of color change  
- Displays visual markers and selected regions  

---

## Screenshot

![DeltaE Analyzer] (screenshot.png)

---

## ΔE2000 Interpretation

| ΔE Value | Meaning |
|---------|--------|
| < 1 | No significant difference |
| 1 – 3 | Noticeable but acceptable |
| ≥ 3 | Noticeable and not acceptable |

---

## Features
- Click on image to select region  
- Compare same region across two images  
- Region-based sampling (improves accuracy)  
- Real-time ΔE calculation  
- Visual feedback (crosshair + region box)  

---

## How It Works
1. Load two images (before and after)  
2. Click on a location in the image  
3. Extract RGB values from a small region  
4. Convert RGB → LAB color space  
5. Compute ΔE2000 between the two images  
6. Display the color difference  

---
## Technologies Used

- Python  
- OpenCV  
- NumPy  
- Scikit-image  

## How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the script:
```bash
python main.py
```

3. Click on the image to analyze color change.

## Project Structure

```
project/
│
├── main_ciede2000.py
├── screenshot.png
├── requirements.txt
└── README.md
```
## Note

Sample images are not included in this repository.

To use the tool, provide your own pair of images (before and after) with consistent size, lighting, and positioning for accurate color comparison.
##  Author
Bilal Lukman Alkrayem  

---

##  License
MIT License

