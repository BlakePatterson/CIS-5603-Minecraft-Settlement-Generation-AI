from gdpc import interface as INTF
from gdpc import geometry as GEO

treeAndLeaves = [
    'minecraft:oak_log',
    'minecraft:oak_leaves',
    'minecraft:dark_oak_log',
    'minecraft:dark_oak_leaves',
    'minecraft:birch_log',
    'minecraft:birch_leaves',
    'minecraft:spruce_log',
    'minecraft:spruce_leaves',
    'minecraft:birch_log',
    'minecraft:birch_leaves',
    'minecraft:acacia_log',
    'minecraft:acacia_leaves',
    'minecraft:jungle_log',
    'minecraft:jungle_leaves',
    'minecraft:mushroom_stem',
    'minecraft:mushroom_block',
    'minecraft:brown_mushroom_block'
    ]

tree = [
    'minecraft:oak_log',
    'minecraft:dark_oak_log',
    'minecraft:birch_log',
    'minecraft:spruce_log',
    'minecraft:birch_log',
    'minecraft:acacia_log',
    'minecraft:jungle_log',
    'minecraft:mushroom_stem',
    'minecraft:mushroom_block',
    'minecraft:brown_mushroom_block'
    ]
      
        
def treeAnnihilator(heights, buildArea):
    print('Terraforming...')
    print(buildArea)
    start_x, start_y, start_z, end_x, end_y, end_z = buildArea
    
    tree_tops = []
    tree_bottoms = []
    
    # looks for wood in heightmap across build area and gets coordinates of tree tops
    for x in range(start_x, end_x):
        for z in range(start_z, end_z):
            y = heights[(x - start_x, z - start_z)] - 1
            block = INTF.getBlock(x, y, z)
            if block in tree:
                tree_tops.append([x,y,z])
    print(tree_tops)
    
    # check if block below is still tree, add coords to new array when bottom found
    for m in range(0, len(tree_tops)):
        x = 0
        while INTF.getBlock(tree_tops[m][0], tree_tops[m][1] + x, tree_tops[m][2]) in tree:
            x -= 1
        tree_bottoms.append([tree_tops[m][0], tree_tops[m][1] + x, tree_tops[m][2]])
    
    # put air in a 4x4 by height buffer around each tree
    for m in range(0, len(tree_tops)):
        buffer = 3
        # place the first layer with no buffer
        INTF.placeBlock(tree_bottoms[m][0], tree_bottoms[m][1], tree_bottoms[m][2], "grass_block")
        # place first buffer starting at y + 1
        GEO.placeCuboid(tree_tops[m][0] - buffer, tree_bottoms[m][1] + 1, tree_tops[m][2] - buffer,
                        tree_tops[m][0] + buffer, tree_tops[m][1] + buffer, tree_tops[m][2] + buffer, "air")
        if tree_tops[m][1] > 5:
            buffer = 4
            # place second buffer at y + 3
            GEO.placeCuboid(tree_tops[m][0] - buffer, tree_bottoms[m][1] + 3, tree_tops[m][2] - buffer,
                        tree_tops[m][0] + buffer, tree_tops[m][1] + buffer, tree_tops[m][2] + buffer, "air")
            
        

        
        
                
        
    
