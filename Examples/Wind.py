# Wind - randomised gravity

import cv2, sys
import numpy as np
import particlescv2 as part

DRAWTYPE_POINT = 0
DRAWTYPE_CIRCLE = 1
DRAWTYPE_LINE = 2
DRAWTYPE_SCALELINE = 3
DRAWTYPE_BUBBLE = 4
DRAWTYPE_IMAGE = 5

def on_mouse(event, x, y, flags, param):
	global circle
	"""
	# circle.SetPos(pygame.mouse.get_pos())
	"""
	circle.SetPos((x, y))

# screen = pygame.display.set_mode((800, 600))
# screen = cv.CreateImage((800,600), 8, 3)
screen = np.zeros((600, 800, 3), np.uint8)
# pygame.display.set_caption("PyIgnition demo: wind")
# clock = pygame.time.Clock()
windowname = "PyIgnition demo: wind"
cv2.namedWindow(windowname)
cv2.setMouseCallback(windowname, on_mouse)

effect = part.ParticleEffect(screen, (0, 0), (800, 600))
source = effect.CreateSource((400, 600), initspeed = 5.0, initdirection = 0.0, initspeedrandrange = 2.0, initdirectionrandrange = 0.2, particlesperframe = 10, particlelife = 200, drawtype = DRAWTYPE_POINT, colour = (200, 255, 255))
grav = effect.CreateDirectedGravity(0.0, 0.2, [1, 0])
#othergrav = effect.CreateDirectedGravity(0.05, 0.0, [0, 1])
circle = effect.CreateCircle((0, 0), (0, 0, 0), bounce = 0.2, radius = 30.0)


while True:
	# for event in pygame.event.get():
	# 	if event.type == pygame.QUIT:
	# 		sys.exit()
	k = cv2.waitKey(30)
	if k == 27:
		sys.exit()
		
	# screen.fill((100, 125, 200))
	# cv.Set(screen, cv.RGB(100, 125, 200))
	screen[:] = (200, 125, 100)
	# circle.SetPos(pygame.mouse.get_pos())
	effect.Update()
	effect.Redraw()
	# pygame.display.update()
	# cv.Smooth(screen, screen)
	cv2.imshow(windowname, screen)
	# clock.tick(30)
