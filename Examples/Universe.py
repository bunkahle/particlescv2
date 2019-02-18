# Catherine wheel

import particlescv2 as parts
import cv2, sys
import numpy as np

# screen = pygame.display.set_mode((600, 600))
# screen = cv.CreateImage((800,600), 8, 3)
universe = cv2.imread("universe.jpg")
screen = np.zeros(universe.shape, np.uint8)
# pygame.display.set_caption("part demo: catherine wheel")
# clock = pygame.time.Clock()
windowname = "part demo: catherine wheel"
cv2.namedWindow(windowname)
DRAWTYPE_POINT = 0
DRAWTYPE_CIRCLE = 1
DRAWTYPE_LINE = 2
DRAWTYPE_SCALELINE = 3
DRAWTYPE_BUBBLE = 4
DRAWTYPE_IMAGE = 5
wheel = parts.ParticleEffect(screen, (0, 0), (600, 600))
#image = pygame.image.load("Spark.png").convert_alpha()
spark = cv2.imread("Spark.png")
# spark = np.zeros((5, 5, 3), np.uint8)
# spark = cv.CreateImage((5,5), 8, 3)
spark = cv2.resize(spark, (5,5))
image = spark
#flame = wheel.CreateSource((300, 300), initspeed = 20.0, initdirection = 0.0, initspeedrandrange = 0.0, initdirectionrandrange = 0.5, particlesperframe = 3, particlelife = 50, drawtype = parts.DRAWTYPE_SCALELINE, colour = (255, 200, 200), length = 20.0)
sparks0 = wheel.CreateSource((430, 170), initspeed = 1.0, initdirection = 0.0, initspeedrandrange = 0.4, initdirectionrandrange = 3.141592653, particlesperframe = 5, particlelife = 20, genspacing = 0, drawtype = DRAWTYPE_IMAGE, image = image, colour = (255, 0, 0))
sparks1 = wheel.CreateSource((90, 550), initspeed = 1.0, initdirection = 0.0, initspeedrandrange = 0.4, initdirectionrandrange = 3.141592653, particlesperframe = 5, particlelife = 20, genspacing = 0, drawtype = DRAWTYPE_IMAGE, image = image, colour = (255, 0, 0))
sparks2 = wheel.CreateSource((330, 630), initspeed = 1.0, initdirection = 0.0, initspeedrandrange = 0.4, initdirectionrandrange = 3.141592653, particlesperframe = 5, particlelife = 20, genspacing = 0, drawtype = DRAWTYPE_IMAGE, image = image, colour = (255, 0, 0))
wheel.CreateDirectedGravity(strength = 0.05, direction = [0, 1])
velocity = 0.1
maxvelocity = 0.5
acceleration = 0.001

while True:
    # for event in pygame.event.get():
    #	if event.type == pygame.QUIT:
    #		sys.exit()
    k = cv2.waitKey(30)
    if k == 27:
        sys.exit()
    
    #flame.CreateKeyframe(flame.curframe, initdirection = flame.initdirection + velocity)
    
    if velocity <= maxvelocity:
        velocity += acceleration
    
    # screen.fill((10, 0, 50))
    # cv.Set(screen, cv.RGB(10, 0, 50))
    # screen = universe.copy()	
    screen[:] = (0, 0, 0)
    wheel.Update()
    wheel.Redraw()
    # pygame.display.update()
    # cv.Smooth(screen, screen)
    blur = cv2.blur(screen,(5,5))
    screen2 = cv2.bitwise_or(blur, universe)
    cv2.imshow(windowname, screen2)
    # clock.tick(30)
