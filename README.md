🧠 Emotion Detector
🎯 Overview

This project uses DeepFace and OpenCV to perform real-time emotion detection through your webcam.
It captures your face, analyzes it frame by frame, and displays your dominant emotion (like Happy, Sad, Angry, etc.) on screen — instantly!

⚙️ Technologies Used

Python 3

OpenCV → handles webcam video capture and on-screen display

DeepFace → pre-trained deep learning model for facial emotion recognition

🚀 How to Run
1️⃣ Install Dependencies

Make sure you have Python 3 installed, then open your terminal and run:

pip install opencv-python deepface

2️⃣ Run the Script

Navigate to your project folder and run:

python emotion_detector.py

3️⃣ Quit Anytime

Press Q in the webcam window to exit the program.

🧩 How It Works

Opens your webcam and reads each video frame in real-time.

Uses DeepFace to detect and classify facial emotions.

Displays the detected emotion directly on the video feed.

If no face is detected, it displays “No face detected.”

If you smile, it shows a green message: “😊 You are smiling!” 😄

💡 Example Output

When you smile:

😊 You are smiling!


When you’re neutral or another emotion:

Emotion: Neutral

🌱 Possible Improvements

Add logging or analytics for emotion trends over time.

Support multiple faces in one frame.

Use other DeepFace models (like age, gender, or race analysis).

🙌 Author

Developed by Mrunmayee Kulat
A simple and fun experiment combining computer vision + AI!
