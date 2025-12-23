import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Sayfa Ayarları
st.set_page_config(page_title="VisionSketch Engine", layout="centered", page_icon="🎨")

# CSS: Modern ve Temiz Bir Tasarım
st.markdown("""
    <style>
    .stApp { background-color: #2b2b2b; }
    h1 { color: #ffffff !important; font-family: 'Helvetica', sans-serif; }
    div[data-testid="stFileUploader"] { background-color: #383838; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# Başlık
st.title("🎨 VisionSketch: Algorithmic Art Engine")
st.markdown("**Core:** :orange[OpenCV] | **Filter:** Gaussian Blur & Dodge | **Status:** Ready")

# Sidebar Ayarları
st.sidebar.header("✏️ Sketch Parameters")
blur_intensity = st.sidebar.slider("Stroke Intensity (Blur)", 1, 99, 21, step=2)
contrast = st.sidebar.slider("Contrast Enhancement", 50, 150, 100)

def convert_to_sketch(image, k_size):
    # 1. Gri Tonlamaya Çevir
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
    # 2. Görüntüyü Ters Çevir (Invert)
    inverted_image = cv2.bitwise_not(gray_image)
    
    # 3. Bulanıklaştır (Gaussian Blur) - Çizgileri yumuşatır
    blurred = cv2.GaussianBlur(inverted_image, (k_size, k_size), 0)
    
    # 4. Renk Soldurma (Color Dodge) Tekniği ile Birleştir
    # Bu formül fotoğrafı karakalem çizimine çeviren sihirli matematik kısmıdır.
    inverted_blurred = cv2.bitwise_not(blurred)
    sketch_image = cv2.divide(gray_image, inverted_blurred, scale=256.0)
    
    return sketch_image

# Görsel Yükleme
uploaded_file = st.file_uploader("📂 Upload an Image to Sketch...", type=['jpg', 'png', 'jpeg'])

if uploaded_file is not None:
    # Görüntüyü Oku
    original_image = np.array(Image.open(uploaded_file))
    
    # İşlem Animasyonu
    with st.spinner('🎨 Rendering Pencil Strokes...'):
        # Sketch Fonksiyonunu Çağır
        sketch = convert_to_sketch(original_image, blur_intensity)
        
        # Kontrast Ayarı (Opsiyonel Güzelleştirme)
        # Sadece daha net görünsün diye
        if contrast != 100:
            f = 131 * (contrast - 127) / (127 * (131 - contrast))
            alpha_c = f + 1
            gamma_c = 127 * (1 - f)
            sketch = cv2.addWeighted(sketch, alpha_c, sketch, 0, gamma_c)

        # Sonuçları Göster
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Original")
            st.image(original_image, use_container_width=True)
            
        with col2:
            st.subheader("Pencil Sketch")
            st.image(sketch, use_container_width=True, channels="GRAY")
            
        # İndirme Butonu
        result_image = Image.fromarray(sketch.astype('uint8'))
        st.download_button(
            label="Download Sketch Art 📥",
            data=cv2.imencode('.png', sketch)[1].tobytes(),
            file_name="vision_sketch_output.png",
            mime="image/png"
        )
        
        st.success("✅ Image processed successfully using Gaussian Blend Algorithm.")