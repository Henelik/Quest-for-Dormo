import pygame

level = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]]

class Level:
    def __init__(self, screenScale):
        self.tileset = level
        self.screenScale = screenScale
        self.xSize = len(self.tileset)
        self.ySize = len(self.tileset[0])

        self.instantiate()

    def instantiate(self):
        self.tiles = []
        for y in range(self.ySize):
            for x in range(self.xSize):
                if self.tileset[y][x] == 1:
                        self.tiles.append(Tile(x, y, self.screenScale))

    def update(self):
        pass

    def getSpawn(self): # Called by player class to get spawning location
        return(1, 1)

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, screenScale):
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([screenScale, screenScale])
        self.image.fill((100, 100, 100))

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

        self.update(x, y, screenScale)

    def update(self, x, y, screenScale):
        self.rect.x = x * screenScale
        self.rect.y = y * screenScale
