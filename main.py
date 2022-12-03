import pygame

pygame.init()
screen = pygame.display.set_mode((2240, 1280))

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
LevelDirectionPNG = pygame.image.load('GUIPngs/leveldirectiondisplay.png')
xPNG = pygame.image.load('GUIPngs/xdisplay.png')
yPNG = pygame.image.load('GUIPngs/ydisplay.png')
zPNG = pygame.image.load('GUIPngs/zdisplay.png')
texturesPNG = pygame.image.load('GUIPngs/texturesdisplay.png')
startPNG = pygame.image.load('GUIPngs/startdisplay.png')

myVars = vars()
font = pygame.font.Font('freesansbold.ttf', 96)
currentlevelint = 1

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
    allbuttons = []

    def __init__(self, cor1x, cor1y, cor2x, cor2y, typafunc, funcvalue):
        self.allbuttons.append(self)
        self.cor1x = cor1x
        self.cor1y = cor1y
        self.cor2x = cor2x
        self.cor2y = cor2y
        self.typefunction = typafunc
        self.functionvalue = funcvalue

    def click(self):
        if self.cor1x < mousex < self.cor2x:
            if self.cor1y < mousey < self.cor2y:
                return True


def loadupdateoptions():
    screen.blit(LevelDirectionPNG, (0, 0))
    screen.blit(font.render(f'{currentlevelint}', True, (255, 255, 255)), (290, 50))
    screen.blit(xPNG, (0, 490))
    screen.blit(yPNG, (0, 760))
    screen.blit(zPNG, (0, 1030))
    screen.blit(texturesPNG, (1760, 0))
    screen.blit(startPNG, (1760, 640))
    for row in currentlevel:
        for texture in row:
            screen.blit(texture.texture, (texture.x, texture.y))


def checkbuttonclicks():
    for button in Button.allbuttons:
        if button.click():
            print("Something clicked!")
            button.typefunction(button.functionvalue)
            break


def levelchange(butval):
    global currentlevelint
    global currentlevel
    if 8 != currentlevelint and butval == 1 or 1 != currentlevelint and butval == -1:
        currentlevelint += butval
        print(f'Level{currentlevelint}MATRIX')
        currentlevel = eval(f'Level{currentlevelint - 1}MATRIX')


def directionchange(butval):
    pass


def sizelimiter(butval):
    pass


def texturechange(butval):
    global textureselected
    textureselected = butval


def versionchange(butval):
    pass


def start():
    pass


currentlevel = Level1MATRIX
textureselected = EmptyPNG

xdiffercoordset = [480, 640, 800, 960, 1120, 1280, 1440, 1600]

ydiffercoordset = [0, 160, 320, 480, 640, 800, 960, 1120]

mousex = 0
mousey = 0

LevelUP = Button(359, 23, 440, 70, levelchange, 1)
LevelDOWN = Button(359, 99, 440, 151, levelchange, -1)

North = Button(238, 210, 310, 282, directionchange, 0)
West = Button(48, 289, 167, 393, directionchange, 1)
South = Button(238, 390, 310, 482, directionchange, 2)
East = Button(378, 291, 429, 390, directionchange, 3)

Xlimit1 = Button(60, 630, 190, 730, sizelimiter, "textentry")
Xlimit2 = Button(290, 630, 420, 730, sizelimiter, "textentry")
Ylimit1 = Button(60, 890, 190, 990, sizelimiter, "textentry")
Ylimit2 = Button(290, 890, 420, 990, sizelimiter, "textentry")
Zlimit1 = Button(60, 1150, 190, 1250, sizelimiter, "textentry")
Zlimit2 = Button(290, 1150, 420, 1250, sizelimiter, "textentry")

Redsand = Button(1850, 90, 1930, 170, texturechange, RedsandPNG)
Sand = Button(1960, 90, 2040, 170, texturechange, SandPNG)
Stone = Button(2070, 90, 2150, 170, texturechange, StonePNG)
Podzol = Button(1850, 200, 1930, 280, texturechange, PodzolPNG)
Mycelium = Button(2070, 200, 2150, 280, texturechange, MyceliumPNG)
Netherrack = Button(1850, 310, 1930, 390, texturechange, NetherrackPNG)
Dirt = Button(1960, 310, 2040, 390, texturechange, DirtPNG)
Grass = Button(2070, 310, 2150, 390, texturechange, GrassPNG)

Version1_12 = Button(1790, 710, 1910, 810, versionchange, "1.12")
Version1_16 = Button(2100, 710, 2220, 810, versionchange, "1.16")

Go = Button(1780, 1090, 2220, 1260, start, True)

running = True

# Fills matrices with values
for level in range(8):
    for row in range(8):
        for value in range(8):
            texturename = 'Texture_' + f'{level}' + '_' + f'{row}' + '_' + f'{value}'
            myVars[texturename] = Block(xdiffercoordset[row], ydiffercoordset[value])
            eval(f"Level{level}MATRIX")[row][value] = myVars[texturename]


print(Level1MATRIX)
print(Level2MATRIX)
textureselected = DirtPNG

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseposition = pygame.mouse.get_pos()
            mousex, mousey = mouseposition[0], mouseposition[1]
            print(f'x = {mousex}, y = {mousey}')
            checkbuttonclicks()
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
    loadupdateoptions()
    pygame.display.update()
    fpsClock.tick(FPS)
