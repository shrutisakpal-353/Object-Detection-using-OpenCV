# Object-Detection-using-OpenCV
This project aims to develop a system that can detect objects in real time using a webcam and utilizes a speech system to  announce the list of objects detected. 
In this project, I used the cv2 (OpenCV) library and cvlib (a high-level computer vision library) to perform real-time object detection through your computer's webcam. The code can identify various common objects in the webcam feed and then generate speech output to describe the objects it detects.
This project provided an excellent opportunity for me to learn more about the capabilities of OpenCV and computer vision libraries. I was astounded at how simple it was to identify objects and integrate vocal output. It opens up a whole new world of possibilities, ranging from assisting visually challenged users to developing interactive applications that use real-time object identification.
Libraries Used:
cv2: OpenCV is an incredibly powerful computer vision library that provides a wide range of functionalities for image and video processing.
cvlib: A wrapper around OpenCV, which simplifies common computer vision tasks like object detection.
gtts (Google Text-to-Speech): A Python library that converts text into speech.
playsound: Used to play the generated speech as an audio output.

How it Works:
The script initializes the webcam capture using cv2.VideoCapture(0).
It then continuously reads frames from the webcam and performs object detection using cvlib.detect_common_objects(frame). This function returns bounding box coordinates, object labels, and confidence scores for each detected object.
The detected objects are then visualized on the frame using cvlib.object_detection.draw_bbox.
The program waits for the space key to be pressed, at which point it stops the object detection loop and proceeds to the speech generation part.
The script prepares a sentence describing the detected objects based on the labels and uses gTTS (Google Text-to-Speech) to convert the sentence into speech.
The generated speech is saved as an MP3 file and played using playsound.
