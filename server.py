from flask import Flask, url_for, Response,json, request, send_file
import jsonpickle
import numpy as np
import base64
import cv2

class Pose():
    def __init__(self, name = None, x = None, y = None, ang = None):
        self.name = name
        self.x = x
        self.y = y
        self.ang = ang


class Server():
    def __init__(self, ):
        self.ip = "192.168.1.2"
        self.app = Flask(__name__)
        self.init_variables()
    
    def init_variables(self):
        self.robot_pose = Pose()
        self.goal_pose = Pose()

    def run(self):
        self.app.run(host="0.0.0.0",port=5010)



    @self.self.app.route('/')
    def api_root(self):
        data = {'text':'Welcome to the Robot root page!'}
        js = json.dumps(data)
        resp = Response(js, status=200, mimetype='application/json')
        return resp

    @self.app.route('/postScreenPosition', methods = ['POST'])
    def api_postScreenPosition(self):
        recived = json.loads(request.data)
        goToX = recived['x']
        goToY = recived['y']
        return recived

    @self.app.route('/getScreenPosition', methods = ['GET'])
    def api_getScreenPosition(self):
        data = {'x': goToX, 'y': goToY}
        js = json.dumps(data)
        resp = Response(js, status=200, mimetype='application/json')
        return resp

    @self.app.route('/postAmbient', methods = ['POST'])
    def api_postAmbient(self):
        recived = json.loads(request.data)
        ambient = recived['ambiente']
        f = open("Desktop/Server/cache.txt","w+")
        f.write(ambient)
        f.close()
        return ambient

    @self.app.route('/getAmbient', methods = ['GET'])
    def api_getAmbient(self):
        f = open("Desktop/Server/cache.txt","r")
        content = f.read()
        f.close()
        
        data = {
            'ambient': content,
        }
        js = json.dumps(data)

        resp = Response(js, status=200, mimetype='application/json')
        return resp


    @self.app.route('/postRobotMap', methods=['POST'])
    def api_postRobotMap(self):
        recived = json.loads(request.data)
        print(recived)
        mapa = recived['mapImg']
        print('imagem: ' + mapa)
        return mapa

    @self.app.route('/getRobotMap', methods = ['GET'])
    def api_getRobotMap(self):
        img = open('Desktop/Server/robot.jpg', 'rb').read()
        encoded_string = base64.b64encode(img)
        data = {'img': encoded_string}
        js = json.dumps(data)
        resp = Response(js, status=200, mimetype='application/json')
        return resp



    @self.app.route('/post_PC_on', methods = ['POST'])
    def api_postRobotPosition():
        self.PC_on = request.data
        return Response(self.PC_on, status=200, mimetype='application/json')
    @self.app.route('/get_PC_on', methods = ['GET'])
    def api_getRobotPosition(self):
        return Response(self.PC_on, status=200, mimetype='application/json')


    @self.app.route('/post_App_on', methods = ['POST'])
    def api_postRobotPosition():
        self.App_on = request.data
        return Response(self.App_on, status=200, mimetype='application/json')
    @self.app.route('/get_App_on', methods = ['GET'])
    def api_getRobotPosition(self):
        return Response(self.App_on, status=200, mimetype='application/json')


    @self.app.route('/post_navigation_mode', methods = ['POST'])
    def api_postRobotPosition():
        self.navigation_mode = request.data
        return Response(self.navigation_mode, status=200, mimetype='application/json')
    @self.app.route('/get_navigation_mode', methods = ['GET'])
    def api_getRobotPosition(self):
        return Response(self.navigation_mode, status=200, mimetype='application/json')


    @self.app.route('/post_maps_list', methods = ['POST'])
    def api_postRobotPosition():
        self.maps_list = request.data
        return Response(self.maps_list, status=200, mimetype='application/json')
    @self.app.route('/get_maps_list', methods = ['GET'])
    def api_getRobotPosition(self):
        return Response(self.maps_list, status=200, mimetype='application/json')


    @self.app.route('/post_apagou_mapa', methods = ['POST'])
    def api_postRobotPosition():
        self.apagou_mapa = request.data
        return Response(self.apagou_mapa, status=200, mimetype='application/json')
    @self.app.route('/get_apagou_mapa', methods = ['GET'])
    def api_getRobotPosition(self):
        return Response(self.apagou_mapa, status=200, mimetype='application/json')










    @self.app.route('/postRobotPosition', methods = ['POST'])
    def api_postRobotPosition():
        self.robot_pose = request.data
        return Response(self.robot_pose, status=200, mimetype='application/json')

    @self.app.route('/getRobotPosition', methods = ['GET'])
    def api_getRobotPosition(self):
        return Response(self.robot_pose, status=200, mimetype='application/json')

if __name__ == '__main__':
    s = Server()
    s.run()