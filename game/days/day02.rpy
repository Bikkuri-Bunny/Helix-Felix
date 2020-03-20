#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  day3.rpy
#
#  Copyright 2020
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#


#Day 2
label day2:
    $ config.side_image_tag ="addison"
    calendar day 2
    play audio bell
    a pajamas happy "Mmmmm! Big stretch!"
    a -pajamas happy "..."

    "This morning goes well, despite the kittens still being tired from the two consecutive days of adoption notices. Breakfast is uneventful and I'm particularly glad for it."
    "No one was adopted last night, I shouldn't be glad for it, but I actually am. I decided to take a break from the kittens and spend the morning in my room."
    "It's just like Dr. Kronauer said, maybe I should take more time for myself?"
    "I sit down and work on one of my coloring books. I like to experiment with the colors and see what I can make appear."
    "Sometimes I shade the shapes from light to dark, or from one color to another."
    "Sitting back and looking over what I've made always makes me smile."

    play sound knock

    play music musicneutral loop

    scene bg bedroomlight with hpunch

    a surprised "Oh!"

    "Oh- it's just my door."

    a happy "Come in!"

    play sound dooropen

    show jesse happy at myright
    with easeinleft
    show steven neutral at myleft
    with easeinleft

    j "Good morning, Addy. I'm giving our new doctor a tour of the floor."

    "Oh, it's him!"

    a happy "Good morning! Nice to meet you. I'm Addison."

    "I try and smile for him, but the way he looks at me makes the hair on the back of my neck stand up. There's something in his eyes that makes his gaze so... strong. It's a little scary."

    s "..."

    play music musicsteven loop

    "Is he not going to introduce himself?"

    j "This is Dr. Moore. Since you and the other Felixes are going to be seeing him quite a bit I want you two to get along quickly, okay?"

    "I glance at Mr. Jesse. Is he saying Dr. Moore will be hard to get along with? I keep my smile and nod, but my ears feel so hot. Dr. Moore still just looks like he's angry at me."

    s "I don't think that will be hard."

    show steven happy
    with dissolve

    "He offers his hand to me and I try not to take it too slowly. His smile seems nice... But..."

    a "No, not at all. I get along with everyone!"
    j "He sure does. Everybody here adores Addison. He's our Staff Companion, so the employees can get a feel of what it's like to have a Felix around and why people would want one."
    j "He can give massages, is soft and nice to pet, and he always seems to be smiling. He also helps me out with the Felixes who are still for sale all the time. The kittens really look up to him."
    j "He is a very good Felix, aren't you?"

    "Dr. Moore hasn't let go of my hand yet."

    a blush "Thank you, but you don't have to praise me..."

    "Finally, Dr. Moore steps back."

    show steven neutral
    with dissolve

    s "Nice to meet you."
    j "Well, let's get on with the tour, then. Thanks Addy."

    hide jesse
    with easeoutleft

    "Dr. Moore hesitates before he leaves, glancing back at me. But he doesn't look angry this time. Did he want to say something to me?"

    hide steven
    with easeoutleft

    "The door closes behind them and I let out a heavy sigh. It was getting really cramped in here with all three of us, and the way Dr. Moore's eyes felt... My ears burn just thinking about it."
    "Has he never seen a Felix before?"
    "I know that we're rare on the outside, but surely I can't be the first one he's seen, right? Or maybe he's just shy? I don't know."
    "I guess I'll have to learn more about him. I shuffle from one foot to the other, thinking..."

    play sound ding

    play music musicneutral loop

    menu:
        "Stay and draw":
            jump stay
        "Follow the new doctor":
            $ steven_points += 1
            jump follow

