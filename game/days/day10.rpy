#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  day10.rpy
#
#  Copyright 2020
#

label day10:

  calendar day 10

  $ config.window_title=u'Part II - Friends'
  cards open parttwo
  if not achievement.has("part1"):
    $ achievement.grant("part1")

  a pajamas sleepy "Mhh."
  "Happy monday."
  "None of the kittens or the staff like Monday because classes and work start again for the week. Since I stopped taking classes though, the edge of Mondays have worn off."
  "I don't dislike them, though I don't really like them either."
  "It's just another day to get up and get dressed, to brush out my hair and my fur, wash my face, and eat breakfast."

  scene bg hallway1
  with dissolve
  pause (2)
  scene bg cafeteria
  with dissolve

  "Today's breakfast is thick sourdough slices with eggs and tomatoes."
  "I sit down in my corner so I can watch over all of the kittens and sip from my carton of milk."
  "The air has a buzz of electricity in it. I can feel the hairs on the back of my neck and on my tail start to stand on end..."
  a sad "No, not again..."
  "Haven't we had enough kittens adopted this month?"
  "I have so much else to deal with."
  "It's so rude of me, so selfish and wrong but..."
  "Please don't let someone be adopted..."

  c "No! No!"
  "Oh no..."

  show charlie sad
  with dissolve

  "He's a mess."

  $ config.side_image_tag = "alfa"
  show charliecrying onlayer event
  with dissolve
  $ persistent.cg_charliecrying=True

  c "No! Nooo!!!"
  a "Charlie, oh dear..."

  "I get up and find him, kneeling down and wrapping my arms around his little body. Even if no one has said it yet, I still know exactly what's going on."

  c "Ainsleyyyyy..."
  a "Shhh.... It's alright. She's with her Master now."

  "I pet his hair, knowing it wont help the hurt in his heart."

  c "But I w-want..."
  a "Shhh... But her Master wants her. You can't say no to that."
  c "Waahhhhh!!!!"

  "He bursts out into another round of sobs."

  a "We have to be happy for her. She's going to have a lot of fun now."
  c "Wahhhhh!!!"
  a "-sigh-"

  "I can only do so much... And right now it feels pointless to try and help. I'm powerless to make him feel better..."
  "They were best friends, inseparable in every way."
  "Now he'll have to learn how to play by himself or make new friends..."
  "New friends that could also be taken away from him at any time."

  a "Shh... It'll be okay."

  "I keep petting his smooth hair as his tears soak my cardigan."

  hide image charliecrying onlayer event
  with dissolve
  $ config.side_image_tag = None

  "The other kittens are upset as well, but I have to stay with Charlie."
  "Not only is he hit the hardest by this, but his tears are also going to inspire the others to cry more."
  "There's no point in trying to force him to eat now. So I let him cry into me and pat his back for as long as he needs, and then slowly escort him to morning classes."

  scene bg hallway1
  show charlie sad
  with dissolve
  pause (2)
  scene bg classroom
  show charlie sad
  with dissolve

  a "-sigh-"
  c "-sniff-"

  hide charrlie
  with dissolve

  scene bg hallway1
  with dissolve
  pause (2)
  scene bg clinic
  with dissolve
  show steven neutral
  with dissolve

  "Oh no..."
  "I didn't even think about Dr. Moore."
  "He had grown really close to Ainsley. But he must understand it better than the kittens..."
  "She's with her Master now, so it's a time to be happy."
  "So why does he look so heartbroken?"

  s smile "Hello Addison."

  "He's smiling without his eyes..."

  a "Good morning."

  "I turn to go straight to organizing the shelves. Something about Dr. Moore is making my stomach turn over. I can't look him in the face."

  a mad "..."

  "This should be a happy time!!"
  "So why does it feel so..."

  s "Ah- Fuck."
  a confused "Huh?"
  s "Mh- Sorry Addison. You didn't hear me say that."

  "When I turn around I can see that Dr. More has dropped a pile of papers onto the floor."

  a surprised "Oh, here, let me help."
  s "No. I'll get it. Could you unpack the new supplies that came in?"
  a "Oh, alright."

  "I go to the back of the room to the shrink wrapped boxes to pull out the needles, gloves, and facemasks."
  "Behind me I can hear Dr. Moore cleaning up his papers."
  "The air is stiff and I feel my own heart pounding as I pull out and organize supplies."
  "..."
  "..."
  "Should I say something?"
  "Or should I let Dr. Moore do the talking?"
  "I have to come up behind him to refill a roll of paper towels. He looks up from his desk to follow the movement of my hand."
  "Oh right- Addison. Could you unpack the new supplies in the back?"
  a confused "That's what I'm doing."
  s confused "Oh. Sorry then."
  "..."
  "I go back to work, my ears trained on Dr. Moore."
  "Maybe he's sick?"
  "His breathing sounds fine. All I can hear is the tap of his keyboard."
  "..."
  s "I'll be right back. I'm going to step out."
  a "Oh, okay."
  "Where is he going?"
  "He closes the clinic door behind him. My feet turn in the direction of the door."

  hide steven
  with dissolve

  menu:
    "Check on Dr. Moore":
      $ steven_points += 1
      "I should check on him, since he's not acting like himself."
      "I open the door, not expecting to see anything, but-"
      jump checkonsteven
    "Let him have his space":
      "I'll let him have some space..."
      jump day10space

