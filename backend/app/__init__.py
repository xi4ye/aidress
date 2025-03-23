from flask import Flask
from flask_cors import CORS
from .routes import api_blueprint  # 导入定义 API 路由的蓝图

def create_app():
    app = Flask(__name__)
    
    # 启用跨域资源共享（CORS）
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    # 注册蓝图
    app.register_blueprint(api_blueprint, url_prefix='/api')
    
    return app
