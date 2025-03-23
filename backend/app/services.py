import os
import time
import subprocess
import base64
import requests
import json
import random
import shutil


def handle_shape_data(data):

    
    # 这里可以进行一些逻辑处理
    kg = data[0]
    cm = data[1]
    skin = ["黑皮肤","黄皮肤","白皮肤"]
    user_skin = skin[data[2]]
    shape_woman = ["沙漏型","直筒型","倒三角","梨型","苹果型"]
    shape_man = ["O型",'正三角型','矩型','倒三角型','倒梯型']
    if data[4] == 0:
        user_shape = shape_woman[data[3]]
    else:
        user_shape = shape_man[data[3]]
    gender = ["woman","man"]
    user_gender = gender[data[4]]
    user_case = ''
    bmi = kg / ((cm / 100) ** 2)
    if bmi < 18.5:
        user_case = 'thin'
    elif 18.5 <= bmi < 24:
        user_case = ''
    elif 24 <= bmi < 28:
        user_case = 'overweight'
    else:
        user_case = 'obese'            

    return user_skin,user_shape,user_case,user_gender


def handle_clothes_img(data):
    pass

def handle_model_img(data):
    pass

def process():
    clothe_arr = []
    clothe_path = os.path.join(os.getcwd(),'backend','app','uploads')
    for i in range(5):
        if os.path.exists(clothe_path + f'\\file{i + 1}.jpg'):
            clothe_arr.append(f'file{i + 1}.jpg')
    return clothe_arr

def create(clothe):
    img_dir = os.getcwd()
    imgs_dir = os.path.join(img_dir,'backend','app','uploads')
    py_dir = os.path.join(img_dir,'OOTDiffusion','run')
    model_dir = os.path.join(py_dir,'images_output','out_dc_0.png')
    clothes_dir = os.path.join(imgs_dir,clothe)
    index = int(clothe[4]) - 2
    if clothe == 'file5.jpg':
        index = 2
    cmd = f'python run_ootd.py --model_path {model_dir} --cloth_path {clothes_dir} --scale 0.75 --sample 1 --step 15' 
    cmdd = f'python run_ootd.py --model_path {model_dir} --cloth_path {clothes_dir} --model_type dc --category {index} --scale 0.75 --sample 1 --step 20'
    start_time = time.time()
    try:
        process = subprocess.Popen(
            cmdd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            cwd=py_dir
        )
        
        # 实时读取输出
        while True:
            line = process.stdout.readline()
            if not line and process.poll() is not None:
                break
        
        elapsed = time.time() - start_time
        print(f"命令执行完成，耗时 {elapsed:.2f} 秒")
        os.remove(clothes_dir)
    except Exception as e:
        print(f"执行失败: {e}")
        return time.time() - start_time
        
def create_model(data):
    skin,shape,case,gender = handle_shape_data(data)
    gender_negative_prompt = 'woman'
    if gender == 'woman':
        gender_negative_prompt = 'man'
    skin_prompt = {'黑皮肤':'(black:1.3)','黄皮肤':'(Asian:1.3)','白皮肤':'(white:1.3)'}
    base_positive_prompt = f'''
    (a {skin_prompt[skin]} young {case} {gender}:1.3),
    (simple white fitted T-shirt:1.2), (fitted jeans:1.4),
    (ultra realistic:1.3), (best quality:1.4), 8k,
    (symmetrical face:1.3), perfectly aligned eyes, balanced facial features, 
    (standing on flat ground: 1.4), 
    (clean sneakers:1.2), (visible face:1.3), 
    (minimalist studio background:1.4), studio lighting, sharp focus, 
    professional photography,  
    Canon EOS R5, depth of field
    '''
    base_negative_prompt = f'''
    ({gender_negative_prompt}:1.4),(nsfw:1.5),(ugly face:1.5),
    (deformed, distorted:1.3), (blurry:1.2), low resolution, cropped legs, hidden feet,  
    (cut off head:1.3), (face covered:1.4), (hat:1.4),(cap:1.4),(sunglasses:1.1), (barefoot:1.3),  
    (extra limbs:1.2), (unnatural pose:1.1), (crowded background:1.4), (text, watermark:1.3),  
    cartoon, anime, (baggy clothes:1.1), (poor lighting:1.1), (grainy:1.1)
    '''
    url = "http://127.0.0.1:7860/sdapi/v1/txt2img"

    # 读取控制图并编码为 Base64
    def image_to_base64(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8")
    control_image_path = os.path.join(os.getcwd(),'backend','app','poses')  
    poses = ["pose1.png",'pose2.png','pose3.png','pose4.png','pose0.png'] 
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
    adetailer = {
        'args' : [
            True,
            False,
            {
                "ad_model": "face_yolov8n.pt",
                'ad_tab_enabled': True,
                "ad_prompt": "Asian male face",  # 使用你的面部提示词
                'ad_negative_prompt':"Asian woman face",
                "ad_denoising_strength": 0.4,
                "ad_mask_blur": 4,
                "ad_inpaint_only_masked": True,
                "ad_inpaint_only_masked_padding": 32,
                "ad_use_steps": True,
                "ad_steps": 30,
                "ad_use_cfg_scale": True,
                "ad_cfg_scale": 12.5,
                "ad_use_checkpoint": True,
                "ad_checkpoint": "realisticVisionV60B1_v51HyperVAE [f47e942ad4]",
                "ad_use_sampler": True,
                "ad_sampler": "DPM++ 2M",
                "ad_scheduler": "Use same scheduler",

            }
        ]
    }
    payload = {
        "prompt": base_positive_prompt,
        "negative_prompt": base_negative_prompt,
        "steps": 20,
        "width": 768,
        "height": 1024,
        "cfg_scale": 6,
        "sampler_name": "DPM++ 2M Karras",
        "alwayson_scripts": {
            "controlnet": {
                "args": controlnet_args
            },
            "ADetailer": adetailer
        }
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    result = response.json()
    if "images" in result:
        image_data = base64.b64decode(result["images"][0])
        with open("output.png", "wb") as f:
            f.write(image_data)
        print("图像已保存为 output.png")
        shutil.copy('output.png',os.path.join(os.getcwd(),'OOTDiffusion','run','images_output','out_dc_0.png'))

def close_SD():
    pass
    # with open("D:\\chengxu\\aidress\\stable_disfusion\\webui.pid", "r") as f:
    #     pid = int(f.read().strip())
    # 终止进程
    # os.system(f"taskkill /f /pid {pid}")

if __name__ == '__main__':
    create('file5.jpg')     