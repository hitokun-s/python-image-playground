#!/usr/bin/python

import dlib
from skimage import io

image_file = 'img/test.jpg'
img = io.imread(image_file)
# Locations of candidate objects will be saved into rects
rects = []
dlib.find_candidate_object_locations(img, rects, min_size=1000)

win = dlib.image_window()
win.set_image(img)
for k, d in enumerate(rects):
    print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
            k, d.left(), d.top(), d.right(), d.bottom()))
    win.add_overlay(d)
dlib.hit_enter_to_continue()