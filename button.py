import pygame

class Button():
	def __init__(self, x, y, i, s):
		w = i.get_width()
		h = i.get_height()
		self.i = pygame.transform.scale(i, (int(w * s), int(h * s)))
		self.rect = self.i.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		event = False
		pos = pygame.mouse.get_pos()
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				event = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False
		surface.blit(self.i, (self.rect.x, self.rect.y))

		return event