#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import os
from pandas.io.json import json_normalize
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Rectangle, ConnectionPatch
from matplotlib.offsetbox import  OffsetImage
#import squarify
from functools import reduce


# In[273]:


def sb_pitch(pitch, line, orientation,view):
        
    orientation = orientation
    view = view
    line = line
    pitch = pitch
    
    if orientation.lower().startswith("h"):
        
        if view.lower().startswith("h"):
            fig,ax = plt.subplots(figsize=(8.0,12.0))
            plt.xlim(-1,121)
            plt.ylim(-1,81)
        else:
            fig,ax = plt.subplots(figsize=(10.4,6.8))
            plt.xlim(-1,121)
            plt.ylim(-1,81)
        ax.axis('off') # this hides the x and y ticks
    
        # side and goal lines #
        ly1 = [0,0,80,80,0]
        lx1 = [0,120,120,0,0]

        plt.plot(lx1,ly1,color=line,zorder=5)


        # boxes, 6 yard box and goals

            #outer boxes#
        ly2 = [18,18,62,62] 
        lx2 = [120,102,102,120]
        plt.plot(lx2,ly2,color=line,zorder=5)

        ly3 = [18,18,62,62] 
        lx3 = [0,18,18,0]
        plt.plot(lx3,ly3,color=line,zorder=5)

            #goals#
        ly4 = [36,36,44,44]
        lx4 = [120,120.4,120.4,120]
        plt.plot(lx4,ly4,color=line,zorder=5)

        ly5 = [36,36,44,44]
        lx5 = [0,-0.4,-0.4,0]
        plt.plot(lx5,ly5,color=line,zorder=5)


           #6 yard boxes#
        ly6 = [30,30,50,50]
        lx6 = [120,114,114,120]
        plt.plot(lx6,ly6,color=line,zorder=5)

        ly7 = [30,30,50,50]
        lx7 = [0,6,6,0]
        plt.plot(lx7,ly7,color=line,zorder=5)

        #Halfway line, penalty spots, and kickoff spot
        ly8 = [0,80] 
        lx8 = [60,60]
        plt.plot(lx8,ly8,color=line,zorder=5)


        plt.scatter(60,40,color=line,zorder=5)
        plt.scatter(12,40,color=line,zorder=5)
        plt.scatter(108,40,color=line,zorder=5)

        circle1 = plt.Circle((108.5,40), 9.15,ls='solid',lw=1.5,color=line, fill=False, zorder=1,alpha=1)
        circle2 = plt.Circle((12.5,40), 9.15,ls='solid',lw=1.5,color=line, fill=False, zorder=1,alpha=1)
        circle3 = plt.Circle((60, 40), 9.15,ls='solid',lw=1.5,color=line, fill=False, zorder=2,alpha=1)

        ## Rectangles in boxes
        rec1 = plt.Rectangle((102,18), 120,62,ls='-',color=pitch, zorder=1,alpha=1)
        rec2 = plt.Rectangle((0, 18), 18,62,ls='-',color=pitch, zorder=1,alpha=1)

        ## Pitch rectangle
        rec3 = plt.Rectangle((-1, -1), 122,82,ls='-',color=pitch, zorder=1,alpha=1)

        ax.add_artist(rec3)
        ax.add_artist(circle1)
        ax.add_artist(circle2)
        ax.add_artist(rec1)
        ax.add_artist(rec2)
        ax.add_artist(circle3)
        
    else:
        if view.lower().startswith("h"):
            fig,ax = plt.subplots(figsize=(10.4,6.8))
            plt.ylim(59,121)
            plt.xlim(-1,81)
        else:
            fig,ax = plt.subplots(figsize=(6.8,10.4))
            plt.ylim(-1,105)
            plt.xlim(-1,69)
        ax.axis('off') # this hides the x and y ticks

        # side and goal lines #
        lx1 = [0,0,80,80,0]
        ly1 = [0,120,120,0,0]

        plt.plot(lx1,ly1,color=line,zorder=5)


        # boxes, 6 yard box and goals

            #outer boxes#
        lx2 = [18,18,62,62] 
        ly2 = [120,102,102,120]
        plt.plot(lx2,ly2,color=line,zorder=5)

        lx3 = [30,30,50,50] 
        ly3 = [120,114,114,120]
        plt.plot(lx3,ly3,color=line,zorder=5)

            #goals#
        lx4 = [36,36,44,44]
        ly4 = [120,120.4,120.4,120]
        plt.plot(lx4,ly4,color=line,zorder=5)

        lx5 = [30.34,30.34,37.66,37.66]
        ly5 = [0,-0.2,-0.2,0]
        #plt.plot(lx5,ly5,color=line,zorder=5)


           #6 yard boxes#
        lx6 = [24.84,24.84,43.16,43.16]
        ly6 = [104,99.5,99.5,104]
        #plt.plot(lx6,ly6,color=line,zorder=5)

        lx7 = [36,36,44,44]
        ly7 = [0,4.5,4.5,0]
       # plt.plot(lx7,ly7,color=line,zorder=5)

        #Halfway line, penalty spots, and kickoff spot
        lx8 = [0,80] 
        ly8 = [120,120]
        plt.plot(lx8,ly8,color=line,zorder=5)


        #plt.scatter(34,93,color=line,zorder=5)
        plt.scatter(40,108,color=line,zorder=5)
        plt.scatter(40,60,color=line,zorder=5)

        circle1 = plt.Circle((40,108), 9.15,ls='solid',lw=1.5,color=line, fill=False, zorder=1,alpha=1)
        circle2 = plt.Circle((40,108), 9.15,ls='solid',lw=1.5,color=line, fill=False, zorder=1,alpha=1)
        circle3 = plt.Circle((40,60), 9.15,ls='solid',lw=1.5,color=line, fill=False, zorder=2,alpha=1)
        
        ## Rectangles in boxes
        rec1 = plt.Rectangle((18, 102), 62,120,ls='-',color=pitch, zorder=1,alpha=1)
        rec2 = plt.Rectangle((20, 0), 30,16.5,ls='-',color=pitch, zorder=1,alpha=1)

        ## Pitch rectangle
        rec3 = plt.Rectangle((-1, -1), 82,122,ls='-',color=pitch, zorder=1,alpha=1)

        ax.add_artist(rec3)
        ax.add_artist(circle1)
        ax.add_artist(circle2)
        ax.add_artist(rec1)
        ax.add_artist(rec2)
        ax.add_artist(circle3)
        #ax.add_artist(rightArc)


# In[274]:


"""call this for full horizontal pitch """
#sb_pitch("#195905","#faf0e6","horizontal","full")

"""call this for half vertical pitch """
#sb_pitch("#195905","#faf0e6","vertical","half")