label stay:

    "I was going to draw, I so should stick to it and follow through. Plus, that new doctor... Something about him doesn't sit right in my stomach yet. I'll probably like him once I get to know him better."
    "I've been playing with some shapes lately. There are some books in the library that are full of famous painter's works. I like to look through them sometimes."
    "My favorites are when they paint and the picture comes out blurry, or when they use the wrong shapes, but you can still tell what the picture is supposed to be."
    "I think it's called an... impression?"
    "I fill the blank pages with crayon scribbles in unconfined blotches, trying to make my own pictures appear in the same way."

    a "-yawn-"

    "I rest my head on the desk while watching the crayon glide over the page."
    "It's so relaxing..."
    "..."

    show bg bedroomlight with hpunch

    play music musiclukas loop

    show lukas confused
    with easeinleft

    a "Ahh!!"
    l "It's just me. You okay?"
    a "Yeah... Did I fall asleep?"
    l "You must have. Here-"

    hide lukas confused
    show lukas happy at center,zoom_in

    a "What?"

    "He gets close and has his fingers in my hair."

    a blush "?"

    l "There. You had a scrap of paper in your hair."

    a "Oh."
    l "Are you sure you're okay? Are you feeling sick? Tired?"
    a laugh "No, I'm fine. I just needed a nap, I guess."
    l "Promise?"
    a "Promise."

    show lukas at center,zoom_off

    "Dr. Kronauer had always been this worried about me. He hates seeing me get sick. He's always so worried about me, like he did something to cause it, since he has to test his medicines on me sometimes."

    "I remember once when I fell over onto him because his medicine was too strong. The look on his face was priceless."

    l confused "What?"
    a happy "Nothing. Did I sleep through lunch?"

    jump lunchday1

label follow:

    a surprised "Wait- wait for me!"

    scene bg hallway1
    with dissolve

    show steven thinking at myleft
    with easeinright
    show jesse thinking at myright
    with easeinright

    j "Oh, Addison?"
    a "Can I come with? I can help show him around too."

    show jesse happy
    with dissolve

    j "See what I mean? Always helping. Sure, you can come along for now."

    "Dr. Moore doesn't seem to mind as we all head down the hallway, while Mr. Jesse explains the layout of the floor and the different rooms around us."

    scene bg classroom
    with dissolve

    j "This here is the classroom: the kittens have classes on reading, writing, math, and health when they transfer here up until they leave. Our curriculum is pretty basic, and once they turn 12 they are allowed to stop if they choose."
    j "They are either assigned to either morning classes or evening classes so they're not all in here at once."

    scene bg hallway1
    show jesse happy at myright
    show steven neutral at myleft
    with dissolve
    pause (2)
    scene bg playroom
    show jesse happy at myright
    show steven neutral at myleft
    with dissolve

    j "This is the playroom where they spend most of their free time. The clinic is actually connected through this door, just in case they play too rough. But they know not to get into trouble, so it’s not very often an accident like that happens."
    s "Hmm."

    scene bg clinic
    show jesse happy at myright
    show steven neutral at myleft
    with dissolve

    j "And then your office is right through this door."

    scene bg stevenoffice1
    show jesse happy at myright
    show steven neutral at myleft
    with dissolve
    $ persistent.bg_stevenoffice1=True

    a surprised "It looks so different now!"

    "The room has been stripped of everything. There isn't even a computer in here yet. with just shelves and the desk, it looks like it's brand new."

    show steven happy
    with dissolve

    s "Don't worry, I have some bright clinic posters I can put up."
    a "That sounds nice."
    s "What else should I bring in? Do you think the kids would like candy or stickers more?"

    play sound ding

    menu:
        "Candy!":
            a "Everyone loves candy in here."
            $ candy = True
            jump continueday1
        "Stickers.":
            a "Stickers would be more fun and better for the kittens' tummies too."
            jump continueday1
            $ stickers = True
        "Both!":
            $ steven_points += 1
            a excited "Both!!"
            $ candy = True
            $ stickers = True
            jump continueday1

label continueday1:

    s "Okay. I'll also get a couple of plants to liven it up a bit more too."
    a excited "I love plants!"
    s "Okay. Lots of plants then."
    j "That sounds wonderful. Addy, we'll have to talk about some things privately. Will you excuse us?"
    a thinking "Oh, okay."

    "That's it for me and the tour then."

    hide jesse
    with easeoutright
    hide steven
    with easeoutright

    scene bg clinic
    with dissolve
    pause (2)
    $ persistent.bg_clinic=True
    scene bg playroom
    with dissolve
    pause (2)
    scene bg hallway1
    with dissolve

    "At least the new doctor seemed to warm up at the end. Maybe it's just the nerves? I'm not entirely sure."
    "I still feel like I need to get to know him better so I can find out if he's scary or just shy."
    "My stomach rumbles. Lunchtime already? I guess I hadn't been paying attention to the time I spent with Dr. Moore and Mr. Jesse."
    "It's not quite 11:45 AM yet, so I meander slowly down the halls towards the stairway when Dr. Kronauer comes through the doorway holding our lunch boxes."

    play sound dooropen

    show lukas surprised
    with easeinleft

    a surprised "Oh!"

