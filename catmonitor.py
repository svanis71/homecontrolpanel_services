#!/usr/bin/env python3
from flask_restful import Resource
import os;

class CatMonitor(Resource):
    def get(self):
        latest = ''
        if(os.path.exists('/home/pi/cat_is_here')):
            with open('/home/pi/cat_is_here') as f:
                latest = f.read()
        return {'latest': latest}, 200

