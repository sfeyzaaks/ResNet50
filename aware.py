GÖREV 1
import cv2
import numpy

path = "resources/horse.jpg"
img = cv2.imread(path)
cv2.imshow("horse picture", img)
cv2.waitKey(0)
cv2.imwrite("horse.png", img)



GÖREV 2
import cv2
import numpy as np

path = "resources/horse.jpg"
img = cv2.imread(path)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray picture", img_gray)
cv2.imshow("horse", img)
cv2.waitKey(0)

GÖREV 3
import cv2
import numpy as np

path = "resources/horse.jpg"
img = cv2.imread(path)
cv2.imshow("the original one", img)
print(img.shape)
img_resized = cv2.resize(img, (650,440))
img_cropped = img_resized[0:220,0:300]
cv2.imshow("the resized one", img_resized)
cv2.imshow("the horse head", img_cropped)
cv2.waitKey(0)
cv2.waitKey(0)
#######alternative
path = "resources/horse.jpg"
img = cv2.imread(path)
cv2.imshow("the original one", img)
print(img.shape)
img_resized = cv2.resize(img, (650,440))
img_cropped = img_resized[0:220,0:300]
img_cropppedone = cv2.resize(img_cropped , (img.shape[1], img.shape[0]))
cv2.imshow("cropped", img_cropppedone)
cv2.imshow("the resized one", img_resized)
cv2.imshow("the horse head", img_cropped)
cv2.waitKey(0)
cv2.waitKey(0)


GÖREV 4
import cv2
import numpy as np

path = "resources/horse.jpg"
img = cv2.imread(path)
img_1 = np.uint8(img)
cv2.rectangle(img_1 , (0,0), (564,846), (0,255,255),10)

cv2.imshow("square", img_1)
cv2.waitKey(0)

GÖREV 5
import cv2
import numpy as np

path = "resources/horse.jpg"
img = cv2.imread(path)
img_1 = np.uint8(img)
cv2.rectangle(img_1 , (0,0), (564,846), (0,255,255),10)
img_gray = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7,15), 0)
cv2.imshow("the gray one", img_gray)
cv2.imshow("the gray one with blur", img_blur)
cv2.waitKey(0)
#her pikselin üç ayrı parlaklık değeri vardır. Birçok bilgisayarlı görü algoritması daha çok renk parlaklıklarıyla ilgilendiği için gri tonlama yapma, iş yükünü 
#azaltır ve performansı arttırır. Bunun örneğini tıbbi görüntülemelerde görebiliriz. x ışını ve ultrason gibi görüntüler griye çevrilerek tanı daha kolay konulur.
#Blurlama ise sensör hatalarından kaynaklanan keskin görüntüleri yumuşatmaya yarar.Canny ise görüntüdeki sadece önemli ve keskin detaylara odaklanmamızı sağlar.
#Aynı zamanda blurlama işlemi ile günlük hayatta tanınmayan kişilerin blurlanması sağlanabilir.
#Kısacası gri tonlama ile görüntüler sadeleştirir blurlama ile ise gürültü azaltılmış olur.

GÖREV 6
path = "resources/yaprak.jpg"
img = cv2.imread(path)
cv2.imshow("yaprak resmi", img)
img_thresholding = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]

cv2.imshow("yaprak thresholding", img_thresholding)
cv2.waitKey(0)

#tresholding : her pikselin kenar kalınlığını belirlenmiş bir eşik değerle karşılaştırma işlemidir. mesela her pikselin kenar kalınlığı 
# (100,200) değerindeki alt eşik ve üst eşikle karşılaştırılabilir.
# temel amaç gürültüyü azaltmak ve nesneleri arka plandan keskin bir şekilde ayırmaktır.
#günlük hayatta somut olan belgeleri( el yazısı vs.) dijital ortama aktarılmasını sağlar.
# kalite kontrolünde belirlenmiş eşiğin üzerindeki nesnelerin ve anormalliklerin ortaya çıkmasını sağlar.
#özellikle tıbbi görüntülemede tümör doku zedelenmesinin vs. fark edilmesini sağlar.
# parmak izinin taranmasının ardından izlerin belirgin olması sağlanabilir.
# kısacası önemli görülen kısımların belirginleşmesini sağlayarak bir sonraki adıma karmaşıklaşmadan geçilmesini sağlar.

GÖREV 8(EDGE CORNER DETECTION)
import cv2
import numpy as np
path = "resources/shapes.png"
img = cv2.imread(path)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
corners = cv2.goodFeaturesToTrack(gray_img, 50, 0.01, 15, useHarrisDetector=True, k=0.1) #köşe tespiti için kıullanılan fonksiyon
corner = np.int32(corners)
for c in corner:
    x,y = c.ravel() #birden fazla boyutlu olan diziyi tek bri diziye indirgedi
    img = cv2.circle(img,(x,y),5,(0,0,255),-1)
