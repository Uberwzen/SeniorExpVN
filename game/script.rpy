# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Violet = Character("Violet")
define Unknown = Character("???")
define Vincent = Character("Vincent")
define Teacher = Character("Teacher")
define narrator = Character(None, italics = True)
define Student1 = Character("Student #1")
define Student2 = Character("Student #2")

image vpic = im.Scale("violet.png", 700, 700)
image bgroom = im.Scale("room.jpg", 1280, 720)
image bgclassroom = im.Scale("classroom.png", 1280, 720)

label start:
    call scene1
    call scene2
    call credits
    return


label scene1:
    scene black
    play music yourname fadein 1.0
    "Violet was dreaming. His dreams were usually of nothing important, and this one was no exception."
    "But this time, the mundane events he was usually faced with included a little bit of feeling. Kinda."
    "He could feel physical sensations and he was somewhat aware of his emotions."
    "As he was dreaming, he felt... content. Not just content, but happy."
    "In his dream, brief scenes fly by as he watched as a 10-second protagonist."
    "He wasn’t allowed to stay, but to just watch for a few moments."
    "He saw his mom cut some cake for him. There were candles placed in a uniform pattern on top."
    "Someone’s birthday? His birthday?"
    "He could tell that he was around ten years old based on the anticipation bubbling in his chest."
    "He felt special. Birthdays are special. He hadn’t felt this in a while..."
    "Violet was lying in a dark field, looking up at the stars."
    "His back was wet from the cold grass, but it felt nice."
    "He let his weight sink into the ground below him."
    "The dead silence put his usually–loud mind at peace."
    "The stars watched Violet from above."
    "They seemed so far away..."

    Unknown "Hey."
    "Riding a bike down a sidewalk on a sunny day..."
    Unknown "Hey, wake up."
    "Someone’s voice? It sounded like Vincent..."
    Vincent "HEY VIOLET!"
    "(SMACK)"
    Violet "OW!"
    "Yup, that was Vincent’s voice, and unfortunately, his hand as well. Across the back of Violet’s head."

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    scene bgroom
    show vpic at left
    show vincent at right


    Violet "Ughh stop talking. What do you want?"
    Vincent "So do you want me to not talk or should I answer that question?"
    Violet "You’re stupid. And you’re talking anyways."
    Vincent "Ah, well, I guess you’re right."
    Vincent "Now that I’ve passed the point of no return, I just wanted to let you know that class starts in a few minutes."
    Violet "So you’ve denied me a few minutes of peaceful slumber?"
    Vincent "You poor kid. Come on, try to look at least a bit more lively"
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
    Vincent "Maybe. Did you see that new episode of Konosuba?"
    Violet "Yeah, I did! Let’s talk about it later because I need at least an hour."
    Vincent "So I’m guessing you liked it then?"
    Violet "Of course!"
    Vincent "You’re always so shy and quiet until I get you talking about Konosuba."
    Violet "Oh, shut up. What are we even doing in history today?"
    Vincent "Some Pre-War Era stuff."
    Vincent "Back when people drove cars? I don’t know."
    Vincent "At least it’s sometimes funny to read about the dumb stuff they believed."
    Violet "I feel like they had it better back then..."
    Vincent "Hey, man. Just let me cope."
    Violet "(sighs) Well, I guess there’s nothing wrong with that...coping..."
    Vincent "Hey, don’t sound so gloomy."
    Violet "..."
    "Violet cursed himself. He felt like he always ruined the mood of conversations with his own dark mood."
    "He at least tried to be a little more cheerful. Well, trying was different from actually being successful..."
    Vincent "Got any plans after school?"
    Violet "Never."
    Vincent "Wonderful. Do you wanna go to that new bookstore that just opened?"
    Violet "Why? So you can throw away your paycheck on those stupid comics?"
    Vincent "Hey, let me keep my hobbies in peace."

    menu:
        "Sure, fine, I’ll come.":
            Vincent "Alright sweet. I’ll pick you up at 7?"
            Violet "Sounds good."
            Vincent "Looking forward to it!"

        "No, I’m good.":
            Vincent "Are you sure?"
            Violet "Yeah, I’m not really feeling up to it."
            Vincent "That’s okay man. I’ll always be here if you wanna hang out."

    "(Bell rings, maybe put in footstep sounds to show that people are getting to their seats?)"
    Vincent "Alright, talk soon?"
    Violet "Sure."

    stop sound fadeout 1.0

