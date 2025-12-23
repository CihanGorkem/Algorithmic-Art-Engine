# 🎨 VisionSketch: Algorithmic Art Engine

VisionSketch is a Python application that converts digital images into realistic pencil sketches using computer vision algorithms. It creates a "Color Dodge" blend between the grayscale and inverted-blurred layers of an image.

## ⚙️ How it Works ( The Algorithm)
1.  **Grayscale Conversion:** Reduces the image to luminance channels.
2.  **Inversion:** Creates a negative of the image.
3.  **Gaussian Blur:** Softens the inverted image to simulate pencil shading.
4.  **Color Dodge Blend:** Mathematically divides the grayscale image by the inverted blur to highlight edges.

## 🛠️ Tech Stack
* **Python**
* **OpenCV** (Matrix operations & Filtering)
* **Streamlit** (UI)
* **NumPy**



## 📸 Video
https://github.com/user-attachments/assets/80513021-a490-4e6b-8b4f-53536f714575
