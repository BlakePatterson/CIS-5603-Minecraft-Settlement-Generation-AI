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
import analysis.heightAnalysis as heightAnalysis


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
        subgrid_sort = heightAnalysis.find_flat(heights, buildArea)
          
        # build perimeter
        perimeterGenerator.buildPerimeter(heights, buildArea)

        # build village
        door_coords = houseGenerator.build_settlement(subgrid_sort)

        # reload worldslice to account for changed blocks
        WORLDSLICE = WL.WorldSlice(STARTX, STARTZ,
                                 ENDX + 1, ENDZ + 1)

        # reload heightmap
        heights = WORLDSLICE.heightmaps["MOTION_BLOCKING_NO_LEAVES"]

        # build paths between all the houses
        pathGenerator.build_paths_between_houses(door_coords, heights, STARTX, STARTZ, ENDX, ENDZ)

        # pathGenerator.build_path(STARTX + 5, STARTZ + 5, ENDX - 5, ENDZ - 5, heights, STARTX, STARTZ)

        print("Done!")
        
    except KeyboardInterrupt:
        print("Pressed Ctrl-C to kill program.")
