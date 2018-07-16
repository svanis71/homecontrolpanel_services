#imports allowing the use of our library
from ctypes import c_int, c_ubyte, c_void_p, POINTER, string_at
from ctypes import cdll, CFUNCTYPE

# Import the telldus api
lib = cdll.LoadLibrary('libtelldus-core.so.2')

class Tellstick(self):
