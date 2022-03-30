import argparse
from gdpc import interface as INTF

def giveArgs():
    parser = argparse.ArgumentParser(description="AI Minecraft Settlement, by Blake Patterson & Michael Ward")
    group = parser.add_mutually_exclusive_group(required=False)

    group.add_argument("-p", "--player",
                        help="Use player's current location as build area",
                    action="store_true")
    
    group.add_argument("-c", "--coordinates", nargs = 6, type=int,
                    metavar=('x0', 'y0', 'z0', 'x1', 'y1', 'z1'),
                    help="Define coordinates for build area")
    
    group.add_argument("-d", "--default",
                        help="Build using default area",
                    action="store_true")
    
    parser.add_argument("-t", "--terraform",
                        help="Clear trees and grass",
                    action="store_true")
    
    parser.add_argument("-r", "--radius", type=int, metavar="R",
                        help="Use in conjunction with -p to override default radius of 128")
    
    args = parser.parse_args()
    return [args, parser]
    
def getBuildArea(args):
    size = 128
    
    if(args.radius):
        size = args.radius
    if (args.player):
        area = INTF.requestPlayerArea(size, size)
    elif (args.coordinates):
        x0, y0, z0, x1, y1, z1 = args.coordinates
        area = INTF.setBuildArea(x0, y0, z0, x1, y1, z1)
    elif(args.default):
        area = INTF.setBuildArea(0, 0, 0, size, 256, size)
    else :
        area = INTF.requestBuildArea()
        
    print("AREA :" + str(area))
    return area