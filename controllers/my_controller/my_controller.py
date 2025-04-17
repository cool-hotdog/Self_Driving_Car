from vehicle import Driver
from controller import Camera
import cv2
import time
from line import main 
import numpy as np
from scipy.integrate import quad
from scipy.misc import derivative
from dönüş import start
from park import main2
from durak import main3
driver = Driver()
timestep = int(driver.getBasicTimeStep())
    
# kamera eklenmesi
camera = driver.getDevice("camera")
camera.enable(timestep)  # 'Camera' nesnesinin 'enable' yöntemini kullanın

camera2 = driver.getDevice("camera2")
camera2.enable(timestep)  # 'Camera' nesnesinin 'enable' yöntemini kullanın

cam_width = 1080 
cam_height = 720

# Sabit değişkenler hem pid hem araç için
speed = 20

Kp = 0.418
Ki = 0.21
Kd = -0.006

model_cfg = "yolo/spot_yolov4.cfg"
model_weights = "yolo/spot_yolov4_last.weights"
labels_path = "yolo/spot.names"  

# Tabela etiketlerini obj.names dosyasından yükle
with open(labels_path, 'r') as f:
    labels = [line.strip() for line in f.readlines()]

# Modeli yükle
model = cv2.dnn.readNetFromDarknet(model_cfg, model_weights)

# Tespit katmanlarının isimlerini al
layer_names = model.getLayerNames()
output_layers = [layer_names[i - 1] for i in model.getUnconnectedOutLayers()]

detected_signs = []

park = True
# Pid algoritması
def pid_controller(error,fin_time,start_time):
    P = -Kp * error
    (integral_value,_) = quad(lambda x: function(error),start_time,fin_time)
    I = -Ki * integral_value
    derivative_value = derivative(function,error,dx = (fin_time-start_time))
    D = -Kd * derivative_value 
    a = P + I + D
    return a

def function(x):
    return x

def is_close(center1, center2, threshold=50):
    """
    İki merkezi karşılaştırarak aralarındaki mesafeyi kontrol eder.
    Eğer mesafe threshold değerinden küçükse, True döner. Bu sayede aynı nesneyi 1 den fazla tespit etmesi engellenir.
    """
    return np.linalg.norm(np.array(center1) - np.array(center2)) < threshold

def get_detected_labels_with_area_filter(image, min_area=5000, conf_threshold=0.7, distance_threshold=50):
    # Resmin boyutlarını al
    (H, W) = image.shape[:2]

    # Resmi YOLO'nun beklediği şekilde işle
    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    model.setInput(blob)
    layer_outputs = model.forward(output_layers)

    detected_signs = []
    detected_centers = []  # Tespit edilen nesnelerin merkezlerini tutacağımız liste

    # Tespit sonuçlarını işle
    for output in layer_outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > conf_threshold:
                box = detection[0:4] * np.array([W, H, W, H])
                (centerX, centerY, width, height) = box.astype("int")

                # Nesnenin alanını hesapla
                area = width * height
                # Eğer alan min_area'dan küçükse, nesneyi atla
                if area < min_area:
                    continue

                current_center = (centerX, centerY)

                # Eğer yeni tespit edilen nesne mevcut bir nesneye çok yakın değilse işle
                if not any(is_close(current_center, prev_center, distance_threshold) for prev_center in detected_centers):
                    detected_centers.append(current_center)  # Yeni merkezi listeye ekle

                    x = int(centerX - (width / 2))
                    y = int(centerY - (height / 2))

                    # Tespit edilen nesnenin ismini ve ID numarasını listeye ekle
                    detected_signs.append([labels[class_id], class_id, centerX])
                    cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)

                    # Nesne ismini ve güven skorunu yaz
                    text = f"{labels[class_id]}: {confidence:.2f}"
                    cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Sonuçları göster
    cv2.imshow("windows", image)
    cv2.waitKey(1)

    return detected_signs

start_time = time.time()  # Başlangıç zamanını kaydedin
last_prediction_time = time.time()
prediction_interval = 2
cam_center_x = cam_width // 2

