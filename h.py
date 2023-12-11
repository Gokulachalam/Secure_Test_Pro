import cv2

# Load Haar Cascade for face and eye detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Start video capture
cap = cv2.VideoCapture(0)

warning_count = 0
last_face_position = None
last_eye_positions = []

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

        # Draw rectangle around face (head tracking)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Head movement detection
        if last_face_position:
            dx = abs(last_face_position[0] - x)
            dy = abs(last_face_position[1] - y)
            if dx + dy > 20:  # Adjusted threshold for head movement
                warning_count += 1

        last_face_position = (x, y)

        # Eye movement detection
        current_eye_positions = []
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
            current_eye_positions.append((ex, ey, ew, eh))

        # Check if the eye positions have significantly changed
        if len(current_eye_positions) == 2 and len(last_eye_positions) == 2:
            eye_movement = 0
            for (last_eye, current_eye) in zip(last_eye_positions, current_eye_positions):
                eye_movement += abs(current_eye[0] - last_eye[0]) + abs(current_eye[1] - last_eye[1])
                eye_movement += abs(current_eye[2] - last_eye[2]) + abs(current_eye[3] - last_eye[3])
            if eye_movement > 20:  # Adjusted threshold for eye movement
                warning_count += 1

        last_eye_positions = current_eye_positions

    # Display the warning count
    cv2.putText(frame, 'Warning Count: ' + str(warning_count), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    if warning_count >= 20:
        # Save the frame as an image
        screenshot_path = f"warning_screenshot_{warning_count}.jpg"
        cv2.imwrite(screenshot_path, frame)
        
        # Reset warning count after taking a screenshot
        warning_count = 0

    cv2.imshow('Frame', frame)

    key = cv2.waitKey(1)
    if key == 27:  # Exit on ESC
        break

cap.release()
cv2.destroyAllWindows()
