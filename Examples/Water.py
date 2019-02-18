# Water - collisions demo

import cv2, sys, math
import numpy as np
import particlescv2 as part

DRAWTYPE_POINT = 0
DRAWTYPE_CIRCLE = 1
DRAWTYPE_LINE = 2
DRAWTYPE_SCALELINE = 3
DRAWTYPE_BUBBLE = 4
DRAWTYPE_IMAGE = 5

def on_mouse(event, x, y, flags, param):
	global source
	"""
	source.SetPos(pygame.mouse.get_pos())
	"""
	source.SetPos((x, y))

# screen = pygame.display.set_mode((800, 600))
# screen = cv.CreateImage((800,600), 8, 3)
screen = np.zeros((600, 800, 3), np.uint8)
# pygame.display.set_caption("PyIgnition demo: collisions")
# clock = pygame.time.Clock()
windowname = "PyIgnition demo"
cv2.namedWindow(windowname)
cv2.setMouseCallback(windowname, on_mouse)

effect = part.ParticleEffect(screen, (0, 0), (800, 600))
source = effect.CreateSource((0, 0), initspeed = 2.0, initdirection = math.pi, initspeedrandrange = 1.0, initdirectionrandrange = math.pi, particlesperframe = 20, particlelife = 80, drawtype = DRAWTYPE_CIRCLE, colour = (250, 100, 100), radius = 10.0)
grav = effect.CreateDirectedGravity(0.2, 0.0, [0, 1])
circle1 = effect.CreateCircle((100, 200), (0, 0, 0), bounce = 0.1, radius = 50.0)
circle2 = effect.CreateCircle((400, 100), (0, 0, 0), bounce = 0.1, radius = 50.0)
circle3 = effect.CreateCircle((300, 300), (0, 0, 0), bounce = 0.1, radius = 50.0)
circle4 = effect.CreateCircle((500, 250), (0, 0, 0), bounce = 0.1, radius = 50.0)
circle5 = effect.CreateCircle((150, 400), (0, 0, 0), bounce = 0.1, radius = 50.0)
rect1 = effect.CreateRectangle((500, 450), colour = (200, 200, 100), width = 250.0, height = 100.0, bounce = 0.2)
rect1.CreateKeyframe(200, pos = (400, 100), width = 400.0, interpolationtype = "cosine")
rect1.CreateKeyframe(300, colour = (255, 0, 0))
circle2.CreateKeyframe(250, pos = (400, 500), interpolationtype = "cosine")
circle2.CreateKeyframe(300, colour = (50, 255, 0))
source.CreateParticleKeyframe(60, colour = (250, 100, 100), radius = 10.0)
source.CreateParticleKeyframe(80, colour = (255, 255, 255), radius = 20.0)
line = effect.CreateBoundaryLine((700, 500), colour = (0, 0, 0), bounce = 0.1, normal = [-1.4142, -1.4142])
line.CreateKeyframe(300, normal = [-2, -1])
line.CreateKeyframe(500, normal = [-1, 0])
line2 = effect.CreateBoundaryLine((0, 600), colour = (0, 0, 0), bounce = 0.1, normal = [0, -1])
line3 = effect.CreateBoundaryLine((0, 600), colour = (0, 0, 0), bounce = 0.1, normal = [1, 0])


while True:
	# for event in pygame.event.get():
	# 	if event.type == pygame.QUIT:
	#		sys.exit()
	k = cv2.waitKey(30)
	if k == 27:
		sys.exit()	
	# screen.fill((255, 255, 255))
	# cv.Set(screen, cv.RGB(255, 255, 255))
	screen[:] = (255, 255, 255)
	# source.SetPos(pygame.mouse.get_pos())
	effect.Update()
	effect.Redraw()
	# pygame.display.update()
	cv2.imshow(windowname, screen)
	# clock.tick(30)
