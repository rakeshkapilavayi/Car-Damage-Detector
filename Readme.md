# 🚗 Car Damage Detector

An intelligent web application built with **Streamlit** that automatically detects and classifies vehicle damage from images. This project helps car owners, insurance agents, and auto repair professionals assess vehicle damage instantly using deep learning.

---

## 🌐 Live Demo
Try it out here: **[Car Damage Detector](https://rakesh-project-car-damage-detector.streamlit.app/)**  
🎥 Watch the full presentation: **[Project Presentation](./Car-Damage-Detector-Presentation.pdf)**

---

## 🧠 Model Highlights

- ✅ Powered by a fine-tuned **ResNet50** deep learning model.
- 🔍 Detects and classifies car damage into six categories:
  - Front Normal
  - Front Crushed
  - Front Breakage
  - Rear Normal
  - Rear Crushed
  - Rear Breakage
- 🖼️ Works on varied lighting and angles.
- ⚡ Lightweight, fast, and deployable on local or cloud environments.
- 🧪 No backend server required — runs entirely in Streamlit.

---

## 🛠 Features

- Upload a car image (JPG/PNG) and get an instant prediction.
- Preprocessing with image normalization and resizing.
- Damage classification output is displayed in a clean, simple UI.
- Download-free, just run with Streamlit.

---


## 🗂️ Project Structure

 ``` Car_Damage_Detector/
 ├── model/ 
 │ └── saved_model.pth        # Trained ResNet50 weights 
 ├── app.py                   # Streamlit app logic
 ├── damage_prediction.ipynb  # End-to-end notebook    
 ├── model_helper.py          # Prediction logic using model 
 ├── requirements.txt         # Required Python libraries 
 ├── LICENSE                  # Apache 2.0 license 
 ├── Car-Damage-Detector-Presentation.pdf # PDF project presentation 
 └── README.md                # Project documentation
```

---

## 🚀 How to Run Locally

### Prerequisites
- Python 3.8+

### Clone the Repository
```bash
git clone https://github.com/vaibhavgarg2004/Car-Damage-Detector.git
cd Car-Damage-Detector
```
### 📦 Install Dependencies
```bash
pip install -r requirements.txt
```
### ▶️ Run the Streamlit App
```bash
streamlit run app.py
```

---

## 🧠 How It Works

### 🖼️ Image Upload & Display
- The user uploads a car image (JPG/PNG) through the Streamlit interface.
- The app saves the uploaded file locally (e.g., as a temporary file) and displays it in the app.

### ⚙️ Preprocessing & Model Inference
- The saved image is resized, normalized, and converted to a tensor.
- The pre-trained **ResNet50** model processes the image to classify it into one of **six damage categories**.

### 📊 Prediction Output
- The predicted damage class is instantly shown in the app interface, allowing users to quickly understand the car’s condition.

---

## Deployment
[▶️ Watch demo video](https://youtu.be/m7k9y359yA8)

