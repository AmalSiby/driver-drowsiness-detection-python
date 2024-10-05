from detect_drowsiness import get_webcam_frame, process_webcam_frame
from laneDetection import trigger_lane_detection, is_deviated
import playsound
from threading import Thread
import time

def sound_alarm(path):
    # play an alarm sound
    playsound.playsound(path)

Thread(target = trigger_lane_detection).start()

while True:
    webcam_frame = get_webcam_frame()
    is_drowsy = process_webcam_frame(webcam_frame)

    # check to see if an alarm file was supplied,
    # and if so, start a thread to have the alarm
    # sound played in the background
    if  is_drowsy or (is_drowsy and is_deviated()):
        t = Thread(target=sound_alarm,
                   args=("alarm.wav",), daemon=True)
        t.start()

# detect_drowsiness_clean_up()
# lane_detection_clean_up()``