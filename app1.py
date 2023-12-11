from flask import Flask, render_template, Response
from flask_cors import CORS  # Import the CORS extension
import cv2

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load Haar Cascade for face and eye detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

def generate_frames():
    warning_count = 0
    last_face_position = None
    last_eye_positions = []

    cap = cv2.VideoCapture(0)  # Start video capture inside the generator function

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)

            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            if last_face_position:
                dx = abs(last_face_position[0] - x)
                dy = abs(last_face_position[1] - y)
                if dx + dy > 20:
                    warning_count += 1

            last_face_position = (x, y)

            current_eye_positions = []
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
                current_eye_positions.append((ex, ey, ew, eh))

            if len(current_eye_positions) == 2 and len(last_eye_positions) == 2:
                eye_movement = 0
                for (last_eye, current_eye) in zip(last_eye_positions, current_eye_positions):
                    eye_movement += abs(current_eye[0] - last_eye[0]) + abs(current_eye[1] - last_eye[1])
                    eye_movement += abs(current_eye[2] - last_eye[2]) + abs(current_eye[3] - last_eye[3])
                if eye_movement > 20:
                    warning_count += 1

            last_eye_positions = current_eye_positions

        cv2.putText(frame, 'Warning Count: ' + str(warning_count), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

        if warning_count >= 20:
            screenshot_path = f"warning_screenshot_{warning_count}.jpg"
            cv2.imwrite(screenshot_path, frame)
            warning_count = 0

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()  # Release the video capture when generator loop ends

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