durak = True
while driver.step() != -1:

    driver.setCruisingSpeed(speed) 
    start_time = time.time()

    # Kameradan görüntüyü alın
    kamera_goruntusu = camera.getImage()
    tabela_kamerası = camera2.getImage()

    # Görüntüyü kaydedin
    camera.saveImage("camera.png", 1)  # 'saveImage' yöntemini kullanın
    camera2.saveImage("camera2.png", 1)  # 'saveImage' yöntemini kullanın
    
    # Görüntüyü OpenCV ile okuyun
    img = cv2.imread("camera.png")
    img = cv2.resize(img, (cam_width,cam_height))

    img2 = cv2.imread("camera2.png")
    img2 = cv2.resize(img2, (cam_width,cam_height))

    if durak:
        fin_time = time.time()
        
        dev,deger = main3(img)
        rotation_angle = pid_controller(dev,fin_time,start_time) 

        print(f"dev = {dev} rotation_angle = {rotation_angle}")
        driver.setSteeringAngle(rotation_angle)
        driver.step()
        time.sleep(0.1)

        if deger == True:

            durma_zamanı = time.time()
            driver.setCruisingSpeed(0)
            move_straight_time = 10
            while time.time() - durma_zamanı < move_straight_time:
                driver.step()
                print(time.time() - durma_zamanı)
                time.sleep(0.1)

            şerit_değiştirme_zamanı = time.time()
            driver.setSteeringAngle(-0.5)
            move_straight_time = 6

            while time.time() - şerit_değiştirme_zamanı < move_straight_time:
                driver.setCruisingSpeed(20)
                driver.step()
                time.sleep(0.1)
            driver.setSteeringAngle(0.3)

            şerit_değiştirme_zamanı = time.time()
            while time.time() - şerit_değiştirme_zamanı < 6:
                driver.setCruisingSpeed(20)
                driver.step()
                time.sleep(0.1)
            driver.setSteeringAngle(0)

            durak = False

    if not park:

        fin_time = time.time()
        dev = main(img)
        rotation_angle = pid_controller(dev,fin_time,start_time) 
        driver.setSteeringAngle(rotation_angle)
        current_time = time.time()
        
        if current_time - last_prediction_time >= prediction_interval:
            clas = get_detected_labels_with_area_filter(img2,6000)
            print(clas)
            if len(clas) > 0:
                
                if clas[0][1] == 0:
                    park = True
                    continue

                elif clas[0][1] == 15:
                    if clas[0][2] > (cam_width/2): 
                        print("sol şeride geç")
                        şerit_değiştirme_zamanı = time.time()
                        driver.setSteeringAngle(-0.5)
                        move_straight_time = 4
                        while time.time() - şerit_değiştirme_zamanı < move_straight_time:
                            driver.setCruisingSpeed(20)
                            driver.step()
                            time.sleep(0.1)
                        driver.setSteeringAngle(0.3)
                        şerit_değiştirme_zamanı = time.time()
                        while time.time() - şerit_değiştirme_zamanı < 7:
                            driver.setCruisingSpeed(20)
                            driver.step()
                            time.sleep(0.1)                         
                        driver.setSteeringAngle(0)

                    elif clas[0][2] < (cam_width/2):
                        print("sol şeride geç")
                        şerit_değiştirme_zamanı = time.time()
                        driver.setSteeringAngle(0.5)
                        move_straight_time = 4
                        while time.time() - şerit_değiştirme_zamanı < move_straight_time:
                            driver.setCruisingSpeed(20)
                            driver.step()
                            time.sleep(0.1)
                        driver.setSteeringAngle(-0.3)
                        şerit_değiştirme_zamanı = time.time()
                        while time.time() - şerit_değiştirme_zamanı < 6:
                            driver.setCruisingSpeed(20)
                            driver.step()
                            time.sleep(0.1)
                        driver.setSteeringAngle(0)

                elif clas[0][1] == 13:
                    durma_zamanı = time.time()
                    driver.setCruisingSpeed(0)
                    move_straight_time = 15
                    while time.time() - durma_zamanı < move_straight_time:
                        driver.step()
                        time.sleep(0.1)

                elif clas[0][1] == 2:
                    durak = True
                    şerit_değiştirme_zamanı = time.time()
                    move_straight_time = 60
                    while time.time() - şerit_değiştirme_zamanı < move_straight_time:
                        main3(img)
                        driver.setSteeringAngle(0)
                        driver.step()
                        time.sleep(0.1)
                else:
                    signal_clas = clas[0][1]
                    start(signal_clas,driver)
                
            last_prediction_time = current_time

    else:
        driver.setCruisingSpeed(20)
        clas= get_detected_labels_with_area_filter(img2)
        min_distance = float('inf')
        fin_time = time.time() 
        for _,i,centerX, in clas:
            if i == 0:
                current_distance = abs(cam_center_x - centerX)  # Kamera merkezi ile tespit edilen nesnenin merkezi arasındaki mesafe
                if current_distance <= min_distance:  # Eğer bu mesafe daha küçükse en küçük mesafe olarak güncelle
                    min_distance = current_distance
                    closest_center = centerX
                xline = main2(img2,closest_center)
                dev = ((xline / (cam_width/2.7))- 1) * -1
                rotation_angle = pid_controller(dev,fin_time,start_time)  
                driver.setSteeringAngle(rotation_angle)