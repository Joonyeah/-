import json
from http.server import BaseHTTPRequestHandler
from auto_validator import AutoValidator
import os

# 此为 Vercel Serverless Function 入口适配器
def handler(request):
    try:
        # 解析请求体中的活动配置数据
        body = request.get_json()
        poster_url = body.get('poster_url')
        config = body.get('config')
        
        # 执行校验
        validator = AutoValidator(poster_url, config)
        is_valid, total = validator.validate_probabilities()
        
        return {
            "statusCode": 200,
            "body": json.dumps({
                "valid": is_valid,
                "total_probability": total,
                "message": "校验完成"
            })
        }
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}