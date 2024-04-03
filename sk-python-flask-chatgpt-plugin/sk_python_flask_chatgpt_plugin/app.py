import os
from flask import Flask, request, Response, send_file
from flask_cors import CORS
#from semantic_kernel.kernel_exception import KernelException

#from sk_python_flask_chatgpt_plugin.kernel_utils import (
#    create_kernel_for_request,
##    create_context_variables_from_request,
#)


app = Flask(__name__)
CORS(app)
app.config['login'] = False
app.config['downloaded'] = False

@app.route("/download_code", methods=["POST"])
def execute_download():
    try:
        body = request.get_json()
        print(body)
        filename = body['filename']
        if not filename:
            filename = 'code.py'
        code = body['code']
        code = code.encode('latin-1', 'backslashreplace').decode('unicode-escape')
        with open(filename, 'w') as f:
            f.write(code)
        app.config['downloaded'] = True
        print("Successfully downloaded code")
        return 'Success', 200
    except:
        return 'Failure', 500

@app.route("/push_code", methods=["POST"])
def execute_push():
    if not app.config['login']:
        return 'Unauthorized', 401
    body = request.get_json()
    branch = body['branch']
    filename = body['filename']
    if not os.path.exists(filename):
        return 'File not found', 404
    if branch == 'my_cool_branch':
        print(f"Successfully pushed {filename} to {branch}")
        return 'OK', 200
    print(f'branch was {branch}')
    return 'branch not found', 404

@app.route("/login", methods=["POST"])
def execute_login():
    body = request.get_json()
    key = body['key']
    if key == '123Key':
        app.config['login'] = True
        print(f"Successfully logged in with key {key}")
        return "Successfully logged in", 200
    else:
        return 'Unauthorized', 401

@app.route("/get_key", methods=["GET"])
def execute_get_login_key():
    return '123Key', 200

@app.route("/get_active_branch", methods=["GET"])
def execute_get_active_branch():
    return 'my_cool_branch', 200

@app.route("/.well-known/ai-plugin.json", methods=["GET"])
def get_ai_plugin():
    with open("./.well-known/ai-plugin.json", "r") as f:
        text = f.read()
        return Response(text, status=200, mimetype="text/json")


@app.route("/logo.png")
def get_logo():
    return send_file("../logo.png", mimetype="image/png")


@app.route("/openapi.yaml", methods=["GET"])
def get_openapi():
    with open("./openapi.yaml", "r") as f:
        text = f.read()
        return Response(text, status=200, mimetype="text/yaml")
