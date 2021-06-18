import cv2

cascade_file = "haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(cascade_file)

img = cv2.VideoCapture(0)


def mosaic(img, rect, size):
    (x1, y1, x2, y2) = rect
    w = x2 - x1
    h = y2 - y1
    i_rect = img[y1:y2, x1:x2]
    i_small = cv2.resize(i_rect, ( size, size))
    i_mos = cv2.resize(i_small, (w, h), interpolation=cv2.INTER_AREA)
    img2 = img.copy()
    img2[y1:y2, x1:x2] = i_mos
    return img2


while(True):
    ret, frame = img.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_list = cascade.detectMultiScale(gray, minSize=(150, 150))

    for (x, y, w, h) in face_list:
        print("顔の座標=", x, y, w, h)
        mos = mosaic(frame, (x, y, x+w, y+h), 10)
        cv2.imshow('mosaic', mos )

    if cv2.waitKey(10) == 27:  # 27-> [ESC] Key
        break

img.release()
cv2.destroyAllWindows()