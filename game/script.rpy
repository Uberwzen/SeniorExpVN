# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define Violet = Character("Violet")
define Unknown = Character("???")
define Vincent = Character("Vincent")
define Teacher = Character("Teacher")
define narrator = Character(None, what_italic=True)
define Student1 = Character("Student #1")
define Student2 = Character("Student #2")
define Sophia = Character("Sophia")



image vpic = im.Scale("violet.png", 350, 600)
image teacher = "teacher.png"
image sophia = im.Scale("sophia.png", 350, 600)
image vpicFlip = im.Flip(im.Scale("violet.png", 350, 600), horizontal = True)
image student1 = im.Scale("schoolboy.png", 350, 600)
image student2 = im.Scale("schoolgirl.png", 350, 600)
image bgroom = "bgroom.png"
image bgclassroom = "bgclassroom.jpg"
image bgcourtyard = im.Scale("bgcourtyard.jpg", 1280, 720)
image bgroad = "road.jpg"


label start:
    call scene1
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
    call scene2
    return


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
    show vpicFlip at right
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
    call scene3
    return


label scene3:
    scene bgcourtyard with fade
    play music april fadein 1.0
    show vpic
    "Violet sat on a bench outside his school, watching as his classmates exited the gates and into their lives outside of school."
    "They were all required to wear uniforms, which sometimes made Violet forget that each of his classmates lead lives different from his own."
    "Well, probably not. He felt like everyone has his same worries, same minimal aspirations, desires to just make it through life safety, etc."
    "But maybe that girl over there was into some boyband that he’s never heard of. Maybe that guy walking with his friends plays piano in his spare time."
    "Maybe the girl walking towards him, Sophia, shared some of his own hobbies and interests."
    "It made Violet oddly happy to think about what his classmates looked forward to in their personal lives."
    show vpic at left
    show sophia at right
    Sophia "Enjoying the warm weather?"
    Violet "Yeah. I’m not in any rush to get home, so I just thought I’d stay here for a while."
    Sophia "Well, I’m probably gonna head out now. Wanna join me?"
    Violet "Alright, sure."
    scene road with fade
    show vpic at left
    show sophia at right
    Sophia "How was physics? I thought it was pretty interes—"
    Violet "It was pretty boring"
    Sophia "OH YEAH it was so boring! Math seriously isn’t my thing. Mr. Claudius’s voice seriously just—"
    Violet "This class goes way too slow. I think I might study math in the future, so this pace is just pretty slow for me."
    Sophia "So true! I get pretty good grades in math, but uh... I think I just might be a slow learner."
    Sophia "If you uh... don’t mind... umm..."
    Violet "Hm?"
    Sophia "Well... maybe could (whispers) you tutor me someti—"
    Violet "Whoa, Sophia, you look really red. It’s pretty hot out, did you drink enough water?"
    Sophia "Oh yeah haha, I think I’m just dehydrated."
    "Violet takes out some bottled water."
    Violet "Here, take this."
    Sophia "Oh, thank you!"
    "Sophia drinks the entire bottle at an alarming speed."
    Sophia "Ahem. {i}(takes a deep breath){\i} Hey, Violet?"
    Violet "Yeah?"
    Sophia "We’ve been friends for a pretty long time, right?"
    "Sophia had this determined look on her face. Violet was a little confused."
    Violet "{i}Did something happen? Was something wrong?"
    Violet "{i}Well, her expression looked kinda cute, so he didn’t have any complaints.{\i}"
    Sophia "Okay, so I should feel confident asking. Could you tutor me in physics sometime?"
    "Sophia’s cheeks were red again. Violet was a little concerned, because that was his last bottle of water."
    Violet "{i}Oh God, what if she passes out? What was she asking about again? Math tutoring?{\i}"
    Violet "Uh... yeah sure."
    Sophia "Really?"

    "Sophia sounded excited."
    Violet "I mean, yeah. I don’t see why not."
    Violet "We hang out a lot anyway, right? I don’t mind helping a friend out."
    Sophia "(coughs) a friend..."
    "..."
    Violet "Hm, it sure is beautiful out, huh?"
    Sophia "Yeah. (sighs) Your eyes really shine in this sunlight..."
    "..."
    Violet "Hey, thanks. No one’s ever said that to me before."
    Sophia "(quiet) boys are actually fucking stupid."
    Violet "Huh?"
    Sophia "Huh?"
    Violet "Never mind."

    play music missionimpossible fadein 1.0
    "Suddenly, they hear gunshots. Then yelling. That first yell was a man, possibly a middle-aged adult."
    "Then they heard more shouting."
    "These shouts sounded angry, but Violet could hear that familiar tone of fear buried within their voices."
    "Maybe it was more accurate to say that they were screaming."
    "More gunshots."
    "Violet didn’t understand why the resistance couldn’t just fight back a little quieter."
    "He often laid awake at night, reminded of the way that he could hear very little courage in these yells."
    "Maybe yelling was cathartic? Violet wished that their only hope could at least sound a little braver..."
    "The shouting grew closer. The gunshot grew closer."
    "The piercing sound of magazines being emptied made it impossible for Violet to think straight."
    "There’s always a window of time. At the moment, they were safe from being hit in the crossfire."
    "But this wouldn’t last long. Once they miss that window, it’s near-impossible to escape."
    "He’s lost enough classmates to know this. Violet knows that he should run away, and yet—"

    Sophia "Violet, we have to go."
    "Violet couldn’t feel his legs. He’s been in this situation too many times, and it’s always the same."
    "Many will default on running away between their instinct of fight or flight."
    "Very few give into their idiotic impulse to fight. In Violet’s case..."

    menu:
        "he needed to protect Sophia, even if it meant his death.":
            Violet "Sophia, run."
            Sophia "WHAT? Violet: Just run!"
            hide sophia
            "Violet sprinted towards the gunfire as it got louder and louder in his ears."
            "He could feel his head throbbing. Why did he choose this?"
            "Was Sophia actually any safer? Maybe she’s in even more danger."
            "Violet saw about six men sprinting across the street. He heard a lot more voices than what would belong to six people."
            "What was going on? He heard yelling from all around him."
            "Violet turned around and saw a man in a military uniform pointing a gun at him."
            Violet "Wait, I’m not—"
            scene black
            "Violet collapsed before he heard the bang. Everything went black."
            call credits
            return

        "he couldn’t help but freeze up":
            Sophia "VIOLET!"
            Violet "Hmm?"
            Sophia "WE HAVE TO GO!"
            Violet "I’m sorry?"
            "Violet could hear his own heartbeat, almost as loud as the gunshots."
            Sophia "Good lord—"
            "Sophia grabbed Violet’s hand and sprinted into an alleyway."
            "They made frequent turns into alleyways and streets that Violet didn’t recognize."
            "He didn’t recognize them, but he wasn’t too nervous."
            "Sophia seemed confident enough in leading him to safety, so he trusted her with his life."
            "They reached a street that Violet vaguely recognized."
            "Everything on this street was run down and abandoned, which ironically, made it the safest."
            "Sophia led the two into what used to be a convenience store. They stopped to catch their breath."
            "Violet had no idea how long they were running for."
            Sophia "Hey... are... you... oh god my sides hurt... Violet: I’m... ugh..."
            "They took a few minutes to learn how to breathe normally again."
            "Violet could still hear the rhythmic thump of his heartbeat. This convenience store was too dark."
            "The shelves were scarcely stocked and all the items were probably expired. There was a back door that made him a little nervous."
            Sophia "Hey, you’re still breathing pretty heavily. Are you...?"
            Violet "I don’t... know..."
            Sophia "Hey listen, trust me. We’re 100\% okay now. You’re safe, please trust me."
            "Violet took some deep breaths. After a moment, his breathing returned to the realm of normal."
            play music april fadein 1.0
            Sophia "Violet, are you okay?"
            Violet "I... uh, yeah. I think so. I am."
            "A few moments of silence passed."
            Sophia "I... never know what to say when this happens. I’m sorry."
            Violet "Why are you sorry?"
            Sophia "I don’t know..."
            Violet "It’s them who should fucking apologize."
            Sophia "Violet..."
            Violet "God fucking dammit. I remember just earlier when I was telling you that I want to study math after high school."
            Violet "I told you that, but it’s so hard to just want things that are in the miserable fucking future!"
            Violet "I look into the past and it’s painful, and I look into the future and it’s so damn bleak."
            Sophia "I—"
            Violet "How can our teachers expect us to take standardized tests and be good at school sports and work towards a career?"
            Violet "How are we expected to focus on our future when it feels like the world is an absolutely shit place to be?"
            Violet "Oh yeah, I’ll make goals for a future that I have little to no hope for."
            Sophia "Violet, take it easy. Slow down. We’re okay."
            "..."
            Violet "{i}(quietly){\i} Sophia?"
            Sophia "Yeah?"
            Violet "I’m not crazy for having these feelings, right? I’m not weaker than everyone else?"
            Sophia "You’re not. You’re definitely not."
            Violet "Okay... okay good..."
            Sophia "It’s fucked up. That’s all. You’re right about everything."
            "..."
            Sophia "Just... one day at a time. We’ll take it step by step together. That’s all I can really say."
            "..."
            Violet "Thank you..."
            "..."
            Sophia "Can I walk you home?"
            Violet "Please. Thank you."

            call scene4
            return

label scene4:
    call credits
    return

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

    stop sound fadeout 1.0
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