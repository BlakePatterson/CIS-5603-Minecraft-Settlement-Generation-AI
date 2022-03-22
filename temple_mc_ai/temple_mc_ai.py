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


args, parser = argParser.giveArgs()
buildArea = argParser.getBuildArea(args)

if buildArea == -1:
    exit()
    

STARTX, STARTY, STARTZ, ENDX, ENDY, ENDZ = buildArea

WORLDSLICE = WL.WorldSlice(STARTX, STARTZ,
                          ENDX + 1, ENDZ + 1)


def buildPerimeter():
    """Build a wall along the build area border.

    In this function we're building a simple wall around the build area
        pillar-by-pillar, which means we can adjust to the terrain height
    """

    heights = WORLDSLICE.heightmaps["MOTION_BLOCKING_NO_LEAVES"]
    print("Building east-west walls...")

    for x in range(STARTX, ENDX + 1):
        # the northern wall
        y = heights[(x, STARTZ)]
        GEO.placeCuboid(x, y - 2, STARTZ, x, y, STARTZ, "granite")
        GEO.placeCuboid(x, y + 1, STARTZ, x, y + 4, STARTZ, "granite_wall")
        # the southern wall
        y = heights[(x, ENDZ)]
        GEO.placeCuboid(x, y - 2, ENDZ, x, y, ENDZ, "red_sandstone")
        GEO.placeCuboid(x, y + 1, ENDZ, x, y + 4, ENDZ, "red_sandstone_wall")

    print("Building north-south walls...")

    for z in range(STARTZ, ENDZ + 1):
        # the western wall
        y = heights[(STARTX, z)]
        GEO.placeCuboid(STARTX, y - 2, z, STARTX, y, z, "sandstone")
        GEO.placeCuboid(STARTX, y + 1, z, STARTX, y + 4, z, "sandstone_wall")
        # the eastern wall
        y = heights[(ENDX, z)]
        GEO.placeCuboid(ENDX, y - 2, z, ENDX, y, z, "prismarine")
        GEO.placeCuboid(ENDX, y + 1, z, ENDX, y + 4, z, "prismarine_wall")


if __name__ == '__main__':

    try:
        height = WORLDSLICE.heightmaps["MOTION_BLOCKING"][(STARTX, STARTY)]
        buildPerimeter()

        print("Done!")
    except KeyboardInterrupt:
        print("Pressed Ctrl-C to kill program.")