label lunchday1:

    play music musiclukas loop

    show lukas happy
    with dissolve

    l "I thought we could eat down here for a change."

    a happy "Oh, alright. That sounds good."

    "We don't eat down here often, but it's not unheard of."

    scene bg bedroomlight
    show lukas happy
    with dissolve

    "I sit cross-legged on the bed waiting for lunch."

    a excited "What are we having today?"
    l "I made us some egg rolls and fried rice."
    a "Oooh, what's the sauce?"
    l "Sweet and sour. It has pineapple in it."
    a "Mmmm."
    l "Addy, you're getting it all over your face."

    $ config.side_image_tag = "alfa"
    show food onlayer event
    with dissolve
    $ persistent.cg_food=True

    a "So?"
    l "Here, I'll..."

    "He wipes my face with a napkin while I giggle."

    a "H-hey!"
    l "... There."

    hide food onlayer event
    with dissolve
    $ config.side_image_tag = "addison"

    a smile "..."

    "We sit and eat and laugh a little longer. Eventually, we set the dishes aside and I flop over, resting my head on Dr. Kronauer's lap while he strokes my hair and talks to me."
    "He knows I don't really listen all that much to his long stories about work. Usually I just like to enjoy the vibrations of his voice."
    "My eyes close as he goes on."

    l "I think we may have started off on the wrong foot... But I'm sure he'll warm up eventually."
    a "Hmm..."

    "I cuddle further into him, pressing my cheek against his stomach. I can hear it talking about our lunch better than I can hear Dr. Kronauer's voice..."

    l "Addy. Addy."
    a "Huh?"
    l "You fell asleep."
    a "I did?"

    show lukas sad smile
    with dissolve

    l "Mmmhm. And I have to go now, so you have to get up."
    a thinking "Oh."

    "I sit up, rubbing my eyes while Dr. Kronauer stands, running his hand through my hair one more time before giving it a good shake to mess it up again."

    a mad "Heyyy!"

    show lukas laugh

    a happy "Haha!"

    l "Hahaha. Okay, I'll see you soon Addy."
    a "Okay, goodbye for now."

    hide lukas
    with easeoutleft

    "Looks like it's aleady one o'clock. I can't stay in my room or I'll probably fall asleep again. Instead, I get up and stretch. A round of games in the playroom sounds nice."

    play music musicsecretspace loop

    scene bg hallway1
    with dissolve
    pause (2)
    scene bg playroom
    with dissolve

    "Before I can even talk to the kittens, though, someone grasps my arm."

    show pumpkin nervous
    with easeinright

    a surprised "???"
    p "Addison, can I talk to you?"
    a "Sure – what's wrong?"

    "Even though we're around the same age, we don't talk much. Sometimes he helps the kittens with their lessons or plays games with them like I do, but I think he likes smaller groups instead of taking care of everyone at once."
    "Even his giant personality can't compete with a big crowd of kittens."

    p "Nothing's wrong, I just wanted to talk. Well, actually... It's not wrong but it's new!"
    show pumpkin excited
    with dissolve
    p "The management is going to take me off the sales list, like you! They're going to make me 'Brand Mascot!'"
    a surprised "Wait, taken off the sales list? You wouldn't be adopted?"
    p "Yeah, I just have to pass a test tomorrow."
    a nervous "A test? What kind of test? What will your job be? I didn't think they would do that with anyone else."
    p "Yeah, it's cool, huh? They want to take pretty pictures and videos of me to make people want to adopt Felixes more. Isn't it great?"
    menu:
        "Be supportive":
            $ pumpkin_points += 1
            a happy "Yeah! That sounds really nice."

            "I'm glad he's taking it so well. I was crushed when I learned that I wasn't going to be adopted, but I guess this is different. It was really hard on me and I felt awful for months. But... It’s good for him if he passes the test. Even now he's smiling right at me."

            p "Isn't it?"
            jump continueday2
        "Be worried":
            #$ pumpkin_points -= 1
            a nervous "You... You're okay with that?"
            p "Why wouldn't I be? It's amazing!"
            a "Well..."
            "I don't have the heart to say what I'm really thinking. Learning that I would never be adopted was so hard for me, but he seems to be fine with it. Honestly, I'm a little jealous."
            jump continueday2

