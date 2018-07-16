from flask import Flask
from flask_restful import Api
from devices import Devices
from device import Device

application = Flask(__name__)
api = Api(application)

api.add_resource(Device, '/device/<device_id>')
api.add_resource(Devices, '/', '/devices')

if __name__ == '__main__':
    application.run()
        
