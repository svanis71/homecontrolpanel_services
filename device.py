#!/usr/bin/env python3
from flask import request
from flask_restful import Resource
from tellstick import Tellstick

class Device(Resource):
    def get(self, device_id):
        tellstick = Tellstick()
        return tellstick.getDevice(int(device_id) - 1), 200
                
    def put(self, device_id):
        deviceid = int(device_id)
        error_response = {'message': ''}
        tellstick = Tellstick()
        json = request.json

        if not json:
            print('Ingen json')
            error_response['message'] = 'Saknas grejer i det anropet'
            return error_response, 400

        new_status = request.json['status']
        if new_status is None:
            print('Ingen status')
            error_response['message'] = 'Saknas grejer i det anropet'
            return error_response, 400
        if new_status > 1:
            error_response['message'] = 'Fel status'
            return error_response, 400

        new_status_set = tellstick.changeStatus(deviceid - 1, new_status)
        return {'new_status': new_status_set, 'id': deviceid}, 200
