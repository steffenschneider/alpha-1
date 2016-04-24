# coding=utf-8

"""
make a sound
"""

import subprocess
subprocess.call(['/usr/bin/canberra-gtk-play', '--id', 'bell'])
