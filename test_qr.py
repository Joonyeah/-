import cv2
from pyzbar.pyzbar import decode

def extract_qr_code(image_path):
    img = cv2.imread(image_path)
    if img is None: return None
    
    # 裁剪海报前 1/3 区域
    h, w, _ = img.shape
    roi = img[0:h//3, 0:w]
    
    # 放大 ROI 区域
    roi_large = cv2.resize(roi, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    
    # 二值化
    gray = cv2.cvtColor(roi_large, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # 解码
    for img_to_decode in [roi_large, thresh]:
        for obj in decode(img_to_decode):
            return obj.data.decode('utf-8')
    return None

image_path = r'c:\Users\HJYEHUANG\WorkBuddy\20260716143631\705de060-9dba-4ce7-ba62-f2421c70818f.jpg'
print(f"Extracted URL: {extract_qr_code(image_path)}")
