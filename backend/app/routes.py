from flask import Blueprint, request, send_file
from .services import process # 导入处理数据的服务
from .create_pic import create_model # 导入创建图片的服务
from .crawl_pic import create # 导入换装图片的服务
import os
import json
import shutil


# 定义 API 路由蓝图

api_blueprint = Blueprint('api', __name__)


# 处理 Vue 发送的数据

@api_blueprint.route('/receive_shape_data', methods=['POST'])
def receive_shape_data():
    # 获取前端传递的数据
    data = request.get_json()  # 获取 POST 请求的 JSON 数据
    
    file = create_model(data)
    # 返回处理结果S
    return 'ok', 200

@api_blueprint.route('/send_model_img', methods=['POST'])
def send_model_img():
    model_dir = os.getcwd()
    file = os.path.join(model_dir,'backend','app','temp','model.png')
    return send_file(file, mimetype='image/jpeg')

@api_blueprint.route('/receive_clothes_img', methods=['POST'])

def receive_clothes_img():
    dirs = json.loads(request.data.decode('utf-8'))
    for key in dirs:
        if dirs[key] != None:
            # 复制文件并重命名
            shutil.copy(os.path.join(os.getcwd(),'src','components','img','clothes',f"{dirs[key][5:]}.jpg"),os.path.join(os.getcwd(),'backend','app','uploads',f'file{key[-1]}.jpg'))

    return 'ok', 200


@api_blueprint.route('/send_clothed_img', methods=['POST'])

def send_clothed_imgs():

    model_dir = os.getcwd()
    clothes_arr = process()
    for clothe in clothes_arr:
        create(clothe)   
    file = os.path.join(model_dir,'backend','app','temp','output_clothed.png')
    return send_file(file, mimetype='image/jpeg')
    # with open(f"{model_dir}/OOtDifussion/run/images_output/out_hd_0.png") as f:
    #     return send_file(f, mimetype='image/jpeg')


@api_blueprint.route('/close_SD', methods=['GET'])

def close_SD():
    # with open("D:\\chengxu\\aidress\\stable_disfusion\\webui.pid", "r") as f:
    #     pid = int(f.read().strip())
    # # 终止进程
    # os.system(f"taskkill /f /pid {pid}")
    return 'ok', 200
