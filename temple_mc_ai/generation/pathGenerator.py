from __future__ import print_function
from time import sleep
from tracemalloc import start
from xml.sax.handler import property_interning_dict
from gdpc import interface as INTF


class State:
    """
    Helper class for representing states in A*
    """
    x = None
    z = None
    previous = None

    def __init__(self, x=-1, z=-1, previous=None):
        self.x = x
        self.z = z
        if previous is not None:
            self.previous = previous

    def to_string(self):
        return '(' + str(self.x) + ', ' + str(self.z) + ')'

    def equals(self, state):
        return self.x == state.x and self.z == state.z


def f(current_state, m, n):
    """
    Evaluation function for use with A*
    """
    return cost(current_state) + h(State(m, n), current_state)


def cost(current_state):
    """
    Helper function which calculates the cost to a certain state (i.e., how many steps it took to get there)
    """
    cost_val = 0
    state = current_state
    while state is not None:
        state = state.previous
        cost_val += 1
    return cost_val


def h(goal_state, current_state):
    """
    Hueristic function for use with A*
    """
    return abs(goal_state.x - current_state.x) + abs(goal_state.z - current_state.z)


def has_reached_goal(current_state, goal_state):
    """
    Helper function to determine whether or not the goal has been reached
    """
    return current_state.equals(goal_state)


def get_height_difference(state1, state2, heights, height_end_x, height_end_z):
    """
    Helper function which returns the height difference between two points
    """
    return abs(heights[(height_end_x - state1.x, height_end_z - state1.z)] - heights[(height_end_x - state2.x, height_end_z - state2.z)])


def build_path(start_x, start_z, end_x, end_z, heights, height_end_x, height_end_z): 
    """
    Builds a simple path between the two specified points using A*
    """

    print("Building path...")

    print("Path starting at coordinates: (", start_x, ", ", start_z, ")")
    print("Path ending at coordinates: (", end_x, ", ", end_z, ")")

    path_material_id = "cobblestone"

    current_state = State(start_x, start_z)

    open_set = []
    open_set.append(State(current_state.x, current_state.z))

    closed_set = []
    
    goal_reached = False

    while len(open_set) > 0:

        best_move = 0

        # iterate through the open list to determine the best next move (i.e., move with the lowest f value)
        for i in range(1, len(open_set)):

            # if the current state has a smaller f-value, set it as the new best state
            if f(open_set[i], end_x, end_z) < f(open_set[best_move], end_x, end_z):
                best_move = i

            # if there is a tie
            elif f(open_set[i], end_x, end_z) == f(open_set[best_move], end_x, end_z):
                # the state with the smaller h-value wins
                if h(State(end_x, end_z), open_set[i]) <= h(State(end_x, end_z), open_set[best_move]):
                    best_move = i
            
        # use the newly determined best move to update the current state
        current_state = State(open_set[best_move].x, open_set[best_move].z, open_set[best_move].previous)

        # add the best move to the list of explored moves
        closed_set.append(State(current_state.x, current_state.z))

        # remove the best move (now current state) from the open list
        k = 0
        while k < len(open_set):
            if State(current_state.x, current_state.z).equals(open_set[k]):
                open_set.remove(open_set[k])
            else:
                k += 1

        # check to see if goal is reached
        if has_reached_goal(current_state, State(end_x, end_z)):
            print('Reached the goal, terminating A*')
            goal_reached = True
            break


        # examine moving left
        # check whether moving left is a valid move
        if current_state.z - 1 >= start_z:
            # check whether left has already been explored
            left_is_explored = False
            for i in range(len(closed_set)):
                if State(current_state.x, current_state.z - 1).equals(closed_set[i]):
                    left_is_explored = True
                    break

            # check whether left has an obstacle in the way or not
            left_is_obstacle = False
            # if moving left is a more than 4 difference in height, do not move left
            height_diff = get_height_difference(current_state, State(current_state.x, current_state.z - 1), heights, height_end_x, height_end_z)
            if height_diff >= 5:
                left_is_obstacle = True

            # moving left has not been explored yet & is not an obstacle, so add it to the open set
            if left_is_explored is False and left_is_obstacle is False:
                open_set.append(State(current_state.x, current_state.z - 1, current_state))


        # examine moving right
        # check whether moving right is a valid move
        if current_state.z + 1 <= end_z:
            # check whether right has already been explored
            right_is_explored = False
            for i in range(len(closed_set)):
                if State(current_state.x, current_state.z + 1).equals(closed_set[i]):
                    right_is_explored = True
                    break

            # check whether right has an obstacle in the way or not
            right_is_obstacle = False
            # if moving right is a more than 4 difference in height, do not move right
            height_diff = get_height_difference(current_state, State(current_state.x, current_state.z + 1), heights, height_end_x, height_end_z)
            if height_diff >= 5:
                right_is_obstacle = True

            # moving right has not been explored yet & is not an obstacle, so add it to the open set
            if right_is_explored is False and right_is_obstacle is False:
                open_set.append(State(current_state.x, current_state.z + 1, current_state))


        # examine moving up
        # check whether moving up is a valid move
        if current_state.x - 1 >= start_x:
            # check whether up has already been explored
            up_is_explored = False
            for i in range(len(closed_set)):
                if State(current_state.x - 1, current_state.z).equals(closed_set[i]):
                    up_is_explored = True
                    break

            # check whether up has an obstacle in the way or not
            up_is_obstacle = False
            # if moving up is a more than 4 difference in height, do not move up
            height_diff = get_height_difference(current_state, State(current_state.x - 1, current_state.z), heights, height_end_x, height_end_z)
            if height_diff >= 5:
                up_is_obstacle = True

            # moving up has not been explored yet & is not an obstacle, so add it to the open set
            if up_is_explored is False and up_is_obstacle is False:
                open_set.append(State(current_state.x - 1, current_state.z, current_state))


        # examine moving down
        # check whether moving down is a valid move
        if current_state.x + 1 <= end_x:
            # check whether down has already been explored
            down_is_explored = False
            for i in range(len(closed_set)):
                if State(current_state.x + 1, current_state.z).equals(closed_set[i]):
                    down_is_explored = True
                    break

            # check whether down has an obstacle in the way or not
            down_is_obstacle = False
            # if moving down is a more than 4 difference in height, do not move down
            height_diff = get_height_difference(current_state, State(current_state.x + 1, current_state.z), heights, height_end_x, height_end_z)
            if height_diff >= 5:
                down_is_obstacle = True

            # moving down has not been explored yet & is not an obstacle, so add it to the open set
            if down_is_explored is False and down_is_obstacle is False:
                open_set.append(State(current_state.x + 1, current_state.z, current_state))

    # generate an array containing a list of states representing the found path
    path = []
    current_state_copy = current_state
    while current_state_copy is not None:
        path.append(current_state_copy)
        current_state_copy = current_state_copy.previous
    
    # notify if there is no complete path
    if goal_reached is False:
        print('no solution, path not possible given current settings')
        # path.clear()
        # current_state = State(-1, -1)

    print("Starting path")
    for i in range(len(path)):
        print("(", path[i].x, ",", path[i].z, ")", end="; ")
        height = heights[(height_end_x - path[i].x, height_end_z - path[i].z)] - 1
        INTF.placeBlock(path[i].x, height, path[i].z, path_material_id)
    print()
    print("End of path")