label checkonsteven:

  $ config.side_image_tag ="alfa"
  show stevencrying1 onlayer event
  with dissolve
  $ persistent.cg_stevencrying1=True

  a "Ah-"
  s "Mh-"

  show stevencrying2 onlayer event
  hide stevencrying1 onlayer event
  with dissolve

  s "Addison- I-"
  a "It's okay. It's what I'm here for."

  "His face bunches up as he holds back more tears. I know it's not seen as correct for human men to cry. He must be trying really hard."

  a "I'll miss her too."
  s "Mhh-"

  hide image stevencrying2 onlayer event
  with dissolve
  $ config.side_image_tag = None

  scene bg hallway1
  show steven sad
  with dissolve

  s "I-I know."
  "He wipes his eyes hastily."
  s "I shouldn't be acting like this."
  a "You can act however you want."
  s confused "?"
  a "Feelings are important. You can feel however you need to. You're allowed."
  a "And you can act however you need to. If you need to cry, or be mad. It's okay."
  a "You have to feel your feelings or it'll hurt you inside even more."
  a "And you're a human, so you can do whatever you want, you don't have to feel ashamed."
  s sad "..."

  "He slips back into the clinic without saying a word."
  "I think I helped though."

  scene bg clinic
  show steven sad
  with dissolve

label day10space:

  "He doesn't say anything for the rest of the time I'm there."
  "I just work so I can help him feel better, in whatever way I can."
  "When I leave for lunch I slip out without saying goodbye."
  "I think Dr. Moore needs the quiet right now."
  "I wish I could help him in more normal ways."
  "I wish I could hold him and pet his hair and tell him it was going to be okay, like I did with Charlie."
  "Dr. More isn't like that though. He doesn't like being touched."
  "I used to think that maybe he didn't like me, but that can't be true... Right?"
  "He just doesn't like that I'm here at Helix, without a Master."
  "It's unnatural for a Felix to be without a Master."
  "I'm a freak."

  hide steven
  with dissolve
  scene bg hallway1
  with dissolve
  pause (2)
  scene bg officespace
  with dissolve
  pause (2)
  scene bg lukasoffice
  with dissolve
  show lukas neutral
  with dissolve

  l happy "Hey there."
  a sad "Hey..."
  l confused "Oh no, what's that face about?"

  menu:
    "Do you think Dr. Moore will be okay?":
      a "Ainsley got adopted this morning."
      l "I know."
      a "... I don't think Dr. Moore is okay."
      l "He got attached, Felixes are cute and designed to do that. He'll be okay in a while."
      a "You really think so?"
      l "I think so. He acts like he's all tough, but he's got a big soft spot for you kittens."
      l "-sigh-"
      l sad smile "He'll be okay. Just give him some time."
      a "Okay..."
      jump continueday10
    "Is Pumpkin... better than me?":
      a "Is Pumpkin... better than me?"
      l confused "Where in the world did that come from? Of course not."
      a "Well he, he has to stay at Helix because he's so pretty... and I have to stay because I'm broken..."
      l angry "Who told you that you were broken?"
      l sad "Addy, you're perfect the way you are. We all want you here. It wasn't a punishment to keep you here."
      l sad smile "And if you weren't here you wouldn't be with me. It's good that you're here..."
      a "..."
      l "Come here."
      "I step closer and Dr. Kronauer holds me in a soft hug."
      l "I love you, Addy. Everyone here loves you. You're perfect. Please don't think you're anything less."
      a "..."
      a "Okay."

