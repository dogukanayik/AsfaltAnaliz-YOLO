# 🛣️ Akıllı Yol Hasarı Tespit Paneli (YOLOv11L vs YOLOv8n)

Bu proje, derin öğrenme algoritmaları (YOLOv11 ve YOLOv8) kullanarak asfalt üzerindeki hasarları otomatik olarak tespit eden ve iki farklı modelin çıkarımlarını kullanıcıya sunan bir web tabanlı analiz arayüzüdür.

## Model Dosyası

https://drive.google.com/file/d/1F5PsXM9qOGQ7sfOXBb1hbpivl34JehHq/view?usp=drive_link

## 🖼️ Uygulama Arayüzü ve Tespit Performansı

Sistem, yüklenen fotoğraflar ve videolar üzerinde hasar türlerini (Çukur, Çatlak, Timsah Sırtı vb.) gerçek zamanlı olarak sınıflandırmaktadır.

### 📸 Fotoğraf Analiz Testleri
Modelin görsel üzerindeki hasarları başarıyla çerçevelediği ve sınıflandırdığı örnekler aşağıdadır:

| Orijinal Görüntü | YOLOv11L Analiz Sonucu |
| :---: | :---: |
| <img src="https://github.com/user-attachments/assets/cb5932fd-e360-4c58-ac4a-e909cf97e16f" width="500"> | <img src="https://github.com/user-attachments/assets/d3186340-2d4b-465a-a6c2-f4997339c969" width="500"> |

### 🎥 Video Analiz Modülü
Video akışı sırasında anlık tespitler yapılarak yol güvenliği analizi gerçekleştirilmektedir:
<img src="https://github.com/user-attachments/assets/efc80522-95da-4549-b109-7f12ec5e0e33" width="900">

---

## 📊 Model Başarı Metrikleri (Performance Metrics)

Eğitilen modelin (Nano mimarisi üzerine inşa edilmiş) detaylı başarı oranları ve doğrulama sonuçları aşağıdadır:

## Confusion Matrix

 <img width="1460" height="1095" alt="Image" src="https://github.com/user-attachments/assets/ab98202c-18fc-47d0-bd7b-012770df8bb7" />

## Education Graphics

 <img width="1460" height="730" alt="Image" src="https://github.com/user-attachments/assets/065c45dc-d8b1-4cab-bd4e-6dcb74b98c66" />

### 🏆 Genel Performans Özeti
Model, 100 epoch sonunda **%41.8 mAP50** genel başarı skoruna ulaşmıştır. Özellikle **Block (Blok Çatlak)** hasarlarında **%89.3** gibi yüksek bir doğruluk sergilemektedir.

<img src="https://github.com/user-attachments/assets/8fcfea39-858a-4546-adc0-deff807b3de0" width="900">
<img src="https://github.com/user-attachments/assets/61fe4f27-d7ab-4689-913c-c11c4712dc8d" width="900">

### 🔍 Sınıf Bazlı mAP50 Skorları
| Hasar Sınıfı | Başarı (mAP50) | Durum |
| :--- | :--- | :--- |
| **Block (Blok Çatlak)** | **%89.3** | **Mükemmel** |
| **Pothole (Çukur)** | **%63.9** | **Başarılı** |
| **Transverse (Enine Çatlak)** | **%58.8** | **İyi** |
| **Alligator (Timsah Sırtı)** | %35.0 | Orta |
| **Longitudinal (Boyuna Çatlak)** | %26.1 | Zayıf |

---

## 🛠️ Teknik Altyapı
* **Yapay Zeka:** YOLOv11L (Referans) ve YOLOv8n (Hızlı Çıkarım).
* **Arayüz:** Streamlit Web Framework.
* **Görüntü İşleme:** OpenCV & Pillow.
* **Model:** 3 milyon parametre, ~6.4MB ağırlık dosyası (`best.pt`).

---

## 🚀 Hızlı Başlangıç

1. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install -r requirements.txt
2. Uygulamayı çalıştır
   streamlit run app.py
