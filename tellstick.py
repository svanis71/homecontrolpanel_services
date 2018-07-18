#imports allowing the use of our library
from ctypes import c_int, c_ubyte, c_void_p, POINTER, string_at
from ctypes import cdll, CFUNCTYPE

# Import the telldus api
lib = cdll.LoadLibrary('libtelldus-core.so.2')

TELLSTICK_TURNON = 1
TELLSTICK_TURNOFF = 2
TELLSTICK_BELL = 4
TELLSTICK_DIM = 16
TELLSTICK_UP = 128
TELLSTICK_DOWN = 256

class Tellstick:
    def __init__(self):
        self.supportedMethods = TELLSTICK_TURNON | TELLSTICK_TURNOFF

    def getDevice(self, device_id):
        id = lib.tdGetDeviceId(device_id)
        methods = lib.tdMethods(id, self.supportedMethods)
        status = lib.tdLastSentCommand(id, methods)
        name_ptr = lib.tdGetName(id)
        name = string_at(name_ptr).decode('UTF-8')
        is_on = True if status & TELLSTICK_TURNON else False
        lib.tdReleaseString(name_ptr)
        lib.tdClose()
        return {'id': id, 'description': name, 'isOn': is_on}

    
    def getAllDevices(self):
        lib.tdInit()
        numDevices = lib.tdGetNumberOfDevices()
        devices = []
        for i in range(numDevices):
            id = lib.tdGetDeviceId(i)
            methods = lib.tdMethods(id, self.supportedMethods)
            status = lib.tdLastSentCommand(id, methods)
            name_ptr = lib.tdGetName(id)
            name = string_at(name_ptr).decode('UTF-8')
            is_on = True if status & TELLSTICK_TURNON else False
            lib.tdReleaseString(name_ptr)
            devices.append({"id": id, "description": name, "isOn": is_on})
        lib.tdClose()
        return devices

    def changeStatus(self, device_id, new_status):
        lib.tdInit()
        id = lib.tdGetDeviceId(device_id)
        methods = lib.tdMethods(id, self.supportedMethods)
        print('TURN %s %d' % ('ON' if new_status == 1 else 'OFF', id))
        if new_status == 0:
            lib.tdTurnOff(id)
        if new_status == 1:
            lib.tdTurnOn(id)
        status = lib.tdLastSentCommand(id, methods)
        next_status = 1 if status & TELLSTICK_TURNON else 0
        lib.tdClose()
        return next_status
