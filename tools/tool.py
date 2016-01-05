# -*- coding: utf-8 -*-

import os

tool_path = os.path.abspath(__file__)
tool_dir = os.path.dirname(tool_path)

saved_path = os.getcwd()
os.chdir(tool_dir)

if not os.path.exists("gyp"):
    cmd = "7z x {0} -o{1}".format("gyp.7z", ".")
    os.system(cmd)

os.chdir(saved_path)
