"""Tile class"""
import pygame.rect

class Tile(pygame.Rect):
    """clickable tiles"""

    TILE_COLOUR = (80, 80, 80)
    WALL_COLOUR = (0, 0, 127)
    START_COLOUR = (0, 127, 0)
    FINISH_COLOUR = (127, 0, 0)

    def __init__(self, lt, wh):
        """init"""
        super().__init__(lt, wh)
        self.state = "normal"
        self._h = 0
        self._g = 0
        self._f = 0

    def __repr__(self):
        #return "(" + str(self.x) + ", "+ str(self.y) +")"
        return self.state[0] + "(" + str(self.x) + ", "+ str(self.y) +")"

    def makeWall(self):
        self.state = "wall"

    def makeNormal(self):
        self.state = "normal"

    def makeStart(self):
        self.state = 'start'
        return self

    def makeFinish(self):
        self.state = "finish"
        return self

    def makePath(self):
        self.state = "path"

    def switchstate(self):
        """Switches between Normal and Wall"""
        if self.state == "normal":
            self.state = "wall"
        elif self.state == "wall":
            self.state = "normal"

    def swtichTile(self, switchee):
        self.top, switchee.top = switchee.top, self.top
        self.left, switchee.left =  switchee.left, self.left

    def updateColour(self, screen):
        if self.state == "normal":
            pygame.draw.rect(screen, Tile.TILE_COLOUR, self)
        elif self.state == "wall":
            pygame.draw.rect(screen, Tile.WALL_COLOUR, self)
        elif self.state == "start":
            pygame.draw.rect(screen, Tile.START_COLOUR, self)
        elif self.state == "finish":
            pygame.draw.rect(screen, Tile.FINISH_COLOUR, self)
