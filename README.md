OpenCV Face Detection Project
📌 Project Description

This project implements a real-time face detection system using Python and OpenCV.
It captures live video from a webcam, detects human faces using Haar Cascade classifiers, and highlights each detected face with a bounding box. The system also displays the total number of faces detected in real time.

The project demonstrates core concepts of computer vision, image processing, and real-time video analysis, making it suitable for academic projects and beginner-level learning.

🎯 Objectives

To detect human faces in real time using a webcam

To draw bounding boxes around detected faces

To count and display the number of detected faces

To understand the working of OpenCV-based face detection

🛠️ Technologies Used

Programming Language: Python

Library: OpenCV

Algorithm: Haar Cascade Classifier

IDE: VS Code / Any Python IDE

Hardware: Webcam

📂 Project Structure
face-detection-using-opencv
│
├── face_detection.py
├── haarcascade_frontalface_default.xml
├── README.md

▶️ How the Project Runs (Process Flow)

The webcam is activated using OpenCV

Live video frames are continuously captured

Each frame is converted to grayscale for efficient processing

Haar Cascade classifier detects faces in the frame

Rectangular bounding boxes are drawn around detected faces

The total number of faces is counted and displayed

The processed video is shown in real time on the screen

The application runs continuously until the user exits

▶️ How to Run the Project

Open Command Prompt or Terminal

Navigate to the project folder

Execute the Python file

Press Q to stop the execution

📸 Output / Outcome

The webcam opens automatically

Detected faces are highlighted with green rectangles

Face count is displayed on the screen

Detection updates dynamically with movement

Real-time face detection is achieved successfully

🧠 Working Principle

The system uses a Haar Cascade Classifier, which is a machine learning-based approach trained to detect facial features. OpenCV applies this trained model to each video frame, enabling fast and efficient face detection suitable for real-time applications.

🎓 Applications

Academic and mini projects

Attendance and monitoring systems

Security and surveillance applications

Human–computer interaction systems

Base model for face recognition projects

