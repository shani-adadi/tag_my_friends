"""
This is a setup1.py script generated by py2applet

Usage:
    python setup1.py py2app
"""

from setuptools import setup

APP = ['TagMyFriends.py']
DATA_FILES = ['beach-background-with-sunglasses-starfish_1101-313.jpg', 'image_handler.qrc']
OPTIONS = {"includes": ['opencv-python', 'opencv-contrib-python'],
            "packages": ['opencv-python', 'opencv-contrib-python']}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    #install_requires=["opencv-python == 4.1.2.30", "opencv-contrib-python == 4.1.2.30"],
)
