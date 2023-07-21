import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from gtts import gTTS
from playsound import playsound

def speech(text):
    print(text)
    language = "en"
    out = gTTS(text = text,lang = language, slow = False)
    
    out.save("Open CV project/sounds/output.mp3")
    playsound("Open CV project/sounds/output.mp3")
    
obj = cv2.VideoCapture(0)
labels = []

while True:
    ret, frame = obj.read()
    bbox, label, conf = cv.detect_common_objects(frame)
    output = draw_bbox(frame, bbox, label, conf)
    
    cv2.imshow("Detecting Output",output)
    
    for item in label:
        if item in labels:
            pass
        else:
            labels.append(item)
    
    if cv2.waitKey(1) & 0xFF == ord(" "):
        break
        
i = 0
sentence = []
for label in labels:
    if i == 0:
        sentence.append(f"There is a {label} ")
    else:
        sentence.append(f", a {label}")
        
    i += 1
speech(" ".join(sentence))