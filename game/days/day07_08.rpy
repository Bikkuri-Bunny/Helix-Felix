#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  day7_8.rpy
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

#Day 7
label day7:
  calendar day 7
  play audio bell
  play music musicupbeat loop

  "Sometimes you just wake up with a little extra energy, you know? It's a nice change from yesterday morning. Today feels like a good day, and I hop easily off to breakfast."

  scene bg cafeteria
  with dissolve

  "The smell of maple syrup is thick and only fuels my smile. I lean over my tray, face in my hands, and watch over the kittens while I eat. It's a bit too sugary for my taste, but the little ones go wild for the syrup. I've spread my pancakes thick with butter."
  "As we we're cleaning up, Charlie starts to mope."

  show charlie sad
  with dissolve

  a "Hey now, what's wrong?"
  c "I have to clean-up today."
  a "Didn't you have clean-up duty yesterday?"
  c "Yeah. But I lost a game and now I have to do clean-up today too. It's not fair!"

  "He stomps his foot."

  a "Then you've learned your lesson: no more bets. Here, let me help you out."

  "I end up getting my tail pretty sticky after helping Charlie wipe up the syrup mess in the cafeteria, but at least he's giggling again by the end of it. I tell him to run off before stopping at the sink to clean myself off. By the time I glance at the clock, it's already ten."

  a "Shoot."

  scene bg hallway1
  with dissolve
  pause (2)
  scene bg clinic
  with dissolve

  show steven neutral at myright

  a sad "I'm sorry I'm late, Dr. Moore."

  "I don't think he'll be upset with me, but I still feel a rock in my stomach."

  s thinking "Oh, it's not a problem, but you do have someone waiting for you."
  a "I do?"

  show pumpkin happy at myleft
  with easeinleft

  a happy "Pumpkin!"
  p "Hey, Addy. I didn't see you yesterday."

  "Pumpkin has been missing from our daily meals lately, and with all my work in the clinic and his work with pictures, he and I weren’t able to spend time with the kittens or with each other."

  a "No I haven't. I guess we've both been really busy."
  p "I thought we could do something fun together today. If you're not busy."

  play sound ding

  menu:
    "Sure! That sounds fun!":
      $ pumpkin_points += 1
      $ steven_points += 1
      jump day7yes
    "I have work to do here...":
      $ pumpkin_points -= 1
      $ steven_points -= 1
      jump day7no

label day7no:

  play music musicneutral loop

  a nervous "Ah, actually I have work I have to do here."
  p sad "Oh."

  "Pumpkin's ears drop and he shrugs."

  p "Okay, maybe next time."

  hide pumpkin
  with easeoutleft
  show steven sad at center
  with easeinright

  s "You know you could have gone with him."
  a "Yeah."
  s "Is there a reason you said 'no'?"
  a "..."

  "I shuffle and avoid eye contact with Dr. Moore. If I tell him the truth, that there's a rock in my stomach about being around Pumpkin, I don't think he'd understand."

  s "Well, you don't have to explain yourself to me."

  "He turns around and goes back to his work."

  jump overhear

label day7yes:

  a excited "Yes!"

  "I grab his hand."

  a nervous "I mean-"

  "I turn back to Dr. Moore."

  a "Would it be okay if I go?"
  s happy "Of course, Addison. You don't have to stay here."
  a excited "Thank you!"

  hide steven
  with easeoutright

  a "What would you like to do?"
  p "I thought we could-"

  scene bg clinic with hpunch

  "Pumpkin's cut off by the clinic door opening."

  show jesse mad at right
  with easeinright

  j "There you are, Pumpkin. I've been looking for you: you're needed upstairs."
  p confused "But I-"
  j "Come on."

  "Mr. Jesse has Pumpkin's arm and is pulling him out the door."

  p "I thought I had today off?"
  j "There was a change."
  a thinking "Can I come with?"
  j "No, not today."

  hide jesse
  hide pumpkin
  with easeoutleft

  a sad "Ah..."

  "Before I knew it, they were both gone."

  show steven angry
  with easeinright

  play music musicsteven loop

  s "Well."
  a surprised "!"

  "He spooked me standing up so fast."

  s "I'll have to talk to Pumpkin about that later."
  a "He's not in trouble, is he?"
  s thinking "No. He's not."
  s sad "He just looked upset, so I'd like to make sure he's alright."
  a sad "Oh, okay."
  s "Why don't you work on that picture you started yesterday, okay?"
  a "Yeah, okay."

