from flask import Flask
from flask_restful import Api
from flask_cors import CORS, cross_origin
from devices import Devices
from device import Device
from catmonitor import CatMonitor

application = Flask(__name__)
cors = CORS(application)
application.config['CORS_HEADERS'] = 'Content-Type'
api = Api(application)

api.add_resource(Device, '/device/<device_id>')
api.add_resource(Devices, '/', '/devices')
api.add_resource(CatMonitor, '/pollcat')

if __name__ == '__main__':
    application.run()
        
