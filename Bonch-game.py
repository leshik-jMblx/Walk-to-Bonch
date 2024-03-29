# First python-game (test)

import pygame, sys

pygame.init()
main_window = pygame.display.set_mode((1300, 800))
pygame.display.set_caption('First Game (test)')
main_window.fill((100, 150, 200))
# Colors
white_color = (255, 255, 255)
purple_color = (148, 0, 211)
gray_color = (211, 211, 211)
grad_color = (128, 128, 128)
yellow_color = (255, 255, 0)


# MAIN MENU ------------------------------------------------ MAIN MENU
def main_menu():
	main_window.fill((0, 0, 0))
	
	press = pygame.image.load('press.png')
	press_pos = press.get_rect(center=(560, 430))
	main_window.blit(press,press_pos)
	
	enter = pygame.image.load('enter.png')
	enter_pos = enter.get_rect(center=(760, 430))
	main_window.blit(enter,enter_pos)	
	
	bonc = pygame.image.load('bonc.png')
	bonc_pos = bonc.get_rect(center=(475, 150))
	main_window.blit(bonc,bonc_pos)	
	
	hman = pygame.image.load('hman.png')
	hman_pos = hman.get_rect(center=(720, 150))
	main_window.blit(hman,hman_pos)	
	
	smile = pygame.image.load('))).png')
	smile_pos = smile.get_rect(center=(970, 155))
	main_window.blit(smile,smile_pos)	




def paintWindow():
	main_window.fill((0, 0, 0))	
	
	# Road-line and purple border		
	pygame.draw.line(main_window, white_color, [6, 400], [892, 400], 4)
	#pygame.draw.rect(main_window, grad_color, (6, 403, 892, 25))
	

	# Houses
	pygame.draw.lines(main_window, gray_color, False,\
	[[6, 25], [166, 25], [166, 399], [6, 399]], 3)
	pygame.draw.rect(main_window, gray_color, (166, 225, 250, 175), 3)
	pygame.draw.lines(main_window, gray_color, False,\
	[[260, 225], [260, 125], [700, 125], [700, 399], [399, 399]], 3)
	
	# Load character's image
	bonchevec = pygame.image.load('pixil-frame-0.png')
	start_pos = bonchevec.get_rect(center=(50, 430))
	main_window.blit(bonchevec, start_pos)
	
	# Burger King
	bk = pygame.image.load('bk.png')
	bk_pos = bk.get_rect(center=(400, 285))
	main_window.blit(bk, bk_pos)
	
	x,y = 22,50 # Fist window's coordinates
	for floor in range(7):
		for window in range(4):
			# Yellow windows
			if floor == 0 and window == 1 or floor == 2 and\
			(window == 2 or window == 3) or floor == 3 and\
			window == 0 or floor == 4 and window == 2 or\
			floor == 5 and (window == 0 or window == 3) or\
			floor == 6 and window == 2:
				pygame.draw.rect(main_window, yellow_color, (x, y, 17, 25))
			
			else:
				pygame.draw.rect(main_window, gray_color, (x, y, 17, 25), 1)
				
			if window != 3:
				x += 34
			else:
				x = 22
				y += 47


# To open the main window
while True:
	pygame.time.delay(50)
	
	for k in pygame.event.get():
		if k.type == pygame.KEYUP:
			if k.key == pygame.K_RETURN:
				sys.exit()
				
		if k.type == pygame.QUIT:
			sys.exit()
	
	main_menu()	

	
	
	#paintWindow()
	
 
			
	pygame.display.update()
