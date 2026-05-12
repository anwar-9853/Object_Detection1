import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from gtts import gTTS
from playsound import playsound
import os

def speech(text):
    print("Speaking:", text)
    if not text.strip(): return
    
    if not os.path.exists("./sounds"):
        os.makedirs("./sounds")
        
    output = gTTS(text=text, lang="en", slow=False)
    sound_file = os.path.abspath("./sounds/sound.mp3")
    output.save(sound_file)
    
    try:
        playsound(sound_file)
    except Exception as e:
        print(f"Audio error: {e}")

# Automatically find the path to your renamed cfg file
current_dir = os.path.dirname(os.path.abspath(__file__))
cfg_path = os.path.join(current_dir, "yolov4-tiny.cfg")
weights_path = os.path.join(current_dir, "yolov4-tiny.weights")

if not os.path.exists(cfg_path):
    print(f"Error: Still can't find {cfg_path}. Did you rename the .txt file?")
    exit()

video = cv2.VideoCapture(0)
detected_items = []

print("Camera active. Press 'q' to finish.")

while True:
    ret, frame = video.read()
    if not ret: continue

    try:
        # cvlib will now find the correctly named .cfg file
        bbox, label, conf = cv.detect_common_objects(frame, model='yolov4-tiny')
        
        frame = draw_bbox(frame, bbox, label, conf)
        cv2.imshow("Object Detection", frame)
        
        for item in label:
            if item not in detected_items:
                detected_items.append(item)
                print(f"Detected: {item}")

    except Exception as e:
        print(f"Model Error: {e}")
        break

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()

if detected_items:
    speech(f"I detected {', '.join(detected_items)}")