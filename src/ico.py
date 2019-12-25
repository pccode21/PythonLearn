import PythonMagick
img = PythonMagick.Image('.\PythonLearn\src\images\LOGO.jpg')
img.sample('128x128')
img.write('.\PythonLearn\src\images\LOGO.ico')
