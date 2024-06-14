import cv2, time
import numpy as np
from djitellopy import Tello
from modules.drone_calculation_module import *
from modules.frame_module import *

def main():

    #main loop
    while True:
        #frame from camera
        frame = drone.get_frame_read().frame

        #find all faces
        faces = find_face(frame)

        # If a face is detected, track it
        if len(faces) > 0:

            # Get the largest face
            largest_face = max(faces, key=lambda f: f[2] * f[3])

            # Get the center coordinates of the fac
            f_x, f_y,f_w, f_h, dis_x, dis_y, area = center_and_distance_calculations(largest_face, frame)

            #calculate speed and other stuff for drone
            lf, fb, up ,yaw_speed = drone_calculation(dis_x, dis_y, area)

            # Draw a rectangle around the face
            draw(frame, f_x, f_y,f_w, f_h)

            drone.send_rc_control(lf, fb, up, yaw_speed)
        
        #show the frame
        cv2.imshow("Drone Face Tracking", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    drone = Tello()
    drone.connect()
    drone.streamon()
    drone.takeoff()
    main()
    drone.streamoff()
    drone.land()
