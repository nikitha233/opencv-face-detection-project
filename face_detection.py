import cv2
import speech_recognition as sr

# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Start webcam
cap = cv2.VideoCapture(0)

# Speech recognizer
recognizer = sr.Recognizer()
microphone = sr.Microphone()
spoken_text = ""

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize frame for better speed
    frame = cv2.resize(frame, (640, 480))

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Improved face detection accuracy
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=7,
        minSize=(60, 60)
    )

    # Face count
    face_count = len(faces)

    # Draw rectangle and label
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Face Detected",
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2)

    # Display face count
    cv2.putText(frame, f"Faces Detected: {face_count}",
                (20, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2)

    # Speech to Text (non-blocking)
    try:
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.3)
            audio = recognizer.listen(source, timeout=1, phrase_time_limit=3)
            spoken_text = recognizer.recognize_google(audio)
    except:
        pass

    # Display spoken text
    cv2.putText(frame, f"Speech: {spoken_text}",
                (20, 450),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 255, 0),
                2)

    # Show output
    cv2.imshow("Advanced Face Detection System", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
