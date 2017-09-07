import cv2
import numpy as np
from matplotlib import pyplot as plt

def process_img(img_rgb, template, count):
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.5
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        #print('Hee')
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (255,0,255), 2)

    # This will write different res.png for each frame. Change this as you require
    path='C:/Users/VIVTRIPATHI/Desktop/Projects/AdGenceVideoDemo/outputimages/'
    cv2.imwrite(str(path)+'res{0}.jpg'.format(count),img_rgb)   


def main():
    vidcap = cv2.VideoCapture('test1.mp4')
    template = cv2.imread('test1.jpg',0)  # open template only once
    count = 0
    print('Number of Frames: ', int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT)))
    while True:
      success,image = vidcap.read()
      if not success: break         # loop and a half construct is useful
      print ('Read a new frame: ', success)
      process_img(image, template, count)
      count += 1

if __name__ == "__main__":
    main()