#!/usr/bin/env python3

from flask_restful import Resource

class Device(Resource):
    def get(self, device_id):
        return "{id: 1, description: 'Dev 1', isOn: false}"
                
