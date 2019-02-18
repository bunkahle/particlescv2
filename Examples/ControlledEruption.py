# Controlled Eruption - PyIgnition beta 1 demo
# Copyright David Barker 2010
#
# Be forewarned - this is quite possibly the messiest code you will see all year.
# Let this mess be a lesson to those who try tostart coding without deciding
# what they're going to code beforehand...

import particlescv2 as parts
import cv2, sys, math, random
import numpy as np

DRAWTYPE_POINT = 0
DRAWTYPE_CIRCLE = 1
DRAWTYPE_LINE = 2
DRAWTYPE_SCALELINE = 3
DRAWTYPE_BUBBLE = 4
DRAWTYPE_IMAGE = 5

#pygame.font.init()
# screen = pygame.display.set_mode((800, 600))
# screen = cv.CreateImage((800,600), 8, 3)
windowname = 'OpenCV2 & particlescv2'
screen = np.zeros((600, 800, 3), np.uint8)
cv2.imshow(windowname, screen)
# pygame.display.set_caption("PyIgnition 'Controlled Eruption' demo")
#clock = pygame.time.Clock()

curframe = 0
started = False

# 'Press space to start' text
#starttextfont = pygame.font.Font("courbd.ttf", 50)
#starttext = starttextfont.render("Press space to start", True, (255, 255, 255), (0, 0, 0))
#starttextpos = ((400 - (starttext.get_width() / 2)), (300 - (starttext.get_height() / 2)))

# Background
background = parts.ParticleEffect(screen, (0, 0), (800, 600))
backgroundsource = background.CreateSource((10, 10), initspeed = 5.0, initdirection = 2.35619449, initspeedrandrange = 2.0, initdirectionrandrange = 1.0, particlesperframe = 5, particlelife = 125, drawtype = DRAWTYPE_SCALELINE, colour = (255, 255, 255), length = 10.0)
backgroundsource.CreateParticleKeyframe(50, colour = (0, 255, 0), length = 10.0)
backgroundsource.CreateParticleKeyframe(75, colour = (255, 255, 0), length = 10.0)
backgroundsource.CreateParticleKeyframe(100, colour = (0, 255, 255), length = 10.0)
backgroundsource.CreateParticleKeyframe(125, colour = (0, 0, 0), length = 10.0)
backgroundsource2 = background.CreateSource((790, 10), initspeed = 5.0, initdirection = -2.35619449, initspeedrandrange = 2.0, initdirectionrandrange = 1.0, particlesperframe = 0, particlelife = 125, drawtype = DRAWTYPE_SCALELINE, colour = (255, 255, 255), length = 10.0)
backgroundsource2.CreateParticleKeyframe(50, colour = (0, 255, 0), length = 10.0)
backgroundsource2.CreateParticleKeyframe(75, colour = (255, 255, 0), length = 10.0)
backgroundsource2.CreateParticleKeyframe(100, colour = (0, 255, 255), length = 10.0)
backgroundsource2.CreateParticleKeyframe(125, colour = (0, 0, 0), length = 10.0)

# Periodic firework
fireworkcounter = 0.0
fireworkdist = 200.0
firework = parts.ParticleEffect(screen, (0, 0), (600, 800))
firework.CreateDirectedGravity(strength = 0.2, direction = [0, 1])
sparkimg = cv2.imread("Spark.png")
#sparklittle = cv.CreateImage((3,3), 8, 3)
#cv.Resize(sparkimg, sparklittle)
sparklittle = cv2.resize(sparkimg, (3,3))
sparkimg = sparklittle
fireworksource = firework.CreateSource((10, 10), initspeed = 8.0, initdirection = 0.0, initspeedrandrange = 2.0, initdirectionrandrange = math.pi, particlesperframe = 0, particlelife = 150, drawtype = DRAWTYPE_IMAGE, image = sparkimg)
fireworkblast = background.CreateCircle(pos = (1000, 1000), colour = (0, 0, 0), bounce = 1.5, radius = 100.0)

# Ground-level bubbles
bubbles = parts.ParticleEffect(screen, (0, 0), (600, 800))
bubblesource = bubbles.CreateSource(initspeed = 1.0, initdirection = 0.0, initspeedrandrange = 0.5, initdirectionrandrange = math.pi, particlesperframe = 0, particlelife = 200, colour = (200, 255, 200), drawtype = DRAWTYPE_BUBBLE, radius = 5.0, genspacing = 5)
bubblesource.CreateParticleKeyframe(500, colour = (250, 100, 250))
bubblesource.CreateParticleKeyframe(75, colour = (200, 190, 190))
bubblesource.CreateParticleKeyframe(100, colour = (252, 250, 50))
bubblesource.CreateParticleKeyframe(125, colour = (255, 250, 250))
bubbles.CreateDirectedGravity(strength = 0.04, direction = [0, -1])

# Fire, just for laughs
fire = parts.ParticleEffect(screen, (0, 0), (600, 800))
gravity = fire.CreateDirectedGravity(strength = 0.07, direction = [0, -1])
wind = fire.CreateDirectedGravity(strength = 0.05, direction = [1, 0])
source = fire.CreateSource((150, 500), initspeed = 2.0, initdirection = 0.0, initspeedrandrange = 1.0, initdirectionrandrange = 0.5, particlesperframe = 10, particlelife = 100, drawtype = DRAWTYPE_CIRCLE, colour = (100, 200, 255), radius = 3.0)
source.CreateParticleKeyframe(10, colour = (20, 50, 200), radius = 4.0)
source.CreateParticleKeyframe(30, colour = (0, 0, 150), radius = 6.0)
source.CreateParticleKeyframe(60, colour = (20, 20, 50), radius = 20.0)
source.CreateParticleKeyframe(80, colour = (0, 0, 0), radius = 50.0)

