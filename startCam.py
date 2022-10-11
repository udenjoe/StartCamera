
from picamera import PiCamera
import time

with PiCamera(sensor_mode=6) as camera:
        camera.video_stabilization = True
        camera.start_preview()
        time.sleep(86400) #needed to see in ui
