# Reference: http://www.renpy.org/doc/html/udd.html

init python:
    import random
    import pygame

    # Fish
    class Fish():
        # Intialize
        def __init__(self):
            self.image = Image("fish.png")
            self.active = False
            self.dimensions = [100, 150]
            self.position = [0, 0]
            self.speed = [0, 10]
            self.maxY = 275

        # Creates new
        def createNew(self):
            self.position[0] = random.randrange(0, 8) * 100
            self.position[1] = 0 - self.dimensions[1] # Start off-screen
            self.speed[1] = random.randrange(2, 10)
            self.active = True

        # Game updating
        def update(self, deltaTime):
            if (self.active):
                self.position[1] += self.speed[1]

            if (self.position[1] > self.maxY):
                self.active = False

        # Caught
        def isCaught(self, dogPosition, dogDimensions):
            if (dogPosition[0] < self.position[0] + self.dimensions[0] and
                    dogPosition[0] + dogDimensions[0] > self.position[0] and
                    dogPosition[1] < self.position[1] + self.dimensions[1] and
                    dogPosition[1] + dogDimensions[1] > self.position[1] ):
                self.active = False
                return True

            return False

        # Rendering
        def render(self, renderer, shownTimebase, animationTimebase):
            if (self.active):
                r = renpy.render(self.image, 800, 600, shownTimebase, animationTimebase)
                renderer.blit(r, (self.position[0], self.position[1]))

    # Player - Dog
    class Player():
        # Intialize
        def __init__(self):
            self.image = Image("dog.png")
            self.dimensions = [100, 150]
            self.position = [300, 450]
            self.speed = [100, 10]
            self.grabCounter = 0
            self.grabCounterMax = 20
            self.action = "NONE"
            self.score = 0

        # Handles inputs
        def handleInput(self, action):
            if (self.grabCounter <= 0):
                self.action = action

        # Game updating
        def update(self, deltaTime):
            if (self.grabCounter > 0):
                if (self.grabCounter > self.grabCounterMax/2):
                    self.position[1] -= self.speed[1] * deltaTime
                else:
                    self.position[1] += self.speed[1] * deltaTime

                self.grabCounter -= 1
                if (self.grabCounter == 0):
                    self.position[1] = 450
            else:
                if (self.action == "LEFT" and self.grabCounter <= 0):
                    self.position[0] -= self.speed[0] * deltaTime

                elif (self.action == "RIGHT" and self.grabCounter <= 0):
                    self.position[0] += self.speed[0] * deltaTime

                elif (self.action == "GRAB" and self.grabCounter <= 0):
                    self.grabCounter = self.grabCounterMax

                # Adjust position - can't go off screen!
                if (self.position[0] < 0):
                    self.position[0] = 0
                elif (self.position[0] > 800 - self.dimensions[0]):
                    self.position[0] = 800 - self.dimensions[0]

            self.action = "NONE"

        # Rendering
        def render(self, renderer, shownTimebase, animationTimebase):
            r = renpy.render(self.image, 800, 600, shownTimebase, animationTimebase)
            renderer.blit(r, (self.position[0], self.position[1]))

    # Minigame
    class FishCatcherGame(renpy.Displayable):
        # Initialize
        def __init__(self):
            renpy.Displayable.__init__(self)

            self.player = Player()

            self.debug = []
            self.counter = 0

            self.fish = []
            self.fishCaught = 0

            self.lastStart = None
            self.frameRate = 60

            self.clock = pygame.time.Clock()
            self.countdown = 15
            self.milliseconds = 0

            self.gameover = False

        # Events
        def event(self, event, x, y, shownTimebase):
            # Pressed key events
            if event.type == pygame.KEYDOWN:
                # Up key
                if event.key == pygame.K_UP:
                    self.player.handleInput("GRAB")

                # Left key
                if event.key == pygame.K_LEFT:
                    self.player.handleInput("LEFT")

                # Right key
                if event.key == pygame.K_RIGHT:
                    self.player.handleInput("RIGHT")

            if self.gameover == True:
                return self.player.score
            else:
                raise renpy.IgnoreEvent()

        # Game updating
        def update(self, shownTimebase, animationTimebase):
            delta = self.getDelta(shownTimebase)
            rate = 1000 / self.frameRate
            speedAdjust = delta * rate

            if (self.gameover == False):

                chance = random.randrange(0, 20)
                if (chance == 0 and len(self.fish) < 5):
                    fish = Fish()
                    fish.createNew()
                    self.fish.append(fish)

                removalList = []

                for fish in self.fish:
                    fish.update(1)

                    if (fish.isCaught(self.player.position, self.player.dimensions)):
                        self.player.score += 1

                    if (fish.active == False):
                        removalList.append(fish)

                for fish in removalList:
                    self.fish.remove(fish)

                self.player.update(1)

                if (self.milliseconds > 1000):
                    self.countdown -= 1
                    self.milliseconds = 0

                self.milliseconds += self.clock.tick_busy_loop(60)
                if (self.countdown <= 0):
                    self.gameover = True

        # Rendering
        def render(self, width, height, shownTimebase, animationTimebase):
            self.update(shownTimebase, animationTimebase)
            renderer = renpy.Render(width, height)

            if (self.gameover == False):
                for fish in self.fish:
                    fish.render(renderer, shownTimebase, animationTimebase)

                self.player.render(renderer, shownTimebase, animationTimebase)

                counter = 0
                for debug in self.debug:
                    txt = Text(_(debug), size=10)
                    textRender = renpy.render(txt, 800, 600, shownTimebase, animationTimebase)
                    renderer.blit(textRender, (0, 10 * counter))
                    counter += 1

            # Gameover
            else:
                txt = Text(_("Game Over"), size=40)
                renderer.blit(renpy.render(txt, 800, 600, shownTimebase, animationTimebase), (300, 250))

            # Time remaining and player score text
            txtScore = Text(_("Time: " + str(self.countdown)), size=20)
            renderer.blit(renpy.render(txtScore, 800, 600, shownTimebase, animationTimebase), (700, 0))

            txtScore = Text(_("Score: " + str(self.player.score)), size=20)
            renderer.blit(renpy.render(txtScore, 800, 600, shownTimebase, animationTimebase), (700, 20))


            renpy.redraw(self, 0)

            return renderer

        # Per interaction
        def per_interact(self):
            renpy.timeout(0)
            renpy.redraw(self, 0)

        # Update rate
        def getDelta(self, shownTimebase):
            if self.lastStart is None:
                self.lastStart = shownTimebase

            delta = shownTimebase - self.lastStart
            self.lastStart = shownTimebase

            return delta

# Renpy portal to minigame
screen FishCatcher:
    default fcg = FishCatcherGame()

    add "bgfishing_framed.png"

    add fcg

# Minigame label
label fish_catcher:
    # Hides window and quick menu while in minigame
    window hide
    $ quick_menu = False

    call screen FishCatcher

    # Shows window and quick menu once out of minigame
    $ quick_menu = True
    window show
