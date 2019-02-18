# Bubbles!

# import particlescv2 as part
import particlescv2 as part
import cv2, sys, math
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
	if event.type == pygame.MOUSEBUTTONDOWN:
		source.CreateKeyframe(source.curframe + 1, pos = pygame.mouse.get_pos(), particlesperframe = 1)
		source.CreateKeyframe(source.curframe + 2, pos = pygame.mouse.get_pos(), particlesperframe = 0)
	"""
	if event == cv2.EVENT_LBUTTONDOWN or event == cv2.EVENT_RBUTTONDOWN:
		source.CreateKeyframe(source.curframe + 1, pos = (x, y), particlesperframe = 1)
		source.CreateKeyframe(source.curframe + 2, pos = (x, y), particlesperframe = 0)

# screen = pygame.display.set_mode((800, 600))
# screen = cv.CreateImage((800,600), 8, 3)
screen = np.zeros((600, 800, 3), np.uint8)
# pygame.display.set_caption("PyIgnition demo: bubbles")
windowname = "Particles Demo: Bubbles"
cv2.namedWindow(windowname)
cv2.setMouseCallback(windowname, on_mouse)
# clock = pygame.time.Clock()

effect = part.ParticleEffect(screen, (0, 0), (800, 600))
source = effect.CreateSource(initspeed = 1.0, initdirection = 0.0, initspeedrandrange = 0.5, initdirectionrandrange = math.pi, particlelife = 1000, colour = (200, 255, 200), drawtype = DRAWTYPE_BUBBLE, radius = 4.0)
source.CreateParticleKeyframe(500, colour = (250, 100, 250))
source.CreateParticleKeyframe(75, colour = (190, 190, 200))
source.CreateParticleKeyframe(100, colour = (50, 250, 252))
source.CreateParticleKeyframe(125, colour = (250, 250, 255))
effect.CreateDirectedGravity(strength = 0.04, direction = [0, -1])

while True:
	#for event in pygame.event.get():
	#	if event.type == pygame.QUIT:
	k = cv2.waitKey(30)
	if k == 27:
		sys.exit()
	# screen.fill((100, 150, 255))
	# cv.Set(screen, cv.RGB(100, 150, 255))
	screen[:] = (255, 150, 100)
	effect.Update()
	effect.Redraw()
	# pygame.display.update()
	cv2.imshow(windowname, screen)
	# clock.tick(30)
