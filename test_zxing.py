import cv2
import zxingcpp

def extract_qr_code(image_path):
    img = cv2.imread(image_path)
    if img is None:
        return "Image read failed"
    
    # 裁剪前1/3区域
    h, w, _ = img.shape
    roi = img[0:h//3, 0:w]
    
    # zxingcpp 直接处理 BGR 图像
    results = zxingcpp.read_barcodes(roi)
    for result in results:
        return result.text
    return None

image_path = r'c:\Users\HJYEHUANG\WorkBuddy\20260716143631\705de060-9dba-4ce7-ba62-f2421c70818f.jpg'
print(extract_qr_code(image_path))