from separasilabas import *
import sys
import pygame

# Get data from command line:
# print ('Argument List:', str(sys.argv))
# palabra = str(sys.argv[1])

# Get data from file:
palabra="patos"
imgSrc="img.png"
try:
    file = open("input.txt", "r+")
    inputFile = file.readlines()
    file.close()
    palabra = inputFile[1][:-1]
    imgSrc = inputFile[3][:-1]
except:
    print("No se ha cargado el archivo")

silabas = silabizer()
syllables = silabas(palabra)
print(syllables)
BACK_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
pygame.init()

win_x = 500
win_y = 700
win = pygame.display.set_mode((win_x, win_y))  # dimensions of it
pygame.display.set_caption("Syllable Game")  # title of this shit of game
clock = pygame.time.Clock()

# create a instance of the chracter and bullets
# font = pygame.font.SysFont('arial', 50, True, False)
font = pygame.font.Font("bLetter.ttf", 50)
imgImported = True
try:
    image = pygame.image.load(imgSrc)
    image = pygame.transform.scale(image, (360, 210))
except:
    print("Fallo cargando img")
    imgImported = False

run = True  # The game loop running
centerLetter = {
    2: 30,
    3: 30,
    4: 50,
    5: 70,
    6: 85,
    7: 90,
    8: 140,
    9: 165,
    10: 195,
    11: 200,
}
centerWord = {
    2: 60,
    3: 60,
    4: 40,#
    5: 50,#
    6: 60,#
    7: 70,
    8: 80,#
    9: 85,#
    10: 95,
    11: 100,
}
colors = [
    (230, 21, 21),
    (255, 204, 0),
    (55, 214, 2),
    (0, 104, 240),
    (127, 71, 179),
    (2, 227, 145),
    (255, 0, 247),
    (0, 255, 242),
    (3, 107, 55),
    (156, 235, 77),
    (230, 21, 21),
    (255, 204, 0),
    (55, 214, 2),
    (0, 104, 240),
    (127, 71, 179),
    (2, 227, 145),
    (255, 0, 247),
    (0, 255, 242),
    (3, 107, 55),
    (156, 235, 77),
]


