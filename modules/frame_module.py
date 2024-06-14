import cv2


def calculate_dis(face_center, frame_center):
    dis_x = face_center[0] - frame_center[0]
    dis_y = face_center[1] - frame_center[1]
    return dis_x, dis_y


def center_and_distance_calculations(largest_face, frame):

    f_x, f_y,f_w, f_h = largest_face
    area = f_h * f_w
    
    # Get the center coordinates of the frame and face
    face_center = (f_x + f_w // 2, f_y + f_h // 2)
    frame_center = (frame.shape[1] // 2, frame.shape[0] // 2)

    dis_x, dis_y = calculate_dis(face_center, frame_center)

    return f_x, f_y,f_w, f_h, dis_x, dis_y, area

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