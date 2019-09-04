# -*- coding: utf-8 -*

import cv2

try:
    img = cv2.imread('c:/temp/Lenna.jpg')
    if img is None:
        print ('ファイルを読み込めません。')
        import sys
        sys.exit()
    
    cv2.line(img, (50, 50), (200, 50), (255, 0, 0))

    cv2.line(img, (50, 100), (200, 100), (0, 255, 0), 5)
    
    cv2.imwrite('c:/temp/LinesOnImage.jpg', img)
    
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    import sys
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))