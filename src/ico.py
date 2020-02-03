import PythonMagick
img = PythonMagick.Image('.\PyQt5\python_app\Chapter_two\播放.png')
img.sample('128x128')
img.write('.\PyQt5\python_app\Chapter_two\播放.ico')
