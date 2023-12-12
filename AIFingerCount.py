from flask import Flask, Response, jsonify
import cv2
import mediapipe as mp

app = Flask(__name__)

# Initialize MediaPipe for hand pose estimation
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Initialize camera
cap = cv2.VideoCapture(0)
hands = mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.4,
    min_tracking_confidence=0.6)

def generate_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(frame)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            ret, buffer = cv2.imencode('.jpg', cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/finger_count', methods=['GET'])
def get_finger_count():
    success, image = cap.read()
    if not success:
        return jsonify({'error': 'Unable to read the camera.'}), 500

    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    finger_count = 0

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            hand_landmarks_list = []
            for landmark in hand_landmarks.landmark:
                hand_landmarks_list.append([landmark.x, landmark.y])

            if hand_landmarks_list[4][0] > hand_landmarks_list[3][0]:
                finger_count += 1
            if hand_landmarks_list[8][1] < hand_landmarks_list[6][1]:
                finger_count += 1
            if hand_landmarks_list[12][1] < hand_landmarks_list[10][1]:
                finger_count += 1
            if hand_landmarks_list[16][1] < hand_landmarks_list[14][1]:
                finger_count += 1
            if hand_landmarks_list[20][1] < hand_landmarks_list[18][1]:
                finger_count += 1

    return jsonify({'finger_count': finger_count})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
  

cap.release()
