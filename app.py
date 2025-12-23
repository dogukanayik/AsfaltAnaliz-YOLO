import streamlit as st
from ultralytics import YOLO
from PIL import Image
import os
import cv2
import tempfile
import numpy as np

# Sayfa Ayarları
st.set_page_config(page_title="Yol Hasarı Analizi YOLOv11L", layout="wide")

# --- MODEL YÜKLEME ---
@st.cache_resource
def load_model():
    # Kendi eğittiğin yol hasarı modeli
    return YOLO("best.pt") 

model = load_model()

# --- YAN PANEL (SIDEBAR) - KIYASLAMA ---
st.sidebar.title("📊 Model Performans Kıyaslama")

# YOLOv11L Verileri
st.sidebar.markdown("### 🏆 YOLOv11L (Aktif Model)")
if os.path.exists("results.png"):
    st.sidebar.image("results.png", caption="v11L Eğitim Grafikleri")
if os.path.exists("confusion_matrix_normalized.png"):
    st.sidebar.image("confusion_matrix_normalized.png", caption="v11L Normalize Matris")

st.sidebar.markdown("---")

# YOLOv8n Verileri (Kıyaslama için)
st.sidebar.markdown("### 🥈 YOLOv8n (Eski Veriler)")
if os.path.exists("results_v8n.png"):
    st.sidebar.image("results_v8n.png", caption="v8n Eğitim Grafikleri")
if os.path.exists("confusion_matrix_v8n_normalized.png"):
    st.sidebar.image("confusion_matrix_v8n_normalized.png", caption="v8n Normalize Matris")

# --- ANA EKRAN ---
st.title("🛣️ Akıllı Yol Hasarı Tespit Paneli (YOLOv11L)")

# 📸 FOTOĞRAF ANALİZİ
st.subheader("📸 Fotoğraf Analizi")
uploaded_file = st.file_uploader("Bir fotoğraf seçin...", type=['jpg', 'jpeg', 'png'])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    
    # Kendi modelinle (v11L) tahmin yap
    results = model.predict(image, imgsz=1280, conf=0.25)
    
    # Renk düzeltme (BGR -> RGB)
    res_plotted = results[0].plot()
    res_plotted_rgb = cv2.cvtColor(res_plotted, cv2.COLOR_BGR2RGB)
    
    col1, col2 = st.columns(2)
    with col1:
        st.image(image, caption="Orijinal Görüntü", use_container_width=True)
    with col2:
        st.image(res_plotted_rgb, caption="v11L Analiz Sonucu", use_container_width=True)

st.markdown("---")

# 🎥 VİDEO ANALİZİ
st.subheader("🎥 Video Analiz Modülü")
video_upload = st.file_uploader("Bir video dosyası seçin...", type=['mp4', 'mov', 'avi'])

if video_upload:
    tfile = tempfile.NamedTemporaryFile(delete=False) 
    tfile.write(video_upload.read())
    
    cap = cv2.VideoCapture(tfile.name)
    st_frame = st.empty()
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # v11L ile video analizi
        results = model.predict(frame, conf=0.25, imgsz=640)
        
        # Renk düzeltme
        res_plotted = results[0].plot()
        res_plotted_rgb = cv2.cvtColor(res_plotted, cv2.COLOR_BGR2RGB)
        
        st_frame.image(res_plotted_rgb, use_container_width=True)
    
    cap.release()
    st.success("Video analizi bitti.")