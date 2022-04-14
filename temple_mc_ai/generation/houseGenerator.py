from __future__ import print_function
from tracemalloc import start
from gdpc import interface as INTF
import random


def build_house(start_x, start_y, start_z, end_x, end_y, end_z):
    """
    Builds a simple house with corners corresponding to the start and end coordinates provided
    """

    print("Building house...")

    pillar_material_id = "oak_wood"
    floor_material_id = "oak_planks"
    wall_material_id = "cobblestone"
    window_material_id = "glass"
    roof_material_id = "oak_planks"
    air_id = "air"
    door_bottom_id = "spruce_door[facing=south, half=lower]"
    door_top_id = "spruce_door[facing=south, half=upper]"

    roof_height = 5

    # place the floor
    for i in range(start_x, end_x + 1):
        for j in range(start_z, end_z + 1):
            INTF.placeBlock(i, start_y, j, floor_material_id)

    # place pillars in the corners
    for i in range(start_y, end_y):
        INTF.placeBlock(start_x, i, start_z, pillar_material_id)
        INTF.placeBlock(end_x, i, start_z, pillar_material_id)
        INTF.placeBlock(start_x, i, end_z, pillar_material_id)
        INTF.placeBlock(end_x, i, end_z, pillar_material_id)

    # fill in the walls, adding windows at certain spots
    for i in range(start_y + 1, end_y):

        # place the walls along each x coordinate
        for j in range(start_x + 1, end_x):
            block_id = wall_material_id
            if i == start_y + 2 and j > start_x + 1 and j < end_x - 1:
                block_id = window_material_id
            INTF.placeBlock(j, i, start_z, block_id)
            INTF.placeBlock(j, i, end_z, block_id)

        # place the walls along each z coordinate
        for j in range(start_z + 1, end_z):
            block_id = wall_material_id
            if i == start_y + 2 and j > start_z + 1 and j < end_z - 1:
                block_id = window_material_id
            INTF.placeBlock(start_x, i, j, block_id)
            INTF.placeBlock(end_x, i, j, block_id)


    # build the roof
    for i in range(end_y, end_y + roof_height):

        # at the top level, build across all x and z values to fill in the roof
        if i == (end_y + roof_height) - 1:
            for j in range(start_x + (i - end_y), end_x + 1 - (i - end_y)):
                for k in range(start_z + (i - end_y), end_z + 1 - (i - end_y)):
                    INTF.placeBlock(j, i, k, roof_material_id)
        # at all other levels, only build the border to allow for a curved roof on the inside
        else:
            for j in range(start_x + (i - end_y), end_x + 1 - (i - end_y)):
                INTF.placeBlock(j, i, start_z + (i - end_y), roof_material_id)
                INTF.placeBlock(j, i, end_z - (i - end_y), roof_material_id)

            for j in range(start_z + (i - end_y), end_z + 1 - (i - end_y)):
                INTF.placeBlock(start_x + (i - end_y), i, j, roof_material_id)
                INTF.placeBlock(end_x - (i - end_y), i, j, roof_material_id)

    # place a door
    INTF.placeBlock(round((end_x - start_x) / 2) + start_x, start_y + 1, start_z, door_bottom_id)
    INTF.placeBlock(round((end_x - start_x) / 2) + start_x, start_y + 2, start_z, door_top_id)

    INTF.placeBlock(round((end_x - start_x) / 2) + start_x - 1, start_y + 1, start_z, wall_material_id)
    INTF.placeBlock(round((end_x - start_x) / 2) + start_x - 1, start_y + 2, start_z, wall_material_id)

    INTF.placeBlock(round((end_x - start_x) / 2) + start_x + 1, start_y + 1, start_z, wall_material_id)
    INTF.placeBlock(round((end_x - start_x) / 2) + start_x + 1, start_y + 2, start_z, wall_material_id)


def build_settlement(coord_array):
    '''
    Pass this function the flat_finder function and it will build multiple houses
    '''

    for i in range(6):
        startx = coord_array[i][0] +  random.randint(-2, 2)
        startz = coord_array[i][1] +  random.randint(-2, 2)
        endx = coord_array[i][2] +  random.randint(-2, 2)
        endz = coord_array[i][3] +  random.randint(-2, 2)
        starty = coord_array[i][5]
        endy = starty + random.randint(5, 8)

        build_house(startx + 5, starty, startz + 5, endx - 5, endy, endz - 5)