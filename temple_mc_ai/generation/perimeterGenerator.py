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

    fence_material = 'spruce_fence[east=false,north=false,west=false,south=false]'

    for x in range(STARTX, ENDX + 1):
        z = STARTZ
        y = heights[(x - STARTX, z - STARTZ)]
        INTF.placeBlock(x, y - 1, z, "cobblestone")
        GEO.placeCuboid(x, y, z, x, y + 4, z, fence_material)
    for z in range(STARTZ, ENDZ):
        x = STARTX
        y = heights[(x - STARTX, z - STARTZ)]
        INTF.placeBlock(x, y - 1, z, "cobblestone")
        GEO.placeCuboid(x, y, z, x, y + 4, z, fence_material)
    for x in range(STARTX, ENDX + 1):
        z = ENDZ
        y = heights[(x - STARTX, z - STARTZ)]
        INTF.placeBlock(x, y - 1, z, "cobblestone")
        GEO.placeCuboid(x, y, z, x, y + 4, z, fence_material)
    for z in range(STARTZ, ENDZ):
        x = ENDX
        y = heights[(x - STARTX, z - STARTZ)]
        INTF.placeBlock(x, y - 1, z, "cobblestone")
        GEO.placeCuboid(x, y, z, x, y + 4, z, fence_material)

    