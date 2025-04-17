import cv2
import numpy as np

def find_blue_center(img):
    # Görüntüyü BGR formatında alırız (OpenCV varsayılan olarak BGR kullanır)
    
    # Mavi renk aralığını belirle (HSV formatında)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Mavi renk için alt ve üst HSV sınırlarını belirle
    lower_blue = np.array([100, 150, 50])  # Alt HSV sınırı
    upper_blue = np.array([140, 255, 255])  # Üst HSV sınırı
    
    # Mavi alanı maskele (Sadece mavi renge sahip alanları bulmak için)
    mask = cv2.inRange(hsv_img, lower_blue, upper_blue)
    ortada = False
    blue_ratio = np.sum(mask == 255) / (img.shape[0] * img.shape[1])
    print(f"blue_ratio = {blue_ratio}")
    if blue_ratio > 0.56:
        ortada = True
    # Maskenin üzerindeki konturları bulalım
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # En büyük konturu bul (mavi alan en büyük kontur olacak şekilde)
        largest_contour = max(contours, key=cv2.contourArea)

        # Bu konturun min bound circle ile merkezini hesapla
        M = cv2.moments(largest_contour)
        if M["m00"] != 0:
            center_x = int(M["m10"] / M["m00"])
            center_y = int(M["m01"] / M["m00"])
            return center_x, center_y, ortada
        else:
            return None
    else:
        return None

# Ana fonksiyon
def main3(img):
    # Örnek bir görüntü oku
    deger = 0
    ortada = False
    # Mavi alanın merkezini bul
    center = find_blue_center(img)
    print(center)
    if center:
        center_x, center_y ,ortada = center
        print(f"Mavi alanın merkezi: ({center_x}, {center_y})")

        # Görüntüde orta noktayı işaretlemek için bir daire çizelim
        cv2.circle(img, (center_x, center_y), 10, (0, 0, 255), -1)  # Kırmızı daire

        xm = 3.7 / 720

        pos = (540 - (center_x))  * xm # (1080 // 2 - (center_x) // 2) * xm
        deger = pos
    
    else:
        deger = 0
        print("Mavi alan bulunamadı.")

    cv2.imshow("Mavi Alan ve Merkezi", img)
    cv2.waitKey(1)

    return deger, ortada


















































