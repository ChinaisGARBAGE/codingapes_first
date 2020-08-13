# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 14:30:19 2020

@author: USER
"""
from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
time.sleep(1)
mc.executeCommand("time set 2000")