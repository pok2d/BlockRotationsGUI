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
curtextPNG = pygame.image.load('GUIPngs/currenttexturedisplay.png')
curversionPNG = pygame.image.load('GUIPngs/curversiondisplay.png')
curdirectionPNG = pygame.image.load('GUIPngs/currentdirectiondisplay.png')

myVars = vars()
bigfont = pygame.font.Font('freesansbold.ttf', 96)
mediumfont = pygame.font.Font('freesansbold.ttf', 64)
smallfont = pygame.font.Font('freesansbold.ttf', 32)
currentlevelint = 1

for intforlevel in range(8):
    myVars[f"Level{intforlevel}MATRIX"] = [[0 for _ in range(8)] for _ in range(8)]

texturearray = [[RedsandPNG, SandPNG, StonePNG],
                [PodzolPNG, False, MyceliumPNG],
                [NetherrackPNG, DirtPNG, GrassPNG]]

directionarray = [[False, False, False, False],
                  [221, 371, 221, 41],
                  [251, 361, 471, 351]]


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
    screen.blit(bigfont.render(f'{currentlevelint}', True, (255, 255, 255)), (290, 50))
    for i in range(4):
        if directionarray[0][i]:
            screen.blit(curdirectionPNG, (directionarray[1][i], directionarray[2][i]))
    screen.blit(xPNG, (0, 490))
    screen.blit(yPNG, (0, 760))
    screen.blit(zPNG, (0, 1030))
    screen.blit(smallfont.render(f'{databuttons[0]}', True, (255, 255, 255)), (databuttonscalcx[0], 650))
    screen.blit(smallfont.render(f'{databuttons[1]}', True, (255, 255, 255)), (databuttonscalcx[1], 650))
    screen.blit(smallfont.render(f'{databuttons[2]}', True, (255, 255, 255)), (databuttonscalcx[2], 920))
    screen.blit(smallfont.render(f'{databuttons[3]}', True, (255, 255, 255)), (databuttonscalcx[3], 920))
    screen.blit(smallfont.render(f'{databuttons[4]}', True, (255, 255, 255)), (databuttonscalcx[4], 1190))
    screen.blit(smallfont.render(f'{databuttons[5]}', True, (255, 255, 255)), (databuttonscalcx[5], 1190))
    screen.blit(texturesPNG, (1760, 0))
    screen.blit(curtextPNG, (highlighttexturex, highlighttexturey))
    screen.blit(startPNG, (1760, 640))
    screen.blit(curversionPNG, (curversionx, 821))
    screen.blit(mediumfont.render('N/A', True, (255, 255, 255)), (2093, 880))
    screen.blit(mediumfont.render(f'{estimatedsolutions}', True, (255, 255, 255)), (essolutionsx, 1000))
    for rowline in currentlevel:
        for texture in rowline:
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
    global directionarray
    if directionarray[0][butval]:
        directionarray[0][butval] = False
    else:
        directionarray[0][butval] = True


def sizelimiter(butval):
    global enteringdata
    global curdatabutton
    enteringdata = True
    curdatabutton = butval


def texturechange(butval):
    global textureselected
    global highlighttexturex
    global highlighttexturey

    textureselected = butval
    for rowline in texturearray:
        for element in rowline:
            if element == textureselected:
                print(f'{texturearray.index(rowline)}, {rowline.index(element)}')
                highlighttexturex = rowline.index(element) * 110 + 1840
                highlighttexturey = texturearray.index(rowline) * 110 + 80


def versionchange(butval):
    global curversionx
    curversionx = 1760 + butval


def start():
    pass


def estsolutions():
    global numofdecidedtiles
    global estimatedsolutions
    for matrix in range(8):
        for rowtile in eval(f'Level{matrix}MATRIX'):
            for texture in rowtile:
                if texture.texture != EmptyPNG:
                    numofdecidedtiles += 1
    try:
        estimatedsolutions = abs(
            (int(databuttons[0]) - int(databuttons[1]) + 1) * (int(databuttons[2]) - int(databuttons[3]) + 1) * (
                    int(databuttons[4]) - int(databuttons[5]) + 1)) / 4 ** numofdecidedtiles

    except:
        estimatedsolutions = "N/A"

    numofdecidedtiles = 0


numofdecidedtiles = 0