cv2.imshow("corner detection",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
###edge
import cv2

path = "resources/shapes.png"
img = cv2.imread(path)
blurred = cv2.GaussianBlur(img, (5,5),0)
edged = cv2.Canny(blurred,100,200)
cv2.imshow("edged",edged)
cv2.waitKey(0)

GÖREV 9
import cv2
import numpy as np

path = "resources/horse.jpg"
img_original = cv2.imread(path)
gray_img = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)
print(gray_img.shape)
print(img_original.shape)#verilen (856,564,3) değerinde 0.karakter yüksekliği 1.karakter genişliği 2.karakter kanal sayısını verir yani renkli olduğunun göstergesidir
print(gray_img.dtype)
print(img_original.dtype)#verilen dtype uint8 tam sayı olduğunun göstergesidir
print(gray_img.size) #yüksesklik*genişlik
print(img_original.size)#yükseklik*genişlik*kanal sayısı

GÖREV 10

import cv2
import numpy as np
path = "resources/horse.jpg"
img = cv2.imread(path)
img_canny = cv2.Canny(img,100,200)
kernel = np.ones((5,5),np.uint8)
img_dilate = cv2.dilate(img_canny,kernel,iterations = 1)
img_erosion = cv2.erode(img_dilate,kernel,iterations =1)
kapali_img = cv2.morphologyEx(img_erosion , cv2.MORPH_CLOSE , kernel)
cv2.imshow("img",kapali_img)
cv2.waitKey(0)

GÖREV 11
import cv2
import numpy as np

path = "resources/horse.jpg"
img =cv2.imread(path)
img_reverse = cv2.flip(img,0)#alta döndürür
img_reverse_1 = cv2.flip(img,1) #sağa döndürür
img_reverse_2 =cv2.flip(img,-1) #sağa ve alta çevirir
cv2.imshow("flip metodu",img_reverse)
cv2.waitKey(0)




GÖREV 12
import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

while True:
    ret , frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30), flags=cv2.CASCADE_SCALE_IMAGE)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.imshow("yüz tanıma", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

GÖREV 14
import cv2
import numpy as np
def geri_cagirma(x):
    pass
path = "resources/circles.jpg"
cv2.namedWindow("trackbars")
cv2.resizeWindow("trackbars", 640, 540)
cv2.createTrackbar("hue min", "trackbars", 0, 179, geri_cagirma )
cv2.createTrackbar("hue max", "trackbars", 179, 179, geri_cagirma )
cv2.createTrackbar("sat min", "trackbars", 0, 255, geri_cagirma )
cv2.createTrackbar("sat max", "trackbars", 255, 255, geri_cagirma )
cv2.createTrackbar("value min", "trackbars", 0, 255, geri_cagirma )
cv2.createTrackbar( "value max", "trackbars", 255, 255, geri_cagirma )


while True:
    img =cv2.imread(path)
    img_resize = cv2.resize(img, (640, 480))
    img_hsv = cv2.cvtColor(img_resize, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("hue min", "trackbars")
    h_max = cv2.getTrackbarPos("hue max", "trackbars")
    sat_min = cv2.getTrackbarPos("sat min", "trackbars")
    sat_max = cv2.getTrackbarPos("sat max", "trackbars")
    value_min = cv2.getTrackbarPos("value min", "trackbars")
    value_max = cv2.getTrackbarPos("value max", "trackbars")
    lower = np.array([h_min, sat_min, value_min])
    upper = np.array([h_max, sat_max, value_max])
    mask = cv2.inRange(img_hsv, lower, upper)
    result = cv2.bitwise_or(img_resize,img_resize, mask= mask)
    horstack = np.hstack((img_hsv, result))
    cv2.imshow("trackbars", horstack)
    #29,73,165 / 57, 224, 225

    if cv2.waitKey(1 ) & 0xFF == ord('q'):
        break

GÖREV 15
import cv2
import numpy as np
def geri_cagirma(x):
    pass
cap = cv2.VideoCapture(0)

cv2.namedWindow("trackbars")
cv2.resizeWindow("trackbars", 640, 540)
cv2.createTrackbar("hue min", "trackbars", 0, 179, geri_cagirma )
cv2.createTrackbar("hue max", "trackbars", 179, 179, geri_cagirma )
cv2.createTrackbar("sat min", "trackbars", 0, 255, geri_cagirma )
cv2.createTrackbar("sat max", "trackbars", 255, 255, geri_cagirma )
cv2.createTrackbar("value min", "trackbars", 0, 255, geri_cagirma )
cv2.createTrackbar( "value max", "trackbars", 255, 255, geri_cagirma )


while True:
    success, img = cap.read()
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("hue min", "trackbars")
    h_max = cv2.getTrackbarPos("hue max", "trackbars")
    sat_min = cv2.getTrackbarPos("sat min", "trackbars")
    sat_max = cv2.getTrackbarPos("sat max", "trackbars")
    value_min = cv2.getTrackbarPos("value min", "trackbars")
    value_max = cv2.getTrackbarPos("value max", "trackbars")
    lower = np.array([h_min, sat_min, value_min])
    upper = np.array([h_max, sat_max, value_max])
    mask = cv2.inRange(img_hsv, lower, upper)
    result = cv2.bitwise_and(img,img, mask= mask)
    cv2.imshow("trackbars", result)
    #29,73,165 / 57, 224, 225

    if cv2.waitKey(1 ) & 0xFF == ord('q'):
        break

GÖREV 22
ui_2python.py
