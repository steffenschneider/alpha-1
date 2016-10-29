import datetime
import glob
import inspect
import logging
import math
import os
import random
import re
import socket
import string
import struct
import subprocess
import sys
import time
import urllib
import webbrowser
import xml.etree.ElementTree as ET
from time import gmtime, strftime, localtime
from tkinter import SUNKEN, Tk, Canvas, Frame

import PIL  # correct in Python3
import easygui
import numpy
import pyautoit
import pymodbus3
import pymouse
import pymysql
import pyvirtualdisplay
import pywin32  # only win?
import pywinauto  # only win?
import requests
import scipy  # zuerst numpy installieren
import vpython
from selenium import webdriver
from visual import *

#############################################################

if os.name == 'nt':  # Windows
    import winsound

# ignore!
SUNKEN
Tk
Canvas
Frame
gmtime
localtime
strftime
urllib
time
sys.argv
vpython.arrow
webbrowser.browser
ET._Element_Py
socket
string
struct
re
subprocess
datetime
easygui
glob
inspect
logging
math
numpy
os
PIL
pyautoit
pymodbus3
pymouse
pymysql
pyvirtualdisplay
pywin32
pywinauto
random
requests
scipy
webdriver
winsound
