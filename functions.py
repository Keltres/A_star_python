"""functions for a* search"""
# from tiles import Tile

# def get_empty_grid(height, width, block_size):
#     """returns an array of tiles"""
#     blocks = []
#     for i in range(height//(block_size+2)):
#         row = []
#         for j in range(width//(block_size+2)):
#             block = Tile((i*(block_size+2)+1,j*(block_size+2)+1), (block_size, block_size))
#             row.append(block)
#         blocks.append(row)
#     return blocks

# def update_grid_list(grid):
#     """returns sorted grid"""
#     new_grid = []
#     flat_grid = []
#     for row in grid:
#         for element in row:
#             flat_grid.append(element)

#     flat_grid.sort(key=lambda element: element.y)
#     for j in range(len(grid)):
#         row = []
#         for i in range(len(grid[0])):
#             row.append(flat_grid.pop(0))
#         row.sort(key=lambda element:element.x)
#         new_grid.append(row)
#     return new_grid

def reset_falgs(flags):
    for key in flags:
        flags[key] = None

def set_drag_start_tile(grid, flags, mouse_pos):
    for row in grid:
        for element in row:
            if element.collidepoint(mouse_pos):
                flags["drag_start_tile_state"] = element.state
                flags["drag_start_tile"] = element

def update_labels(element, flags):

    # case1: starting at normal, drawing through wall
    if flags["drag_start_tile_state"] == "normal" and element.state != "start" and element.state != "finish":
        element.makeWall()

    # case2: starting at wall, drawing through normal (erasing)
    elif flags["drag_start_tile_state"] == "wall" and element.state != "start" and element.state != "finish":
        element.makeNormal()

    # case3: moving the start and finish tiles
    elif flags["drag_start_tile_state"] == "start" or flags["drag_start_tile_state"] == "finish":
        if element.state == "normal":
            flags["drag_start_tile"].swtichTile(element)

def start_algorithm(grid):
    open_list = []
    closed_list = []
    for row in grid:
        for element in row:
            pass