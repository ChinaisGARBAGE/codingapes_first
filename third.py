# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 09:54:06 2020

@author: USER
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
def plantTree(x,y,z):
    mc.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,57)
    mc.setBlocks(x,y,z,x,y+4,z,17)
x,y,z=mc.player.getPos()    
for i in range(10):
    plantTree(x+i,y,z)