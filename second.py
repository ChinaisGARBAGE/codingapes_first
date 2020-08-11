# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 14:07:44 2020

@author: USER
"""
from mcpi.minecraft import Minecraft
import time
import random
mc=Minecraft.create()
time.sleep(1)

x,y,z=mc.player.getTilePos()

color=random.randrange(0,58)
mc.setBlocks(x+100,y-1,z+100,x-100,y-1,z-100,95,color)
time.sleep(0.5)
try:
    blockType=int(input("Block id:"))
    mc.setBlock(x,y,z,blockType)
except:
    print("InvaLid")