label overhear:

  "I turn around to the makeshift desk Dr. Moore has set up for me in the clinic. He seems to like me around just as much as Dr. Kroanuer does, but in a different way. It's strange how he doesn't like being touched..."
  "..."
  "I can fiddle with my colored pencils as much as I want today, but I still can't get Pumpkin off my mind."

  s "... cleared his partners."

  a thinking "..."

  "My ears prick. Dr. Moore tends to mumble to himself while he's working, usually things I don't really understand, abut it's usually medical things. He doesn't seem to be used to how well Felixes can hear. Maybe it's bad to eavesdrop, but I like listening and seeing if it's anything I've learned."

  s "If I tell him he's okay, I'm no better than that asshole."

  "... Maybe it's best not to listen."

  a sad "Dr. Moore? I'm going to go to lunch now."
  s neutral "Alright."

  scene bg hallway1
  with dissolve

  "He doesn't seem to mind as I slip away. I don't like to get caught up in rumors or office politics. I've done it too many times already, being someone who gets to hear everything from everyone (people say a lot more than they should while they're comfortable petting me.) so I try to ignore Dr. Moore's muttering."
  "Instead I head upstairs to-"

  scene bg officespace
  show lukas surprised
  show bg officespace with hpunch

  play music musiclukas loop

  a surprised "Oh!"
  l "Sorry Addy, I was coming down to meet you in your room."
  a thinking "Oh, alright. Why?"

  show lukas blush
  with dissolve

  "He slips past me and into the stairwell, holding the door open."

  l "You said you wanted something special today."
  a "I did?"
  l "Remember? I wasn't able to give anything to you yesterday?"
  a surprised "Oh!"
  a blush "Right."

  scene bg hallway1
  show lukas happy
  with dissolve

  "Oh boy, I hadn't even thought about that. I wasn't really asking for something special, I just wanted to suck him off."

  scene bg bedroomlight
  show lukas happy
  with dissolve

  a "How is your day?"
  l sad "Uh, not great. I'd rather not talk about work though."
  l sad smile "How about you?"
  a thinking "Probably about the same."

  "We sit on the bed and I'm already nibbling on the celery sticks and peanut butter he brought over. The rest of my meal is too hot to sit in my lap, so I'm waiting for it to cool."
  "He leans against me, sighing. "

  l "I don't know what I'd do without you."
  a laugh "Have more lunch to eat."
  l happy "Ah, haha sure."

  "He chuckles, and finally he made a real smile."

  a "... Are you okay? You've seemed kinda sad lately."
  l sad "Mh."

  "Well, I didn't mean to take his smile away."

  l "Yeah, I'm okay. I'm just not taking my own advice and I may be working too hard."

  "He ruffles my hair."

  l "Do as I say, not as I do."
  a laugh "Okay. Well, take a break then."
  l "I wish it were that easy. My break is time with you."
  a "If you say so."

  "I bump into him jokingly and keep eating."

  l "So I'd like to return the favor from yesterday."

  "He sets a hand on my thigh."

  a thinking "Ah, okay. You really don't have to though. It wasn't a favor."
  l "I want to."
  a "Okay..."

  "He sets the tupperware aside and leans into me. I slowly fall back as he kisses my lips."
  "I do like the feeling of his weight on me, of the warmth and pressure."
  "Before I can really savor it though, he's sliding down to pull off my pants and he kneels on the floor. I place my arm over my face."
  if persistent._legal_age == True:
      play sound ding
      menu:
        "Skip Sex Scene":
            jump skiporalday7
        "Continue Scene":
            jump continueoralday7
  else:
      jump skiporalday7

