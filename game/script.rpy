# Chacter declarations
define Violet = Character("Violet", who_color="#D38CFD")
define Unknown = Character("???")
define Vincent = Character("Vincent", who_color="8CFFBC")
define Vincent_Unknown = Character("???", who_color="8CFFBC")
define Teacher = Character("Teacher", who_color="FF2424")
define narrator = Character(None, what_italic=True)
define Student1 = Character("Student #1", who_color="00FFF4")
define Student2 = Character("Student #2", who_color="1DFF00")
define Sophia = Character("Sophia", who_color="FFC2FF")

# Default variable values
default library = True

# Character images
image violet = im.Scale("violet.png", 300, 600)
image violetFlip = im.Flip(im.Scale("violet.png", 300, 600), horizontal = True)

image teacher = "teacher.png"
image sophia = im.Scale("sophia.png", 325, 625)

image student1 = im.Scale("schoolboy.png", 350, 600)
image student2 = im.Scale("schoolgirl.png", 350, 600)
image vincent = im.Scale("vincent.png", 300, 600)
image vincentFlip = im.Flip(im.Scale("vincent.png", 300, 600), horizontal = True)

image mysteryman = im.Scale("mysteryman.png", 450, 450)

# Backgrounds
image bgroom = "bgroom.png"
image bgclassroom = "bgclassroom.jpg"
image bgcourtyard = im.Scale("bgcourtyard.jpg", 1280, 720)
image bgroad = "road.jpg"
image bgdesk = im.Scale("desk.jpg", 1280, 720)
image bgbookstore = im.Scale("bookstore.png", 1280, 720)

# VFX
image explosion = "explosion.png"

transform halfleft:
    xalign 0.15 yalign 1.0

transform halfright:
    xalign 0.85 yalign 1.0


screen fish_button:
    imagebutton:
       idle "btn_minigame.png"
       hover "btn_minigame_highlighted.png"
       xalign 0.5
       yalign 0.5
       action Function(renpy.call, label="fish_catcher")


# Splash screen
label splashscreen:
    scene black
    with Pause(1)

    show text "Feel Feels Production presents..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return

# Start of game, can change for debugging purposes
label start:
    jump scene1

# SCENE 1: CLASSROOM
label scene1:
    scene black
    play music yourname fadein 3.0
    "Violet is dreaming. His dreams were usually of nothing important—just human, mundane events."
    "Listening to music in his room, walking the streets of his old neighborhood, and other things like that. Pretty normal."
    "These types of dreams may sound boring, but the physical and emotional sensations that hit Violet during these dreams makes him want to hold on to these imagined experiences for as long as he could."
    "In his dream, brief scenes fly by while he watches his personal stories as a 10-second protagonist."
    "Violet watches as his mom cuts some cake for him. Used candles lay discarded on the sides of the plate, with blackened tips and frosting on the lower halves."
    "Someone’s birthday? His birthday? He feels that foreign, yet familiar emotion of anticipation bubbling in his chest."
    "He feels special. Birthdays are special. He hasn’t felt this in a while..."
    "..."
    "Violet is suddenly lying down in a dark field, looking up at the stars. His back is wet from the cold grass, but it feels nice."
    "He let his weight sink into the grown below him. The dead silence put his usually-loud mind at peace."
    "The stars watch Violet from above as he stares back at them. If only he could stay like this for just a little longer..."

    Vincent_Unknown "Hey."
    "Riding a bike down a sidewalk on a sunny day..."
    Vincent_Unknown "Hey, wake up."
    "Someone’s voice? It sounded like Vincent..."
    Vincent "HEY VIOLET!"

    play sound whack
    "(SMACK)" with vpunch

    Violet "OW!"
    "Yup, that was Vincent’s voice, and unfortunately, his hand as well. Across the back of Violet’s head."

    scene bgclassroom
    show violet at halfleft
    show vincent at halfright
    play music silly fadein 3.0

    Vincent "Sleep well?"
    Violet "Ughh stop talking. What do you want?"
    Vincent "So do you want me to not talk or should I answer that question?"
    Violet "You’re stupid. And you’re talking anyways."
    Vincent "Ah, well, I guess you’re right."
    Vincent "Now that I’ve passed the point of no return, I just wanted to let you know that class starts in a few minutes."
    Violet "So you’ve denied me a few minutes of peaceful slumber?"
    Vincent "You poor kid. Come on, try to look at least a bit more lively."
    Violet "Listen, I’m tired."
    Vincent "So I’m guessing you stayed up too late playing that dating sim?"

    menu:
        "...":
            Vincent "I’m kidding, don’t be mad."
            Violet "I’m not."
            Vincent "You sound mad."
            Violet "I hate you."
            Vincent "See? Mad."

        "No, I was actually getting busy with your sister.":
            Vincent "Hey, chill."
            Violet "You started it."
            Vincent "Truce?"
            Violet "Truce."
            "..."
            Vincent "My sister is off-limits."

        "Yeah.":
            Vincent "Wow, you’re really just gonna admit it?"
            Violet "I’ve got no reputation to lose."
            Vincent "Well I admire your confidence, good sir."

    Violet "You’re actually stupid."
    Vincent "Maybe. Did you see that new episode of {i}To the Moon and Back{/i}?"
    Violet "Yeah, I did! Let’s talk about it later because I need at least an hour."
    Vincent "So I’m guessing you liked it then?"
    Violet "Of course!"
    Vincent "You’re always so shy and quiet until I get you talking about that show."
    Violet "Oh, shut up. What are we even doing in history today?"
    Vincent "Some Pre-War Era stuff."
    Vincent "Back when people fought over whether or not the moon was flat or if vaccines gave you autism. Dumb shit like that."
    Vincent "At least it’s funny to read about the stuff they argued about."
    Violet "I feel like they still had it better back then..."
    Vincent "Hey, man. Just let me cope."
    Violet "{i}(sighs){/i} Well, I guess there’s nothing wrong with that... coping..."
    Vincent "Hey, don’t sound so gloomy."
    Violet "..."

    "Violet curses himself. He felt like he always ruines the mood of conversations with his own dark mood."
    "He at least tries to be a little more cheerful."
    "And even then, trying is different from actually being successful..."

    Vincent "Got any plans after school?"
    Violet "Never."
    Vincent "Wonderful. Do you wanna go to that new bookstore that just opened?"
    Violet "Why? So you can throw away your paycheck on those stupid comics?"
    Vincent "Hey, let me keep my hobbies in peace."

    menu:
        "Sure, fine, I’ll come.":
            Vincent "Alright sweet. Me me there at 5?"
            Violet "Sounds good."
            Vincent "Looking forward to it!"
            $ library = True

        "No, I’m good.":
            Vincent "Are you sure?"
            Violet "Yeah, I’m not really feeling up to it."
            Vincent "That’s okay man. I’ll always be here if you wanna hang out."
            $ library = False

    stop music fadeout 3.0
    play sound bell

    Vincent "Alright, talk soon?"
    Violet "Yeah, I’ll see you later..."

    scene black
    with Pause(3)
    jump scene2

