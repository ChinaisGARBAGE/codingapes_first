# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 13:34:47 2020

@author: USER
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
mc.player.setPos(100,100,100)
a=10
while a>0:
x=100
y=100
z=100
    mc.setBlock(100,y,100,57)
    y=y+1
    a=a-1
x=100
y=100
z=100
mc.setBlock(x,y,z,57)
mc.setBlock(x+1,y,z,57)
mc.setBlock(x+2,y,z,57)
mc.setBlock(x+2,y,z-1,57)
mc.setBlock(x+2,y,z-2,57)
mc.setBlock(x+1,y,z-2,57)
mc.setBlock(x,y,z-2,57)
mc.setBlock(x,y,z-1,57)