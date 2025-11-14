import cv2 as cv
def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

cv.waitKey(0)

# img = cv.imread("Photos/cat1.jpg")
# img_resized = rescaleFrame(img)

# cv.imshow("Cat", img)
# cv.imshow("Cat", img_resized)

# cv.waitKey(0)

def changeRes(width, height):
    captrure.set(3,width)
    captrure.set(4,height)

captrure = cv.VideoCapture(0)

while True:
    isTrue, frame = captrure.read()

    frame_resized = rescaleFrame(frame, scale=.20)
    # changedres = changeRes(3,4)
    cv.imshow('Video',frame)
    cv.imshow('Video Resized', frame_resized)
    # cv.imshow('Video',changedres)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

captrure.release()
cv.destroyAllWindows()