### aidress

本项目是一个ai生成模特兼换汉服的网站，其中换汉服调用外部api接口，自行获取api密钥，这是网址
https://www.ailabtools.com/zh-cn/virtual-try-on-clothes

以下是安装过程，分为前端后端以及本地部署生成模特的模型这三个部分
 照着输入
```
npm install
```

 启动前端
```
npm run serve
```

 Compiles and minifies for production
```
npm run build
```

 Lints and fixes files
```
npm run lint
```

 照着输入
```
cd ./backend
```
安装依赖库 
```
pip -r requirements.txt
```
密钥的替换在.backend/app/crawl_pic.py的第14行API_KEY,自行替换

 启动后端

```
python run.py
```

 再切换到项目根目录

```
cd ./stable_disfusion
```
安装一大堆依赖

```
pip install -r requirements.txt
pip install -r requirements_npu.txt
```

 加载模型
```
webui-user.bat
```

然后你就可以换衣服了
浏览器输入localhost:8080/
<img src="D:\chengxu\aidress\lookme.png" alt="lookme" style="zoom:25%;" />

####  注意，这个项目是第一版，还不支持连续生成多个换衣图片，只能一个一个生成，而且只能刷新来重新生成下个图片

这个是前端框架，可以自行了解
 Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).