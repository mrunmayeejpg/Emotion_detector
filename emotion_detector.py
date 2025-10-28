#emotion detector
from deepface import DeepFace
import cv2

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    try:
        # Analyze the frame for emotions
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emotion = result[0]['dominant_emotion']

        # Display emotion text on screen
        if emotion.lower() == 'happy':
            text = "😊 You are smiling!"
            color = (0, 255, 0)  # green
        else:
            text = f"Emotion: {emotion.capitalize()}"
            color = (255, 255, 255)  # white

        # Draw the text
        cv2.putText(frame, text, (50, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.1, color, 3, cv2.LINE_AA)

    except:
        # If no face is detected
        cv2.putText(frame, "No face detected", (50, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.1, (0, 0, 255), 2, cv2.LINE_AA)

    # Show the webcam window
    cv2.imshow('Emotion Detector', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
