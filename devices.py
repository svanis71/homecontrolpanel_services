#!/usr/bin/env python3

from flask_restful import Resource
from tellstick import Tellstick

class Devices(Resource):
    def get(self):
        tellstick = Tellstick()
        return tellstick.getAllDevices(), 200