# SCENE 2: HISTORY CLASS
label scene2:
    scene bgclassroom with fade
    play music school fadein 3.0

    show violet at halfleft

    "Violet seriously didn’t have the energy to pay proper attention to class."
    "Luckily, it's history. His teacher makes his students’ lives simultaneously easier and harder by not lecturing on anything that wasn’t on the prior night’s reading."
    "They didn’t really have to pay attention, but they had to last an entire hour in that classroom..."

    show teacher at halfright

    Teacher "Alright class, today we’ll be studying the Pre-War Era."
    Teacher "You all did the reading last night, so we’ll just be going over that today."
    Violet "{i}God, if you’re real, just put me in a coma.{/i}"
    Teacher "Now, as we know, before the War, poverty was rampant across our nation."
    Teacher "But through our government’s expansion of global influence and the creation of protectorates, global trade has increased in efficiency by more than ten-fold."
    Teacher "Poverty has been cut to historic-low levels due to our increased wealth and power. Our Department of Life and Charity has overseen all of this great work over the past fifty years."
    Violet "{i}Why do we even need to learn about this? Seriously, if I have to hear the word “poverty” one more time, I’m gonna kill somebody.{/i}"
    Violet "{i}Plus, I bet half this shit is DLC propaganda anyways.{/i}"
    Teacher "Can someone tell me what they know about the War? It can be anything, really."

    "(Silence)"

    Teacher "Anyone? Feel free to speak out."

    "(Silence)"

    Violet "{i}I don’t know what he expects from us. I feel like no matter what I say, it’ll be the wrong thing.{/i}"
    Violet "{i}You won’t find too many people who are actually excited to talk about this type of stuff.{/i}"

    "..."

    hide violet

    show student1 at halfleft

    Student1 "Can I answer?"
    Teacher "Sure!"
    Student1 "It’s basically when our original Departments of Defense, Labor, and Commerce united to stage a military coup."
    Student1 "That’s where that acronym DLC comes from. They seized power just to expand our global military influence and power."
    Teacher "Well, not exactly."
    Teacher "They more so fought to protect our nation’s interests, foreign and domestic. Poverty has been nearly eliminated within our borders after our rightful regime took power."
    Teacher "The average citizen is much better off now as compared to fifty years ago."
    Student1 "I mean… I know that’s what we read about, but I think that’s just because of the Draft."
    Student1 "Everybody knows that the Draft is based off income. You haven’t “eliminated poverty,” rather you basically just conscripted all the poor people and sent them to die."

    "(Students whisper amongst themselves)"

    Teacher "Now, where did you learn that from?"
    Teacher "We’ve always taught you that that the Department of Life and Charity cares for its citizens!"
    Student1 "I mean, I can think for myself, right?"
    Student1 "It doesn’t take much to see how poverty was basically an excuse used to increase the military’s power."

    hide teacher
    show student2 at halfright

    Student2 "Hey, relax."
    Student1 "What? I’m not saying anything wrong."
    Student1 "Am I seriously the only one who thinks that it’s unacceptable how the government can just send you to die if you’re suddenly not making enough money?"
    Student1 "Who’s stopping them from setting that income threshold higher?"
    Student1 "And then the rest of the world has the nerve to commend our nation and how “successful” we are based on these broken global rankings!"
    Student1 "We’re all just wage slaves for a government that doesn’t give a shit about us."

    "(The class starts speaking louder amongst themselves)"

    hide student2
    show violetFlip at halfright

    Violet "{i}We always have to have one smartass huh. I’m sure he thinks he’s real clever.{/i}"

    "Violet figured out a while ago that the best way to cope was to hate these types of people. They probably thought they were so much better than everyone else, speaking out as they do."
    "Little did they know that everyone shared their basic-ass opinions."

    Violet "{i}Arrogant bastard.{/i}"

    "Even though Violet doesn’t speak a word of what he was thinking, he feels guilty for a brief moment."
    "Unfortunately, he notices that feeling. He pushes the uncomfortable feeling to the side, trying to forget about it."
    "There's an uncomfortable cognitive dissonance that comes from hating someone that you completely agree with..."
    "Violet just wanted to make himself feel better. There’s nothing wrong with that, right? Why does he always have to feel so uncomfortable?"

    hide student1
    show teacher at halfleft

    Teacher "Class, settle down."
    Violet "{i}At least after today, he’ll learn how to hold his tongue. And as expected, it always ends in...{/i}"
    Teacher "Young man, I’ll speak with you after class."
    Violet "{i}There you go. Godspeed, dipshit.{/i}"

    "Violet tries not to think about what’ll happen to this kid and his family, eventually realizing that he couldn’t even remember his name. They’ve been classmates for two to three years."
    "Oh, well."

    stop music fadeout 3.0
    scene black
    with Pause(3)
    jump scene3

