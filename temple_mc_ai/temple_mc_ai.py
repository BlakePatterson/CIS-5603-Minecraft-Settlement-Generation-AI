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


args, parser = argParser.giveArgs()
buildArea = argParser.getBuildArea(args)

if buildArea == -1:
    exit()
    

STARTX, STARTY, STARTZ, ENDX, ENDY, ENDZ = buildArea

WORLDSLICE = WL.WorldSlice(STARTX, STARTZ,
                         ENDX + 1, ENDZ + 1)


def buildPerimeter(heights):
    """Build a wall along the build area border.
    """

    print("Building walls...")

    for x in range(STARTX, ENDX):
        z = STARTZ
        y = heights[(x - STARTX, z - STARTZ)]
        INTF.placeBlock(x, y - 1, z, "cobblestone")
        GEO.placeCuboid(x, y, z, x, y + 4, z, "granite_wall")
    for z in range(STARTZ, ENDZ):
        x = STARTX
        y = heights[(x - STARTX, z - STARTZ)]
        INTF.placeBlock(x, y - 1, z, "cobblestone")
        GEO.placeCuboid(x, y, z, x, y + 4, z, "red_sandstone_wall")
    for x in range(STARTX, ENDX):
        z = ENDZ
        y = heights[(x - STARTX, z - STARTZ)]
        INTF.placeBlock(x, y - 1, z, "cobblestone")
        GEO.placeCuboid(x, y, z, x, y + 4, z, "sandstone_wall")
    for z in range(STARTZ, ENDZ):
        x = ENDX
        y = heights[(x - STARTX, z - STARTZ)]
        INTF.placeBlock(x, y - 1, z, "cobblestone")
        GEO.placeCuboid(x, y, z, x, y + 4, z, "prismarine_wall")

if __name__ == '__main__':
    
    try:
        heights = WORLDSLICE.heightmaps["MOTION_BLOCKING_NO_LEAVES"]

        buildPerimeter(heights)

        # calculate the center x & z coordinates of the build area
        middle_x = round((STARTX + ENDX) / 2)
        middle_z = round((STARTZ + ENDZ) / 2)

        # get the height of the ground in the middle of the build area
        floor_level = heights[(ENDX - middle_x, ENDZ - middle_z)]

        # build a house in the center of the build area
        houseGenerator.build_house(middle_x - 10, floor_level, middle_z - 10, 
                                    middle_x + 9, floor_level + 6, middle_z + 9)

        print("Done!")
        
    except KeyboardInterrupt:
        print("Pressed Ctrl-C to kill program.")
