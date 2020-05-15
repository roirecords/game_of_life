import pygame
import numpy as np
import time

#Create game screen
pygame.init()
width, height=1000,960 #1000 pixels wide, 1000 pixels height
screen = pygame.display.set_mode((height,width))

bg = 25,25,25 #grey color
screen.fill(bg) #grey color in the whole screen

#create the cells
nCx, nCy = 100,100 #number of cells per x and y axes
dimCx = width/nCx
dimCy = height/nCy

#matrix of the state of the cells
CellState = np.zeros((nCx,nCy)) #if 0, it is dead; if 1, it is alive

NewCellState = np.zeros((nCx,nCy)) #if 0, it is dead; if 1, it is alive

#simple automata
CellState[5,5]=1
CellState[5,4]=1
CellState[5,3]=1

#glider
CellState[15+1,15]=1
CellState[15+1,15+1]=1
CellState[15+2,15+1]=1
CellState[15,15+2]=1
CellState[15+2,15+2]=1

#space ship
CellState[5+1,25]=1
CellState[5+2,25]=1
CellState[5+3,25]=1
CellState[5,25+1]=1
CellState[5+3,25+1]=1
CellState[5+3,25+2]=1
CellState[5+3,25+3]=1
CellState[5,25+4]=1
CellState[5+2,25+4]=1


#space ship
CellState[25+1,25]=1
CellState[25+2,25]=1
CellState[25+3,25]=1
CellState[25,25+1]=1
CellState[25+3,25+1]=1
CellState[25+3,25+2]=1
CellState[25+3,25+3]=1
CellState[25,25+4]=1
CellState[25+2,25+4]=1


#Heavy space ship
CellState[75,56]=1
CellState[75+1,56]=1
CellState[75+2,56]=1
CellState[75+3,56]=1
CellState[75+4,56]=1
CellState[75+5,56]=1
CellState[75,56+1]=1
CellState[75+6,56+1]=1
CellState[75,56+2]=1
CellState[75+1,56+3]=1
CellState[75+6,56+3]=1
CellState[75+3,56+4]=1
CellState[75+4,56+4]=1

#Heavy space ship
CellState[7,56]=1
CellState[7-1,56]=1
CellState[7-2,56]=1
CellState[7-3,56]=1
CellState[7-4,56]=1
CellState[7-5,56]=1
CellState[7,56+1]=1
CellState[7-6,56+1]=1
CellState[7,56+2]=1
CellState[7-1,56+3]=1
CellState[7-6,56+3]=1
CellState[7-3,56+4]=1
CellState[7-4,56+4]=1


##Fentilo
#CellState[75+1,5]=1
#CellState[75+2,5]=1
#CellState[75,5+1]=1
#CellState[75+1,5+1]=1
#CellState[75+1,5+2]=1
#
##Fentilo
#CellState[30+1,30]=1
#CellState[30+2,30]=1
#CellState[30,30+1]=1
#CellState[30+1,30+1]=1
#CellState[30+1,30+2]=1


#game pause
pauseGame = False

while True:


    ev= pygame.event.get()

    for event in ev:
        if event.type == pygame.KEYDOWN:
            pauseGame = not pauseGame

        mousetick=pygame.mouse.get_pressed()
        if sum(mousetick)>0:
            posx,posy = pygame.mouse.get_pos()
            celx,cely = int(np.floor(posx/dimCx)),int(np.floor(posy/dimCy))
            NewCellState[celx,cely]= not mousetick[2]



    for i in range(0,nCx):
        for j in range(0,nCy):
            if not pauseGame:
                neig_alive =   CellState[(i-1) % nCx,(j-1) % nCy] + \
                               CellState[(i) % nCx  ,(j-1) % nCy] + \
                               CellState[(i+1) % nCx,(j-1) % nCy] + \
                               CellState[(i-1) % nCx,(j) % nCy] + \
                               CellState[(i+1) % nCx,(j) % nCy] + \
                               CellState[(i-1) % nCx,(j+1) % nCy] + \
                               CellState[(i)  % nCx ,(j+1) % nCy] + \
                               CellState[(i+1) % nCx,(j+1) % nCy]

                if CellState[(i),(j)] ==0:
                    if neig_alive == 3:
                        NewCellState[(i),(j)] = 1
                    else:
                        NewCellState[(i),(j)] = 0
                else:
                    if neig_alive >1 and neig_alive <4:
                        NewCellState[(i),(j)] = 1
                    else:
                        NewCellState[(i),(j)] = 0

            #print the cells
            poly =[(i    *dimCx,j    *dimCy),
                   ((i+1)*dimCx,j    *dimCy),
                   ((i+1)*dimCx,(j+1)*dimCy),
                   (i    *dimCx,(j+1)*dimCy)] #points of the poygon, they should be put sequentially

            #print the cells
            if NewCellState[i,j] == 0: #if it's dead, only put a empty rectanble
                pygame.draw.polygon(screen, (128,128,128),poly,1)
            else:   #if it's alive, put a white rectanble
                pygame.draw.polygon(screen, (255,255,255),poly,0)

    #update cell CellState
    CellState = np.copy(NewCellState)

    #to show the things
    pygame.display.flip()
    time.sleep(0.10)
    #clean the screen
    screen.fill(bg) #grey color in the whole screen