# SCENE 3: WALKING HOME
label scene3:
    scene bgcourtyard with fade
    play music april fadein 3.0
    show violet

    "Violet sits on a bench outside his school, watching as his classmates exit the gates and into their lives outside of school."
    "Violet forget that each of his classmates lead lives different from his own."
    "Well, probably not too different. Everyone likely shares Violet’s same worries, same minimal aspirations, desires to just make it through life safety, etc."
    "But maybe that girl over there was into some boy band that Violet’s never heard of. Maybe that guy walking with his friends plays piano in his spare time."
    "Maybe the girl walking towards him, Sophia, shared some of his own hobbies and interests."
    "Thinking about what his classmates look forward to in their personal lives makes Violet oddly happy."

    show violet at halfleft
    show sophia at halfright

    Sophia "Enjoying the warm weather?"
    Violet "Yeah. I’m not in any rush to get home, so I just thought I’d stay here for a while."
    Sophia "Well, I’m probably gonna head out now. Wanna join me?"
    Violet "Alright, sure."

    scene road with fade
    show violet at halfleft
    show sophia at halfright

    Sophia "How was physics? I thought it was pretty interes—"
    Violet "It was pretty boring."
    Sophia "OH YEAH it was so boring! Math seriously isn’t my thing. Mr. Claudius’s voice seriously just—"
    Violet "This class goes way too slow. I think I might study math in the future, so this pace is just pretty slow for me."
    Sophia "So true! I get pretty good grades in math, but uh... I think I just might be a slow learner."
    Sophia "If you uh... don’t mind... umm..."
    Violet "Hm?"
    Sophia "{i}(quiet) Come on, Sophia. This is the perfect opportunity.{/i}"
    Sophia "Well... maybe you could {i}(whispers){/i} tutor me someti—"
    Violet "Whoa, Sophia, you look really red. It’s pretty hot out, did you drink enough water?"
    Sophia "Oh yeah haha, I think I’m just dehydrated."

    "Violet takes out some bottled water."

    Violet "Here, take this."
    Sophia "Oh, thank you!"

    "Sophia drinks the entire bottle at an alarming speed." # sound effect?

    Sophia "Ahem. {i}(takes a deep breath){/i} Hey, Violet?"
    Violet "Yeah?"
    Sophia "We’ve been friends for a pretty long time, right?"

    "Sophia has this determined look on her face. Violet was a little confused."
    "Did something happen? Is something wrong?"
    "Well, her expression is kinda cute, so he doesn’t have any complaints."

    Sophia "Okay, so I should feel confident asking. Could you tutor me in physics sometime?"

    "Sophia’s cheeks are red again. Violet was a little concerned, because that was his last bottle of water."

    Violet "{i}Oh God, what if she passes out? What was she asking about again? Math tutoring?{/i}"
    Violet "Uh... yeah sure."
    Sophia "Really?"

    "Sophia sounds excited."

    Violet "I mean, yeah. I don’t see why not."
    Violet "We hang out a lot anyway, right? I don’t mind helping a friend out."
    Sophia "{i}(coughs){/i} a friend..."

    "..."

    Violet "Hm, it sure is beautiful out, huh?"
    Sophia "Yeah. {i}(sighs){/i} Your eyes really shine in this sunlight..."

    "..."

    Violet "Hey, thanks. No one’s ever said that to me before. You’re a really nice friend to me, Sophia."
    Sophia "{i}(quiet){/i} I’m really shooting my shot for one dense motherfucker."
    Violet "Huh? Did you say something?"
    Sophia "Something?"
    Violet "Never mind."

    play music missionimpossible fadein 3.0
    play sound gunshot3 volume 0.1

    "Suddenly, they hear gunshots. Then yelling. That first yell was a man, possibly a middle-aged adult."
    "Then they hear more people shouting."
    "These shouts sound angry, but Violet could hear that familiar tone of fear buried within their voices."
    "Maybe it is more accurate to say that they were screaming?"
    "(More gunshots)"
    "Violet doesn’t understand why the resistance couldn’t just fight back a little quieter."
    "He often laid awake at night, thinking about the way that those yells sounded way more forced than genuine."
    "Maybe yelling is cathartic for them? Violet just wished that their only hope could at least sound a little braver..."
    "The shouting and gunshots grow noticeably closer."
    "The piercing sound of magazines being emptied makes it impossible for Violet to think straight."

    stop sound
    play sound gunshot1

    "There’s always a window of time. At the moment, Violet and Sophia are safe from being hit in the crossfire."
    "But this won’t last long. Once they miss that window, it’s near-impossible to escape."
    "Violet has lost enough classmates to know this. He knows that he should run away, and yet—"

    Sophia "Violet, we have to go."

    "Violet can’t feel his legs. Just like everyone else, he’s been in this situation too many times."
    "The vast majority will default on running away between their instinct of fight or flight."
    "In the past, he has too. But this time, it was different. This time..."

    menu:
        "Violet feels an unexplainable urge to run towards the gunfire.":
            "He couldn’t explain this urge, not even remotely to himself."
            "Maybe it’s like one of those feelings you get when you stand on a tall building and feel a strange urge to throw something valuable off the top?"
            "The urge to just do the most destructive thing in that moment?"
            "No, it’s definitely something more than that."
            "Violet is angry."
            "He’s angry that it’s been ingrained in him and his friends that gunshots mean running."
            "That compliance means safety."
            "That to make yourself seen is to put yourself in danger."
            "He wants to run towards the gunfire because he knows that his reality wants him to do the opposite."
            "And he’s damn tired of staying in his lane."

            Violet "Sophia, run."

            "Violet is angry."

            Sophia "WHAT?"

            "He can’t take it anymore."

            Violet "Just run!"

            hide sophia
            play sound gunshot1

            "Violet sprints towards the gunfire as it gets louder and louder in his ears. He could feel the sides of his head throbbing."
            "He didn’t know where he was. Violet recognizes his surroundings but he couldn’t think straight enough to navigate these roads."
            "He stops for a moment to catch his breath, but he realizes that he can’t breathe any slower."

            Violet "Oh, God. I’m hyperventilating."

            "Why did he do this again? Was Sophia doing okay? How did he get here?"
            "Violet sees about six men with guns sprinting across the street, away from something."
            "He hears a lot more voices than what would belong to six people. Violet couldn’t tell where those voices were coming from."
            "His feet are planted on the ground and refuse to move."

            Violet "Fuck, this was a mistake."
            "Violet turns around and sees a man in a DLC military uniform pointing a gun at him."

            Violet "Wait, I’m not—"

            scene black
            play sound gunshot2

            "Violet collapses before he hears the bang."
            "Everything goes black."
            "..."

            stop music fadeout 3.0
            with Pause(3)
            jump credits

        "Violet can’t help but freeze up.":
            Sophia "VIOLET!"
            Violet "Hmm?"

            play sound gunshot1

            Sophia "WE HAVE TO GO!"
            Violet "I’m sorry?"

            "Violet can hear his own heartbeat, almost as loud as the gunshots."

            Sophia "Good lord—"

            "Sophia grabs Violet’s hand and sprints into an alleyway."
            "They make frequent turns into alleyways and streets that Violet doesn’t recognize."
            "Even though his surroundings are foreign to him, he isn’t too nervous."
            "Sophia seems confident enough in leading him to safety, so he could trust her with his life."
            "I mean, it’s not like he has any other choice."

            Violet "{i}Why am I always the person leaning on someone else...{/i}"
            Violet "{i}I need to learn to hold my own sometimes...{/i}"

            "They reached a street that Violet vaguely recognizes."
            "Everything on this street is run down and abandoned, which ironically, makes it the safest."
            "Sophia leads the two into what used to be a convenience store so they can stop to catch their breath."
            "Violet had no idea how long they were running for."

            Sophia "Hey... are... you... oh my god, my sides..."
            Violet "I’m... ugh..."

            "They took a few minutes to learn how to breathe normally again."
            "Violet could still hear the fast, rhythmic thump of his heartbeat."
            "The shelves were scarcely stocked and all the items were probably expired."
            "It’s too dark. There’s a back door in the corner of the store that makes Violet a little nervous."
            "Violet doesn’t feel out of breath anymore, but for some reason, his heartbeat wouldn’t slow down."

            Sophia "Hey, you’re still breathing pretty heavily. Are you...?"
            Violet "I don’t... know..."
            Sophia "Hey listen, trust me. We’re 100\% okay now. There’s absolutely no one here, and nothing is gonna happen to us."

            "Violet takes some deep breaths. After a moment, his breathing returns to normal."

            play music satie fadein 3.0 volume 3.0

            Sophia "Violet, are you okay?"
            Violet "I... uh, yeah. I think so. I am."

            "A few moments of silence passed."

            Sophia "I... never know what to say when this happens. I’m sorry."
            Violet "Why are you sorry?"
            Sophia "I don’t know..."
            Violet "They should be the ones fucking apologizing."
            Sophia "Violet..."
            Violet "God fucking dammit. I remember just earlier when I was telling you that I want to study math after high school."
            Violet "I told you that, but it’s so hard to just {i}want{/i} things that are in the miserable fucking future!"
            Violet "I look into the past and it’s painful, and I look into the future and it’s so damn bleak."
            Sophia "I—"
            Violet "How can our teachers expect us to take standardized tests and be good at school sports and work towards a career?"
            Violet "How are we expected to focus on our future when it feels like the world is an absolutely shit place to be?"
            Violet "Oh yeah, I’ll make goals for a future that I have little to no hope for."
            Sophia "Violet, take it easy. Slow down. We’re okay."

            "..."
            "..."

            Violet "{i}(quietly){/i} Sophia?"
            Sophia "Yeah?"
            Violet "I’m not crazy for having these feelings, right? I’m not weaker than everyone else?"
            Sophia "You’re not. You’re definitely not."
            Violet "Okay... okay good..."
            Sophia "It’s fucked up. That’s all. You’re right about everything."

            "..."

            Sophia "Just... one day at a time. We’ll take it step by step together. That’s all I can really say."
            Sophia "One day at a time is all we can expect ourselves to do."

            "..."

            Sophia "Violet, I really care about you."
            Violet "I care about you too."

            "..."

            Sophia "Can I walk you home?"
            Violet "Yeah. Thanks for everything."

            "..."

            Violet "{i} She’s really amazing, huh. {/i}"

            stop music fadeout 3.0
            scene black
            with Pause(3)
            jump scene4

