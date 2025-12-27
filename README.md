👤 OpenCV Face Detection Project
   
📌 Project Description:   

This project implements a real-time face detection system using Python and OpenCV.
It captures live video from a webcam, detects human faces using Haar Cascade classifiers, and highlights each detected face with a bounding box. The system also displays the total number of faces detected in real time.The project demonstrates core concepts of computer vision, image processing, and real-time video analysis

🎯 Objectives:

To detect human faces in real time using a webcam
To draw bounding boxes around detected faces
To count and display the number of detected faces
To understand the working of OpenCV-based face detection techniques

🛠️ Technologies Used :

Programming Language: Python
Library: OpenCV
Algorithm: Haar Cascade Classifier
IDE: VS Code / Any Python IDE
Hardware: Webcam

📂 Project Structure:

face-detection-using-opencv
│
├── face_detection.py
├── haarcascade_frontalface_default.xml
├── README.md

How the Project Runs (Step-by-Step):

The webcam is activated using OpenCV
Video frames are continuously captured
Each frame is converted to grayscale for faster processing
Haar Cascade classifier detects facial features
Bounding boxes are drawn around detected faces
The total number of detected faces is displayed
The output is shown in real time on the screen
Press Q to stop the program

Output / Outcome:

The webcam opens automatically
Detected faces are highlighted with green rectangles
The number of faces detected is displayed on the screen
The detection updates dynamically as faces move
Press Q to exit the application

🧠 Working Principle

The project uses a Haar Cascade Classifier, which is a machine learning-based approach where a cascade function is trained with positive and negative images. OpenCV uses this trained model to detect faces efficiently in real-time video streams.

⭐ Conclusion

This OpenCV face detection project successfully demonstrates real-time face detection using simple yet powerful computer vision techniques. It provides a strong base for building advanced AI-based applications and is ideal for students exploring OpenCV and machine learning concepts.
