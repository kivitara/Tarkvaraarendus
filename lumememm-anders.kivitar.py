import pygame  # Laeme PyGame mooduli

pygame.init()

screen = pygame.display.set_mode([300, 300])  # Tekitame akna suurusega 300*300
pygame.display.set_caption("Lumemees-Anders Kivitar")  # Lisame programmiaknale teksti

running = True  # anname muutujale running väärtuse True
while running:  # loome tsükli pildi ekraanil hoidmiseks
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.circle(screen, [255, 255, 255], [150, 75], 30)  # Teeme esimese valge ringi asukohaga x=150, y=80 raadius=30
    pygame.draw.circle(screen, [255, 255, 255], [150, 140], 40)  # Teeme teise valge ringi asukohaga x=150, y=145, raadius=40
    pygame.draw.circle(screen, [255, 255, 255], [150, 225], 50)  # Teeme kolmanda valge ringi asukohaga x=150 y=230, raadius=50

    # pygame.draw.circle(screen, [0,0,0], [140,75], 5)			# Esmalt said silmadeks tehtud ringid, kuid lähemal vaatamisel
    # pygame.draw.circle(screen, [0,0,0], [160,75], 5)			# paistab, et seal on ruudud.

    pygame.draw.rect(screen, [0, 0, 0, ], [137, 67, 7, 7])  # vasakpoolse silma must ruut
    pygame.draw.polygon(screen, [0, 0, 0], [[135, 70], [140, 65], [145, 70], [140, 75]])  # vasakpoolse silma must romb

    pygame.draw.rect(screen, [0, 0, 0, ], [157, 67, 7, 7])  # parempoolse silma must ruut
    pygame.draw.polygon(screen, [0, 0, 0], [[155, 70], [160, 65], [165, 70], [160, 75]])  # parempoolse silma must romb

    pygame.draw.polygon(screen, [255, 0, 0], [[145, 80], [150, 95], [155, 80]])  # Teeme kolmnurk punase nina

    pygame.display.flip()  # uuendame ekraani pilti

pygame.quit()  # paneme ekraani kinni