def renderGameWindow():
    # I firs adjust the word in the middle:
    adjust = centerLetter[len(palabra)]
    # Add the visual part:
    win.fill(BACK_COLOR)

    pygame.draw.rect(win, BLACK_COLOR, (20, 20, win_x-40, 300))
    pygame.draw.rect(win, BACK_COLOR, (23, 23, win_x-40-6, 300-6))
    if (imgImported):
        win.blit(image, (75, 50))
    pygame.draw.rect(win, BLACK_COLOR, (20, 350, win_x-40, 100))
    pygame.draw.rect(win, BACK_COLOR, (20+3, 350+3, win_x-40-6, 100-6))

    index = 0

    text = font.render(palabra, 1, BLACK_COLOR)

    win.blit(text, (win_x/2 - centerWord[len(palabra)], 380))
    # print(palabra, len(palabra))
    # Print the syllables:
    colorIndex = 0
    sizeBox = 30
    distanceBetweenCube = 27
    for i, syl in enumerate(syllables):
        t = font.render(str(syl), 1, BLACK_COLOR)
        x = win_x/2 - adjust + index
        y = 450 + 50 + 8
        win.blit(t, (win_x/2 - adjust + index, y - 58))
        # print(len(str(syl)), x)
        if (len(str(syl)) == 1):
            pygame.draw.rect(win, BLACK_COLOR, (x-8, y, sizeBox, sizeBox))
            pygame.draw.rect(win, colors[colorIndex],
                             (x + 3-8, y + 3, sizeBox-6, sizeBox-6))
            index += 50
        if (len(str(syl)) == 2):
            pygame.draw.rect(win, BLACK_COLOR, (x-8, y, sizeBox, sizeBox))
            pygame.draw.rect(win, colors[colorIndex],
                             (x + 3-8, y + 3, sizeBox-6, sizeBox-6))
            colorIndex += 1
            pygame.draw.rect(win, BLACK_COLOR,
                             (x-8 + distanceBetweenCube, y, sizeBox, sizeBox))
            pygame.draw.rect(
                win, colors[colorIndex], (x + 3-8 + distanceBetweenCube, y + 3, sizeBox-6, sizeBox-6))
            index += 80
            colorIndex += 1
        if (len(str(syl)) == 3):
            pygame.draw.rect(win, BLACK_COLOR, (x-8, y, sizeBox, sizeBox))
            pygame.draw.rect(win, colors[colorIndex],
                             (x + 3-8, y + 3, sizeBox-6, sizeBox-6))
            colorIndex += 1
            pygame.draw.rect(win, BLACK_COLOR,
                             (x-8 + distanceBetweenCube, y, sizeBox, sizeBox))
            pygame.draw.rect(
                win, colors[colorIndex], (x + 3-8 + distanceBetweenCube, y + 3, sizeBox-6, sizeBox-6))
            colorIndex += 1
            pygame.draw.rect(
                win, BLACK_COLOR, (x-8 + distanceBetweenCube*2, y, sizeBox, sizeBox))
            pygame.draw.rect(
                win, colors[colorIndex], (x + 3-8 + distanceBetweenCube*2, y + 3, sizeBox-6, sizeBox-6))
            colorIndex += 1
            index += 110
        if (len(str(syl)) == 4):
            pygame.draw.rect(win, BLACK_COLOR, (x-8, y, sizeBox, sizeBox))
            pygame.draw.rect(win, colors[colorIndex],
                             (x + 3-8, y + 3, sizeBox-6, sizeBox-6))
            colorIndex += 1
            pygame.draw.rect(win, BLACK_COLOR,
                             (x-8 + distanceBetweenCube, y, sizeBox, sizeBox))
            pygame.draw.rect(
                win, colors[colorIndex], (x + 3-8 + distanceBetweenCube, y + 3, sizeBox-6, sizeBox-6))
            colorIndex += 1
            pygame.draw.rect(
                win, BLACK_COLOR, (x-8 + distanceBetweenCube*2, y, sizeBox, sizeBox))
            pygame.draw.rect(
                win, colors[colorIndex], (x + 3-8 + distanceBetweenCube*2, y + 3, sizeBox-6, sizeBox-6))
            colorIndex += 1
            pygame.draw.rect(
                win, BLACK_COLOR, (x-8 + distanceBetweenCube*3, y, sizeBox, sizeBox))
            pygame.draw.rect(
                win, colors[colorIndex], (x + 3-8 + distanceBetweenCube*3, y + 3, sizeBox-6, sizeBox-6))
            colorIndex += 1
            index += 120

    temp = 0
    index = 0
    for i, letter in enumerate(palabra):
        t = font.render(letter, 1, BLACK_COLOR)
        x = win_x/2 - adjust + temp - 40
        y = 580
        win.blit(t, (x, y))
        pygame.draw.rect(win, BLACK_COLOR, (x-8, y + 50 + 8, 40, 40))
        pygame.draw.rect(win, colors[i], (x + 3-8, y + 3 + 50 + 8, 40-6, 40-6))
        a = 28 + index
        b = 222
        pygame.draw.rect(win, BLACK_COLOR, (a-8, b + 50 + 8, 40, 40))
        pygame.draw.rect(win, colors[i], (a + 3-8, b + 3 + 50 + 8, 40-6, 40-6))
        temp += 50
        index += 36

    pygame.display.update()  # update the win frames


while(run):
    pygame.time.delay(500)  # 64x64 images
    if (len(palabra) > 10):
        run = False
        print("Palabra demasiasdo larga, máximo 10")
    for event in pygame.event.get():  # Check for events of close
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()  # check the diferent letters of the key board
    if (keys[pygame.K_SPACE]):
        pass
    if (keys[pygame.K_RIGHT]):
        pass
    elif (keys[pygame.K_LEFT]):
        pass
    renderGameWindow()  # For drawing all the canvas
pygame.quit()
