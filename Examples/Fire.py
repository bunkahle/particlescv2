# Fire

import cv2, sys
import particlescv2 as part
import numpy as np

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
# pygame.display.set_caption("PyIgnition demo: fire")
# clock = pygame.time.Clock()
windowname = "Particles demo"
cv2.namedWindow(windowname)
cv2.setMouseCallback(windowname, on_mouse)

fire = part.ParticleEffect(screen, (0, 0), (800, 600))
gravity = fire.CreateDirectedGravity(strength = 0.07, direction = [0, -1])
wind = fire.CreateDirectedGravity(strength = 0.05, direction = [1, 0])
source = fire.CreateSource((300, 500), initspeed = 2.0, initdirection = 0.0, initspeedrandrange = 1.0, initdirectionrandrange = 0.5, particlesperframe = 10, particlelife = 100, drawtype = DRAWTYPE_CIRCLE, colour = (100, 200, 255), radius = 3.0)
source.CreateParticleKeyframe(10, colour = (20, 50, 250), radius = 4.0)
source.CreateParticleKeyframe(30, colour = (0, 0, 150), radius = 6.0)
source.CreateParticleKeyframe(60, colour = (20, 20, 50), radius = 8.0)
source.CreateParticleKeyframe(80, colour = (0, 0, 0), radius = 12.0)
fire.CreateRectangle((400, 100), (100, 100, 200), bounce = 0.2, width = 100, height = 20)
fire.CreateCircle((350, 200), (100, 100, 200), bounce = 0.2, radius = 25)
fire.CreateCircle((450, 200), (100, 100, 200), bounce = 0.2, radius = 25)

# Test shizz for generic keyframe creation function
# source.CreateParticleKeyframe(2, colour = (0, 0, 255))
# source.CreateParticleKeyframe(5, colour = (0, 0, 0))
# source.CreateParticleKeyframe(0, colour = (255, 255, 255))
# source.CreateParticleKeyframe(0, colour = (0, 100, 255))
# source.CreateParticleKeyframe(80, colour = (255, 255, 255), radius = 1.0)


while True:
	# for event in pygame.event.get():
	#	if event.type == pygame.QUIT:
	#		sys.exit()
	k = cv2.waitKey(30)
	if k == 27:
		sys.exit()
	
	# screen.fill((0, 0, 0))
	# cv.Zero(screen)
	screen[:] = 0
	if source.curframe % 30 == 0:
		source.ConsolidateKeyframes()
	fire.Update()
	fire.Redraw()
	# pygame.display.update()
	# screen = cv2.blur(screen,(5,1))
	cv2.imshow(windowname, screen)
	# clock.tick(30)
