import pygame

pygame.init()
screen = pygame.display.set_mode((1680, 1280))

pygame.display.set_caption("Block Rotation Sexploit 3000!!!!!")
FPS = 60
fpsClock = pygame.time.Clock()

DirtPNG = pygame.image.load('BlockTopPngs/DirtTop.png')
GrassPNG = pygame.image.load('BlockTopPngs/GrassTop.png')
MyceliumPNG = pygame.image.load('BlockTopPngs/MyceliumTop.png')
NetherrackPNG = pygame.image.load('BlockTopPngs/NetherrackTop.png')
PodzolPNG = pygame.image.load('BlockTopPngs/PodzolTop.png')
RedsandPNG = pygame.image.load('BlockTopPngs/RedsandTop.png')
SandPNG = pygame.image.load('BlockTopPngs/SandTop.png')
StonePNG = pygame.image.load('BlockTopPngs/StoneTop.png')
EmptyPNG = pygame.image.load('BlockTopPngs/EmptyTile.png')

myVars = vars()
font = pygame.font.Font('freesansbold.ttf', 32)

for intforlevel in range(8):
    myVars[f"Level{intforlevel}MATRIX"] = [[0 for _ in range(8)] for _ in range(8)]


class Block:
    def __init__(self, x, y):
        self.texture = textureselected
        self.rotation = 0
        self.x = x
        self.y = y

    def rotate(self):
        self.texture = pygame.transform.rotate(self.texture, -90)

        if self.rotation == 3:
            self.rotation = 0
        else:
            self.rotation += 1
        print(self.rotation)

    def clear(self):
        self.rotation = 0
        self.texture = EmptyPNG


class Button:
    def __init__(self, cor1x, cor1y, cor2x, cor2y):
        self.cor1x = cor1x
        self.cor1y = cor1y
        self.cor2x = cor2x
        self.cor2y = cor2y
        self.triggervalue = False

    def checkclick(self, mousex, mousey):
        if self.cor1x < mousex < self.cor2x:
            if self.cor1y < mousey < self.cor2y:
                self.triggervalue = True


def loadoptions():
    screen.blit(font.render('Level ' + f'{currentlevelint}', True, (255, 255, 255)), (100, 100))

currentlevel = Level1MATRIX
currentlevelint = 1
textureselected = EmptyPNG

xdiffercoordset = [400, 560, 720, 880, 1040, 1200, 1360, 1520]

ydiffercoordset = [0, 160, 320, 480, 640, 800, 960, 1120]

running = True

# Fills matrices with values
for level in range(8):
    for row in range(8):
        for value in range(8):
            texturename = 'Texture_' + f'{level}' + '_' + f'{row}' + '_' + f'{value}'
            myVars[texturename] = Block(xdiffercoordset[row], ydiffercoordset[value])
            currentlevel[row][value] = myVars[texturename]

textureselected = DirtPNG

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseposition = pygame.mouse.get_pos()
            # print(mouseposition[0])
            # print(mouseposition[1])
            print('click')
            for xtocompare in xdiffercoordset:
                if xtocompare < mouseposition[0] < xtocompare + 160:
                    for ytocompare in ydiffercoordset:
                        if ytocompare < mouseposition[1] < ytocompare + 160:
                            curimgtile = currentlevel[xdiffercoordset.index(xtocompare)][
                                ydiffercoordset.index(ytocompare)]
                            if event.button == 1:
                                if curimgtile.texture == EmptyPNG:
                                    curimgtile.texture = textureselected
                                else:
                                    curimgtile.rotate()
                            if event.button == 3:
                                curimgtile.clear()

    # Keys pressed list
    # keys = pygame.key.get_pressed()

    for row in currentlevel:
        for texture in row:
            screen.blit(texture.texture, (texture.x, texture.y))
    loadoptions()
    # Updates displayer and makes sure FPS is stable.
    pygame.display.update()
    fpsClock.tick(FPS)