label continueoralday7:

  play music musictender loop

  hide lukas
  $ config.side_image_tag = "alfa"

  show lukasoral1 onlayer event
  with dissolve
  $ persistent.cg_lukasoral1=True

  "He presses my legs open, his hands are placed on the back of my knees."
  "I'd done this before, but still my thighs shake. Am I embarrassed? Not really, I know my pussy is cute."
  "Felixes have naturally hairless bodies for cleanliness, and almost everyone says it's really cute. "
  "No, I think I'm shaking because I can't do anything about this."
  "I don't have the control of the situation that I get from sucking him off or riding him, even just from fucking. It's a little scary. My heart is pounding in my ears."

  a "!!!"

  "And all thoughts blink away as his tongue runs over my skin. My arm presses tighter into my eyes."
  "He's quick to take my clit in between his lips, then he starts sucking. It feels nice, but I try to keep my concentration on other things, on the feeling of his fingertips on the skin on my thighs, or the wet on my arm from my breath."
  "I could tell him that I don't want this, but I don't think that would be the exact truth. The look in his eyes, that sparkle, when he said he would... He wants to make me feel good so badly. My face is already hot, but I can feel myself blushing at the thought."
  "He wants to make me feel good: I should enjoy it."

  a "Ahh... ah..."
  l "Mmm..."

  "I grin as he hums into me. Is trying to purr?"
  "His hands slid down, his fingers were soft and hot. He began to trace the curve of my legs. When one disappears, it isn't hard to realize where it's going to come back."
  "My own hands trace the sheets, feeling the texture of the thread as I wait. His lips and tongue are still prodding, the slick movements making me shiver."
  "There were his fingers. I squirm as they make their appearance, slipping to gently rub at the rim of my hole."

  a "Ahh... ah-"

  "I don't know if I can orgasm like this, but his fingers tease further and further towards pressing inside me, I shake."

  a "Doctor, I... ahh, oh, Ah!"

  "His fingers are inside me, his tongue taking their place at the sensitive flesh at my opening."

  a "Mhh!"

  "My lips were between my teeth as I felt a scream dying in my throat and my leg kicked out."

  l "?"

  hide lukasoral1 onlayer event
  with dissolve
  $ config.side_image_tag = None
  show lukas confused

  a blush "..."

  "Thank god he pulled back."