estimatedsolutions = 0
essolutionsx = 2100

curdatabutton = 0

databuttons = ['', '', '', '', '', '']
databuttonscalcx = [115, 345, 115, 345, 115, 345]

curversionx = 1781

highlighttexturex = 1950
highlighttexturey = 300

currentlevel = eval('Level0MATRIX')
textureselected = EmptyPNG

xdiffercoordset = [480, 640, 800, 960, 1120, 1280, 1440, 1600]

ydiffercoordset = [0, 160, 320, 480, 640, 800, 960, 1120]

mousex = 0
mousey = 0

recentkeyspressed = []
validkeys = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8,
             pygame.K_9, pygame.K_BACKSPACE, pygame.K_MINUS]

LevelUP = Button(359, 23, 440, 70, levelchange, 1)
LevelDOWN = Button(359, 99, 440, 151, levelchange, -1)

North = Button(230, 180, 300, 250, directionchange, 0)
East = Button(390, 260, 440, 360, directionchange, 1)
South = Button(230, 380, 300, 470, directionchange, 2)
West = Button(40, 270, 130, 350, directionchange, 3)

Xlimit1 = Button(60, 630, 190, 730, sizelimiter, 0)
Xlimit2 = Button(290, 630, 420, 730, sizelimiter, 1)
Ylimit1 = Button(60, 890, 190, 990, sizelimiter, 2)
Ylimit2 = Button(290, 890, 420, 990, sizelimiter, 3)
Zlimit1 = Button(60, 1150, 190, 1250, sizelimiter, 4)
Zlimit2 = Button(290, 1150, 420, 1250, sizelimiter, 5)

Redsand = Button(1850, 90, 1930, 170, texturechange, RedsandPNG)
Sand = Button(1960, 90, 2040, 170, texturechange, SandPNG)
Stone = Button(2070, 90, 2150, 170, texturechange, StonePNG)
Podzol = Button(1850, 200, 1930, 280, texturechange, PodzolPNG)
Mycelium = Button(2070, 200, 2150, 280, texturechange, MyceliumPNG)
Netherrack = Button(1850, 310, 1930, 390, texturechange, NetherrackPNG)
Dirt = Button(1960, 310, 2040, 390, texturechange, DirtPNG)
Grass = Button(2070, 310, 2150, 390, texturechange, GrassPNG)

Version1_12 = Button(1790, 710, 1910, 810, versionchange, 21)
Version1_16 = Button(2100, 710, 2220, 810, versionchange, 331)

Go = Button(1780, 1090, 2220, 1260, start, True)

running = True
enteringdata = False

# Fills matrices with values
for level in range(8):
    for row in range(8):
        for value in range(8):
            texturename = 'Texture_' + f'{level}' + '_' + f'{row}' + '_' + f'{value}'
            myVars[texturename] = Block(xdiffercoordset[row], ydiffercoordset[value])
            eval(f"Level{level}MATRIX")[row][value] = myVars[texturename]

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
    if enteringdata:
        activekeys = pygame.key.get_pressed()
        for key in validkeys:
            if activekeys[key]:
                if validkeys.index(key) not in recentkeyspressed:
                    recentkeyspressed.append(validkeys.index(key))
                    if key == pygame.K_BACKSPACE:
                        if len(f'{databuttons[curdatabutton]}') == 1:
                            databuttons[curdatabutton] = ''
                        else:
                            databuttons[curdatabutton] = (f'{databuttons[curdatabutton]}'[:-1])
                    elif key == pygame.K_MINUS:
                        databuttons[curdatabutton] = (f'{databuttons[curdatabutton]}' + f'-')
                    else:
                        databuttons[curdatabutton] = (f'{databuttons[curdatabutton]}' + f'{validkeys.index(key)}')
                    if curdatabutton % 2 == 0:
                        databuttonscalcx[curdatabutton] = 125 - len(f'{databuttons[curdatabutton]}') * 10
                    else:
                        databuttonscalcx[curdatabutton] = 355 - len(f'{databuttons[curdatabutton]}') * 10
        for key in recentkeyspressed:
            if not activekeys[validkeys[key]]:
                recentkeyspressed.remove(key)
    estsolutions()
    loadupdateoptions()
    pygame.display.update()
    fpsClock.tick(FPS)
