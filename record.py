import numpy as np
import cv2
from PIL import Image
import threading


import time
import sys

import mss

para = None

loop = True

frames = []


def create( frames ):

    count = 0


    print( len(frames) )

    for i in range(0, len(frames)):
        print(str(i)+'/'+str(len(frames)))
        f = open('./frames/frame-'+str(count)+'.txt', 'w')
        f.write("\r"+frames[i])
        count += 1   

    f.close()
    
    print('END!')
    time.sleep(1000)


def gen():

    

    

    print('bad apple')

    global para

    frame = ""


    global loop

    while loop:



        try:

            image = para

    
            image = cv2.pyrDown(image) # 배열 사이즈 축소
            image = cv2.pyrDown(image) # 배열 사이즈 축소
            image = cv2.pyrDown(image) # 배열 사이즈 축소



            y, x, z = np.shape(image) # 사이즈 가져오기



            for i in range(y):

                for j in range(x):


                    if image[i][j][0] >= 35 and image[i][j][1] >= 35 and image[i][j][2] >= 35:
                        frame = frame + "□";


                    else:
                        frame = frame + "■";


                frame = frame + "\n";



            frames.append(frame)
            print( len(frames) , loop )


            sys.stdout.flush()
            frame = ""


        except Exception as e:
            print(e)


    return 0



if __name__ == '__main__':

    print('ready')

    time.sleep(3)

    print('start!')

    video_thread=threading.Thread(target=gen)

    video_thread.start()


    



    with mss.mss() as sct:
        # Part of the screen to capture
        monitor = {"top": 100, "left": 0, "width": 1200, "height": 660}


        try:
            while loop:
                      
                    

                para = np.array(sct.grab(monitor))



        except KeyboardInterrupt:


            loop = False

          
            create( frames )
             