label skiporalday7:

  a "S-sorry."
  l "Ticklish?"
  a "I guess so..."
  l "Hah, it's alright."

  "He moves to sit next to me on the bed and as I sit up my shoulders relax, though my hands ball into the sheets in between my legs."
  "He wraps his arm around me and I lean into his side."

  l "What can I do for you?"
  a "..."
  a "Just hold me, please."
  l "... Are you alright?"
  a "Mmhmm. I just like it when you pet me."

  "I can tell he's holding back from asking me again. I didn't lie to him: I just want to lay on his chest."
  "It feels so much nicer."
  "..."

  scene bg bedroomdark
  with dissolve

  play music musicsleepy loop

  "When did the light turn out?"
  "I push up to look around, but Dr. Kronauer isn't here anymore."
  "I must have fallen asleep on him..."
  "I'll have to apologize later."
  "The day's not over yet though, so I head upstairs to do some Staff Companion duties."

  play music musicneutral loop

  scene bg officespace
  with dissolve

  o "Addison, over here!"
  o "How are you doing?"
  o "Come sit with me for awhile!"

  "Everyone is so happy to see me."

  a happy "Okay."

  "I do rounds, stealing empty chairs or sitting at peoples feet. Enjoying the feeling of someone else scratching at your scalp, it's really something you can't get any other way."

  o "Haven't seen you in a while."
  a blush "Sorry, I've been busy downstairs."
  o "That's alright, just don't forget about us."
  a "I won't."

  "I may have lots of duties and I may mess up sometimes, but I always remember that I need to care for everyone."

  o "Quittin' time. Okay Addy, see ya later."
  a "Bye-bye."

  "By seven, everyone in the office has gone. I can see movement in the lab through the frosted glass, but I'm not allowed back there, so I turn off the office lights and head back downstairs."

  scene bg hallway1
  with dissolve

  "The staff fed me donuts, so I really don't mind that I missed dinner. Instead, I decide to head straight to the kittens' room to help everyone in their pajamas after showers and read some books to them."

  scene bg barracks
  with dissolve

  play music musicsleepy loop

  "Pumpkin's old bed is empty now. I wonder if he's asleep in his new room."
  "..."
  "I should probably talk to Pumpkin about... things. With what happened at lunch, something just wasn't right. Maybe he would know how that feels too."

  scene bg bedroomlight
  with dissolve

  a pajamas sleepy "Mhh..."

  "For now though I clean up, washing myself off thoroughly after being around and touching so many people. I don't want to catch or spread a cold."
  "Still warm from my shower, I crawl into bed."

  scene bg bedroomlight
  with dissolve

  "Goodnight."

  scene bg bedroomdark
  with dissolve
  pause (3)
  scene bg bedroomdark
  with fade

  play sound dooropen

  "..."
  "..."
  "My door opened?"

  a "Hello?"

  show lukas sleepy
  with easeinleft

  l "Just me."
  a surprised "What are you doing?"
  l "Sleeping. Scoot over."

  "I squirm to one side of the bed. Dr. Kronauer settles in besides me in a way that reminds me of when kittens would sleepwalk while I was still in the barracks."

  hide lukas
  $ config.side_image_tag = "alfa"

  show lukassleeping onlayer event
  with dissolve
  $ persistent.cg_lukassleeping=True

  a "Are you okay?"
  l "Just tired."

  "He turns, wrapping his arms around me and pulling me back down and into his chest. I can't say that I don't like it. But something about it makes me nervous."

  a "Are you sure?"
  l "Mmhm, go back to sleep."

  "His hand settles on the back of my head, nudging me down into his chest. I've fallen asleep on him before, but never like this. It feels nice, like it would be easy to sleep like this, so I settle myself down. Still, he shouldn't be here at this hour. Shouldn't he have gone home already?"

  play sound ding

  menu:
    "Did you want to have sex with me?":
      $ lukas_points += 1
      a "Did you want to have sex with me?"
      l sleepy "No, I'm too tired for that."
      jump sleepday7
    "Why are you here so late?":
      a "Why are you still here? Shouldn't you have gone home already?"
      l "Mm, just worked late. Don't worry."

label sleepday7:

  "He pats my head."

  l "Please, just sleep."

  "There's no sense in arguing, so I close my eyes and try to enjoy the sound of his heartbeat."

  hide lukassleeping onlayer event
  with dissolve
  $ config.side_image_tag = None
  scene bg bedroomdark
  with dissolve
  pause (1)

  cards open card1

  scene bg bedroomlight
  with fade
  play audio bell
#day 8

  calendar day 8
  if lukas_points >= 3:
   jump lukasnotgone
  else:
   jump lukasgone

label lukasnotgone:

  a "Hmmm..."

  "Oh."

  show lukas sleepy
  with dissolve

  l "Huh?"

  "Dr. Kronauer is still in my bed. He lifts an arm, rubbing his eyes."

  l "What time is it? I should go- I'm sorry Addy."
  a blush "No, it's okay."

  "It feels so strange to wake up with him there, but I have to admit that it feels pretty nice."
  "I shouldn't get used to it though or even ask for it. He needs to go home at night and get some proper rest."

  l "You get your rest."

  "He ruffles my hair before I can try and get out of bed with him."

  a "What about you- are you alright?"
  l "I'm fine. Don't worry about me."

  "Brushing off his clothes, he sighs and gives me a smile that proves to me that he's lying."

  l "I'll see you later. I got to get back to work."

  hide lukas
  with easeoutleft

  "I hope he's okay..."

  jump headtoart

label lukasgone:

  a "Mmm...."

  "When I wake up... Dr. Kronauer is gone. I don't know if I expected him to be here or not. I hope he got the rest he needed."

  jump headtoart

