from app import create_app
import os
import subprocess

app = create_app()

if __name__ == '__main__':
    arr = os.getcwd()
    app.run(host='0.0.0.0',threaded=False)

