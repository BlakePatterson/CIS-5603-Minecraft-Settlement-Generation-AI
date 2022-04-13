#! /usr/bin/python3

__all__ = []
__author__ = "Blake Patterson & Michael Ward"
__version__ = "v5.0"
__date__ = "21 March 2022"

from random import randint

from gdpc import geometry as GEO
from gdpc import interface as INTF
from gdpc import toolbox as TB
from gdpc import worldLoader as WL

import utils.argParser as argParser
import generation.houseGenerator as houseGenerator
import generation.perimeterGenerator as perimeterGenerator
import generation.pathGenerator as pathGenerator
import generation.terraForm as terraForm
import analysis.height_analysis as height_analysis


args, parser = argParser.giveArgs()
buildArea = argParser.getBuildArea(args)

if buildArea == -1:
    exit()
    
    
if __name__ == '__main__':
    
    try: 
        # define build coords
        STARTX, STARTY, STARTZ, ENDX, ENDY, ENDZ = buildArea

        # load worldslice 
        WORLDSLICE = WL.WorldSlice(STARTX, STARTZ,
                                 ENDX + 1, ENDZ + 1)
        
        # create heightmap
        heights = WORLDSLICE.heightmaps["MOTION_BLOCKING_NO_LEAVES"]
        
        # calculate the center x & z coordinates of the build area
        middle_x = round((STARTX + ENDX) / 2)
        middle_z = round((STARTZ + ENDZ) / 2)

        # get the height of the ground in the middle of the build area
        floor_level = heights[(ENDX - middle_x, ENDZ - middle_z)]
        
        # remove trees around house
        if args.terraform is True:
            terraForm.treeAnnihilator(heights, STARTX, STARTY, STARTZ, ENDX, ENDY, ENDZ)
            #terraForm.cleanerTree(heights, buildArea)
        
        # reload worldslice to account for changed blocks
        WORLDSLICE = WL.WorldSlice(STARTX, STARTZ,
                                 ENDX + 1, ENDZ + 1)
        
        # reload heightmap
        heights = WORLDSLICE.heightmaps["MOTION_BLOCKING_NO_LEAVES"]
        
        # calculate buildable areas
        subgrid_sort = height_analysis.find_flat(heights, buildArea)
          
        # build perimeter
        perimeterGenerator.buildPerimeter(heights, buildArea)
        
        #build a house in the center of the build area
        houseGenerator.build_house(middle_x - 10, floor_level, middle_z - 10, 
                                    middle_x + 9, floor_level + 6, middle_z + 9)

        pathGenerator.build_path(STARTX + 10, STARTZ + 10, ENDX - 10, ENDZ - 10, heights, ENDX, ENDZ)

        print("Done!")
        
    except KeyboardInterrupt:
        print("Pressed Ctrl-C to kill program.")
