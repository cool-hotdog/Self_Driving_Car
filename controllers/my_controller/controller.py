from vehicle import Driver
import cv2
import numpy as np


BASE_SPEED = 20.0
MIN_SPEED = 5.0
MAX_SPEED = 25.0
STEER_GAIN = 0.8
FLOW_GAIN = 0.35


def camera_to_bgr(camera):
    width = camera.getWidth()
    height = camera.getHeight()
    image = camera.getImage()
    if image is None:
        return None
    buffer = np.frombuffer(image, np.uint8).reshape((height, width, 4))
    return cv2.cvtColor(buffer, cv2.COLOR_BGRA2BGR)


def region_of_interest(edges):
    height, width = edges.shape
    mask = np.zeros_like(edges)
    polygon = np.array([
        [0, height],
        [width, height],
        [int(width * 0.6), int(height * 0.55)],
        [int(width * 0.4), int(height * 0.55)],
    ], np.int32)
    cv2.fillPoly(mask, [polygon], 255)
    return cv2.bitwise_and(edges, mask)


def average_lane_line(lines, width, height):
    if lines is None:
        return None
    left_lines = []
    right_lines = []
    for x1, y1, x2, y2 in lines.reshape(-1, 4):
        if x2 == x1:
            continue
        slope = (y2 - y1) / (x2 - x1)
        if abs(slope) < 0.5:
            continue
        intercept = y1 - slope * x1
        if slope < 0:
            left_lines.append((slope, intercept))
        else:
            right_lines.append((slope, intercept))
    left = np.mean(left_lines, axis=0) if left_lines else None
    right = np.mean(right_lines, axis=0) if right_lines else None
    return left, right


def lane_center_offset(frame):
    height, width = frame.shape[:2]
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 150)
    roi = region_of_interest(edges)
    lines = cv2.HoughLinesP(roi, 2, np.pi / 180, 50, minLineLength=40, maxLineGap=100)
    lanes = average_lane_line(lines, width, height)
    if not lanes or lanes == (None, None):
        return 0.0
    left, right = lanes
    y_bottom = height
    y_top = int(height * 0.6)

    def line_x(slope, intercept, y):
        return int((y - intercept) / slope)

    if left is None or right is None:
        return 0.0

    left_x_bottom = line_x(left[0], left[1], y_bottom)
    right_x_bottom = line_x(right[0], right[1], y_bottom)
    lane_center = (left_x_bottom + right_x_bottom) / 2.0
    image_center = width / 2.0
    offset = (lane_center - image_center) / image_center
    return float(offset)


def estimate_speed(prev_gray, gray):
    if prev_gray is None:
        return BASE_SPEED
    flow = cv2.calcOpticalFlowFarneback(prev_gray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    mag, _ = cv2.cartToPolar(flow[..., 0], flow[..., 1])
    roi = mag[int(mag.shape[0] * 0.5):, :]
    mean_mag = float(np.mean(roi))
    target_speed = BASE_SPEED - FLOW_GAIN * mean_mag
    return float(np.clip(target_speed, MIN_SPEED, MAX_SPEED))


def run():
    driver = Driver()
    timestep = int(driver.getBasicTimeStep())

    camera = driver.getDevice("camera")
    camera.enable(timestep)

    prev_gray = None

    while driver.step() != -1:
        frame = camera_to_bgr(camera)
        if frame is None:
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        offset = lane_center_offset(frame)
        steering = float(np.clip(-offset * STEER_GAIN, -1.0, 1.0))
        target_speed = estimate_speed(prev_gray, gray)

        driver.setSteeringAngle(steering)
        driver.setCruisingSpeed(target_speed)

        prev_gray = gray


if __name__ == "__main__":
    run()
