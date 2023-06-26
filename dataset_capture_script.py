# Dataset Capture Script - By: A14426 - Sat May 27 2023

# Use this script to control how your OpenMV Cam captures images for your dataset.
# You should apply the same image pre-processing steps you expect to run on images
# that you will feed to your model during run-time.

import sensor, image, time

width = 96 # Width of frame (pixels)
height = 96 # Height of frame(pixels)

sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE) # set the pixformat as GRAYSCALE (8bit/pixel)
sensor.set_framesize(sensor.QVGA) # set the framesize as QVGA 320 X 240
sensor.set_windowing(width, height) # limit the frame size as 96 x 96
sensor.skip_frames(time = 2000)

clock = time.clock()

while(True):
    clock.tick()
    img = sensor.snapshot() #capture image when clicking play button

    print(clock.fps())
