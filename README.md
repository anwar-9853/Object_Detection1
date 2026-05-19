# 🍎 Real-Time Object Detection and Food Nutrition Analysis

An AI-powered computer vision application that combines **real-time object detection** with **food nutrition analysis** using Python, YOLOv4-Tiny, OpenCV, and the CalorieNinjas API.

The system detects objects from a live webcam feed, announces detected objects through voice feedback, and retrieves nutrition information for food items using an external API.

---

# 📌 System Architecture


                         ┌──────────────────────┐
                         │      Webcam          │
                         │   Live Video Feed    │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │       OpenCV         │
                         │  Capture Video Frame │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │        cvlib         │
                         │    YOLOv4-Tiny       │
                         │   Object Detection   │
                         └──────────┬───────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
                    ▼                               ▼
         ┌────────────────────┐         ┌────────────────────┐
         │ Bounding Box Draw  │         │  Detected Objects  │
         │ Labels + Confidence│         │  Unique Item Store │
         └──────────┬─────────┘         └──────────┬─────────┘
                    │                               │
                    ▼                               ▼
         ┌────────────────────┐         ┌────────────────────┐
         │ Live Detection UI  │         │   Food Detection   │
         │ Display with OpenCV│         │    Food Name       │
         └────────────────────┘         └──────────┬─────────┘
                                                    │
                                                    ▼
                                        ┌────────────────────┐
                                        │ CalorieNinjas API  │
                                        │ Nutrition Analysis │
                                        └──────────┬─────────┘
                                                    │
                                                    ▼
                                        ┌────────────────────┐
                                        │ Nutrition Results  │
                                        │ Fat, Protein, etc. │
                                        └──────────┬─────────┘
                                                    │
                                                    ▼
                                        ┌────────────────────┐
                                        │       gTTS         │
                                        │ Text-to-Speech     │
                                        └──────────┬─────────┘
                                                    │
                                                    ▼
                                        ┌────────────────────┐
                                        │     playsound      │
                                        │  Voice Playback    │
                                        └────────────────────┘
```

---

# 🚀 Features

## 👁️ Real-Time Object Detection

- Detects common objects using webcam
- Uses YOLOv4-Tiny for fast object detection
- Displays bounding boxes and labels
- Provides voice feedback using Text-to-Speech
- Stores unique detected objects

---

## 🍔 Food Nutrition Analysis

Retrieves nutritional information for food items using the CalorieNinjas API.

### Displays:

- Saturated Fat
- Total Fat
- Carbohydrates
- Protein
- Sugar
- Sodium
- Cholesterol

---

# 🛠️ Technologies Used

- Python
- OpenCV (`cv2`)
- cvlib
- YOLOv4-Tiny
- gTTS
- playsound
- Requests API
- CalorieNinjas API

---

# 📂 Project Structure

```text
project-folder/
│
├── object_detection.py
├── food.py
├── requirements.txt
├── yolov4-tiny.cfg
├── yolov4-tiny.weights
├── sounds/
│   └── sound.mp3
└── README.md
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/realtime-object-detection.git
cd realtime-object-detection
```

---

## 2. Install Required Packages

```bash
pip install -r requirements.txt
```

---

# 📦 Requirements

```text
opencv-python
cvlib
gtts
playsound==1.2.2
tensorflow
numpy
pillow
requests
```

---

# ⬇️ Download YOLOv4-Tiny Files

Download and place these files in the project directory:

```text
yolov4-tiny.cfg
yolov4-tiny.weights
```

---

# 👁️ Real-Time Object Detection

## ▶️ Run the Application

```bash
python object_detection.py
```

---

## 🧠 How It Works

1. Opens the webcam
2. Captures video frames
3. Detects objects using YOLOv4-Tiny
4. Draws bounding boxes
5. Announces detected objects using voice

---

## 📌 Example Output

```text
Camera active. Press 'q' to finish.

Detected: person
Detected: laptop
Detected: bottle

Speaking: I detected person, laptop, bottle
```

---

# 🍎 Food Nutrition Analysis

## ▶️ Run the Food Nutrition Script

```bash
python food.py
```

---

## 📌 Food API Function

```python
food_facts("pizza")
```

---

## 📊 Example Output

```text
Saturated Fat: 3.3
Total Fat: 10.4
Carbs: 33.2
Protein: 12.1
Sugar: 4.2
Sodium: 640
Cholesterol: 18
```

---

# 🌐 Food Nutrition API

The project uses the CalorieNinjas API to retrieve nutritional information.

## API Endpoint

```text
https://api.calorieninjas.com/v1/nutrition
```

---

# 📌 Future Improvements

- Integrate food detection with nutrition analysis
- Detect fruits and vegetables automatically
- Add speech output for nutrition facts
- Save detection history
- Build a GUI dashboard
- Deploy as desktop application
- Add mobile app support
- Add calorie tracking history

---

# ⚠️ Troubleshooting

## Webcam Not Working

- Ensure webcam permissions are enabled
- Close other applications using the camera

---

## Audio Not Playing

Try installing:

```bash
pip install pygobject
```

---

## Missing YOLO Files

Ensure these files exist:

```text
yolov4-tiny.cfg
yolov4-tiny.weights
```

---

# 👨‍💻 Author

Developed by **Anwar Mohammed**

- Biomedical Engineering Student
- AI & Computer Vision Enthusiast

---

# 📜 License

This project is open-source and available under the MIT License.

---