# SCENE 4: AT HOME
label scene4:
    scene bgdesk with fade
    play music mitsuha fadein 3.0

    "..."

    Violet "{i}Damn, I told Sophia that I was into math, but that’s just because Vincent told me that girls are into smart guys.{/i}"
    Violet "{i}And then she asked me to tutor her! Lying is really not the way, huh.{/i}"
    Violet "I really just signed myself up for twice the amount of work if I want Sophia to like me back."
    Violet "{i}Oh fuck, what if I have to study math in college? I’ll actually die...{/i}"

    "..."

    Violet "Hm..."
    Violet "What the hell is Cantor’s diagonalization? That sounds fake."
    Violet "Hmmm..."
    Violet "Halting problem? Also fake."
    Violet "Hmmmmmmmm..."
    Violet "Godel’s incompleteness theorem??"
    Violet "Motherfucker needs to complete the damn theorem before I can use it. Definitely not real."

    "..."

    Violet "I’m tired of this shit! I’m tired. Maybe I just need to get up and walk around."

    scene bgroom with fade
    show violet

    Violet "These things are getting kinda dusty..."
    Violet "Grandpa took pretty good care of these. Compared to me, he probably took way better care of these figurines when he was 18."

    "COOL DESK STUFF"
    # TODO: Change to button image to a game controller, don't have text - static screen with a proceed button to progress game
    show screen fish_button

    Violet "God, I’ve had these for so long..."
    Violet "As someone who bullies Vincent for having his interests, I’m a damn hypocrite."
    Violet "I mean, this isn’t even anywhere near my generation. At least he stays up to date on whatever comics he’s into."

    "..."

    Violet "I’m so fucking weird..."

    "..."

    hide screen fish_button

    # TODO: Why changing from normal to italics? Maybe all italics?
    Violet "God, why do I feel so uncomfortable? What exactly is wrong with owning these?"
    Violet "Why would I rather die than have anyone from school see any of this shit?"
    Violet "{i}This all feels... meaningless. It’s just pathetic. Seriously.{/i}"
    Violet "{i}I don’t even think I have a future and I’m still worried about my classmates finding out that I have this collection.{/i}"
    Violet "{i}The future...{/i}"
    Violet "{i}Life goes by way too fucking fast. I’m really at the crossroads, where I’m just coming out of my childhood and I’m about to enter adult life. This is too much...{/i}"
    Violet "{i}I’m already eighteen and I feel like I missed out on being a kid. This is fucked.{/i}"
    Violet "{i}I’m graduating soon and I’m never going to see classmates ever again.{/i}"
    Violet "{i}These are the people I grew up with, and I feel weirdly attached and distant to them at the same time.{/i}"
    Violet "{i}They would never know or even really care about my dumb hobbies, so why do I care if they really know me? It’s not like I’ll miss them.{/i}"
    Violet "{i}If I care so much, then does that mean I’m going to miss them? Why?{/i}"
    Violet "{i}I guess, in a way, the past is safer even if it wasn’t the greatest. I might actually miss my classmates.{/i}"
    Violet "{i}I’ll just miss my childhood, honestly.{/i}"
    Violet "{i}Maybe I’m still holding onto these figurines because I wanna keep being a kid.{/i}"

    "..."

    Violet "{i}I don’t know who these characters are... but for some reason, owning these make me kinda happy...{/i}"

    "..."

    Violet "{i}I really don’t know why. These feel so small in the face of everything else.{/i}"
    Violet "{i}But... maybe that’s why I like these. It’s something that I can actually control.{/i}"
    Violet "God, why am I thinking about this shit?"

    "{i}Maybe it was the mere fact that his collection makes him happy. It’s small, but it makes him happy.{/i}"
    "{i}That's really the only reason he needs to hold onto these figurines for as long as possible.{/i}"
    "{i}Maybe he just needs to stop thinking once in a while and just enjoy what he's got. Forget about the big stuff...{/i}"

    Violet "{i}When everything seems so big, maybe I just like the fact that I own these small few items that I can hold in the palm of my hand.{/i}"
    Violet "{i}I think... that’s good enough.{/i}"
    Violet "{i}I can’t really hold the future in the palm of my hand... haha...{/i}"

    "..."

    if library == False:
        Violet "{i}I’m tired. I’m going to bed. Another day, same as before.{/i}"
        Violet "{i}I can’t tell if that’s good or bad.{/i}"

        stop music fadeout 3.0
        scene black with fade
        with Pause(3)
        jump credits

    else:
        menu:
            "It’s getting late, I should probably get going.":
                stop music fadeout 3.0
                scene black with fade
                with Pause(3)
                jump scene5

            "I’m going to bed. There’s no point to any of this.":
                "{i}Sorry, Vincent. Maybe next time.{/i}"

                stop music fadeout 3.0
                scene black with fade
                with Pause(3)
                jump credits