label continueday10:

  "I can't really argue with that..."
  "But I still don't know how to help Dr. Moore, or Charlie..."
  "It feels like I'm failing at all of my jobs."
  "Dr. Kronauer holds and pets me during lunch. I sink down to the floor, finding it hard to stay in his lap like this, and sit at his feet."
  "His fingers in my hair feel nice, but they don't solve anything."
  "I eat what I can and say goodbye softly."
  "He kisses my forehead."
  l "It'll be okay."
  a "Mhm..."

  hide lukas
  with dissolve

  scene bg hallway1
  with dissolve
  pause (2)
  scene bg clinic
  with dissolve
  show steven neutral at myright
  with dissolve

  "I hadn't finished all the work in the clinic, and, to be honest..."
  "My stomach is in knots at the idea of facing the kittens right now."
  "So I came back to finish up and maybe check on Dr. Moore, but it looks like nothing has changed."
  "He's still silent and the air is still thick."
  "I keep my mouth shut and stock the cupboards."
  "..."

  show lukas neutral at myleft
  with easeinleft

  a confused "?"
  "What's Dr. Kronauer doing here?"
  "He glances at me before turning to Dr. Moore."
  l "Hey, Steven. I heard you're having a long day."
  s angry "..."
  l "I just wanted to see if you-"

  s "I don't need anything."
  "He doesn't even look up to Dr. Kronauer."
  s "I'm busy"
  l sad smile "You should take a break, no one would blame you."
  l "You don't have to hide in your work."
  l "The first time one leaves is really hard, and I know she was-"
  s "I'm not taking advice from you."
  "I wince. Dr. Moore isn't very good at talking..."
  l "Well,"
  s "I'm fine. I looked into the family that adopted her. She's going to be safe."
  l "Well-"
  s "So there's no problem. I have to get back to work now."
  l "..."

  "Dr Kronauer gives me another glance before sighing and heading back into the hallway, presumably back to his office."

  hide lukas
  with easeoutleft

  s "..."
  "It stays quiet for another few minutes."
  s "I'm sorry you had to hear that, Addison."
  a "It's okay."
  a "Not everyone can get along... it's okay..."

  "Really, it's not okay, but it's not my place to get involved."
  "I can solve disagreements between the kittens easily. I just make them talk to each other until the issue gets sorted out."
  "But it's not that easy with humans, and while I know that office politics is messy..."
  "It hurts that they can't be friends, since I like them both so much."
  "..."
  "I finish up my tasks and slink off to dinner."

  hide steven
  with dissolve

  scene bg hallway1
  with dissolve
  pause (2)
  scene bg cafeteria
  with dissolve

  a sad "-sigh-"
  "No Pumpkin tonight either..."
  "... Breakfast was too chaotic for me to notice if he was here or not, but I could really use him right now..."
  "I don't know what I would say, but I wish I could talk to someone..."
  "I pick at my meatloaf while I think, the kittens quiet and somber as they eat."
  "Charlie is still sniffling, but he's going to be okay..."

  scene bg hallway1
  with dissolve
  pause (2)
  scene bg barracks
  with dissolve

  "I feel like a ghost all night, going through the motions of getting the kittens showered and changed into their pajamas."
  "I read them their book, but I can't get the voices right tonight."
  "Nothing is going my way..."

  scene bg hallway1
  with dissolve
  pause (2)
  scene bg bedroomlight
  with dissolve

  a pajamas sad "Goodnight..."

  scene bg bedroomdark
  with dissolve

  cards open card4

  jump day11
