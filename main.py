import pygame
import random
from word_box import Box


pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Ghetto Wordle")
image = pygame.image.load('ghetto_icon.png')
pygame.display.set_icon(image)
clock = pygame.time.Clock()

box_list = {
    'row0' : [],
    'row1' : [],
    'row2' : [],
    'row3' : [],
    'row4' : []
}
all_boxes = []

r = 0
c = 0
for i in range(25):
    box_list['row{}'.format(r)].append(Box(screen, 160, 100, r, c))
    all_boxes.append(box_list['row{}'.format(r)][c])
    c += 1
    if (i+1) % 5 == 0:
        if i != 0:
            r += 1
            c = 0

with open('words.txt', 'r') as file:
    lines = file.readlines()
    word = random.choice(lines).upper()

correct = False

def UnMessyTheCode():
    if all(box.changed for box in box_list['row0']):
        if correct != True:
            for box in box_list['row0']:
                i = box_list['row0'].index(box)
                checkSimilar(box, word, box_list['row0'], i)

    if all(box.changed for box in box_list['row1']):
        if correct != True:
            for box in box_list['row1']:
                i = box_list['row1'].index(box)
                checkSimilar(box, word, box_list['row1'], i)

    if all(box.changed for box in box_list['row2']):
        if correct != True:
            for box in box_list['row2']:
                i = box_list['row2'].index(box)
                checkSimilar(box, word, box_list['row2'], i)

    if all(box.changed for box in box_list['row3']):
        if correct != True:
            for box in box_list['row3']:
                i = box_list['row3'].index(box)
                checkSimilar(box, word, box_list['row3'], i)

    if all(box.changed for box in box_list['row4']):
        if correct != True:
            for box in box_list['row4']:
                i = box_list['row4'].index(box)
                checkSimilar(box, word, box_list['row4'], i)

    if all(box.changed for box in all_boxes) or correct == True:
        print(word)

def checkSimilar(box : Box, word, word_list, index):
    if box.letter.capitalize() in word:
        if word_list[index].letter.upper() == word[index]:
            box.color = (100, 200, 100)
        else:
            box.color = (200, 200, 100)
    else:
        box.color = (200, 100, 100)

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if correct != True:
                for box in all_boxes:
                    box.changeValue(event)
            if ''.join(box.letter.upper() for box in box_list['row0']) == word:
                correct = True
            elif ''.join(box.letter.upper() for box in box_list['row1']) == word:
                correct = True
            elif ''.join(box.letter.upper() for box in box_list['row2']) == word:
                correct = True
            elif ''.join(box.letter.upper() for box in box_list['row3']) == word:
                correct = True
            elif ''.join(box.letter.upper() for box in box_list['row4']) == word:
                correct = True
    
    for box in all_boxes:
        box.draw()
    
    if correct == True:
        for box in all_boxes:
            i = box_list['row{}'.format(box.ROW)].index(box)
            checkSimilar(box, word, box_list['row{}'.format(box.ROW)], i)
            if all_boxes[i+1] == None:
                break
    
    # row nonsense
    UnMessyTheCode()
    
    pygame.display.flip()
    clock.tick(30)