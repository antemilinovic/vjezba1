import pygame
import time

pygame.init()

broj_redaka=500
broj_stupaca=800
velicina_ekrana=(broj_stupaca,broj_redaka)
gameDisplay=pygame.display.set_mode(velicina_ekrana)
pygame.display.set_caption('Moja igra')

zelena = (0,255,0)
crna = (0,0,0)
plava=(0,0,255)

pygame.display.update()

FPS = 30
clock = pygame.time.Clock()

gameExit = False

velicina_bloka = 20
pomak = 10


lead_x = 0
lead_y = broj_redaka-velicina_bloka
lead_x_change = 0
lead_y_change = 0

lead_y2=0
lead_x2=broj_stupaca-velicina_bloka

#gameLoop
while not gameExit:
    for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_y_change = 0
                    lead_x_change= -pomak
                if event.key == pygame.K_RIGHT:
                    lead_y_change = 0
                    lead_x_change= pomak
                if event.key == pygame.K_UP:
                    lead_x_change = 0
                    lead_y_change = -pomak
                if event.key == pygame.K_DOWN:
                    lead_x_change = 0
                    lead_y_change = pomak

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    lead_x_change = 0
                if event.key == pygame.K_RIGHT:
                    lead_x_change = 0
                if event.key == pygame.K_DOWN:
                    lead_y_change = 0
                if event.key == pygame.K_UP:
                    lead_y_change = 0

    if lead_x2>lead_x & lead_y2>lead_y:
        lead_x2-=pomak/1.5
        lead_y2-=pomak/1.5
    if lead_x2<lead_x & lead_y2<lead_y:
        lead_x2+=pomak/1.5
        lead_y2+=pomak/1.5
    if lead_x2<lead_x & lead_y2>lead_y:
        lead_x2+=pomak/1.5
        lead_y2-=pomak/1.5
    if lead_x2>lead_x & lead_y2<lead_y:
        lead_x2-=pomak/1.5
        lead_y2+=pomak/1.5
    

    if (lead_x + velicina_bloka - 1) >= broj_stupaca:
        gameExit = True
    if  lead_x < 0:
        gameExit = True
    if (lead_y + velicina_bloka - 1) >= broj_redaka:
        gameExit = True
    if  lead_y  < 0:
        gameExit = True

    lead_x += lead_x_change
    lead_y += lead_y_change

    

    gameDisplay.fill(zelena)

    pygame.draw.rect(gameDisplay, crna, [lead_x,lead_y, velicina_bloka, velicina_bloka])

    pygame.draw.rect(gameDisplay, plava, [lead_x2,lead_y2, velicina_bloka, velicina_bloka])
    
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit()
    
    
