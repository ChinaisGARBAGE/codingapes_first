# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 09:54:06 2020

@author: USER
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
while True:
    hits=mc.events.pollBlockHits()
    if len(hits)>0:
        hits=hits[0]
        x,y,z=hits.pos.x,hits.pos.y,hits.pos.z
        mc.setBlock(x,y,z,57)
        block=mc.getBlock(x,y,z)
        mc.postToChat("恭喜你獵到了"+str(block))