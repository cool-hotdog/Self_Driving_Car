import cv2
import numpy as np

def birdseye_view(image):
    height,width = image.shape[:2]
    tl = [0,440]
    bl = [0,height]
    tr = [1079,440]
    br = [width,height]
    src_points = np.float32([tl, tr, br, bl])
    dst_points = np.float32([[0,0], [width-1, 0], [width-1, height-1], [0, height-1]])
    matrix = cv2.getPerspectiveTransform(src_points, dst_points)
    birdseye_image = cv2.warpPerspective(image, matrix, (width, height))

    return birdseye_image

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

def draw_the_lines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_image, (x1, y1), (x2, y2), (0, 255, 0), thickness=10)

    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return img

deger = 0
def main2(image, center_x):
    height = image.shape[0]
    width = image.shape[1]
    region_of_interest_vertices = [
        (0, height),
        (0, height / 2),
        (width, height / 2),
        (width, height)
    ]
    #image = birdseye_view(image)

    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    cropped_image = region_of_interest(gray_image,
                                       np.array([region_of_interest_vertices], np.int32))

    ret, threshold_image = cv2.threshold(cropped_image, 110, 255, cv2.THRESH_BINARY)
    kernel = np.ones((5,5), np.uint8)  # 5x5 boyutunda bir çekirdek

    # Genişletme (Dilation) işlemi
    threshold_image = cv2.dilate(threshold_image, kernel, iterations=2)
    
    canny_image = cv2.Canny(threshold_image, 150, 300)

    lines = cv2.HoughLinesP(canny_image,
                            rho=1,
                            theta=np.pi / 180,
                            threshold=50,
                            lines=np.array([]),
                            maxLineGap=100)

    min_left_distance = float('inf')
    min_right_distance = float('inf')
    closest_left_line = None
    closest_right_line = None

    for line in lines:
        for x1, y1, x2, y2 in line:
            #line_center_x = (x1 + x2) / 2
            #cv2.circle(image, (int(x1), int(y1)), 5, (200, 205, 255), -1)
            #cv2.circle(image, (int(x2), int(y2)), 5, (255, 0, 0), -1)
            line_center_x = x2

            # Solundaki en yakın çizgiyi bul
            if line_center_x < center_x:
                current_left_distance = center_x - line_center_x
                if current_left_distance < min_left_distance:
                    min_left_distance = current_left_distance
                    closest_left_line = line

            # Sağındaki en yakın çizgiyi bul
            elif line_center_x > center_x:
                current_right_distance = line_center_x - center_x
                if current_right_distance < min_right_distance:
                    min_right_distance = current_right_distance
                    closest_right_line = line


    if closest_left_line is not None and closest_right_line is not None:
        left_x1, left_y1, left_x2, left_y2 = closest_left_line[0]
        right_x1, right_y1, right_x2, right_y2 = closest_right_line[0]

        # En yakın sol ve sağ çizgilerin orta noktalarını bul
        left_mid_x = (left_x1 + left_x2) / 2
        left_mid_y = (left_y1 + left_y2) / 2
        right_mid_x = (right_x1 + right_x2) / 2
        right_mid_y = (right_y1 + right_y2) / 2

        midpoint_x = (left_mid_x + right_mid_x) / 2
        midpoint_y = (left_mid_y + right_mid_y) / 2
        cv2.circle(image, (int((left_x1 + right_x1)/2), int((left_y1 + right_y1)/2)), 5, (0, 255, 255), -1)
        #cv2.circle(image, (int(right_mid_x), int(right_mid_y)), 5, (0, 255, 255), -1)

        image_with_lines = draw_the_lines(image, [closest_left_line, closest_right_line])
        cv2.imshow("Detected Lines", image_with_lines)
        cv2.waitKey(1)
        global deger 
        midpoint_x = (left_x1 + right_x1)/2
        deger = midpoint_x
        return midpoint_x

    else:
        print("No lines detected on both sides.")
        return deger