label headtoart:

  play music musicneutral loop

  scene bg hallway1
  with dissolve
  pause (2)
  scene bg cafeteria
  with dissolve

  a sleepy "-yawn-"

  "After a groggy breakfast, I'm on autopilot as I wander over to the clinic to see how I can help Dr. Moore today."

  scene bg hallway1
  with dissolve
  pause (2)
  scene bg clinic
  with dissolve

  play music musicsteven loop

  a thinking "?"

  "That's strange. He's not here?"

  a "Dr. Moore?"
  s "Over here, Addison."

  scene bg stevenoffice2
  with dissolve

  show steven happy
  with dissolve

  s "I've got a surprise for you today!"
  a happy "Really? What is it?"
  s "Your new desk."

  a thinking "?"

  "In the corner of his office , I see a desk that is smaller than Dr. Moore’s desk. It was neatly piled with papers and boxes."

  a thinking "What?"
  s "I wanted you to have somewhere where you could work on your art uninterrupted. I also brought you some art supplies. I wasn't sure what you liked, so I got a little of everything. You should try them out."
  a "You what?"

  play music musicupbeat loop

  "Picking up the boxes, I realize they're all full of colors. There's more crayons, pencils, pens, paints, watercolors, watercolor... pencils? Even a pack of paper in different colors too."

  a surprised "Thank- thank you!"
  s "Of course! You're welcome! You should try them."
  a thinking "But that isn't helping you. I'm supposed to be helping you."
  s "I'm fine, don't worry. You'll be helping me just by staying here with me."
  a "Okay... Okay!"

  hide steven
  $ config.side_image_tag = "alfa"

  show artsupplies onlayer event
  with dissolve
  $ persistent.cg_artsupplies=True

  "My heart is racing! All these fun new colors and mediums. I've never even heard of some of these before!"
  "After working hard to try a little bit of everything, I realized I was so excited that I missed lunch."
  "No matter, I know what I need to do. I need to paint someone a gift!"
  "Who should I paint for today?"

#I need way more Pumpkin choices, the current ranges are really skewed
#you could, at this point have:
#pumpkin points: -1 to 2
#steven points: -4 to 5
#lukas points: -1 to 3

  play sound ding

  menu:
    "Dr. Moore" if (steven_points>=2) or debug_test:
      "Of course, because he gave me all these wonderful supplies in the first place. He has been so kind to me, even though he started out to be a shy person. In the end, he’s now giving me all those stuff to show his kindness. I should return the favor right now!"
      $ steven_points += 2
      $ giftsteven = True
      jump giftmaking
    "Dr. Kronauer" if (lukas_points>=2) or debug_test:
      "Dr. Kroanuer has been busy lately, and he needs something to cheer him up."
      $ lukas_points += 2
      $ giftlukas = True
      jump giftmaking
    "Pumpkin"if (pumpkin_points>=2) or debug_test:
      "Pumpkin has been going through so many changes, and he's moving into his new room. Maybe a picture would be a good way to start decorating it. I can't make it like his secret room with just one picture, but I can try my best."
      $ pumpkin_points += 2
      $ giftpumpkin = True
      jump giftmaking

label giftmaking:

  if not persistent.draw_mode:
    $ persistent.draw_mode=True
    $ renpy.notify("Unlock Draw MODE")

#call screen freehand_draw
#needs to take a screenshot of the drawing and store it when the player is done
#then return to here
  $renpy.scene()
  window hide
  minigame draw start 0
  #$ renpy.free_memory()
  #show screen show_hand_draw(78,108,0) #xpos,ypos,id_draw
  scene bg stevenoffice2
  minigame draw open 160 40 0 #show draw xpos=160,ypos=40,id_draw=0
#######################
  "There. It's not perfect, but I think it'll make him smile."

  s "That looks nice."
  a "Ah!"

  #hide screen show_hand_draw #hide hand_draw
  minigame draw close #hide draw

  hide artsupplies onlayer event
  with dissolve
  $ config.side_image_tag = None
  show steven surprised

  a surprised "!"

  show bg stevenoffice2 with hpunch

  "Dr. Moore startled me, my hands shaking as I lifted the page up off the desk. The colors shudder and run down, the water is not quite dry."

  a sad "Oh no..."
  s thinking "I'm sorry! Did I scare you?"
  a "It's okay, the colors just ran..."
  s "I thought you were doing that on purpose."
  a "... I was."
  s laugh "That's the spirit!"
  a smile "I'll have to let it dry just a little bit longer. What time is it?"
  s "Almost time for me to head out. I was trying to let you know that I'll be leaving soon."

  if giftsteven:
   jump giftsteven
  if giftlukas:
   jump giftlukas
  if giftpumpkin:
   jump giftpumpkin

