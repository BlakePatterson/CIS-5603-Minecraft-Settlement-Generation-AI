import statistics as stat

    
def find_flat(heights, buildArea):
    '''
    Divides main build area into 16 subgrids. Calculates the height standard deviation of all cells in each subgrid
    
    Optimally, build area should be divisible by 4
    
    Returns
    -------
    ordered arrays of 16 subgrids, from flattest to least flat, stored in array [[startx, startz, endx, endz, height_std_dev, floor level], ...]

    '''
    # this line will be rewritten as the subgrid coords
    startx, starty, startz, endx, endy, endz = buildArea
    
    # this line is used as the original build area coords
    startx_area, starty_area, startz_area, endx_area, endy_area, endz_area = buildArea
    
    subgrids = [] #[startx, startz, endx, endz]

    width = (endx - startx + 1)
    subgrid_length = width / 4
    
    # create 16 subgrids of original build area
    # write x, endx, z, endz coord of each subgrid to an array
    for i in range(4):
        endz = startz + subgrid_length                       
        endx = startx + subgrid_length
        subgrids.append([int(startx), int(startz), int(endx), int(endz)])
        for j in range(3):
            subgrids.append([int(startx), int(endz), int(endx), int(endz + subgrid_length)])
            endz += subgrid_length
        startx = endx
    
    # calculate height std dev for each subgrid
    for m in range(0, len(subgrids)):
        startx = int(subgrids[m][0])
        endx = int(subgrids[m][2])
        startz = int(subgrids[m][1])
        endz = int(subgrids[m][3])
        all_heights = []
        for z in range(startz, endz):
            for x in range(startx, endx):
                all_heights.append(heights[(x - startx_area, z - startz_area)])
        subgrids[m].append(stat.pstdev(all_heights))

    # calculate middle height of each subgrid
    for m in range(0, len(subgrids)):
        startx = int(subgrids[m][0])
        endx = int(subgrids[m][2])
        startz = int(subgrids[m][1])
        endz = int(subgrids[m][3])
        middlex = round((startx + endx) / 2)
        middlez = round((startz + endz) / 2)
        floor_level = heights[(middlex - startx_area, middlez - startz_area)]
        print(floor_level)
        subgrids[m].append(floor_level)

    # order subgrids by descending flatness
    subgrid_sort = sorted(subgrids, key=lambda x: x[4])
    return subgrid_sort
