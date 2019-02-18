import sys, math, random
import cv2
import numpy as np
import particlescv2 as parts

DRAWTYPE_POINT = 0
DRAWTYPE_CIRCLE = 1
DRAWTYPE_LINE = 2
DRAWTYPE_SCALELINE = 3
DRAWTYPE_BUBBLE = 4
DRAWTYPE_IMAGE = 5


# screen = pygame.display.set_mode((800, 600))
screen = np.zeros((600, 800, 3), np.uint8)
# clock = pygame.time.Clock()

effect = parts.ParticleEffect(screen, (0, 0), (800, 600))
gravity = effect.CreateVortexGravity(strength = 1.0, strengthrandrange = 0.0, pos = (400, 300))
particles = effect.CreateSource(pos = (0, 0), initspeed = 5.0, initdirectionrandrange = 0.5, particlesperframe = 5, particlelife = 200, drawtype = DRAWTYPE_LINE, length = 5.0, radius = 5.0)

def on_mouse(event, x, y, flags, param):
    global particles
    particles.SetPos((x, y))

def Draw():    
    # screen.fill((255, 255, 255))
    screen[:] = 255
    effect.Update()
    effect.Redraw()
    cv2.circle(screen, (400, 300), 3, (100, 0, 255), 3)
    # pygame.draw.circle(screen, (255, 0, 100), (400, 300), 3)
    
    # mpos = (mousex, mousey)
    #f = gravity.GetForce(mpos)
    #endpos = [mpos[0] + f[0], mpos[1] + f[1]]
    
    #pygame.draw.aaline(screen, (0, 0, 0), mpos, endpos)

windowname = "Vortex Gravity demo"
cv2.namedWindow(windowname)
cv2.setMouseCallback(windowname, on_mouse)

while True:
    #for event in pygame.event.get():
    #    if event.type == pygame.QUIT:
    #        sys.exit()
    k = cv2.waitKey(30)
    if k == 27:
        sys.exit()
    Draw()
    cv2.imshow(windowname, screen)
    # pygame.display.update()
    # clock.tick(30)