label continueday2:

    show pumpkin nervous
    with dissolve

    p "The test tomorrow – it's after our shots. I'm sure I'll be really good at it! But..."

    "I know where this is going."

    a thinking "You're nervous."
    p "Yeah... A little, I guess."
    a "Like you said, you'll do great. What's the test going to be about?"
    p "I think it's just pictures to make sure I'm pretty enough..."
    a "Pumpkin, you're beautiful! Of course you're going to pass!"

    show pumpkin excited
    with dissolve

    p "Yeah! Of course I am!"

    "I don't know if I should ask or not, but I'm worried about something else."
    "Does he really want to pass?"
    "Maybe I'm assuming too much. He doesn't have to react the same way I did, or maybe he really doesn't mind not being adopted."
    "We sit and chat a while longer. Pumpkin even rests his head on my shoulder. It's nice to spend time with him alone for a change. Even though I feel that I don't know him well enough."
    "He's always been loud and he thinks he wants to be the center of attention. But once he's there, he would get nervous and back down from being the leader. Usually that role got passed onto me instead."
    "I may be quiet, but I still like helping everyone out."
    "I lean back against him."

    p "I think there's going to be kissing and stuff."

    a thinking "In the test?"
    p "In the test and in the job. I think there's going to be kissing and sex and stuff."


    a thinking "Oh... how do you feel about that?"
    p "About sex?"
    a "Yeah."

    show pumpkin excited
    with dissolve

    p "I'm really excited!"


    a happy "Haha, well that's good I guess."
    p "Why wouldn't I be excited?"
    a "I don't know, everybody thinks differently."
    p "Mm... I guess. But I'm excited."
    a "That's good."
    p "What's it like?"
    a "What?"
    p "Sex!"


    a thinking "Ahh...."

    "Really, I don't know what to say to him."

    a "It's probably different for everybody. It feels nice, but yeah. I don't think you can explain it..."

    show pumpkin sad
    with dissolve

    p "That's stupid."
    a sad "Sorry..."

    "Yeah, Pumpkin, I know, I feel a little stupid."

    scene bg hallway1
    with dissolve
    pause (2)
    scene bg cafeteria
    with dissolve
    play audio bell
    play music musicneutral loop

    "Pumpkin doesn't sit with me for dinner. I guess he asked all the questions he wanted to ask in private."
    "Tonight, we're having some sort of squash or pumpkin with pickled vegetables and stewed pork. I like the pumpkin, it's sweet and tastes like vegetable candy. But the pickles are too strong for me."

    show ainsley happy
    with easeinright

    g "Can I have them, then?"
    a "Don't tell anybody, okay?"

    "She's still just a baby, and growing like a weed. Sneakily, I let her have my serving while no one is looking."

    g "Thanks, Addy!"

    "Too loud! I looked around quickly, making sure no one heard her. Once I'm sure they didn't, I smile. It's kind of funny."

    hide ainsley
    with easeoutright

    play music musicsleepy loop

    scene bg hallway1
    with dissolve
    pause (2)
    scene bg bedroomlight
    with dissolve

    a pajamas sleepy "-sigh-"

    "I wanted to relax, but today was just as busy as the rest of the week has been."
    "After dinner, I go straight to bed. Tomorrow is Drug Day, when we get our weekly shots."
    "Dr. Moore will be doing that now- I hope his shyness doesn't mean he'll have the shaky hands."
    "But he's a medical doctor, so it shouldn't be too bad. When Dr. Kronauer was first learning how to give me shots that was the worst. He's doing a lot better now."
    "I curl into my blankets, happy and cozy."

    show bg bedroomdark
    with dissolve

    "Another dream tonight, another day tomorrow. Goodnight."

    cards open card3

    scene bg bedroomlight
    with fade
    jump day3
