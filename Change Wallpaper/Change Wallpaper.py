import ctypes
path="KJ.jpg"
ctypes.windll.user32.SystemParametersInfoW(20,0,path,3)