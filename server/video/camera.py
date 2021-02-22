import os
import cv2
from video.base_camera import BaseCamera
import time

class Camera(BaseCamera):
    video_source = 1

    def __init__(self):
        if os.environ.get('OPENCV_CAMERA_SOURCE'):
            Camera.set_video_source(int(os.environ['OPENCV_CAMERA_SOURCE']))
        super(Camera, self).__init__()

    @staticmethod
    def set_video_source(source):
        Camera.video_source = source

    @staticmethod
    def frames():
        camera = cv2.VideoCapture(Camera.video_source)

        # used to record the time when we processed last frame 
        prev_frame_time = 0
        # used to record the time at which we processed current frame 
        new_frame_time = 0
  
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            _, img = camera.read()
            
            ############ CALCULATING FPS ##################
            new_frame_time = time.time()
            # Calculating the fps 
            # fps will be number of frame processed in given time frame 
            # since their will be most of time error of 0.001 second 
            # we will be subtracting it to get more accurate result
            fps = 1/(new_frame_time-prev_frame_time)
            prev_frame_time = new_frame_time
            fps = int(fps)
            fps = str(fps)
            print(f"Frame Rate = {fps}")
            ############ END CALCULATING FPS ##################
            # puting the FPS count on the frame 
            cv2.putText(img,"fps"+fps, (550, 460), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 255, 0), 2, cv2.LINE_AA) 
  

            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()