"""import cv2
import numpy as np
import math

# resimde kırpma işlemi yapılıyor
def get_perspective_matrices(img):

    src = np.float32([(200, 600), (200, 0), (630, 0), (630, 600)])
    w, h = image_w, image_h
    img_size=(w, h)
    dst = np.float32([(0, h), (0, 0), (w, 0), (w, h)])
    M = cv2.getPerspectiveTransform(src, dst)
    M_inv = cv2.getPerspectiveTransform(dst, src)
    img = cv2.warpPerspective(img, M, img_size, flags=cv2.INTER_LINEAR)

    return cv2.warpPerspective(img, M_inv, img_size, flags=cv2.INTER_LINEAR)

# Yolun tamamının histogramını hesaplar.
def hist(img):

    bottom_two_thirds = img[img.shape[0]//2:,:]  # full_image = img[:,:] Resmin alt yarısını almak için bottom_half = img[img.shape[0]//2:,:] , ekranı 3 e böl alt 2 sini al img[img.shape[0]//3:,:]
    return np.sum(bottom_two_thirds, axis=0)

# Pencere içindeki pikselleri bulur.
def pixels_in_window(center, margin, height, nonzerox, nonzeroy):

    topleft = (center[0] - margin, center[1] - height//2)
    bottomright = (center[0] + margin, center[1] + height//2)
    condx = (topleft[0] <= nonzerox) & (nonzerox <= bottomright[0])
    condy = (topleft[1] <= nonzeroy) & (nonzeroy <= bottomright[1])
    return nonzerox[condx & condy], nonzeroy[condx & condy]

# Görüntüden özelliklerin çıkarılmasını sağlar.
def extract_features(img):

    window_height = int(img.shape[0] // nwindows)
    nonzero = img.nonzero()
    nonzerox = np.array(nonzero[1])
    nonzeroy = np.array(nonzero[0])

    return nonzerox, nonzeroy, window_height

# Yolun sol ve sağ şeritlerini bulur.
def find_lane_pixels(img, nwindows, margin, minpix,nonzerox, nonzeroy, window_height):

    out_img = np.dstack((img, img, img))
    histogram = hist(img)
    midpoint = histogram.shape[0] // 2
    leftx_base = np.argmax(histogram[:midpoint])
    rightx_base = np.argmax(histogram[midpoint:]) + midpoint
    leftx_current = leftx_base
    rightx_current = rightx_base
    y_current = img.shape[0] + window_height // 2
    leftx, lefty, rightx, righty = [], [], [], []

    for _ in range(nwindows):
        y_current -= window_height
        center_left = (leftx_current, y_current)
        center_right = (rightx_current, y_current)
        good_left_x, good_left_y = pixels_in_window(center_left, margin, window_height, nonzerox, nonzeroy)
        good_right_x, good_right_y = pixels_in_window(center_right, margin, window_height, nonzerox, nonzeroy)
        leftx.extend(good_left_x)
        lefty.extend(good_left_y)
        rightx.extend(good_right_x)
        righty.extend(good_right_y)

        if len(good_left_x) > minpix:
            leftx_current = np.int32(np.mean(good_left_x))

        if len(good_right_x) > minpix:
            rightx_current = np.int32(np.mean(good_right_x))

    return leftx, lefty, rightx, righty, out_img

# Şerit eğrilerini hesaplar
def fit_poly(img, leftx, lefty, rightx, righty):

    maxy = img.shape[0] - 1
    miny = img.shape[0] // 3

    if len(lefty):
        maxy = max(maxy, np.max(lefty))
        miny = min(miny, np.min(lefty))

    if len(righty):
        maxy = max(maxy, np.max(righty))
        miny = min(miny, np.min(righty))

    ploty = np.linspace(miny, maxy, img.shape[0])

    if len(lefty) > 500: # if len(lefty) > 0 and len(leftx) > 0:
        left_fit = np.polyfit(lefty, leftx, 2)
    else:
        left_fit = [0, 0, 0]  

    if len(righty) > 500: # if len(righty) > 0 and len(rightx) > 0:
        right_fit = np.polyfit(righty, rightx, 2)
    else:
        right_fit = [0, 0, 0]  

    left_fitx = left_fit[0] * ploty**2 + left_fit[1] * ploty + left_fit[2]
    right_fitx = right_fit[0] * ploty**2 + right_fit[1] * ploty + right_fit[2]

    out_img = np.dstack((img, img, img))

    for i, y in enumerate(ploty):
        l = int(left_fitx[i])
        r = int(right_fitx[i])
        y = int(y)
        cv2.line(out_img, (l, y), (r, y), (0, 255, 0))

    return out_img

# Şerit eğrilerinin kıvrılma yarıçapını hesaplar.
def measure_curvature(left_fit, right_fit):

    ym = 30 / 720
    xm = 3.7 / 700

    y_eval = 700 * ym

    left_curveR = ((1 + (2 * left_fit[0] * y_eval + left_fit[1])**2)**1.5) / np.absolute(2 * left_fit[0])
    right_curveR = ((1 + (2 * right_fit[0] * y_eval + right_fit[1])**2)**1.5) / np.absolute(2 * right_fit[0])

    xl = np.dot(left_fit, [700**2, 700, 1])
    xr = np.dot(right_fit, [700**2, 700, 1])
    pos = (1280 // 2 - (xl + xr) // 2) * xm

    return left_curveR, right_curveR, pos

# Şerit tespiti için gerekli değişkenler ve işlevler tanımlanıyor
nwindows = 9
margin = 100
minpix = 60

# Ana fonksiyon
def main3(image):

    while True:
        
        img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        kernel = np.ones((5, 5), np.uint8)
        dilation = cv2.dilate(img, kernel, iterations=1)
        img = cv2.erode(dilation, kernel, iterations=1)
        _, img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

        nonzerox, nonzeroy, window_height = extract_features(img)

        leftx, lefty, rightx, righty, out_img = find_lane_pixels(img, nwindows, margin, minpix, nonzerox, nonzeroy, window_height)

        right_middle_point = (int(np.mean(rightx)), int(np.mean(righty)))
        print(right_middle_point)
        cv2.circle(image, (right_middle_point[0], right_middle_point[1]), radius=5, color=(0, 0, 255), thickness=-1)
        cv2.imshow("winname", image)
        cv2.waitKey(1)

        return 0"""