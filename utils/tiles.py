"""Tile class"""
import sys
import pygame.rect

class Tile(pygame.Rect):
    """clickable tiles"""

    TILE_COLOUR = (80, 80, 80)
    WALL_COLOUR = (0, 0, 127)
    START_COLOUR = (0, 127, 0)
    FINISH_COLOUR = (127, 0, 0)
    PATH_COLOUR = (127, 127, 0)
    SEARCH_COLOUR = (80, 80 ,255)

    def __init__(self, lt, wh, screen):
        """init"""
        super().__init__(lt, wh)
        self.screen = screen
        self.state = "normal"

    def __repr__(self):
        #return "(" + str(self.x) + ", "+ str(self.y) +")"
        return self.state[0] + "(" + str(self.x) + ", "+ str(self.y) +")"
        # return self.state[0]

    def __str__(self):
        return self.state[0] + "(" + str(self.x) + ", "+ str(self.y) +")"
        # return self.state[0]

    def makeWall(self):
        """changes the tiles state to wall"""
        self.state = "wall"
        pygame.draw.rect(self.screen, Tile.WALL_COLOUR, self)

    def makeNormal(self):
        """changes the tiles state to normal"""
        self.state = "normal"
        pygame.draw.rect(self.screen, Tile.TILE_COLOUR, self)

    def makeStart(self):
        """changes the tiles state to start"""
        self.state = 'start'
        pygame.draw.rect(self.screen, Tile.START_COLOUR, self)
        return self

    def makeFinish(self):
        """changes the tiles state to finish"""
        self.state = "finish"
        pygame.draw.rect(self.screen, Tile.FINISH_COLOUR, self)
        return self

    def makePath(self):
        """changes the tiles state to path"""
        self.state = "path"
        pygame.draw.rect(self.screen, Tile.PATH_COLOUR, self)

    def makeSearch(self):
        """changes the tiles state to path"""
        self.state = "search"
        pygame.draw.rect(self.screen, Tile.SEARCH_COLOUR, self)