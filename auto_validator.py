import json
import cv2
from pyzbar.pyzbar import decode

class AutoValidator:
    def __init__(self, poster_path, config_json_path):
        self.poster_path = poster_path
        self.config = json.load(open(config_json_path, 'r', encoding='utf-8'))

    def validate_probabilities(self):
        """校验奖池概率总和是否为100%"""
        probs = [item['prob'] for item in self.config['rewards']]
        total = sum(probs)
        is_valid = abs(total - 1.0) < 0.001
        return is_valid, total

    def run_all_checks(self):
        """运行所有校验规则"""
        print("--- 开始自动化校验 ---")
        is_valid, total = self.validate_probabilities()
        if is_valid:
            print(f"✅ 奖池概率校验通过 (Sum: {total})")
        else:
            print(f"❌ 奖池概率校验失败 (Sum: {total})")

if __name__ == "__main__":
    # 示例使用，后期可接自动化流水线
    # validator = AutoValidator('poster.jpg', 'config.json')
    # validator.run_all_checks()
    pass