label giftsteven:

  play music musicsteven loop

  a "Oh, wait- actually, this is for you."
  s thinking "Hm?"

  "I get up and quickly bring the painting over to his desk before he can stand back up."

  a "I made it for you."

  hide steven
  $ config.side_image_tag = "alfa"

  show giftsteven onlayer event with dissolve
  $ renpy.free_memory()
  show screen show_gift_steven(0)
  $ persistent.cg_giftsteven=True

  s "Addison, that's so sweet. Thank you."

  "His smile is so soft and genuine that my heart swells."

  a "I wanted to thank you for everything. You've been doing so much for me and teaching me so much. It's the least I can do."
  if kissedsteven = True:
      "Especially when I'm not allowed to kiss him."

  s "That... That means a lot to me, Addison. Thank you."

  hide giftsteven onlayer event with dissolve
  hide screen show_gift_steven
  $ config.side_image_tag = None
  show steven happy

  s happy "Do you mind if I leave it here overnight so it dries completely?"
  a happy "No, not at all!"
  s "I'll bring a frame for it as soon as I can."
  a blush "You don't have to do that!"
  s "Don't be silly. I really want to."

  "He sets the painting down gingerly on a free space at his desk and packs up his bag."

  s "Have a good night, Addison."
  a "You too."

  "He hesitates."

  a "Hm?"
  s "... Please let me know if you think I can do anything else for you."
  a thinking "No, you've already done so much!"
  s sad smile "Haha, well, if you can think of anything, please let me know."

  "He really gets tense. Is this really just him being shy?"

  s "I really mean it, I want to help. So if you think of anything, just ask."

  hide steven
  with easeoutleft

  "He heads out and I turn to clean up the big mess I've made at my new desk."
  "Something about what he said..."
  "No, something about how he said what he said... It's bothering me."
  "I really have to figure out why he's so tense and nervous around me, around the subject of Felixes even."
  "He has such a kind smile. So why does he always seem so sad?"
  "I finished cleaning up while I pondered those thoughts."

  jump day8end

label giftlukas:

  play music musiclukas loop

  "Oh no. If Dr. Moore is heading out, then Dr. Kronauer is probably leaving too."

  a "Oh- I'll see you tomorrow then! I promise to clean up my mess!"
  s "Huh? No problem, goodnight."
  a "Goodnight!"

  "I scoop up the painting- even if it's still a little damp. I decided to scurry out into the hallway."

  scene bg hallway1
  with dissolve

  "Not here..."

  scene bg hallway2
  with dissolve
  pause (2)
  show lukas neutral
  with dissolve

  a "!!! Dr. Kronauer!"
  l confused "Hm? Addy. Are you okay?"
  a happy "Yeah, I'm fine. I just wanted to see you before you left."
  l happy "Ah, what for?"
  a "This."

  "I offer him the page, hoping he'll like it. He knows I do art, obviously, but... We met when I was 14, but I don't think I ever gave him somthing like this before."
  "He takes the damp paper and looks it over curiously."

  l neutral "..."
  l "..."
  l "Addy, I..."

  hide lukas
  $ config.side_image_tag = "alfa"

  show lukasgift onlayer event
  with dissolve
  $ persistent.cg_lukasgift=True

  "All at once, he's wrapped me up in a tight squeeze. I can't help but to grin as I balance on my toes."

  a "-laugh-"
  l "Addy, thank you. Thank you."
  a "Of course! I thought you needed something to cheer you up, and you're always there for me."
  l "..."

  "For a while, it seems as though he might not let go. But the way his breath tingles at the back of my neck, I don't mind that too much."

  hide lukasgift onlayer event
  with dissolve
  $ config.side_image_tag = None
  show lukas happy


  l happy "Thank you again, Addy."
  a "You're welcome, silly."
  l "Ha-"

  "His eyes linger on the page, before he leans in to give me a kiss on the forehead."

  l "Goodnight."
  a "Night."

  hide lukas
  with easeoutleft

  a "-sigh-"
  "Something really is bothering him."
  "I can tell because we're so close. He's been caring for me for ten years now. We're best friends. He should be able to tell me anything that might be on his mind."
  "So why does it feel like he's hiding something?"
  "I don't want him to feel blue. I want to make him feel better. I want to be there for him, like he's always been there for me."
  "I guess I have to step up and let him know he can talk to me somehow."
  "Hopefully this was a good first step."

  jump day8end

