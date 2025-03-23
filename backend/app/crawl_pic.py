import requests
import time
import os


#-------------------------------------------
# 1. 发起异步任务请求
#-------------------------------------------
def submit_try_on_task(clothe):

    
    img_dir = os.path.join(os.getcwd(),'backend','app','uploads',clothe)
    # 配置参数
    API_KEY = "lSDoue50U67kFIicDASdV1BgQ122Gbsxip4La9wmBvJnThuWZd0ozKJ8MvbHjqCH"  # 替换为你的API密钥
    API_ENDPOINT = "https://www.ailabapi.com/api/portrait/editing/try-on-clothes"

    # 文件路径（需替换为实际路径）
    PORTRAIT_PATH = "./backend/app/temp/model.png"    # 肖像图片（<3MB，JPG/JPEG/PNG）
    CLOTHES_PATH = img_dir                      # 衣物图片（<3MB，JPG/JPEG/PNG）
    CLOTHES_TYPE = "full_body"            # 衣物类型：upper_body/lower_body/full_body


    headers = {"ailabapi-api-key": API_KEY}
    
    # 准备multipart/form-data数据
    files = {
        "person_image": open(PORTRAIT_PATH, "rb"),
        "clothes_image": open(CLOTHES_PATH, "rb")
    }
    data = {
        "task_type": "async", 
        "clothes_type": CLOTHES_TYPE
    }
    
    # 发送POST请求
    response = requests.post(API_ENDPOINT, headers=headers, data=data, files=files)
    
    # 处理响应
    if response.status_code == 200:
        result = response.json()
        if result.get("error_code") == 0:
            task_id = result.get("task_id")
            print(f"任务提交成功！任务ID: {task_id}")
            return task_id
        else:
            print(f"API错误：{result.get('error_msg')}")
            return None
    else:
        print(f"HTTP错误码：{response.status_code}, 响应内容：{response.text}")
        return None

#-------------------------------------------
# 2. 查询异步任务结果
#-------------------------------------------
def check_async_result(task_id):


    API_KEY = "lSDoue50U67kFIicDASdV1BgQ122Gbsxip4La9wmBvJnThuWZd0ozKJ8MvbHjqCH"
    RESULT_URL = f"https://www.ailabapi.com/api/common/query-async-task-result"
    
    params = {
        "task_id": task_id
    }
    while True:
        response = requests.get(RESULT_URL, headers={"ailabapi-api-key": API_KEY},params=params)
        
        if response.status_code != 200:
            print(f"查询失败, HTTP错误码：{response.status_code}")
            break
            
        result = response.json()
        
        # 检查公共错误
        if result.get("error_code") != 0:
            print(f"任务处理错误：{result.get('error_msg')}")
            break
            
        # 处理业务状态
        task_status = result.get("task_status")
        
        if task_status == 2:  # 任务成功
            image_url = result["data"]["image"]
            print(f"任务完成！图片URL：{image_url}\n（有效期24小时内下载保存）")
            return image_url
        elif task_status in [0, 1]:  # 排队中/处理中
            print(f"任务状态：{task_status}，等待5秒后重试...")
            time.sleep(5)
        else:  # 未知状态
            print(f"未知任务状态：{task_status}")
            break

#-------------------------------------------
# 主流程
#-------------------------------------------
def create(clothe):


    # 提交任务

    task_id = submit_try_on_task(clothe)    
    if task_id:
        # 查询结果（阻塞式等待）
        image_url = check_async_result(task_id)        
        # 如果获取到URL，可添加下载逻辑：
        if image_url:
            # 下载图片
            response = requests.get(image_url)
            if response.status_code == 200:
                with open("./backend/app/temp/output_clothed.png", "wb") as f:
                    f.write(response.content)
                    print("图片下载成功！")
            else:
                print(f"图片下载失败：HTTP错误码 {response.status_code}")
        else:
            print("任务结果获取失败！")
    else:
        print("任务提交失败！")

    # 删除衣服图片
    os.remove(os.path.join(os.getcwd(),'backend','app','uploads',clothe))    

if __name__ == "__main__":
    create('file8.jpg')
    # check_async_result('1741611589736.862da763-142e-a124-0d6d-ffda2bf34d78')