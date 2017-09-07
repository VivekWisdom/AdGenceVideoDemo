import cv2
import numpy as np
from matplotlib import pyplot as plt
import argparse
import os
import sys

def match_img(query_image, train_image, count, current_video_time_ms):
    global accuracy_dict
    #Create SIFT Object
    sift = cv2.xfeatures2d.SIFT_create()

    # find the keypoints and descriptors with SIFT
    query_kp, query_des = sift.detectAndCompute(query_image,None)
    train_kp, train_des = sift.detectAndCompute(train_image,None)

    # FLANN parameters
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks=50)   # or pass empty dictionary

    flann = cv2.FlannBasedMatcher(index_params,search_params)

    matches = flann.knnMatch(query_des,train_des,k=2)
 
    # Need to draw only good matches, so create a mask
    matchesMask = [[0,0] for i in range(len(matches))]

    good_matches_count = 0
    # ratio test as per Lowe's paper
    for i,(m,n) in enumerate(matches):
        if m.distance < 0.8 * n.distance:
            matchesMask[i]=[1,0]
            good_matches_count += 1
    mlen = len(matches)

    accuracy = good_matches_count/len(query_des) * 100
    accuracy_dict[current_video_time_ms] = accuracy

    # print('Matches length {}, Good Matches Count {}, and accuracy list is {}'.format(mlen, good_matches_count, accuracy_dict.values())
    
    draw_params = dict(matchColor = (0,255,0),
                    singlePointColor = (255,0,0),
                    matchesMask = matchesMask,
                    flags = 0)
    result_img = cv2.drawMatchesKnn(query_image,query_kp,train_image,train_kp,matches,None,**draw_params)

    # Get Path and filename setup
    path = os.getcwd() + '/outputimages/image_time/'
    file_name = os.path.basename(sys.argv[0])
    # This will write different res.png for each frame. Change this as you require
    cv2.imwrite(str(path)+'{0}_{1}.jpg'.format(current_video_time_ms, count),result_img)

    # Code to show the image side by side  
    # plt.imshow(result_img)
    # plt.show()

def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('query_image', help='path of query image to be used')
    parser.add_argument('train_video', help='path of train video to be used')
    args = parser.parse_args()

    query_image = cv2.imread(args.query_image)
    train_video = cv2.VideoCapture(args.train_video)

    global accuracy_dict
    count = 0
    print('Number of Frames: ', int(train_video.get(cv2.CAP_PROP_FRAME_COUNT)))
    fps = train_video.get(cv2.CAP_PROP_FPS)
    print('FPS of Video: ', fps)


    while True:
      success,video_image = train_video.read()
      if not success: break         # loop and a half construct is useful
      print ('Read a new frame: ', success)
      current_video_time_ms = train_video.get(cv2.CAP_PROP_POS_MSEC)
      print('CV_CAP_PROP_POS_MSEC ', current_video_time_ms)
      match_img(query_image, video_image, count, current_video_time_ms)
      count += 1
    
    value_list = list(accuracy_dict.values())
    key_index = value_list.index(max(value_list))
    print(key_index)
    print(list(accuracy_dict.keys())[key_index])
    
if __name__ == "__main__":
    accuracy_dict = {}
    main()