label giftpumpkin:

  play music musicsecretspace loop

  a "Oh, okay. Well I'm going to stay here and clean up my mess. Have a good night."
  s happy "Have a good night, Addison. I'll see you in the morning."

  "I'm true to my word and I let the picture dry out while I sort out the supplies. I wipe them down and place them back in their boxes, sorted by colors, until everything is neat again."
  "Well, almost neat. Some of the boxes don't quite close right anymore. But it's okay, just as long as it's close enough."
  "By the time I finished cleaning, the painting was mostly dry. At this time of night, Pumpkin should be..."
  "Uh..."
  "I have no idea where Pumpkin would be."

  scene bg hallway1
  with dissolve

  "Not here..."

  scene bg classroom
  with dissolve

  "Not here..."

  scene bg cafeteria
  with dissolve

  "Dinner is over and my stomach growls at the thought of missing two meals in a row. He's not here either..."

  scene bg playroom
  with dissolve

  "Oh!"

  show pumpkin happy
  with dissolve

  a "Pumpkin! I was looking for you."
  p confused "Really?"
  a "Yeah, I wanted to give this to you. It's for your new room."

  "He takes the paper and turns it over in his hands."

  p happy "Addy you drew this? For me?"
  a "Yeah."
  p excited "That's amazing!!!"

  "Oh, he has a grip on my arm again."

  p "Come on!"

  scene bg hallway1
  with dissolve

  a "Okay-"

  "He pulls me into his room and immediately tacks the picture to the wall before flopping onto the bed."

  hide pumpkin
  $ config.side_image_tag = "alfa"

  show giftpumpkin onlayer event #if you press "h" all screen hide
  with dissolve
  $ renpy.free_memory()
  show screen show_gift_pumpkin(0)
  $ persistent.cg_giftpumpkin=True

  "Something about his smile makes me feel light. He rambles on and I forget about my empty stomach for the night as I listen to him."

  p "I'm so glad you're my friend."
  a "!"

  "Is that it?"

  a "Me too."

  "Yeah. It's nice to have a friend."
  "I want to be better friends with him. He's such a good boy and now I have a chance to spend more time with him, without the fear of him ever leaving."
  "It's not something I've ever had before."
  "But even so, there's doubts in the back of my mind... our situtations are so different... We're practically oposites."
  "I stayed here because I'm concidered 'broken', but he's staying because he's so pretty and confident..."
  "No one wants me, but everyone want's him..."
  "But that shouldn't change our relationship, right?"
  "We can still become even closer as family."

  scene bg bedroomdark
  hide giftpumpkin onlayer event with fade
  hide screen show_gift_pumpkin
  $ config.side_image_tag = None
label day8end:

  play music musicsleepy loop

  "With all that out of the way, I end up sneaking into the back of the cafeteria and grabbing a few bites of leftovers before heading to bed."
  "I can't believe I worked straight through two meals, but..."
  "I haven't had this much fun in a very long time. Even now I still can't stop smiling."

  scene bg bedroomlight
  with dissolve
  pause (2)
  scene bg bedroomdark
  with dissolve

  a pajamas happy "Ah..."

  "I hope tomorrow goes the same way. Goodnight."

  scene bg bedroomdark
  with dissolve
  pause (1)

  cards open card2

  scene bg bedroomlight
  with fade
  jump day9
