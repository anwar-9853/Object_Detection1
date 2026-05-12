# Real-Time Object Detection and Food Nutrition Analysis

This project is an AI-powered **Real-Time Object Detection System** combined with a **Food Nutrition Analysis API** using Python.
The application detects common objects from a live webcam feed and can also retrieve nutritional information about food items using the CalorieNinjas API.

---

## Features

### Real-Time Object Detection

* Detects common objects using webcam
* Uses **YOLOv4-Tiny** for fast detection
* Displays bounding boxes and labels
* Provides voice feedback using Text-to-Speech
* Stores unique detected objects

### Food Nutrition Analysis

* Retrieves nutrition information for food items
* Uses the **CalorieNinjas API**
* Displays:

  * Saturated fat
  * Total fat
  * Carbohydrates
  * Protein
  * Sugar
  * Sodium
  * Cholesterol

---

## Technologies Used

* Python
* OpenCV (`cv2`)
* cvlib
* YOLOv4-Tiny
* gTTS
* playsound
* Requests API
* CalorieNinjas API

---

## Project Structure

```bash id="rl9lzc"
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

## Installation

### 1. Clone the Repository

```bash id="gmb0aj"
git clone https://github.com/yourusername/realtime-object-detection.git
cd realtime-object-detection
```

---

### 2. Install Required Packages

```bash id="nn1g60"
pip install -r requirements.txt
```

---

## Requirements

```txt id="z3kl9m"
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

## Download YOLOv4-Tiny Files

Download and place these files in the project directory:

* `yolov4-tiny.cfg`
* `yolov4-tiny.weights`

---

# Real-Time Object Detection

## Run the Application

```bash id="6l9j0h"
python object_detection.py
```

---

## How It Works

1. Opens the webcam
2. Captures video frames
3. Detects objects using YOLOv4-Tiny
4. Draws bounding boxes
5. Announces detected objects using voice

---

## Example Output

```bash id="c6h3wy"
Camera active. Press 'q' to finish.

Detected: person
Detected: laptop
Detected: bottle

Speaking: I detected person, laptop, bottle
```

---

# Food Nutrition Analysis

## Run the Food Nutrition Script

```bash id="o0r2h4"
python food.py
```

---

## Food API Function

```python id="25j85m"
food_facts("pizza")
```

---

## Example Output

```bash id="zq69f8"
Saturated Fat: 3.3
Total Fat: 10.4
Carbs: 33.2
Protein: 12.1
Sugar: 4.2
Sodium: 640
Cholesterol: 18
```

---

## Food Nutrition API

The project uses the CalorieNinjas API to retrieve nutritional information.

API Endpoint:

```bash id="0n6n3h"
https://api.calorieninjas.com/v1/nutrition
```

---

## Future Improvements

* Integrate food detection with nutrition analysis
* Detect fruits and vegetables automatically
* Add speech output for nutrition facts
* Save detection history
* Build a GUI dashboard
* Deploy as desktop application

---

## Troubleshooting

### Webcam Not Working

* Ensure webcam permissions are enabled
* Close other applications using the camera

---

### Audio Not Playing

Try installing:

```bash id="xb2n9d"
pip install pygobject
```

---

### Missing YOLO Files

Ensure these files exist:

* `yolov4-tiny.cfg`
* `yolov4-tiny.weights`

---

## Author

Developed by Anwar Mohammed

---

## License

This project is open-source and available under the MIT License.
