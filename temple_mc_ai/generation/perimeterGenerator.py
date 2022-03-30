from random import randint

from gdpc import geometry as GEO
from gdpc import interface as INTF
from gdpc import toolbox as TB
from gdpc import worldLoader as WL


def buildPerimeter(heights, buildArea):
    """Build a wall along the build area border.
    """

    print("Building walls...")
    
    STARTX, STARTY, STARTZ, ENDX, ENDY, ENDZ = buildArea

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