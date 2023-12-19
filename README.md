# Secure_Test_Pro

SecureTest Pro is a Flask application that combines face and eye detection to enhance the security of an online test-taking environment. It captures the webcam feed, analyzes facial features, and issues warnings based on detected movements. The application also takes a screenshot when a certain threshold of warnings is reached.





## Development Environment

This project is developed and tested on a Debian 12 Linux platform


## Features

- **Webcam Integration:** Utilizes the user's webcam to capture live video feed.
- **Face and Eye Detection:** Implements Haar Cascade classifiers to detect faces and eyes in real-time.
- **Warning System:** Issues warnings based on face and eye movements, enhancing security.
- **Screenshot Capture:** Takes a screenshot when a predefined warning threshold is reached.
- **User-friendly Web Interface:** Provides a clean and intuitive web interface for student login.





SecureTestPro/
│
├── static/
│ └── css/
│ └── style.css
│
├── templates/
│ └── index1.html
│
├── venv/ # (Optional: Virtual environment)
│
├── your_app_name.py
│
└── README.md






## Getting Started

1. Install the required packages using the following command:

    ```bash
    pip install flask opencv-python flask-cors
    ```

2. Run the Flask application:

    ```bash
    python your_app_name.py
    ```

3. Open a web browser and navigate to [http://localhost:5000](http://localhost:5000).

## How to Use

1. Enter the student's name, roll number, and password in the login form.
2. Click the "Login" button to start the webcam feed.
3. The application will issue warnings based on detected face and eye movements.
4. A screenshot will be captured if the warning count reaches the predefined threshold.

## File Structure

- `your_app_name.py`: The main Flask application file.
- `static/`: This directory is used to store static files such as CSS, JavaScript, and images.
    - `css/`: Style sheets.
- `templates/`: This directory is used to store HTML templates.
    - `index1.html`: HTML template for the user interface.

## Dependencies

- Flask
- OpenCV
- Flask-CORS

- 

## Login
![Screenshot from 2023-12-10 20-31-38](https://github.com/Gokulachalam/Secure_Test_Pro/assets/89055461/7e1b252f-c4ec-4616-8a3e-9538e8597906)












## Detection
![Screenshot from 2023-12-10 20-31-51](https://github.com/Gokulachalam/Secure_Test_Pro/assets/89055461/b6e42b1f-626b-40a5-8d8d-74f464309357)


















## Warning
![Screenshot from 2023-12-10 20-33-18](https://github.com/Gokulachalam/Secure_Test_Pro/assets/89055461/a0791ffa-da1b-4ce7-aaa3-e7cadfdeb1bf)

























## Note


Feel free to customize the application according to your requirements and security needs. Happy testing!