# Text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(screen, windowname,(100,100), font, 2, (255,255,255))
"""
font = pygame.font.Font("arial.ttf", 70)
font2 = pygame.font.Font("arial.ttf", 40)
text = font.render("PyIgnition", True, (255, 255, 255), (0, 0, 0))
text2 = font2.render("ExeSoft", True, (200, 200, 200), (0, 0, 0))
textalpha = font.render("PyIgnition", True, (255, 255, 255))
text2alpha = font2.render("ExeSoft", True, (200, 200, 200))
temptext = text.copy()
temptext2 = text2.copy()
temptext.set_alpha(0)
temptext2.set_alpha(0)
textpos = ((400 - (text.get_width() / 2)), 250)
textpos2 = (textpos[0] + 110, textpos[1] - 30)
font3 = pygame.font.Font("courbd.ttf", 20)
text3 = font3.render("Beta 2", True, (200, 200, 255), (0, 0, 0))
textpos3 = ((800 - text3.get_width()) - 5, (600 - text3.get_height()))
"""

def on_mouse(event, x, y, flags, param):
    global source
    """
    source.SetPos(pygame.mouse.get_pos())
    """
    # print x, y
    source.SetPos((x, y))
    if event == cv2.EVENT_LBUTTONDOWN or event == cv2.EVENT_RBUTTONDOWN:
        fireworksource.CreateKeyframe(fireworksource.curframe + 1, pos = (x, y), particlesperframe = 1)
        fireworksource.CreateKeyframe(fireworksource.curframe + 2, pos = (x, y), particlesperframe = 0)

def Update():
    global curframe, fireworkcounter, temptext, temptext2
    
    background.Update()

    if curframe == 100:
        backgroundsource2.SetParticlesPerFrame(5)

    fireworksource.SetPos((300 + fireworkdist * math.sin(fireworkcounter), 400 + fireworkdist * math.cos(fireworkcounter)))
    if (curframe > 200) and (curframe % 50 == 0):
        fireworksource.CreateKeyframe(fireworksource.curframe, particlesperframe = 10)
        fireworksource.CreateKeyframe(fireworksource.curframe + 4, particlesperframe = 0)
        firework.Update()
        fireworkblast.SetPos(fireworksource.pos)
        fireworksource.ConsolidateKeyframes()
        #fireworkblast.ConsolidateKeyframes()
    else:
        if curframe % 30 == 0:
            fireworkblast.ConsolidateKeyframes()
        firework.Update()
        fireworkblast.SetPos((1000, 1000))
    fireworkcounter = fireworkcounter + 0.1

    random.seed()
    if curframe == 300:
        bubblesource.SetParticlesPerFrame(1)
    bubbles.Update()
    bubblesource.SetPos((random.randint(0, 800), 600))
    if curframe % 30 == 0:
        bubblesource.ConsolidateKeyframes()

    if curframe > 500:
        if curframe==501:
            cv2.setMouseCallback(windowname, on_mouse)
        fire.Update()
        # source.SetPos(pygame.mouse.get_pos())
        # source.SetPos((200,200))
        if curframe % 30 == 0:
            source.ConsolidateKeyframes()

    if curframe > 400:
        pass
        """
        if curframe > 500:
            temptext = textalpha.copy()
            temptext2 = text2alpha.copy()
        else:
            factor = (float(curframe) - 400.0) / 100.0
            if factor > 1.0:
                factor = 1.0
            alpha = int(factor * 255.0)
            temptext = text.copy()
            temptext.set_alpha(alpha)
            temptext2 = text2.copy()
            temptext2.set_alpha(alpha)
        """
    text_border = 500
    if curframe > text_border:
        col = curframe-text_border
        if col>255: col = 255
        cv2.putText(screen, windowname,(100,300), cv2.FONT_HERSHEY_PLAIN, 3, (col,col,col), 2)
        cv2.putText(screen, windowname,(102,302), cv2.FONT_HERSHEY_PLAIN, 3, (0,col,0), 2)
    curframe += 1

def Redraw():
    #if curframe > 500:
    #    screen.blit(text3, textpos3)
    fire.Redraw()
    #screen.blit(temptext, textpos)
    #screen.blit(temptext2, textpos2)
    background.Redraw()
    firework.Redraw()
    bubbles.Redraw()
    # cv.ShowImage("Particles 'Controlled Eruption' demo", screen)
    cv2.imshow(windowname, screen)

started = True
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    #for event in pygame.event.get():
    #    if event.type == pygame.QUIT:
    #        sys.exit()
    k = cv2.waitKey(30)
    if k == 27:
        sys.exit()
    
    # cv.Zero(screen)
    # screen.fill((0, 0, 0))
    screen[:] = 0

    if started:
        Update()
        Redraw()
    else:
        # screen.blit(starttext, starttextpos)
        pass

    # pygame.display.update()
    #clock.tick(30)
