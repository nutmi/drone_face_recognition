import cv2

def find_face(frame):
    face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
        )
    return faces

def draw(frame, f_x, f_y, f_w, f_h):
    cv2.rectangle(
                frame,
                (f_x, f_y),
                (f_x + f_w, f_y + f_h),
                (0, 255, 0),
                2,
            )