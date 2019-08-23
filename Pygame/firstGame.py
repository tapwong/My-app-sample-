import pygame
pygame.init()

screenWidth = 500
screenHeight = 500
x = 0
y = 400
width = 40
height = 60
vel = 1

win = pygame.display.set_mode((screenWidth,screenHeight))

pygame.display.set_caption("First Game")

isJump = False
jumpCount = 10

run = True
while run:
	pygame.time.delay(10)

	for event in  pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and x > vel:
		x -= vel
	if keys[pygame.K_RIGHT] and x < screenWidth- vel - width:
		x += vel
	if not isJump:
		if keys[pygame.K_UP] and y > vel:
			y -= vel
		if keys[pygame.K_DOWN] and y < screenHeight - vel - height:
			y += vel
		if keys[pygame.K_SPACE]:
			isJump = True

	else:
		if jumpCount >= -10:
			y -= abs(jumpCount) * jumpCount * 0.5
			jumpCount -= 1
		else:
			isJump = False
			jumpCount = 10


	win.fill((0,0,0))
	pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
	pygame.display.update()
pygame.quit()
