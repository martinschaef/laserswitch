#!/usr/bin/python
#import numpy
#print numpy.__path__

import os, sys
import cv2
import imutils
import numpy

color = numpy.uint8([[[250,255,0 ]]])
print cv2.cvtColor(numpy.uint8([[[50,50,100 ]]]),cv2.COLOR_BGR2HSV)
print cv2.cvtColor(numpy.uint8([[[200,200,255 ]]]),cv2.COLOR_BGR2HSV)
#sys.exit(1)


redLower = (0, 55, 240) # in hsv
redUpper = (10, 130, 255) # in hsv

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    cam_readable, frame = vc.read()
else:
    cam_readable = False

while cam_readable:
    cam_readable, frame = vc.read()

    # From http://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/
    # resize the frame, blur it, and convert it to the HSV
    # color space
    frame = imutils.resize(frame, width=800)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
 
    # construct a mask for the color "red", then perform
    # a series of dilations and erosions to remove any small
    # blobs left in the mask
    mask = cv2.inRange(hsv, redLower, redUpper)
    #mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None
    #cnts = []
    # only proceed if at least one contour was found
    for cnt in cnts:
        c = cnt
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
 
        # only proceed if the radius is in a range that could
        # come from the laser pointer
        if radius > 2 and radius < 10:
            # draw the circle and centroid on the frame,
            # then update the list of tracked points
            cv2.circle(frame, (int(x), int(y)), int(radius),
                (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)
 
    
    cv2.imshow("preview", frame)
    cv2.imshow("mask", mask)

    key = cv2.waitKey(200)
    if key == 27: # exit on ESC
        cv2.imwrite("frame.png", hsv )
        break

cv2.destroyWindow("preview")