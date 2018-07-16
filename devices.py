#!/usr/bin/env python3

from flask_restful import Resource

class Devices(Resource):
    def get(self):
        return "[{id: 1, description: 'Dev 1', isOn: false}]"

