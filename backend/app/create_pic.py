import base64
import requests
import json
import os
import random
from .services import handle_shape_data

def create_model(data):

    skin,shape,case,gender = handle_shape_data(data)
    # 黄皮肤 沙漏型 thin man

    user_skin = 'Asian'
    if skin == '黑皮肤':
        user_skin = 'Black African'
    elif skin == '白皮肤':
        user_skin = 'White European'

    color = 'yellow'
    if skin == '黑皮肤':
        color = 'black'
    elif skin == '白皮肤':
        color = 'white'

    gender_negative_prompt = 'woman'
    if gender == 'woman':
        gender_negative_prompt = 'man'

    # 配置 API 地址
    url = "http://127.0.0.1:7860/sdapi/v1/txt2img"

    # 读取控制图并编码为 Base64
    def image_to_base64(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8")

    control_image_path = os.path.join(os.getcwd(),'backend','app','poses')  
    poses = ["pose1.png",'pose2.png','pose3.png','pose4.png','pose0.png'] # 替换为你的控制图路径
    control_image_path = os.path.join(control_image_path,poses[random.randint(0,4)])
    control_image_base64 = image_to_base64(control_image_path)

    # 构造 ControlNet 参数（关键部分）
    controlnet_args = [
        {
            "enabled": True,
            "image": control_image_base64,
            "module": "none",                # 预处理器设为 "none"（控制图已预处理）
            "model": "controlV11pSd15_v10 [1ed950ce]",  # ControlNet 模型名称
            "weight": 0.75,                   # 控制权重（0.5-1.5）
            "resize_mode": "Envelope (Outer Fit)",
            "low_vram": True,
            "guidance_start": 0.0,           # 控制生效起始步数（0.0=全程生效）
            "guidance_end": 0.8,             # 控制生效结束步数（1.0=全程生效）
            "control_mode": "My prompt is more important",      # Balanced/My prompt is more important/ControlNet is more important
        }
    ]

    adetailer = [{
            "ad_model": "face_yolov8n.pt",
            "ad_prompt": f"{user_skin} {gender} face,beardless",
            "ad_confidence": 0.7,
            "ad_mask_blur": 4,
            "ad_denoising_strength": 0.4,
            "ad_use_steps": True,
            "ad_steps": 30,
            "ad_use_cfg_scale": True,
            "ad_cfg_scale": 14.0,
            "ad_use_checkpoint": True,
            "ad_checkpoint": 'realisticVisionV60B1_v51HyperVAE [f47e942ad4]',
            "ad_use_sampler": True,
            "ad_scheduler": "Use same scheduler",
            }
    ]
    # 构造完整请求体

    payload = {
        "prompt": f'''
        (8k, best quality, masterpiece:1.2), (realistic, photo-realistic:1.2),(big eyes:1.3)
        (1 {user_skin} {case} {gender}:1.5),perfect face, perfect eyes,(short hair:1.4),({color} race:1.4),(simple hairstyle:1.3),
        (long sleeve:1.1),(beardless:1.3),(minimalist studio background:1.4),(show shoes:1.3),
        studio lighting,pureerosface_v1, (black hanfu:1.5),song style, studio lighting,<lora:hanfu_v30:0.6>
        ''',
        "negative_prompt": f'''
        ({gender_negative_prompt}:1.5),(EasyNegative:1.2),
        (Bad_Prompt_v2:0.8),(Bad_Hands_5),sketch by Bad_Artist, (worst quality, low quality:1.4), (bad anatomy),
        watermark, signature, text, logo,contact, (extra limbs),
        Six fingers,Low quality fingers,monochrome,
        (((missing arms))),(((missing legs))), (((extra arms))),(((extra legs))),less fingers,lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, (depth of field, bokeh, blurry:1.4),blurry background,bandages,
        ''',
        "steps": 20,
        "width": 768,
        "height": 1024,
        "cfg_scale": 9,
        
        "sampler_name": "DPM++ 2M Karras",
        "alwayson_scripts": {
            "ADetailer": {
                "args": adetailer
            },        
            "controlnet": {
                "args": controlnet_args
            },
        }
    }

    # 发送请求
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    result = response.json()

    # 保存生成的图像
    if "images" in result:
        image_data = base64.b64decode(result["images"][0])
        with open("./backend/app/temp/model.png", "wb") as f:
            f.write(image_data)
        print("图像已保存为 output.png")
    else:
        print("生成失败：", result.get("error", "未知错误"))

if __name__ == "__main__":
    data = [80,170,2,0,1]
    create_model(data)