label scene2:
    scene bgclassroom with fade
    play music school fadein 1.0
    show vpic at left
    "Violet seriously didn’t have the energy to pay proper attention to class."
    "Luckily, it was history. His teacher made his students’ lives easier and harder by not introducing anything that wasn’t on the prior night’s reading."
    "They didn’t really have to pay attention, but they had to last an entire hour in that classroom..."

    show teacher at right
    Teacher "Alright class, today we’ll be studying the Pre-War Era."
    Teacher "You all did the reading last night, so we’ll just be going over that today."
    Violet "God, if you’re real, just put me in a coma."
    Teacher "Now, as we know, before the War, poverty was rampant across our nation."
    Teacher "But through our government’s expansion of global influence and the creation of protectorates, global trade has increased in efficiency by more than ten-fold."
    Teacher "Poverty has been cut to historic-low levels due to our increased wealth and power. Our Department of Life and Charity has overseen all of this great work over the past fifty years."
    Violet "Why do we even need to learn about this? Seriously, if I have to hear the word “poverty” one more time, I’m gonna kill somebody."
    Violet "Plus, I bet half this shit is DLC propaganda anyways."
    Teacher "Can someone tell me what they know about the War? It can be anything, really."
    "(Silence)"
    Teacher "Anyone?"
    "(Silence)"
    Violet "I don’t know what he expects from us. I feel like no matter what I say, it’ll be the wrong thing."
    Violet "You won’t find too many people who are actually excited to talk about this type of stuff."

    hide vpic
    show student1 at left
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
    show student2 at right
    Student2 "Hey, relax."
    Student1 "What? I’m not saying anything wrong."

    hide student2
    show vpic at right
    "(The class starts speaking louder amongst themselves)"
    Violet "{i}We always have to have one smartass huh. I’m sure he thinks he’s real clever.{\i}"
    "Violet figured out a while ago that the best way to cope was to hate these types of people. They probably thought they were so much better than everyone else, speaking out."
    "Little did they know that everyone shared their basic-ass opinions."
    Violet "{i}Arrogant bastard.{\i}"
    "Even though Violet didn’t speak a word of what he was thinking, he felt guilty for a brief moment."
    "Unfortunately, he noticed that feeling. He didn’t know what was right anymore..."
    "There was an uncomfortable cognitive dissonance that resulted from hating someone that you completely agree with."
    "Violet just wanted to make himself feel better. There’s nothing wrong with that, right?"

    hide student1
    show teacher at left
    Teacher "Class, settle down."
    Violet "At least after today, he’ll learn how to hold his tongue. And as expected, it always ends in..."
    Teacher "Young man, I’ll speak with you after class."
    Violet "{i}There you are. Godspeed, dipshit.{\i}"
    stop sound fadeout 1.0

label credits:
    play music konosuba fadein 1.0
    image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{size=80}The End", text_align=0.5)
    image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5)
    $ credits_speed = 25 #scrolling speed in seconds
    scene black #replace this with a fancy background
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(5)
    hide theend
    with dissolve
    with Pause(credits_speed - 5)
    show vpic
    with dissolve
    with Pause(3)
    hide vpic
    with dissolve
    with Pause(1)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(4)
    hide thanks
    with dissolve
    return


init python:
    credits = ('Writing', 'Nithya Sastry'), ('Art', 'Felicia Quan'), ('Programming', 'Matthew Ding'), ('Programming', 'Jason Liang'), ('Programming', 'William Zeng')
    credits_s = "{size=80}Capstone Project 2021\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=60}" + c[0] + "\n"
        credits_s += "{size=40}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=60}Engine\n{size=40}" + renpy.version()