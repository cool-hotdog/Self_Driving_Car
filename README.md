<div align="center">

# Self Driving Car

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org) 
[![OpenCV](https://img.shields.io/badge/OpenCV-4.10.0-green.svg)](https://opencv.org) 
[![YOLOv4](https://img.shields.io/badge/YOLOv4-Detection-red.svg)](https://github.com/AlexeyAB/darknet) 
[![Webots](https://img.shields.io/badge/Webots-R2023b-orange.svg)](https://cyberbotics.com) 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

🚗 **An intelligent autonomous vehicle simulation project featuring advanced computer vision and control algorithms**

---

[🇬🇧 English](#english) | [🇹🇷 Türkçe](#türkçe) | [🇨🇳 中文](#chinese)

</div>

---

## English

## 🇬🇧

### About This Project

This autonomous driving simulation represents a comprehensive approach to self-driving car technology, built entirely within the Webots simulation environment. The project demonstrates real-world autonomous vehicle capabilities including lane detection, traffic sign recognition, obstacle avoidance, and parking assistance.

The system employs sophisticated computer vision techniques powered by OpenCV and a custom-trained YOLOv4 model for traffic sign detection. The vehicle navigates complex urban environments using advanced PID control algorithms, making real-time decisions based on visual input from dual camera systems.

### ✨ Key Features

**🎯 Advanced Lane Detection**
- Histogram-based lane pixel analysis
- Sliding window technique for precise lane tracking  
- Second-degree polynomial curve fitting
- Real-time curvature radius calculation
- Dynamic vehicle positioning within lanes

**🚦 Intelligent Traffic Recognition**
- YOLOv4-powered traffic sign detection
- Real-time decision making based on traffic signals
- Support for stop signs, turn signals, and traffic lights
- Robust filtering to prevent false detections

**🅿️ Autonomous Parking System**
- Vision-based parking space detection
- Specialized lane detection for parking areas
- Automatic alignment and positioning
- Multi-step parking maneuver execution

**🚧 Smart Obstacle Avoidance**
- Camera-based obstacle detection
- Safe return to original lane after avoidance

**⚙️ Advanced Control Systems**
- PID controller for smooth steering
- Multi-camera sensor fusion
- Real-time image processing pipeline
- Adaptive speed control based on traffic conditions

### 🔧 Installation & Setup

#### Prerequisites
- **Webots R2023b**: Download from [official releases](https://github.com/cyberbotics/webots/releases/tag/R2023b)
- **Python 3.8+** with pip package manager

#### Required Dependencies
```bash
pip3 install opencv-python==4.10.0.84
pip3 install scipy==1.14.1
```

#### YOLOv4 Model Files
Download the pre-trained YOLOv4 model files from our [Google Drive repository](https://drive.google.com/drive/folders/12GEDLy-Ujzgo5AEnpvfesSiQYkwWzi02?usp=sharing) and place them in the same directory as `main.py`.

#### Getting Started
1. Install Webots R2023b for your operating system
2. Open Webots and navigate to **File → Open World**
3. Select the `.wbt` file from the `worlds` folder
4. Install the required Python dependencies
5. Download and place the YOLOv4 model files
6. Click the play button in Webots to start the simulation

### 🎥 Demonstration Videos

**Bus Stop Detection & Navigation**
The vehicle demonstrates sophisticated behavior when encountering bus stops, including precise positioning and timed waiting periods.

https://github.com/user-attachments/assets/3796ba41-0a23-4283-8fb9-9ec3148ce33c

**Dynamic Lane Switching** 
Advanced obstacle avoidance showcasing intelligent lane changing maneuvers with smooth transitions.

https://github.com/user-attachments/assets/a90081f1-d1e7-478b-adcc-0c72c80e530e

**Autonomous Parking Capabilities**
Precise parking maneuvers demonstrating vision-based space detection and multi-point turn execution.

https://github.com/user-attachments/assets/98a1f074-7a3d-4bde-9d32-81b64f40e523

**Traffic Light Recognition**
Real-time traffic light detection and appropriate stopping behavior at intersections.

https://github.com/user-attachments/assets/328c157a-2127-43dd-b30e-6ebad8208eec

**Complete Lane Following System**
Demonstration of the core lane detection and following capabilities with PID control.

https://github.com/user-attachments/assets/c2809628-b58f-4afc-876c-97b30633844d

**Traffic Sign Recognition & Navigation**
Advanced YOLOv4-based traffic sign detection with appropriate vehicle responses.

https://github.com/user-attachments/assets/30a03da8-7f35-4071-8cfa-f2636c6b6632

### 🏗️ Technical Architecture

**Core Components:**
- `main.py`: Primary control loop and sensor integration
- `line.py`: Advanced lane detection algorithms  
- `durak.py`: Bus stop detection and management
- `park.py`: Autonomous parking system
- `dönüş.py`: Turn navigation and traffic sign response

**Camera Systems:**
- **Primary Camera**: Lane detection and road analysis
- **Secondary Camera**: Traffic sign recognition and obstacle detection

**Control Algorithms:**
- **PID Controller**: Precise steering angle calculation
- **Histogram Analysis**: Lane pixel detection and processing
- **Polynomial Fitting**: Smooth curve representation of lanes
- **Sliding Window**: Dynamic lane tracking methodology

### 🚀 Development Roadmap

- ✅ Lane detection and tracking  
- ✅ Traffic sign recognition  
- ✅ Obstacle avoidance  
- ✅ Traffic light recognition  
- ✅ Parking/stop algorithm  
- 🔄 Roundabout navigation algorithm  
- 🔄 Control AI  
- 🔄 Full system integration (all modules working together)  
- 🔄 Adaptation to weather conditions  
- 🔄 Neural network integration  

---

## Türkçe

## 🇹🇷

### Proje Hakkında

Bu otonom sürüş simülasyonu, tamamen Webots simülasyon ortamında geliştirilmiş kapsamlı bir sürücüsüz araç teknolojisi yaklaşımını temsil eder. Proje, şerit algılama, trafik işareti tanıma, engel kaçınma ve park yardımı dahil olmak üzere gerçek dünya otonom araç yeteneklerini göstermektedir.

Sistem, OpenCV ile desteklenen gelişmiş bilgisayarlı görü teknikleri ve trafik işareti algılama için özel eğitilmiş YOLOv4 modeli kullanır. Araç, çift kamera sistemlerinden gelen görsel girdilere dayalı gerçek zamanlı kararlar alarak, gelişmiş PID kontrol algoritmaları kullanarak karmaşık şehir ortamlarında gezinir.

### ✨ Temel Özellikler

**🎯 Gelişmiş Şerit Algılama**
- Histogram tabanlı şerit piksel analizi
- Hassas şerit takibi için kayan pencere tekniği
- İkinci derece polinom eğri uydurma
- Gerçek zamanlı eğrilik yarıçapı hesaplama
- Şeritler içinde dinamik araç konumlandırma

**🚦 Akıllı Trafik Tanıma**
- YOLOv4 destekli trafik işareti algılama
- Trafik sinyallerine dayalı gerçek zamanlı karar verme
- Dur işaretleri, dönüş sinyalleri ve trafik lambaları desteği
- Yanlış algılamaları önlemek için güçlü filtreleme

**🅿️ Otonom Park Sistemi**
- Görü tabanlı park alanı algılama
- Park alanları için özelleşmiş şerit algılama
- Otomatik hizalama ve konumlandırma
- Çok adımlı park manevra gerçekleştirme

**🚧 Akıllı Engel Kaçınma**
- Kamera tabanlı engel algılama
- Kaçınma sonrası orijinal şeride güvenli dönüş

**⚙️ Gelişmiş Kontrol Sistemleri**
- Yumuşak direksiyon için PID kontrolör
- Çok kameralı sensör füzyonu
- Gerçek zamanlı görüntü işleme hattı
- Trafik koşullarına göre uyarlanabilir hız kontrolü

### 🔧 Kurulum ve Ayarlar

#### Ön Gereksinimler
- **Webots R2023b**: [Resmi sürümlerden](https://github.com/cyberbotics/webots/releases/tag/R2023b) indirin
- **Python 3.8+** ve pip paket yöneticisi

#### Gerekli Bağımlılıklar
```bash
pip3 install opencv-python==4.10.0.84
pip3 install scipy==1.14.1
```

#### YOLOv4 Model Dosyaları
Önceden eğitilmiş YOLOv4 model dosyalarını [Google Drive depomuzdaki](https://drive.google.com/drive/folders/12GEDLy-Ujzgo5AEnpvfesSiQYkwWzi02?usp=sharing) bağlantıdan indirin ve `main.py` dosyası ile aynı dizine yerleştirin.

#### Başlangıç
1. İşletim sisteminiz için Webots R2023b'yi kurun
2. Webots'u açın ve **File → Open World**'a gidin
3. `worlds` klasöründen `.wbt` dosyasını seçin
4. Gerekli Python bağımlılıklarını kurun
5. YOLOv4 model dosyalarını indirin ve yerleştirin
6. Simülasyonu başlatmak için Webots'ta oynat düğmesine tıklayın

### 🎥 Demonstrasyon Videoları

**Durak Algılama ve Navigasyon**
Araç, durak karşılaştığında hassas konumlandırma ve zamanlanmış bekleme süreleri dahil gelişmiş davranış sergiler.

https://github.com/user-attachments/assets/3796ba41-0a23-4283-8fb9-9ec3148ce33c

**Dinamik Şerit Değiştirme**
Yumuşak geçişlerle akıllı şerit değiştirme manevralarını gösteren gelişmiş engel kaçınma.

https://github.com/user-attachments/assets/a90081f1-d1e7-478b-adcc-0c72c80e530e

**Otonom Park Yetenekleri**
Görü tabanlı alan algılama ve çok noktalı dönüş gerçekleştirmesini gösteren hassas park manevraları.

https://github.com/user-attachments/assets/98a1f074-7a3d-4bde-9d32-81b64f40e523

**Trafik Lambası Tanıma**
Kavşaklarda gerçek zamanlı trafik lambası algılama ve uygun durma davranışı.

https://github.com/user-attachments/assets/328c157a-2127-43dd-b30e-6ebad8208eec

**Komple Şerit Takip Sistemi**
PID kontrolü ile temel şerit algılama ve takip yeteneklerinin gösterimi.

https://github.com/user-attachments/assets/c2809628-b58f-4afc-876c-97b30633844d

**Trafik İşareti Tanıma ve Navigasyon**
Uygun araç tepkileri ile gelişmiş YOLOv4 tabanlı trafik işareti algılama.

https://github.com/user-attachments/assets/30a03da8-7f35-4071-8cfa-f2636c6b6632

### 🏗️ Teknik Mimari

**Temel Bileşenler:**
- `main.py`: Birincil kontrol döngüsü ve sensör entegrasyonu
- `line.py`: Gelişmiş şerit algılama algoritmaları
- `durak.py`: Durak algılama ve yönetimi  
- `park.py`: Otonom park sistemi
- `dönüş.py`: Dönüş navigasyonu ve trafik işareti tepkisi

**Kamera Sistemleri:**
- **Birincil Kamera**: Şerit algılama ve yol analizi
- **İkincil Kamera**: Trafik işareti tanıma ve engel algılama

**Kontrol Algoritmaları:**
- **PID Kontrolör**: Hassas direksiyon açısı hesaplama
- **Histogram Analizi**: Şerit piksel algılama ve işleme
- **Polinom Uydurma**: Şeritlerin yumuşak eğri temsili
- **Kayan Pencere**: Dinamik şerit takip metodolojisi

### 🚀 Geliştirme Yol Haritası

- ✅ Şerit algılama ve takibi  
- ✅ Trafik işareti tanıma  
- ✅ Engel kaçınma  
- ✅ Trafik lambası tanıma  
- ✅ Park/durma algoritması  
- 🔄 Döner kavşak algoritması  
- 🔄 Kontrol yapay zekası  
- 🔄 Tüm sistemlerin entegrasyonu (modüllerin birlikte çalışması)  
- 🔄 Hava koşullarına uyum  
- 🔄 Sinir ağı entegrasyonu  

---

## Günlük ilerlemeler

---

## 3 Ekim 2024 (Eklemeler ve Güncellemeler)

### Eklenenler

#### Durak algoritamsı:

Teknofest'teki görevlerden biri, otonom aracın durak tabelasını gördüğünde durak cebine girip belirli bir süre beklemesi ve ardından yola devam etmesidir. Bu görevi gerçekleştirmek için birkaç farklı algoritma geliştirdim.

İlk olarak, park algoritmasında kullandığım şerit tespit algoritması ile durak cebinin şeritlerinin orta noktasını bulup aracı bu noktaya yönlendirmeyi planladım. Ancak bu yöntem tam olarak istediğim stabiliteyi sağlayamadı. Bazen şerit tespiti kayboluyor veya şeritlerin kaymasından dolayı araç ani dönüşler yapıyordu, bu da görevin başarısız olmasına yol açıyordu.

Daha sonra, kameranın en solundaki şeridi sürekli takip eden bir algoritma denedim, ancak bu da istediğim başarıyı getirmedi. Sonunda geliştirdiğim üçüncü algoritma ile istediğim başarıyı elde ettim. Bu algoritma, durak tabelası tespit edildiğinde direksiyon açısını sabit tutarak aracın düz bir şekilde ilerlemesini sağlıyor. Araç ilerlerken, şerit tespiti için kullanılan kameradan gelen veriler ile mavi alan araması yapılıyor.

Mavi alan araması için görüntü işleme teknikleri kullanılıyor. Önce, `inRange` fonksiyonu ile mavi alan maskelemesi yapılıyor. Ardından, `findContours` ile maskede beyaz noktaların koordinatları bulunuyor. Bu koordinatlar, mavi alanın yerini gösteriyor. Araç, mavi alanı bulana kadar düz bir şekilde ilerliyor ve alan bulunduğunda, bu alanın orta noktası alınıyor.

Bu orta noktanın x koordinatı, pozisyon değerini hesaplamak için kullanılıyor. Formül şu şekilde:

```python
pos = (540 - center_x) * 0.00513888888
```

Bu formül, kameranın orta noktası ile tespit edilen mavi alanın x koordinatının farkını ve webots simülasyonunda piksel uzunluğunun metreye oranını kullanarak hesaplanıyor. Bu pos değeri, PID algoritmasına veriliyor ve çıkan sonuç direksiyon açısı olarak kullanılıyor.


Aracın durak cebinde olduğunu belirlemek için şu formülü kullanıyorum:

```python
np.sum(mask == 255) / (img.shape[0] * img.shape[1])
```

Bu formül, maskede 255 değeri ile gösterilen beyaz piksellerin ekran oranını hesaplıyor. Eğer bu oran 0.56’dan büyükse, araç durak cebinin içinde kabul ediliyor. Araç 10 saniye boyunca durduktan sonra, önceden belirlenmiş bir hareket planı ile durak cebinden çıkıp yola devam ediyor.

Bu yöntem, görevde istenen stabiliteyi sağlamada başarılı oldu.

### Güncellemeler.

Main.py dosyasındaki durak algoritmasını sağlamak için bazı güncellemeler yapıldı. 

Öncelikle durak tabelası tespit edilip kontrol edilir ve eğer tabela bir durak tabelasıysa, durak algoritması devreye girer ve şerit tespit için kullanılan kamera göreslleri durak algoritmasına aktarılıyor. Durak algoritmasından gelen veriler PID algoritmasına gönderilir ve çıkan değer direksiyon açısı olarak ayarlanır. Ardından, aracın durak cebinin içinde olup olmadığı kontrol edilir. Eğer araç cebin içindeyse, 10 saniye boyunca bekler. Bekleme süresi dolduğunda, önceden belirlenmiş hareketler ile araç cebin dışına çıkar. Son olarak, durak algoritması devre dışı bırakılır ve araç yoluna devam eder.

https://github.com/user-attachments/assets/3796ba41-0a23-4283-8fb9-9ec3148ce33c

---
## 17 Eylül 2024 (Eklemeler ve Güncellemeler)

### Eklenenler

#### Şerit değiştirme algoritması:


Engel çıkması veya gerekli durumlarda aracın karşı şeride geçebilmesi gerekmektedir. Bu şerit değişimini sağlamak için kamera kullanılmıştır. Genellikle engel tespiti gibi durumlarda LIDAR tercih edilse de, özellikle Tesla gibi otonom sürüş özelliklerine sahip elektrikli araç satan büyük firmalar, maliyetleri düşürmek için LIDAR sensörlerini çıkarmakta ve genel olarak kamera ve mesafe sensörleri kullanmaktadır. Bu projede de benzer bir yaklaşım izleyerek, LIDAR sensörü eklemenin mantıklı olmadığını düşündüm. Bunun yerine, kameradan gelen verileri YOLOv4 ile eğittiğim modele vererek engel tespitini gerçekleştirmeyi planlıyorum.

Şerit değiştirme, kameradan gelen görsel verilerle algılanacak. Şerit değiştirmenin gerektiği durumlarda, örneğin videoda girilmez tabelasının tespit edilmesiyle bu işlem başlatılacak. Tespit edilen nesnenin kameranın hangi yönünde olduğuna bağlı olarak şerit değiştirme işlemi yapılacak. Örneğin, engel kameranın solundaysa araç sağa, sağındaysa sola geçecek(Şerit tespiti kısmında, şerit koordinatları alınarak, şerit bilgilerine göre sağ veya sol şerit belirlemesi de yapılabilir.). Bu geçiş işlemi sırasında, aracın önce direksiyonu sabit bir açıyla belli bir süre döndürülüp, ardından tam tersi açıya geçilerek şerit değiştirilmiş olacak. Bu işlem tamamlandıktan sonra, aracın şerit tespit ve takip sistemi devreye girecek ve yeni şeritte aracı ortalayacak. Şerit takip, başka bir işlem gerektiğinde devre dışı kalana kadar devam edecek.



https://github.com/user-attachments/assets/a90081f1-d1e7-478b-adcc-0c72c80e530e

---
#### Park algoritması:

Park etme aşamasında, araç park tabelasını görene kadar "kör ilerleyiş" olarak adlandırılan, önceden tanımlanmış bir sürüş gerçekleştirecektir. Bu süreçte, YOLOv4 ile eğitilmiş modele sürekli olarak kamera görüntüleri aktarılacak ve model park tabelasını tespit etmeye çalışacaktır. Park tabelası tespit edildiğinde, sistemin kararlılığını korumak adına birden fazla tabela tespit edilme olasılığı göz önünde bulundurulacaktır. Bu durumda, kamera merkezine en yakın olan tabela ve park alanı esas alınacaktır. Ardından HoughLinesP ile geliştirilen şerit tespit algoritması devreye girecektir.

Bu noktada ana şerit tespit algoritması kullanılmayacaktır. Bunun nedeni, ana algoritmanın histogram yöntemini kullanarak görüntüdeki en yoğun piksel bölgelerini şerit olarak algılamasıdır. Bu yöntem, park alanlarındaki istenilen şeritleri doğru şekilde algılayamayabilir. Çünkü park alanında birden fazla şerit bulunur ve sadece "park edilebilir" tabelasının olduğu şeritler algılanmalı ve takip edilmelidir. Bu nedenle, park alanlarındaki şeritler için HoughLinesP kullanılarak özel bir şerit tespit algoritması geliştirilmiştir.

Geliştirilen şerit tespit algoritması, park tabelasının x koordinatına en yakın sol ve sağ şeritleri belirler. Tabelanın hemen solunda ve sağında yer alan bu iki şerit, aracın park edebileceği alanı tanımlar. Algoritma, bu iki şeridin orta noktasını hesaplayarak aracı bu bölgeye yönlendirir. Hesaplama orta nokta bu formülle verilir: 

(((line_center / (cam_width / 2)) - 1) * -1) 

Bu forlüm sonucunda elde edilen değer, PID kontrol sistemine iletilir ve aracın direksiyon açısı buna göre ayarlanır.

 Sistem şu an tam olarak stabil olmasa da, ilerleyen zamanlarda yapılacak iyileştirmelerle daha kararlı ve güvenilir hale getirilmesi planlanmaktadır.


https://github.com/user-attachments/assets/98a1f074-7a3d-4bde-9d32-81b64f40e523

---

### Kırmızı ışıkta durma

Yolo modelini eğitmek için kullanılan veri setinde trafik ışık görselleri eklendi, bu sayede aracın kırmızı ışıkta durması salanacak. Kameradan gelen görselde, kırmızı işık tespit edilirse araç belli bir süre boyunca hızını kesecek ve süre bitince eski hızı ile ilerlemeye devam edecek. 

https://github.com/user-attachments/assets/328c157a-2127-43dd-b30e-6ebad8208eec

---

## Geliştirmeler.

10 Eylül'de eklenen YOLOv4 modeli, yeterince iyi eğitilmediği için yanlış tespitler yapıyordu ve bu durum, sistemin stabilitesini ve güvenilirliğini olumsuz etkiliyordu. Bu aşamada, elimdeki görsellerle modeli eğitmeye devam ettim. Her ne kadar model hala istediğim doğruluk seviyesine ulaşmamış olsa da, önceki duruma kıyasla çok daha doğru ve hassas tespitler yapıyor. Bu da sistemin güvenilirliğini ve stabilitesini artırıyor.

---
## 10 Eylül 2024 (Eklemeler ve Güncellemeler)

### main.py Ana Kod (Güncellemeler)

Main koduna, trafik tabelalarını ve işaretlerini tespit etmek için YOLOv4 ile eğitilmiş bir model entegre edilmiştir. Bu modelin veri seti, [TTVS veri seti](https://github.com/ituracingdriverless/TTVS) içindeki verilerden alınmıştır, ancak model tam olarak eğitilmediği için doğruluk oranı yüksek değildir. Ayrıca, dönüş işlemlerini gerçekleştirmek için `dönüş.py` kodu eklenmiştir. Bu kod, aracın sola, sağa ve ileri doğru dönüşlerini başarılı bir şekilde, ancak tam olarak stabil olmayan bir şekilde yapabilmesini sağlar.

[YoloV4 dosyaları](https://drive.google.com/drive/folders/12GEDLy-Ujzgo5AEnpvfesSiQYkwWzi02?usp=sharing)

#### Genel Yapı

1. **Mesafe Kontrolü (`is_close`)**

   YOLOv4 ile görselden nesne tespiti yaparken aynı nesneyi birden fazla kez tespit etmesini engellemek için bu fonksiyon eklenmiştir. Bu fonksiyon, tespit edilen iki nesnenin merkezlerini karşılaştırarak, aralarındaki mesafe belirli bir değerin altında olduğunda aynı nesne olarak değerlendirilmesini sağlar.

2. **Trafik İşareti Tespiti ve Filtreleme (`get_detected_labels_with_area_filter`)**

   YOLOv4 modeli, ikinci kameradan gelen görüntüler ile belirli bir süre (kodda 2 saniyede bir olarak ayarlandı) içinde nesne tespiti yapar. Bu süre sınırı, kaynakların sürekli olarak kullanılmasını önlemek içindir. Model, TTVS veri setinden alınan 3000 görsel üzerinde eğitilmiştir, ancak eğitim tam olarak tamamlanmadığı için doğruluk oranı yüksek değildir. Tabela tespiti dönüş algoritması için kullanıldığından, tespit edilen nesnelerin bir alan ölçeği eklenmiştir; bu sayede küçük alanlı nesneler dönüş algoritması tarafından dikkate alınmaz.

#### dönüş.py Dönüş Algoritması (Ekleme)

Aracın trafik işaretlerine göre yönlendirilmesi için PID kontrol algoritması kullanılmıştır. PID algoritmasının kullanımı, dönüşlerin daha düzgün ve genel yapının daha stabil olmasını sağlamaktadır. Tabela tespiti gerçekleştiğinde `dönüş.py` modülündeki `start()` fonksiyonu çalışır. Bu fonksiyon, ilk olarak tespit edilen tabelaya göre yapılması gereken eylemi belirler. Şimdilik sağa, sola ve ileri gitme eylemleri eklenmiştir. Daha sonra, araç belirli bir süre düz gider ve ardından işarete göre düz, sola veya sağa dönüş başlar. Hedef direksiyon açısı belirlenir ve PID algoritması aracın direksiyon açısını hesaplayarak ayarlar. Dönüş tamamlandığında, direksiyon açısı sıfırlanır. Sol veya sağ dönüşlerde, dönüş sonrası şerit tekrar tespit edilebilmesi için araç belirli bir süre boyunca düz gitmeye devam eder. Kod, aracın şerit tespit ve takibine devam etmesiyle sonlanır.

> [!NOTE]
> Kullanılan YOLOv4 modelinin eğitiminin tamamlanmamış olması nedeniyle doğruluğun düşük olması ve dönüş algoritmasının hala istenilen stabiliteye ulaşamaması sebebiyle yapı tam olarak stabil değil.
>

---

https://github.com/user-attachments/assets/30a03da8-7f35-4071-8cfa-f2636c6b6632

---

## 4 Eylül 2024 (eklemeler ve güncellemeler)

---
### main.py Ana kod. (Ekleme)

`main.py` dosyası, Webots simülasyon ortamında bir aracı şeritler üzerinde yönlendirmek için kullanılan ana kontrol kodunu içerir. Kod, araç kameralardan aldığı görüntülerle şeritleri tespit eder ve PID kontrol algoritmasını kullanarak aracın yönünü ayarlar.

#### 1. Kameraların Tanımlanması

İki kamera kullanılır:

- **Birinci Kamera**: Yol şeritlerini tespit etmek için kullanılır. Bu kamera, yolun önünü görüntüleyerek şeritlerin doğru bir şekilde takip edilmesini sağlar.
- **İkinci Kamera**: Trafik işaretlerini algılamak için kullanılır. Bu kamera, trafik işaretlerinin tanımlanmasını ve işaretlere göre aracın yönlendirilmesini sağlar.

#### 2. Görüntü İşleme

- **Görüntülerin Alınması ve Kaydedilmesi**: Kameralardan alınan görüntüler `cv2` (OpenCV) kullanılarak işlenir ve kaydedilir. Bu görüntüler, şerit tespiti ve trafik işareti algılama işlemleri için kullanılır.

#### 3. Şerit Tespiti

- **Şerit Tespiti Fonksiyonu**: `line.py` dosyasından içe aktarılan `main()` fonksiyonu, birincil kameradan alınan görüntüde yol şeritlerini tespit eder. Bu fonksiyon, yolun şeritlerini doğru bir şekilde takip edebilmek için gerekli veriyi sağlar.

#### 4. PID Kontrol Algoritması

- **PID Kontrol**: `pid_controller()` fonksiyonu, şerit tespitinden gelen verileri kullanarak aracın direksiyon açısını hesaplar. Bu algoritma, şerit sapmasını en aza indirgemek ve aracın şerit ortasında kalmasını sağlamak için kullanılır. PID (Proportional-Integral-Derivative) algoritması, hatayı, integralini ve türevini değerlendirerek doğru direksiyon açısını belirler.

#### 5. Çalışma Döngüsü

- **Ana Döngü**: Araç sürekli olarak aşağıdaki işlemleri gerçekleştirir:
  - Kameradan görüntü alır.
  - Görüntüleri işleyerek şerit tespiti yapar.
  - PID kontrol algoritmasını uygular ve aracın direksiyon açısını ayarlar.
    
Bu yapı, aracın yol şeritlerini doğru bir şekilde takip etmesini ve uygun şekilde yönlendirilmesini sağlar. Kod, Webots simülasyon ortamında gerçek zamanlı olarak çalışacak şekilde tasarlanmıştır.

---

## line.py (Şerit Tespit Algoritması) (Ekleme)

Bu algoritma, görüntü işleme teknikleri kullanarak yol üzerindeki şeritleri tespit etmeyi amaçlar. Yolun alt yarısındaki şerit pikselleri analiz edilerek, sol ve sağ şeritler bulunur ve bu piksellere polinom eğriler uydurularak şerit çizgilerinin eğriliği ve aracın konumu hesaplanır.

### Algoritmanın Adımları

#### 1. Görüntü İşleme:
Giriş görüntüsü gri tonlamaya çevrilir ve ardından görüntüdeki gürültüleri azaltmak için genişletme ve erozyon işlemleri uygulanır. Bu sayede, şerit çizgileri daha net bir şekilde ortaya çıkarılır.

#### 2. Histogram Analizi:
Görüntünün alt yarısında, şerit çizgilerini tespit etmek için piksel yoğunlukları analiz edilir. Histogram verileri, sol ve sağ şeritlerin başlangıç noktalarını belirlemek için kullanılır.

#### 3. Kayan Pencere Yöntemi:
Algoritma, şerit piksellerini tespit etmek için dikey olarak kayan pencereler kullanır. Bu pencerelerle sol ve sağ şeritlerdeki pikseller taranır ve bu piksellerin koordinatları kaydedilir.

#### 4. Polinom Uydurma:
Tespit edilen şerit piksellerine ikinci derece bir polinom eğrisi uydurulur. Bu eğri, şerit çizgilerinin geometrik yapısını anlamak ve izlemek için kullanılır.

#### 5. Eğrilik Hesaplama:
Uydurulan polinom eğrilerine dayanarak, şeritlerin eğrilik yarıçapı hesaplanır. Ayrıca, aracın şerit ortasına göre pozisyonu belirlenir ve aracın yol üzerindeki hizası hakkında bilgi sağlanır.

Bu algoritma, gerçek zamanlı olarak şerit takibi ve araç hizalama sistemlerinde kullanılabilir.

---

https://github.com/user-attachments/assets/c2809628-b58f-4afc-876c-97b30633844d

---

## chinese

## 🇨🇳

### 项目简介

该自动驾驶仿真项目完整构建于 Webots 仿真环境中，展示了自动驾驶汽车在真实场景中的核心能力，包括车道检测、交通标志识别、障碍物规避和泊车辅助等。

系统采用基于 OpenCV 的计算机视觉方法，并结合自训练 YOLOv4 模型进行交通标志检测。车辆通过双摄像头输入进行实时决策，使用 PID 控制算法在复杂城市环境中稳定行驶。

### ✨ 核心特性

**🎯 高级车道检测**
- 基于直方图的车道像素分析
- 滑动窗口精确跟踪车道
- 二次多项式曲线拟合
- 实时曲率半径计算
- 车道内动态车辆定位

**🚦 智能交通识别**
- 基于 YOLOv4 的交通标志检测
- 基于交通信号的实时决策
- 支持停车标志、转向标志与交通灯
- 具备稳健过滤机制以降低误检

**🅿️ 自动泊车系统**
- 基于视觉的停车位检测
- 面向停车区域的专用车道检测
- 自动对齐与定位
- 多步骤泊车动作执行

**🚧 智能障碍规避**
- 基于摄像头的障碍物检测
- 规避后安全回到原车道

**⚙️ 高级控制系统**
- 使用 PID 控制器实现平滑转向
- 多摄像头传感融合
- 实时图像处理流水线
- 基于交通状况的自适应速度控制

### 🔧 安装与配置

#### 前置要求
- **Webots R2023b**：可从[官方发布页](https://github.com/cyberbotics/webots/releases/tag/R2023b)下载
- **Python 3.8+** 与 pip

#### 依赖安装
```bash
pip3 install opencv-python==4.10.0.84
pip3 install scipy==1.14.1
```

#### YOLOv4 模型文件
请从我们的 [Google Drive 仓库](https://drive.google.com/drive/folders/12GEDLy-Ujzgo5AEnpvfesSiQYkwWzi02?usp=sharing)下载预训练 YOLOv4 文件，并将其放在与 `main.py` 相同目录下。

#### 快速开始
1. 安装 Webots R2023b
2. 打开 Webots，进入 **File → Open World**
3. 选择 `worlds` 目录下的 `.wbt` 文件
4. 安装上述 Python 依赖
5. 下载并放置 YOLOv4 模型文件
6. 在 Webots 中点击播放开始仿真

### 🎥 演示视频

**公交站检测与导航**
车辆在遇到公交站时可实现精确入位与定时等待。

https://github.com/user-attachments/assets/3796ba41-0a23-4283-8fb9-9ec3148ce33c

**动态变道**
展示平滑过渡的智能变道障碍规避能力。

https://github.com/user-attachments/assets/a90081f1-d1e7-478b-adcc-0c72c80e530e

**自动泊车能力**
演示基于视觉的车位检测与多点泊车动作。

https://github.com/user-attachments/assets/98a1f074-7a3d-4bde-9d32-81b64f40e523

**交通灯识别**
在路口进行实时交通灯识别并执行停车策略。

https://github.com/user-attachments/assets/328c157a-2127-43dd-b30e-6ebad8208eec

**完整车道跟随系统**
展示基于 PID 的核心车道检测与跟随能力。

https://github.com/user-attachments/assets/c2809628-b58f-4afc-876c-97b30633844d

**交通标志识别与导航**
展示基于 YOLOv4 的交通标志检测与车辆响应。

https://github.com/user-attachments/assets/30a03da8-7f35-4071-8cfa-f2636c6b6632

### ️ 技术架构

**核心组件：**
- `main.py`：主控制循环与传感器集成
- `line.py`：高级车道检测算法
- `durak.py`：公交站检测与管理
- `park.py`：自动泊车系统
- `dönüş.py`：转向导航与交通标志响应

**摄像头系统：**
- **主摄像头**：车道检测与道路分析
- **副摄像头**：交通标志识别与障碍物检测

**控制算法：**
- **PID 控制器**：精确转向角计算
- **直方图分析**：车道像素检测与处理
- **多项式拟合**：平滑车道曲线表示
- **滑动窗口**：动态车道跟踪方法

### 🚀 开发路线图

- ✅ 车道检测与跟踪
- ✅ 交通标志识别
- ✅ 障碍物规避
- ✅ 交通灯识别
- ✅ 停车/停靠算法
- 🔄 环岛通行算法
- 🔄 控制 AI
- 🔄 全系统集成（所有模块协同）
- 🔄 适应天气条件
- 🔄 神经网络集成

---

## 日志更新

---

## 2024 年 10 月 3 日（新增与更新）

### 新增

#### 公交站算法：

Teknofest 的任务之一是：当自动驾驶车辆识别到公交站标志时，进入停靠区、等待一段时间，再返回道路继续行驶。为此，我实现并尝试了多种算法。

首先，我计划沿用停车算法中的车道检测方式，寻找停靠区车道中线并引导车辆对齐。但该方法稳定性不足：有时车道丢失，或因车道漂移导致车辆急转，任务失败。

随后，我又尝试持续跟踪摄像头最左侧车道，但效果仍不理想。最终第三版算法达到了预期：识别到公交站标志后，先保持固定转角让车辆直行，同时使用车道摄像头数据搜索蓝色区域。

蓝色区域搜索通过图像处理完成：先用 `inRange` 做蓝色掩膜，再用 `findContours` 提取白色点坐标，进而定位蓝色区域；找到后取其中点。

中点的 x 坐标用于计算位置值：

```python
pos = (540 - center_x) * 0.00513888888
```

该公式使用相机中心与蓝色区域 x 坐标差值，以及 Webots 中像素到米的比例。得到的 `pos` 输入 PID，输出转向角。

用于判断车辆是否已进入停靠区的公式如下：

```python
np.sum(mask == 255) / (img.shape[0] * img.shape[1])
```

该公式计算掩膜中白色像素占比。若大于 0.56，则认为车辆已进入停靠区。车辆停车 10 秒后按预设动作驶出并继续行驶。

该方法在稳定性方面表现良好。

### 更新

为支持 `main.py` 中的公交站逻辑，进行了若干更新。

流程为：先识别并确认标志是否为公交站；若是，则启用公交站算法并把车道摄像头图像传入该算法。算法输出送入 PID，结果作为转向角。接着判断车辆是否在停靠区内；若已进入则等待 10 秒，之后按预设动作驶离停靠区，最后关闭该算法并继续正常行驶。

https://github.com/user-attachments/assets/3796ba41-0a23-4283-8fb9-9ec3148ce33c

---
## 2024 年 9 月 17 日（新增与更新）

### 新增

#### 变道算法：

在出现障碍物或必要情况下，车辆需要切换到对向车道。这里采用摄像头实现变道感知。虽然障碍检测常用 LIDAR，但不少具备自动驾驶功能的电动车企业（如 Tesla）会为降低成本减少 LIDAR，改用摄像头与测距方案。本项目也采用类似思路：不新增 LIDAR，而是把摄像头图像输入自训练 YOLOv4 模型进行障碍识别。

变道将依据相机视觉触发，例如视频中的“禁止进入”标志。根据目标在画面中的左右位置决定向哪侧变道：障碍在左则向右，在右则向左（也可结合车道坐标判断左右车道）。执行时先以固定角度转向一段时间，再反向转回完成横移。变道后重新启用车道检测与跟随，将车辆居中到新车道，直到下一次任务触发。

https://github.com/user-attachments/assets/a90081f1-d1e7-478b-adcc-0c72c80e530e

---
#### 停车算法：

在停车阶段，车辆会执行预定义“盲行”动作，直到识别到停车标志。该过程中持续将摄像头图像输入 YOLOv4 模型。识别到停车标志后，考虑多目标场景，优先使用最接近相机中心的标志与停车区域。随后启用基于 HoughLinesP 的车道检测。

这里不使用主车道算法，因为主算法通过直方图寻找高密度像素区域，可能无法准确抽取停车区中真正可停的目标车道。停车区车道线更复杂，因此开发了基于 HoughLinesP 的专用算法。

该算法选取最接近停车标志 x 坐标的左右车道线，二者定义可停车区域。通过计算中点引导车辆驶入：

(((line_center / (cam_width / 2)) - 1) * -1)

该值输入 PID 控制器以确定转向角。

当前系统尚未完全稳定，后续将继续优化其可靠性与稳定性。

https://github.com/user-attachments/assets/98a1f074-7a3d-4bde-9d32-81b64f40e523

---

### 红灯停车

YOLO 训练数据中加入了交通灯图像，使车辆能够在红灯时停车。当相机图像中识别到红灯，车辆会在一段时间内减速/停车，时间结束后恢复原速。

https://github.com/user-attachments/assets/328c157a-2127-43dd-b30e-6ebad8208eec

---

## 改进说明

9 月 10 日添加的 YOLOv4 模型因训练不足，早期误检较多，影响系统稳定性与可靠性。随后我持续使用现有数据扩充训练。虽然尚未达到理想精度，但相较之前已有明显改进，检测更准确，系统稳定性更高。

---
## 2024 年 9 月 10 日（新增与更新）

### main.py 主程序（更新）

主代码中集成了一个基于 YOLOv4 训练的模型用于检测交通标志。训练数据来自 [TTVS 数据集](https://github.com/ituracingdriverless/TTVS)，但因尚未完全训练，精度仍有限。同时新增 `dönüş.py` 用于车辆左转、右转与直行决策，功能可用但稳定性仍在优化。

[YoloV4 文件](https://drive.google.com/drive/folders/12GEDLy-Ujzgo5AEnpvfesSiQYkwWzi02?usp=sharing)

#### 总体结构

1. **距离控制（`is_close`）**

   为避免 YOLOv4 对同一目标重复检测，加入该函数。通过比较目标中心点距离，当两目标距离低于阈值时判定为同一目标。

2. **交通标志检测与过滤（`get_detected_labels_with_area_filter`）**

   YOLOv4 模型对第二摄像头图像按周期（代码中约每 2 秒）执行检测，避免持续占用资源。模型基于 TTVS 的约 3000 张图像训练，但尚未完全收敛。由于检测结果用于转向逻辑，还加入了面积过滤，小面积目标不触发转向。

#### dönüş.py 转向算法（新增）

车辆根据交通标志执行转向，核心使用 PID 控制以提升平滑性和整体稳定性。识别到标志后调用 `dönüş.py` 的 `start()`：先确定动作（当前支持右转、左转、直行），车辆先直行一段时间，再按目标执行转向；设定目标转角后由 PID 输出实际转角。转向结束后角度归零；左/右转后继续短暂直行，帮助重新检测车道，随后恢复正常车道跟随。

> [!NOTE]
> 由于 YOLOv4 训练尚未完成、准确率仍有限，加之转向算法尚在优化，当前系统整体还未完全稳定。

---

https://github.com/user-attachments/assets/30a03da8-7f35-4071-8cfa-f2636c6b6632

---

## 2024 年 9 月 4 日（新增与更新）

---
### main.py 主程序（新增）

`main.py` 是 Webots 环境中用于引导车辆沿车道行驶的主控制代码。程序通过车载摄像头图像进行车道检测，并使用 PID 控制算法调整转向。

#### 1. 摄像头定义

使用两个摄像头：

- **第一摄像头**：用于检测道路车道并保证车辆稳定跟随。
- **第二摄像头**：用于识别交通标志并据此引导车辆动作。

#### 2. 图像处理

- **图像采集与保存**：摄像头图像通过 `cv2`（OpenCV）处理并保存，用于车道检测与交通标志识别。

#### 3. 车道检测

- **车道检测函数**：调用 `line.py` 中的 `main()` 对第一摄像头图像执行车道检测，为车辆跟随提供必要数据。

#### 4. PID 控制算法

- **PID 控制**：`pid_controller()` 使用车道检测结果计算转向角。通过比例-积分-微分项降低偏差，使车辆保持在车道中央。

#### 5. 运行循环

- **主循环**：车辆持续执行以下步骤：
  - 获取摄像头图像
  - 图像处理并进行车道检测
  - 执行 PID 控制并设置转向角

该结构使车辆能够稳定地沿车道行驶，并在 Webots 中实时运行。

---

## line.py（车道检测算法）（新增）

该算法通过图像处理检测道路车道线。它分析图像下半部分中的车道像素，定位左右车道，并对这些像素拟合多项式曲线，以计算车道曲率和车辆相对位置。

### 算法步骤

#### 1. 图像预处理：
输入图像先转灰度，再进行膨胀和腐蚀以降低噪声，从而更清晰地提取车道线。

#### 2. 直方图分析：
在图像下半部分统计像素密度，用于定位左右车道的初始位置。

#### 3. 滑动窗口法：
通过垂直滑动窗口搜索左右车道像素，并记录其坐标。

#### 4. 多项式拟合：
对检测到的车道像素拟合二次多项式，用于表达和跟踪车道几何形态。

#### 5. 曲率计算：
基于拟合曲线计算车道曲率半径，并估计车辆相对车道中心的位置，从而评估车辆对齐情况。

该算法可用于实时车道跟踪与车辆对齐系统。

---

https://github.com/user-attachments/assets/c2809628-b58f-4afc-876c-97b30633844d

---
