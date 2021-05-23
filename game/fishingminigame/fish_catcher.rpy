# Reference: http://www.renpy.org/doc/html/udd.html

init python:
    import random
    import pygame

    class Fish():
        def __init__( self ):
            self.image = Image( "fish.png" )
            self.active = False
            self.dimensions = [ 100, 150 ]
            self.position = [ 0, 0 ]
            self.speed = [ 0, 10 ]
            self.maxY = 275
        # __init__

        def createNew( self ):
            self.position[0] = random.randrange( 0, 8 ) * 100
            self.position[1] = 0 - self.dimensions[1] # Start off-screen
            self.speed[1] = random.randrange( 2, 10 )
            self.active = True
        # createNew

        def update( self, deltaTime ):
            if ( self.active ):
                self.position[1] += self.speed[1]

            if ( self.position[1] > self.maxY ):
                self.active = False
        # update

        def isCaught( self, dogPosition, dogDimensions ):
            if ( dogPosition[0] < self.position[0] + self.dimensions[0] and
                    dogPosition[0] + dogDimensions[0] > self.position[0] and
                    dogPosition[1] < self.position[1] + self.dimensions[1] and
                    dogPosition[1] + dogDimensions[1] > self.position[1] ):
                self.active = False
                return True

            return False
        # isCaught

        def render( self, renderer, shownTimebase, animationTimebase ):
            if ( self.active ):
                r = renpy.render( self.image, 800, 600, shownTimebase, animationTimebase )
                renderer.blit( r, ( self.position[0], self.position[1] ) )
        # render
    # Fish

    class Player():
        def __init__( self ):
            self.image = Image( "dog.png" )
            self.dimensions = [ 100, 150 ]
            self.position = [ 300, 450 ]
            self.speed = [ 100, 10 ]
            self.grabCounter = 0
            self.grabCounterMax = 20
            self.action = "NONE"
            self.score = 0
        # __init__

        def handleInput( self, action ):
            if ( self.grabCounter <= 0 ):
                self.action = action
        # handleInput

        def update( self, deltaTime ):
            if ( self.grabCounter > 0 ):
                if ( self.grabCounter > self.grabCounterMax/2 ):
                    self.position[1] -= self.speed[1] * deltaTime
                else:
                    self.position[1] += self.speed[1] * deltaTime

                self.grabCounter -= 1
                if ( self.grabCounter == 0 ):
                    self.position[1] = 450
            else:
                if ( self.action == "LEFT" and self.grabCounter <= 0 ):
                    self.position[0] -= self.speed[0] * deltaTime

                elif ( self.action == "RIGHT" and self.grabCounter <= 0 ):
                    self.position[0] += self.speed[0] * deltaTime

                elif ( self.action == "GRAB" and self.grabCounter <= 0 ):
                    self.grabCounter = self.grabCounterMax

                # Adjust position - can't go off screen!
                if ( self.position[0] < 0 ):
                    self.position[0] = 0
                elif ( self.position[0] > 800 - self.dimensions[0] ):
                    self.position[0] = 800 - self.dimensions[0]

            self.action = "NONE"
        # update

        def render( self, renderer, shownTimebase, animationTimebase ):
            r = renpy.render( self.image, 800, 600, shownTimebase, animationTimebase )
            renderer.blit( r, ( self.position[0], self.position[1] ) )
        # render
    # Player

    class FishCatcherGame( renpy.Displayable ):

        def __init__( self ):
            renpy.Displayable.__init__( self )

            # Maybe I'll write a sub-class for this stuff
            self.player = Player()

            self.debug = []
            self.counter = 0

            self.fish = []
            self.fishCaught = 0

            self.lastStart = None
            self.frameRate = 60

            self.clock = pygame.time.Clock()
            self.countdown = 10 #Change to 30 for actual game
            self.milliseconds = 0

            self.gameover = False
        # __init__

        def event( self, event, x, y, shownTimebase ):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.handleInput( "GRAB" )
                # Up Key

                if event.key == pygame.K_LEFT:
                    self.player.handleInput( "LEFT" )
                # Left Key

                if event.key == pygame.K_RIGHT:
                    self.player.handleInput( "RIGHT" )
                # Right Key
            # KEYDOWN

            if self.gameover == True:
                return self.player.score
            else:
                raise renpy.IgnoreEvent()

        # event

        def update( self, shownTimebase, animationTimebase ):
            delta = self.getDelta( shownTimebase )
            rate = 1000 / self.frameRate
            speedAdjust = delta * rate

            if ( self.gameover == False ):

                chance = random.randrange( 0, 20 )
                if ( chance == 0 and len( self.fish ) < 5 ):
                    fish = Fish()
                    fish.createNew()
                    self.fish.append( fish )

                removalList = []
                # TODO: There is probably a more Python-idiomatic way to do this
                for fish in self.fish:
                    fish.update( 1 )

                    if ( fish.isCaught( self.player.position, self.player.dimensions ) ):
                        self.player.score += 1

                    if ( fish.active == False ):
                        removalList.append( fish )

                for fish in removalList:
                    self.fish.remove( fish )

                self.player.update( 1 )

                if ( self.milliseconds > 1000 ):
                    self.countdown -= 1
                    self.milliseconds = 0

                self.milliseconds += self.clock.tick_busy_loop( 60 )
                if ( self.countdown <= 0 ):
                    self.gameover = True

                # # TODO: Remove
                # del self.debug[:]
                # self.debug.append( "Debugging" )
                # self.debug.append( "Random: " + str( chance ) )
                # self.debug.append( "Player position: " + str( self.player.position[0] ) + ", " + str( self.player.position[1] ) )
                # for fish in self.fish:
                #     self.debug.append( "Fish position: " + str( fish.position[0] ) + ", " + str( fish.position[1] ) + ", Active: " + str( fish.active ) )
                # self.debug.append( "Delta: " + str( delta ) )

            # Run while game is not over
        # update

        def render( self, width, height, shownTimebase, animationTimebase ):
            self.update( shownTimebase, animationTimebase )
            renderer = renpy.Render( width, height )

            if ( self.gameover == False ):
                for fish in self.fish:
                    fish.render( renderer, shownTimebase, animationTimebase )

                self.player.render( renderer, shownTimebase, animationTimebase )

                counter = 0
                for debug in self.debug:
                    txt = Text( _( debug ), size=10 )
                    textRender = renpy.render( txt, 800, 600, shownTimebase, animationTimebase )
                    renderer.blit( textRender, ( 0, 10 * counter ) )
                    counter += 1

            else: #Gameover
                # Temporary
                txt = Text( _( "Game Over" ), size=40 )
                renderer.blit( renpy.render( txt, 800, 600, shownTimebase, animationTimebase ), ( 300, 250 ) )

            txtScore = Text( _( "Time: " + str( self.countdown ) ), size=20 )
            renderer.blit( renpy.render( txtScore, 800, 600, shownTimebase, animationTimebase ), ( 700, 0 ) )

            txtScore = Text( _( "Score: " + str( self.player.score ) ), size=20 )
            renderer.blit( renpy.render( txtScore, 800, 600, shownTimebase, animationTimebase ), ( 700, 20 ) )


            renpy.redraw( self, 0 )

            return renderer
        # render

        def per_interact( self ):
            renpy.timeout( 0 )
            renpy.redraw( self, 0 )
        # per_interact

        def getDelta( self, shownTimebase ):
            if self.lastStart is None:
                self.lastStart = shownTimebase

            delta = shownTimebase - self.lastStart
            self.lastStart = shownTimebase



            return delta
        # updateRate
    # FishCatcherGame

screen FishCatcher:
    default fcg = FishCatcherGame()

    add bgfishing

    add fcg

label fish_catcher:
    # Hides window and quick menu while in minigame
    window hide
    $ quick_menu = False

    call screen FishCatcher

    # Shows window and quick menu once out of minigame
    $ quick_menu = True
    window show

    #return
    # Have to jump back to whereever it was called from
