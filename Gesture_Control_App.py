import cv2, time, numpy as np
import mediapipe as mp
H = mp.solutions.hands
TIP = H.HandLandmark
ids - {
    "thumb" : TIP.THUMB_TIP
    "index" : TIP.INDEX__FINGER_TIP
    "middle" : TIP.MIDDLE_FINGER_TIP
    "ring" : TIP.RING_FINGER_TIP
    "pinky" : TIP.PINKY_FINGER_TIP
    }

hands = H.Hands(min_detection_confidence = 0.7, min_tracking_confidence = 0.7)
draw = mp.solutions.drawing_utils
pairs = {"middle" : ("SEPHIA", "NEAGTIVE"), "ring" : ("BLUR, GLITCH"), "pinky" : ("EDGE", "CARTOON")}
st = {k:0 for k in pairs} ; cur = SEPHIA
DEB, CAP, TT, TP = 0.6, 1.2, 30, 20
la - lc - 0 ; pinch_on - False
MAIN, POP - "Gesture Controlled Photo App", "Captured (ESC/ Close to resume)"
paused = False; freeze = None
SEPHIA_N = np.array([[0.272, 0.534, 0.131], [0.349, 0.686, 0.168], [0.393, 0.769, 0.189]])

def apply (img, t):
    if t == "SEPHIA" : return np.clip(cv2.transform(img, SEPHIA_M), 0, 255).astype(np.uint8)
    if t=="NEGATIVE" : return cv2.bitwise_not(img)
    if t == "BLUR" : return cv2.GAUSSIANBLUR(img, (15, 15), 0)
    if t == "GLITCH" : 
        h, w = img.shape[:2]; r,g,b = img[:, :, 2], img[:, :, 1], img[:, :, 0]
        return cv2.merge([np.roll(b, -int(0.02*w), 1), g, np.roll(r, int(0.04*w), 1)])
    if t == "EDGE" : return cv2.CANNY(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 80, 160)
    if t == "CARTOON" : 
        g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        e = cv2.adaptiveThreshold(cv2.medianBlur(g, 7), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)
        c = cv2.bilateralFilter(img, 9, 75, 75)
        return cv2.bitwise_and(c, c, mask = e)
    return img
cv2.imshow(MAIN, out)
if cv2.waitKey(1) & 0xFF == ord("q") : break
cap.release(); cv2.destroyAllWindows(); hands.close()