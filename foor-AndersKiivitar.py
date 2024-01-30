import pygame                                                                           # Laeme pygame mooduli

pygame.init()

screen = pygame.display.set_mode([300, 300])                                            # Loome akna
pygame.display.set_caption("Foor - Anders Kivitar")                                     # Lisame aknale teksti

running = True                                                                          # Muutuja running saab väärtuseks True
while running:                                                                          # Loome tsykli akna püsimiseks
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(screen, [130, 130, 130], [100, 10, 100, 270], 2)   # Teeme halli ristkyliku
    pygame.draw.circle(screen, [255, 0, 0], [150, 60], 40)              # Teeme punase ringi
    pygame.draw.circle(screen, [255, 255, 0], [150, 145], 40)           # Teeme kolase ringi
    pygame.draw.circle(screen, [0, 255, 0], [150, 230], 40)             # Teeme rohelise ringi

    pygame.display.flip()                                                               # Värskendame akent

pygame.quit()                                                                           # lõpetame pygame