# SCENE 5: BOOKSTORE
label scene5:
    scene bgroad with fade
    play music ending fadein 3.0

    "Civilians that didn’t have a job in the government aren’t allowed to own cars. Of course, you can own a car if you are rich enough and know the right people."
    "The DLC claims that this policy was to reduce carbon emissions long-term, but good chunk of the planet isn’t habitable anymore due to climate change. Too little too late."

    show violet

    "Violet tries to see the positive in being forced to walk everywhere, since he otherwise wouldn’t have the opportunity to slow down and notice the smaller details of his town."
    "That said, the streets aren’t really the safest either. You can’t have it all..."
    "His town changes too often. His younger self would have a hard time trying to navigate 18-year-old Violet’s roads."
    "Little Violet would eventually realize that whatever store he was looking for had been shut down and replaced by some DLC-sanctioned bullshit."
    "As he walks by a small building for this generic insurance company, he remembers looking forward to seeing his grandmother every Friday after school in her bakery."
    "That DLC building smelled a little too nostalgic for Violet’s liking."
    "Violet laughs to himself as the emotions that remind him of better days collide with a deep hatred. The duality causes a really weird feeling."
    "He’d be able to use this as an example of juxtaposition without his English teacher telling him that he’s using it wrong."
    "'They have to be right next to each other...'"
    "Well, this is as 'next to each other' as you’re gonna get. Hm, does it count if they’re overlapping?"
    "Does on top of each other count as being next to each other? Whatever."
    "Eventually, Violet makes it to the bookstore Vincent told him about. He walks inside and is hit with the smell of burnt paper."
    "He had heard in the news that a bookstore had been burned down in an 'accident' and rebuilt within a little less than a month."
    "The story was oddly inspiring. Is 'that' this store?"

    scene bgbookstore with fade
    show violetFlip at halfright
    show vincentFlip at halfleft

    Vincent "Hey, Violet!"

    "Vincent waves to Violet from across the room. The store is neatly lined with parallel shelves of new books, each shelf labeled by genre."
    "Unsurprisingly, Vincent was over by the comics. Violet quickly joins him, trying not to let his eyes linger at the romance section."
    "Vincent would bully him to death."

    Vincent "How’ve you been?"
    Violet "Um...alright."
    Vincent "I saw you got to walk home with Sophia. Good job, man."
    Violet "Oh, shut up. You know she doesn’t like me back."
    Vincent "Ah, but you have great potential to charm her straight into your arms, my friend."
    Vincent "Listen to me. I know exactly what women like."
    Violet "Uh huh. What’s your body count?"
    Vincent "My what?"
    Violet "..."
    Vincent "I haven’t killed anyone?"
    Violet "..."
    Violet "You have negative ethos right now."
    Vincent "Whatever, man. All I’m saying is that I am a man of action, and you are of inaction. I must guide you, young one."
    Violet "You’re actually so dumb."
    Vincent "Violet, Violet, Violet. Women like a calm, collected man. Treat me like you would Sophia for a moment."
    Violet "HUH??" with vpunch
    Vincent "Actually, forget it. I could never forgive myself if you fell for me."
    Violet "..."
    Violet "Okay."

    "Vincent picks up a comic with a boy on the cover. He wore a big smile and holds a comically large sword."

    Vincent "I remember this one. I think I read it at the beginning of the school year."
    Vincent "Hm, funnily enough, the different comics I’ve read are pretty much the most major events of this year. Everything else has felt so dull."
    Violet "Yeah, I guess when you put it into perspective, not much has really happened."
    Vincent "I mean, I guess that’s not a bad thing. Either way, comics make me happy. It’s whatever."
    Violet "Hm, that was almost a smart thing you just said."
    Vincent "Almost? I recite wisdom on the daily."
    Violet "And you ruined it. Back to normal Vincent."
    Vincent "Out of curiosity, because obviously I already know, why did I say something smart?"
    Violet "I don’t know, man. I’ve been thinking about this a lot these days. Looking back at my entire life, I feel like I haven’t really done anything."
    Violet "I worked really hard in school, but I definitely didn’t really get any enjoyment from that."
    Violet "It was just something that I had to do."
    Violet "Besides exams, there haven’t really been any major events of this year, or really, of the past few years."
    Violet "Everything has just been an investment for a future that I don’t feel too excited about."
    Vincent "I feel that..."
    Violet "That said, I guess this past year was fun. I spent time with friends, my mom taught me how to bake apple pie this one time, and even getting addicted to dating sims was fun in a way."
    Vincent "I kinda get it. But isn’t that obvious? Fun things are fun?"
    Violet "I don’t know, it feels bigger than that. Every headline is a reminder of how fucked the world is, and it’s hard to just be a person sometimes."
    Violet "I guess once in a while, it’s nice to just focus on the smaller things and embrace the things that make me who I am."
    Vincent "Oh yeah, I bet you have to focus on smaller things ahaha..."
    Violet "I actually hate you."
    Vincent "You’re a wise man, Violet. Ladies love wisdom."
    Violet "If that’s true, then I feel kinda bad for you."
    Vincent "Violet, you remind me so much of the protagonist in {i}Under a Sunset{/i}."
    Violet "Wait, you read that?"
    Vincent "Wait, {i}you{/i} read that? 'Mr. Too Superior to Read Comics' read a comic?"
    Violet "Well, I uh—"
    Vincent "What did you think of the ending?"
    Violet "Okay, I actually cried. I’m not usually someone who cries at stories, but that one really got me—wait, why did you read a {i}romance{/i} comic?"
    Vincent "I like the author and wanted to see what he could do with romance. He usually stays in the action genre, but switched it up for some reason."
    Violet "Well, I’m glad he did, because he’s a genius. The way he made the moon a symbol of a steady and persistent love was so good."
    Violet "It sounds lame when I say it, but I was so into it. I tear up every time I see the moon in real life now."
    Vincent "Dude, I think the moonshine shit was just an art flex. Light and shadows, you know?"
    Violet "..."
    Vincent "Either way, it was really cool. I liked the stuff he did when he went into the protagonists’ backstories for a few chapters."
    Vincent "It made the stuff happening in the present feel a lot more meaningful."
    Vincent "I reread it again and noticed so much more that I didn’t pick up the first time around."
    Violet "I KNOW–ahem. Yeah, the way he wrote the characters was so well thought out. He avoided so many cliches that I got bored of, so it was pretty refreshing."
    Vincent "I like seeing you like this, man."
    Violet "Huh?"
    Vincent "I don’t know, the way you talk about these types of things makes me kinda happy."
    Vincent "It gives me hope when a moody guy like you can get so passionate about romance stories. You’re a cool guy to hang out with."
    Violet "You’re an... interesting guy. You go from insightful to stupid way too quickly."
    Vincent "Hey, I said something nice so now it’s your turn."
    Violet "You’re... insightful from time to time."

    "..."

    Vincent "See, you bully me like this yet choose to hang out with me. Speaking of which, I want to ask you something."
    Vincent "Break is coming up, so do you wanna go camping? Honestly you don’t really seem like the type, but it could be fun."
    Violet "Yeah, honest I think I'd really enjoy that."
    Vincent "That sounded oddly enthusiastic. Am I talking to the real Violet?"
    Violet "Uh, yeah. I don’t know, for some reason I was always into the idea of going camping."
    Unknown "Ah, I remember going camping when I was your age."

    "A middle-aged man browsing the section behind the comics stands turned away from Violet and Vincent, looking through the nonfiction books that filled the shelves."
    "He remains turned away as he spoke to the boys."

    Unknown "My friends and I visited this forest with an open field that gave a beautiful view of the clear night sky."
    Violet "That sounds wonderful."
    Unknown "It really was. This is the age where you should be going after experiences like these. Enjoy your youth a bit."
    Violet "Easier said than done."
    Vincent "Well, we {i}are{/i} going camping. He’s right, we should enjoy our youth a bit more."
    Violet "Yeah, okay. I think camping will be fun. Sir, what’s this place you went to with your friends?"
    Unknown "Well, unfortunately I believe that entire acre of land was repurposed for a prison."
    Vincent "Awe..."
    Vincent "That’s unfortunate."
    Unknown "Yeah, it was pretty special."
    Violet "Ugh, shit like that makes me hate our government more and more."
    Violet "Sometimes I can get used to it and not care so much, but for some reason small stuff like that makes me angry."
    Vincent "{i}(whispering){/i} Violet, be careful. You don’t know who this is."
    Violet "Alright, fine."

    "The man turns around to face Violet and Vincent."

    show mysteryman

    Unknown "Don’t worry young man, I share the feeling."
    Unknown "If you think your childhood was ruined by the DLC, then try talking to the people a generation above you."
    Unknown "The war went on for the entirety of my teenage years."
    Violet "God, that sounds terrible."
    Unknown "And then we have kids like you waving your fist at the people above you without wanting to make a stand."
    Violet "Excuse me?"
    Vincent "Damn, that's harsh."
    Unknown "Ah, sorry, I get a bit passionate about this sort of thing. It’s in the job description I suppose."
    Violet "What do you mean?"
    Unknown "Well... all I’m saying is that if you actually want to do something about our current political situation, then I could bring you to the people currently involved in that..."
    Vincent "Are you...?"
    Unknown "Yeah, I’m a part of your unnamed and pitiful resistance force. Pleased to be making your acquaintance."

    # TODO: Declare character for Resistance Member, give both Unknown and Resistance Member the same color
    "Resistance Member" "Despite our unfortunate lifestyle, we rest pretty well at night knowing that we’re doing {i}something{/i}. Plus you meet some pretty good people too."
    "Resistance Member" "So, are you two interested?"

    Violet "God... this is too sudden..."
    Vincent "Violet, I’m still not sure if we can trust him."

    "Resistance Member" "I mean, there’s nothing stopping you from turning me in. I’m the one taking the risk here."
    "Resistance Member" "Well, I guess there’s not much of a risk. I’ve got ten years of experience and can handle my own pretty well."

    Vincent "I guess..."

    "Resistance Member" "Hey, there’s absolutely no pressure to join us. I might’ve understated how stressful the lifestyle is, and you might be better off enjoying your normal lives."

    Violet "It would be nice to not feel so powerless all the time..."
    Violet "Vincent, are you joining them?"

    "..."

    Vincent "Nah, I’m good."
    Violet "Really?"
    Vincent "I don’t really trust him, but even if he’s legit, I wouldn’t."
    Vincent "Like you said, there’s a lot that makes life worth living. I’m good with relying on the cope."
    Violet "I mean..."
    Vincent "Listen, Violet. Either you join and life will be pretty miserable—more miserable than just being a normal guy in this world."
    Vincent "Success is definitely not guaranteed, but you’ll feel like you have a slight bit of freedom and autonomy."
    Vincent "Or, you decide not to join and live a normal life, albeit not the best life under these conditions, but you’ll be safe and have a sense of stability."
    Vincent "You’ll probably feel a bit powerless, but it’s up to you whether you’re okay with that or not."
    Violet "You sound... different."
    Vincent "Dude, I’ve thought about this for a while. We’ve heard about our classmates getting randomly recruited like this, so I couldn’t help but think of my response."
    Vincent "You can’t blame me for it. I’ve thought about it long enough, weighed the pros and cons, and now I can make a decision as fast as I just did."
    Violet "You make some good points..."

    "Resistance Member" "Again, no pressure."

    "..."
    "..."

    Violet "Well, I guess I’ll have to..."

    menu:
        "Join.":
            Vincent "Dude..."

            "Resistance Member" "Welcome aboard. I can’t promise you’ll come out the other side in one piece. We do what we can."

            Violet "I’ll do what I can..."

            hide mysteryman

            Violet "Feeling like I have some control over my life is worth the risk. This is gonna be alright. I’ll be alright."
            Violet "I don’t want to just stand by while people are suffering. I can’t just be complacent like this."
            Vincent "Violet... I’ll respect any decision you make. Just take care of yourself."
            Violet "Okay, I will. I’ll be alright. We’ll be alright."
            Vincent "We will..."

            scene black

            Violet "Yeah, one day at a time."

            "..."

        "Turn down the offer.":
            Vincent "Okay, good."
            Violet "I don’t know, it still feels kinda wrong. I don’t want to just stand by while people are suffering. I feel so complacent."
            Vincent "It’s definitely a hard decision, but I’ll respect any decision you make."
            Vincent "Things are rough, but we’ll get through it together."
            Violet "Okay, that sounds okay."

            "Resistance Member" "Fair enough. Zero recruits out of five that I’ve asked. Fair enough."

            hide mysteryman

            Violet "Vincent, I’m not a coward, right?"
            Vincent "Turning down this offer doesn’t make you a coward, and if you had accepted, that doesn’t change who you are either."
            Violet "I think... we’ll be okay."
            Vincent "We will..."

            scene black

            Violet "Yeah, one day at a time."
            Violet "Together."
            "..."

    stop music fadeout 3.0
    with Pause(3)
    jump credits


label credits:
    image cred = Text(credits_s, text_align=0.5)
    image end = Text("{size=80}The End", text_align=0.5)
    image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5)

    play music konosuba fadein 3.0

    $ credits_speed = 25 #scrolling speed in seconds

    scene black
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")

    show end:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(4.5)
    hide end
    with dissolve
    with Pause(credits_speed - 5)

    show sophia
    with dissolve
    with Pause(3)
    hide sophia
    with dissolve
    with Pause(1)

    show vincent
    with dissolve
    with Pause(3)
    hide vincent
    with dissolve
    with Pause(1)

    show violet
    with dissolve
    with Pause(3)
    hide violet
    with dissolve
    with Pause(1)

    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(6)
    hide thanks
    with dissolve
    stop music fadeout 3.0
    with Pause(3)
    return


init python:
    # TODO: Create separate credits button on main menu for further credits
    credits = ('Writing', 'Nithya Sastry'), ('Art', 'Felicia Quan'), ('Programming', 'Matthew Ding'), ('Programming', 'Jason Liang'), ('Programming', 'William Zeng')
    credits_s = "{size=80}Dreaming of a Violet Sunset\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=60}" + c[0] + "\n"
        credits_s += "{size=40}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=60}Engine\n{size=40}" + renpy.version()
