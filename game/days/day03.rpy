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

#day 3
label day3:
  calendar day 3
  play audio bell
  "Already morning? I stretch and feel my back crack with a satisfying 'pop.' I hope I'm not getting old. But that pop still feels good, so I don't think so."

  scene bg hallway1
  with dissolve
  pause (2)
  scene bg cafeteria
  with dissolve

  play music musicneutral loop

  "Oatmeal this morning. I mix raisins, apple bits, and milk into mine."
  "Drug Day is always oatmeal because it's nice and filling, but simple, so the shots don't make our tummies upset. I like oatmeal so I don't mind, but I have to make sure some of the kittens finish their bowls first."

  show charlie sad
  with easeinright

  c "Addy, I don't want to."
  a "Come on, it's just a few more bites."
  c "But I don't like it."
  a "I know, but please?"
  c " .... Yuck."
  a "Oh, it can't be that bad."
  c "Yuck. It's gross!"

  "He really has his way with words."

  a "But you're a big responsible boy! You can finish your oatmeal, right?"
  c " ... ... Yuck."

  hide charlie
  with easeoutright

  scene bg hallway1
  with dissolve

  "After breakfast we all lined up in the hallway for our shots. I'm always at the end because I have to watch over everyone, as usual."
  "I lean against the wall, letting my mind wander. However, when I think about Dr. Moore, the way he looked at me was weird. He is still pretty handsome though, so it isn't too hard to imagine him relaxing a little if he spent some time with me."
  "A movement out of the corner of my eye and I stand upright again."

  show pumpkin thinking
  with easeinright

  a surprised "What are you doing, Pumpkin? You'll lose your place in line."
  show pumpkin nervous
  with dissolve
  p "Haha, that's okay. Is it okay if I stand with you?"
  a thinking "Yeah. You're still nervous about your test aren't you?"
  p "Well..."
  a happy "It's after the shots, right? I told you, you're going to do great."
  p "Yeah, I know..."

  "He still doesn't look convinced, so I grab a shoulder and give a reassuring squeeze."

  a "I hope I can see the pictures. You're going to be so handsome."
  show pumpkin blush
  with dissolve
  p "Haha. Yeah, I will."

  show pumpkin nervous
  with dissolve

  "That didn't help the way I hoped it would."

  p "I was just wondering, I mean, I thought that maybe I would feel better- I mean it would be better- if you, if you come with me to the test."

  "Pumpkin never stumbles over his words, so I have to stop and think about it. Is he being really serious? Or is he that nervous? This kind of face should be perfect for the test because he's so cute--he'll pass easily."

  a "It's right after shots? But isn't that lunch time?"
  p "They said they would feed me there."
  a "Oh..."

  "I always try to have lunch with Dr. Kronauer though, I can see him getting lonely and sad if I didn't show up today..."
  "Before I can answer though, the lines moved far enough that it's my turn to get my shot. I give Pumpkin a small smile before ducking through the door."

  a "Sorry, I'll be right back."

  "Maybe that'll give me some time to think things over."

  scene bg clinic
  with dissolve

  show steven happy
  with easeinleft

  s "Oh good morning, Addison. It's good to see you again."
  a "Ah, nice to see you too."

  "He doesn't look half as nervous as he was yesterday. He's even smiling. I sit down as he unwraps a clean needle and measures out the diazepine. There's a moment of silence and I'm desperate to fill it."

  show steven at zoom_in

  hide steven
  $ config.side_image_tag = "alfa"
  show shot onlayer event
  with dissolve
  $ persistent.cg_shot=True

  play sound ding

  menu:
    "Flirt with Dr. Moore":
      $ steven_points -= 1
      $ kissedsteven = True
      jump flirt
    "Ask a question":
      $ steven_points += 1
      jump question

label flirt:

  a "You're very handsome."
  s "Excuse me?"
  a "You're very handsome."
  s "Ah, well, thank you."

  "It doesn't seem like he's going to be comfortable enough to make the first move. So I lean in and kiss him on the cheek, hoping that will make him a little more confident. Instead he pulls back."

  hide shot onlayer event
  with dissolve
  $ config.side_image_tag = "addison"

  show steven angry at zoom_off, center

  s "Addison, stop."
  a thinking "O-Okay."
  a sad "Sorry, I'll go."
  show steven sad
  with dissolve
  s "No Addison, I'm not angry with you. Just- Don't kiss me. I know you're... used to being personal with everyone, but I would rather not."

  "So he doesn't want me around?"

  a "Okay... Do you want me to leave you alone?"
  show steven sigh
  with dissolve
  s "Yes. I mean. No, I need to ask you something... I want to get to know you. I just don't want- I don't like being touched without my permission."
  a "Oh."

  jump continueday3

label question:

  a "What's your favorite color?"
  s "? ... My favorite color? Ah, I guess blue. Why?"
  a "I just want to learn more about you since you're new."
  s "Oh, well, you can ask me whatever you like then."
  a "Hm, well what else do you like?"
  s "Um ... Oreos?"
  a "What are Oreos?"
  s "A type of cookie."
  a "Oh! Okay. Uh,"
  a "Why did you want to work here?"

  hide shot onlayer event
  with dissolve
  $ config.side_image_tag = "addison"

  show steven thinking

  s "Ah, well, I wanted to... work with you and the rest of the Felixes. I wanted... I wanted to take care of you all. Someone needs to take care of you all."


  a excited "I think you're going to do great!"

label continueday3:

  show steven happy
  with dissolve

  s "We don't have a lot of time right now, but I know you like to help out a lot, so I wanted to ask for your help. There's a lot of Felixes here, and I don't know if it's going to take me awhile to get used to this place."
  s "In the meantime, I was thinking since the kids are already so fond of you, you could maybe help me with tasks here in the clinic?"
  s "I didn't realize I wouldn't have an assistant, and you're the eldest..."

  a happy "Oh, I can help!"
  s "Thank you, that'll help me a lot. I'll see you later then, Addison. Oh, wait- before you go."

  if stickers == True:
    "He grins and reaches over to a bowl on the counter, offering me a piece of paper in the shape of a square."
    s "I brought stickers today. The kids have been liking them so far."

  if candy == True:
    "I take a piece of candy from his bowl before leaving."

  a excited "Thank you!"

  hide steven
  with easeoutleft

  scene bg hallway1
  with dissolve

  show pumpkin nervous
  with easeinright

  a sad "..."

  p "Addy, please wait for me. I really want you to come with me."

  "Oh, he's finally being direct about it. Well..."

  play sound ding

  menu:
    "Of course I can!":
      $ pumpkin_points += 1
      $ lukas_points -= 1
      $ test = True
      jump followpumpkin
    "I have lunch with Dr. Kronauer, though.":
      $ pumpkin_points -= 1
      $ lukas_points += 1
      jump followlukas

label followpumpkin:

  play music musicupbeat loop

  a "Yeah of course I'll come with you! I'll get to see you all pretty and it's my job as your big brother to help out. Don't worry, I'll wait."

  show pumpkin happy
  with dissolve

  p "Okay!"

  hide pumpkin
  with dissolve

  "Dr. Kronauer will understand I had to help Pumpkin with his nerves. When Pumpkin's back, he pops out of the door like a spring and grabs my arm."

  show pumpkin excited
  with dissolve

  p "Okay, let's go!"

  a surprised "Oh!"

  scene bg hallway2
  show pumpkin happy at myleft
  with dissolve

  a "So where is it?"
  p "Mr. Jesse said to meet him over here."

  show jesse neutral at myright
  with easeinright

  j "There you are. What did you bring Addison for?"

  a happy "Moral support."

  "Mr. Jesse seems to accept this and shrugs, unlocking the keycard door to another hallway. I don't think I've ever been this way, but it looks almost exactly the same."

  scene bg hallway1
  show pumpkin happy at myleft
  show jesse neutral at myright
  with dissolve

  j "In here."

  scene bg filmset
  with dissolve
  $ persistent.bg_filmset=True

  show pumpkin surprised at myleft
  show jesse neutral at myright
  with dissolve

  a surprised "Wow..."
  p "Whoa..."

  "It's a big room full of lights and cameras. Even from here I can tell that the lights are warm. Mr. Jesse ushers us over to a couch. A lady with a stack of papers welcomes us over."

  o "Welcome! You must be Pumpkin!"

  "Her cheerful smile becomes confused as she looks over me."

  o "And this is..?"

  a "Addison. I'm just here for Pumpkin."

  o "Oh, okay. Well, Pumpkin, you know why you're here, right?"
  p "Yes. I mean, to be pretty, right?"

  "The lady chuckles."

  o "They must not have explained it very well. You're going to be the face of all of the Felixes."
  o "Yes, you'll be very pretty. But you're going to have a lot to do."
  o "You'll be making promotional materials for Helix Scientific, both photography and video. You're going to be modeling in lots of clothes and eventually doing product and location shoots."

  "She hands over a thin book with glossy pages, and I start leaning over Pumpkin's shoulder to try and look at it with him. The cover has a picture of a pretty girl printed on it."
  "She talks fast and I get the feeling she's trying to water things down for us, but I wouldn't dare to let on that I really don't understand what she's saying."

  o "This has quite a few examples of what you'll be doing for us."

  "Pumpkin flips through the pages. It's full of pictures of pretty looking people. I don't really understand the point of the pictures, but glancing up at Pumpkin's face, he seems happy with it."

  p "This looks really fun."
  o "I thought you might say that. Today we're going to just be doing some photography so you can get used to the makeup and clothes. How does that sound?"
  show pumpkin excited
  with dissolve
  p "Great!"

  hide jesse
  with easeoutright
  hide pumpkin
  with easeoutright

  "Before I knew it, Mr. Jesse and the lady are whisking Pumpkin away. I try to stand and follow, but from the looks on everyone's faces... "

  a sad "Oh..."

  "... I don't think I'm supposed to follow. Was it a bad idea to come with?"
  "He disappears behind another door, and I squirm nervously on the seat. Out here are humans setting up big spider-legged cameras and tall, hot lights."
  "While I'm waiting for Pumpkin I pick the book back up, taking my time to look over the pictures page by page."
  "Those people are all humans, most of them frowning as they wear colorful clothes and strike in strange poses."
  "They're all pretty, and Pumpkin would fit in among them, though I don't think he can make a face as serious as these people."
  "Usually he's smiling wide or he looks just like he buried treasure."
  "The huge cloth in front of the cameras must be normal, but I see some of the pictures are in houses, gardens, or places I can't even recognize."

  "Will Pumpkin be going places for this job? Or will he stay here with me?"

  p "Addy, look!"

  show pumpkin makeup_excited
  with easeinleft

  a surprised "Oh!"
  a happy "You look so pretty!"
  p "I do!"

  "He twirls for me, showing off his new clothes and his strangly painted face."

  j "Okay, enough showing off-- let's go."

  hide pumpkin
  with easeoutleft

  "He scrambles back to Mr. Jesse and the lady, where I can hear them talking about the camera and how to follow directions from the man behind it."
  "I lean my arm over the top of the couch to settle in and watch."
  "I don't think Pumpkin needed me here after all."

  a happy "..."

  $ config.side_image_tag = "alfa"
  show pumpkin_model onlayer event
  with dissolve
  $ persistent.cg_pumpkin_model=True

  "It's a few hours I watch him. At first, his smiles were big and goofy, his poses were also wild and exaggerated."
  "But the cameraman gives him a lot of directions, and by his third set of clothes I wouldn't be able to tell if his poses were from that thin book the lady had shown us before."
  "The outfits were really interesting to watch. We've always worn our uniforms, and I don't even have any other clothes except for the pajamas that Dr. Kronauer gave me."
  "I knew about the clothes that the staff wore, but Pumpkin wasn't dressing in button ups and jeans."
  "They almost looked like costumes, with bright colors, printed images, or silly zippers that didn't seem like they could do anything."
  "Even if they made me giggle, Pumpkin would enthusiastically show them off to me each time he changed before going back in front of the camera."
  "The camera man says something about lunch, so Pumpkin hops over to me, grabbing my hand and pulling me along."

  hide pumpkin_model onlayer event
  with dissolve
  $ config.side_image_tag = "addsion"

  show pumpkin excited
  with easeinleft

  p "Lunch time! We can have whatever we want."

  "There's a table filled with snacks and paper plates. It certainly doesn't look like lunch from the cafeteria or from Dr. Kronauer either."

  p "Those lights are really hot, but I'm having a lot of fun! Do I look good?"
  a "Yeah, you look great. I liked those scarves you wore."

  "He giggles, piling a paper plate with some lunch meat and baby carrots. I have to hold myself back from taking two yogurt cups."

  p "Yeah! They were cute. There's so many clothes in the back room! You wouldn't believe it!"
  a "Hahaha, yeah?"
  p "Mmmm-hmmm!"

  "His mouth is full, but he keeps talking anyways."

  p "I'll eventually get to try all of them!"
  a "I'm glad you're having fun."
  p "Yep! After this they said that someone else will take pictures with me too."
  a thinking "Someone else?"
  show pumpkin nervous
  with dissolve
  p "Yeah, someone pretending to be my Master."
  show pumpkin happy
  with dissolve
  p "I'm excited! I hope he's cute."
  a happy "Mmhm."

  "He inhales his food and scrambles back up to the stage. At least I can take my time with mine, I haven't even touched anything yet. It's hard for me to eat and talk at the same time."
  "It's obvious that Pumpkin doesn't have that kind of problem."
  "The only time he seems even vaguely nervous is when a man comes onto the stage with him, I overhear them speaking."
  "Ah, that man is going to pretend to be Pumpkin's Master."
  "That would make me nervous too."
  "But he's back on his feet in no time, the two widen their silly grins as they hug each other and hold hands. I find myself smiling just watching them. It's cute. Pumpkin is adorable."
  "It goes on like this for about a few more hours. I really didn't think that it would be an all day event."
  "Pumpkin changed back into his facility clothes, then he startles me from a daydream as he starts jabbering excitedly."

  show pumpkin excited
  with dissolve

  p "Addy! Wasn't it super fun?! I'm so excited, but boy I'm tired! It's a lot of work being this cute! Come on, we gotta eat something before we leave-- dinner is already over."
  p "What was your favorite part? Did you see Samuel? He was my fake Master. He's pretty cute, don't you think? These crackers are really good. I want to get out of here so bad. Augh- come on, grab a whole plate of stuff and let's go!"

  "After I barely stumble to the snack table, he's still dragging me around, but there's not as much strength in his grip as there was this morning. All that playing and work must have taken a lot out of him."

  scene bg hallway2
  show pumpkin happy
  with dissolve
  $ persistent.bg_hallway2=True

  play music musicsleepy loop

  "He sure has gotten quiet too."

  a thinking "Where are we going?"
  p "It's a secret."

  "I don't think I've been down this hallway before. It's not out of limits, but as far as I know there's nothing this way."
  "Pumpkin stops at a random door, peeking back and forth down the hallway before pulling me inside."
  "It's just an empty office."

  scene bg stevenoffice1
  show pumpkin happy
  with dissolve

  a "What are we doing here?"
  p "Shhh."

  "He moves over to a bookcase and pulls it aside, revealing... a small door?"

  a "What is that?"
  p "My secret space."

  scene bg secretspace
  show pumpkin happy
  with dissolve
  $ persistent.bg_secretspace=True

  play music musicsecretspace loop

  a excited "Wow!"
  show pumpkin excited
  with dissolve
  p "Yep. This is all mine. Nobody has ever seen it before but you."
  a "How did you do all this? How did you even find this place?"
  show pumpkin happy
  with dissolve
  p "I found it a really long time ago. Then I saved up some sheets and some holiday decorations that Mr. Jesse was throwing out. I've even got pillows, and Christmas lights, and-"
  a "You put all this together?"
  p "Yeah, aren't you listening? The Christmas lights were dead but it's easy to get them to turn on again. There's a little glass tube in the plug that you have to move."
  a "Wow..."

  "Really, it was like a blanket fort that the kittens would make, but it's lit up and it feels so much cozier too."

  a "How did no one find out?"
  p "I'm sneaky."
  a happy "You sure are."
  p "Now move over, I'm tired and I want to lay down."

  $ config.side_image_tag = "alfa"
  show secretspace onlayer event
  with dissolve
  $ persistent.cg_secretspace=True

  "I scoot over to the wall, one of the blankets draped from the ceiling begin to brush against my ear."
  "The space was tiny, it was hard to do much but sit and crawl. Pumpkin shifted and leaned against me, finding a few pillows to make it more comfortable. I smiled and opened my arms, letting him settle against my chest."
  "He yawned wide and closed his eyes."

  a "Tired?"
  p "Mm-hmm. It was a lot of hard work today..."
  a "You did amazing. I thought you were really handsome."
  p "I was."
  a "Do you think you'll like this job?"
  p "Yeah..."

  "He yawns again, wrapping one of his arms over me."

  p "I think I'll like it."

  a "Yeah, I think you will too."

  "I lean back and let my eyes unfocus, the twinkling Christmas lights blurring and spreading in a very satisfying lack of pattern."

  a "I still can't believe you set this place up. It's so cozy... and there's so much in here."
  p "It took a long time, but it's perfect."

  "His reply feels cut short, he's probably just tired."

  a "You saved all of this from being thrown away?"
  p "Yeah, most of it. Some of it I just stole."
  a "You stole it?"
  p "Yeah, but nobody noticed, so it can't have been that bad. Like those Halloween decorations. I always need more of those."

  "I grin. Halloween is Pumpkin's favorite holiday, obviously."
  "We talk idly. I get the feeling he wants to ask me something, but he's not able to. Instead of worrying too much about it I just try and stay comfortable for him, playing with his curls while he rests his eyes."
  "If my intuition is right, he never brings up what's on his mind. Instead his responses get slower and slower until he falls asleep in my lap."
  "He had a big day today, he needs the rest."
  "There's no clock in here so I'm not sure how Pumpkin follows his schedule. However when I jerk awake when there is a distinct feeling in my legs that I've been here longer than I should have."

  a "Pumpkin?"
  "He's still asleep in my arms."
  p "Hm?"
  a "It's late. I think it's past lights out."
  p "Oh... You can go to bed. I can stay here..."
  "He lazily flops back down."
  a "No- won't everyone notice that you're gone? I don't want you to get in trouble or for anyone to find out about this place."
  p "Mmmhhhh..."
  "He rolls over."
  p "I guess, but I gotta sneak in then..."
  a "I can help."
  p "Mhhh..."
  a "Come on. I can say you were with me."
  p "Auuuu... Fine."

  "I get him up and we go back into the hallway."

  hide secretspace onlayer event
  with dissolve
  pause (2)
  $ config.side_image_tag = "addison"
  show bg hallway1
  show pumpkin happy
  with dissolve

  play music musicsleepy loop

  "Mr. Jesse shouldn't be out at this time. He has to sleep, too."

  scene bg barracks
  show pumpkin happy
  with dissolve

  "We quietly tiptoe our way back and I open the door to the kittens' room as slowly as possible."

  a "Okay."

  "The kittens don't stir."

  a surprised "!! Oh!"

  "Pumpkin hugs me from behind, nuzzling his face and nose into my neck. It's still warm from his sleep."

  p "Thanks Addy..."

  "I think he's still asleep."

  a happy "You're welcome, Pumpkin. Goodnight."
  p "Goodnight..."

  hide pumpkin
  with easeoutright

  "He wanders into the dark room and I make sure he gets under his blankets before closing the door."

  a "-sigh-"

  "Time for bed then."

  scene bg hallway1
  with dissolve
  pause (2)
  scene bg bedroomlight
  with dissolve

  "Goodnight."

  show bg bedroomdark
  with dissolve

  cards open card4

  jump day4

label followlukas:

  play music musiclukas loop

  a sad "Dr. Kronauer is really... sensitive. He'll be sad if I don't spend lunch with him."
  show pumpkin sad
  with dissolve
  p "Oh, okay. I'll see you later then."

  "Pumpkin turns and closes the clinic door behind him."

  hide pumpkin
  with easeoutright

  "I just made Pumpkin really sad, didn't I?"
  "This isn't like him. He's always energetic and he's always loud. That means he'll be okay soon, right?"
  "I turn the other direction and hurry down the hall to the stairs to get to Dr. Kronauer's office."

  scene bg officespace
  with dissolve
  pause (2)
  scene bg lukasoffice
  with dissolve

  show lukas sleepy
  with easeinleft

  a thinking "He doesn't look so good, either."
  show lukas sad smile
  with dissolve
  l "Oh, Addison. I'm still in the middle of work, but you can sit with me for a while. That would be great."
  a "Sure ... Are you okay?"
  l "I'm fine, just busy."
  a "Alright..."

  "I kick my legs and watch him from my seat, eyeing his desk to see if I can grab his lunch box and at least heat up the food for us. I spy it under the table."

  play sound ding

  menu:
    "Heat up the food":
      $ lukas_points += 1
      jump heatfood
    "Ask a question":
      $ steven_points += 1
      jump askaboutnumbers

label askaboutnumbers:

  a "Dr. Kronauer?"
  l "Hm?"

  "He glances up from his screen, eyes wide and curious."

  a "Has Dr. Moore never seen a Felix before?"
  show lukas confused
  with dissolve
  l "Why are you asking me?"
  a nervous "Well he, he's... a little hard to talk to."
  show lukas happy
  with dissolve
  l "Ha, you can say that again. Uh... yeah, he probably had never seen one before he came here. Why do you ask?"
  a "It's just, he always acts pretty odd around me. Is he just uncomfortable aorund me?"
  l "I don't think it's just around you. Don't worry about him, I'm sure he'll thaw out eventually. Some people will take a little while to get used to their new surroundings."
  a "Yeah, okay."

label heatfood:

  "I kick my legs again and sigh. When I look back up, Dr. Kronauer is typing again. Is he ever going to eat?"
  "Well, it's my job to take care of him anyways. I hop down and scoop up his lunchbox from the floor."
  show lukas confused
  with dissolve
  l "Oh, what are you doing?"
  a "I'm heating up our lunch."
  l "Oh, sorry- yeah. That's fine."

  scene bg officespace
  with dissolve

  "It isn't hard to help out like this, but it makes me worry a little. If something as easy as eating is something Dr. Kronauer is willing to skip... why is he working so hard? I know the answer can't be that simple. He talks about management and about how they push him to make unrealistic deadlines..."
  "That's probably it, but he's never been like this before."

  scene bg lukasoffice
  with dissolve

  a "Here you go."
  l "Ah, thanks."

  "I eat and keep an eye on him at the same time. He barely touches his food and it only makes me frown harder. I eventually set the tupperware aside to wash later and I stood behind him, leaning over his shoulder to look at his screen."
  "There wrer lots of numbers and lots of other things I didn't even understand. I set my hands on his shoulders and wondered..."

  a "You seem really stressed."

  "His shoulders really are stiff, and he hasn't touched his food yet. I try pushing harder on the muscles, my fingertips straining against his shirt fabric."

  l "-sigh- You see right through me, don't you Addy?"

  "He switches between windows and even more numbers come up, these with shapes and diagrams of what could be molecules. I can't read that fast-- otherwise maybe I could make sense of it."
  "No matter. Instead I settle my hands on his neck, then I rub gently along his jaw and collar bones."

  l "Addison."

  "I can tell he's trying to sound angry so he can threaten me, but I see right through it."

  a "Can't I rub your shoulders?"

  "He makes a huff, and then he stays quiet."
  "Good. He needs some attention and love, otherwise he's going to work too hard and hurt himself."
  "I continue on, running my thumbs along the back of his neck and into his hairline. I can feel his spine and the tendons around it, his pulse, and I can smell his shampoo. It's light, but there..."
  "I rub around the base of his neck, and then around and back to the front where I loosen his tie."
  "..."
  "He doesn't protest. He keeps typing, and I run my palms under his shirt, pressing firmly, fingers rounding, the pressure lets me feel he is rather tight not just in his shoulders, but it's all over..."
  "Maybe I should give him massages more often."
  "I learned a while ago how to do it, the management brought someone in to teach me. It was really nice to have the classes all to myself-- it made me feel really special. I don't rub people much though, unless they are at their desks."
  "Then I really like chatting and giving shoulder massages at the same time."
  "When I feel like I've loosened it as much as I can, I let my hands slide down his chest as I lean in, nuzzling my nose against his ear and smiling as I close my eyes."

  a "Dr. Kronauer, I think you need a break."

  play music musictender loop

  "He doesn't look up and me, but when I peek, I can see him smiling."

  l happy "Who taught you to behave like this?"
  a "Like what?"
  l "Like a horny flirt."
  a "Hmmm... Even if I knew, I keep private matters private, sir."

  "I try not to giggle and kiss his ear, letting my lips linger there."
  "We've been having sex since I was 18. He was the first person I trusted, the only person.  This is nothing new, and neither is me teasing him."

  a "But if you promise to keep it as a secret, I'll let you know- it was you, sir."
  l "Ha- Addy-"

  "Finally I get him to turn around in his chair and face me."

  l sad smile "Was it really just me?"

  "I tilt my head to the side, feigning thought. I touch a finger to my own lips, looking up at the ceiling."

  a "Ahh... maybe not /just/ you."

  "Lots of people like my company, including the more intimate things. That's what Staff Companion means. Anyways, I can't really say that anyone taught me to be any way in particular, I just do things that I like and that I know other people like. But it's a lot of fun to tease Dr. Kronauer, because we're such good friends."

  a "You just like me the most."
  l happy "I love you, Addy."

  "He reaches up and with his hands on my hips he grins up at me."

  l "If you want, your toy's in my bottom drawer."
  a excited "Yes!!"

  "He knows /me/ too well."
  "I'm already on it, on my knees as I pull open the drawer with a loud KER-THUNK. Dr. Kronauer is chuckling in his seat."

  a thinking "What?"
  l "I'm just so lucky."
  if persistent._legal_age == True:
      play sound ding
      menu:
        "Skip Sex Scene":
            jump skipride
        "Continue Scene":
            jump continueride
  else:
      jump skipride


label continueride:

  "That toy (he said it was called a dildo, but we called it a 'toy') was a bit soft compared to the real thing, but vibrates. That made it something that is completely different. I was almost as if I were vibrating myself just handing it to him and getting up close again."
  "I even sneak a kiss."

  a "Do you have something you want to do-"

  "In my excitement my hand runs up his leg. It's easy to tell that he's excited about this too."

  a "You're already hard. Was that from the shoulder rub?"

  "It's fun to tease him as if I don't know anything. But it doesn't seem like he takes my bait, instead he pushes me gently back and stands up from his chair. He then placed his hands in  front of my pants."
  "Knowing exactly what to do, I strip them off as well as my sweater, hopping up onto the desk as he guides me with my hips. I have to move some papers and his keyboard out of the way, but it's fine."
  "With a hand already in between my legs I turn back to Dr. Kronauer and kiss him."

  a "What are you thinking?"

  "He already has the toy slick with lube and is pressing it towards my pussy. I really do have him excited."

  a surprised "Ahh- that's cold-"
  l sad "Sorry-"
  a "Don't you usually want that hole?"
  l happy "Ah- it'll be easier like this."
  a blush "Mhh..."

  "I close my eyes as it fills me. I'm not entirely sure what Dr. Kronauer is planning, but I have an idea of it. But the thought of that halts once he flips the switch. The small electric hum travels all the way through my body like a shock."

  a "Ohh!"

  "We're kissing again. It's deep and wet, his hand gripping hard against my hips. I can feel his fingertips pushed into my flesh. They ease enough to let his hands slide around to my back and up so his arms wrap fully around me."
  "Yes, please hold me."
  "It feels nice, even if he's neglecting to move the toy inside of me, to feel him squeeze me like this. My legs return the favor as I try and keep my balance, wrapping around him to pull us close. But it seems like he wants to do more than just hug, and I squirm as I realize he's picking me up off the desk."

  a surprise "Ah!"

  "As he picks me up off the desk I struggle to keep the toy inside me. But just in time, I'm straddling his lap in the chair."

  hide lukas
  $ config.side_image_tag = "alfa"

  show lukasride onlayer event
  with dissolve
  $ persistent.cg_lukasride=True

  a "Ah... Oh."

  "So warm... He hasn't taken off his clothes, just undone his pants it seems. But I can feel how warm he is through them. Even his tongue is warm. His fingers, his arms, nose, lips. Oh, and his dick... I can feel the tip pressing against me, getting slick in my lube."

  a "Dr. Kronauer-"
  l "I know, I know."

  "I want him to fuck me."
  "I never really mind which hole he uses, since he always makes sure that I come at the end, but I am used to having him fucking my pussy."
  "Just because I don't want it doesn't mean I can't use it."
  "The toy feels good inside now. My ass is tight and he uses more lube to slide slick fingers in to ease the transition."

  a "Ah-"

  "It's tight with the toy already inside me. I shift, face pressed into Dr. Kronauer's neck. I focus on my breathing, but the constant hum of the toy and the feeling of myself getting fuller and fuller..."

  a "Fuck me, doctor... Ohhhhh..."
  l "Soon, my dear."

  "He's slow, he always takes it slow with my ass just because he did't want to hurt me. I appreciate it, but it still feels like ages until the tip of his cock presses against my hole. I try and push down on it, but he has a strong hold on my hips."

  l "Slow."
  a "-whine-"

  "I have to wait for him to let me slowly lower onto his dick. When he's finally inside, I groan, my arms tightening around his neck. If he starts to move, it's small and cautious. I roll my hips, trying to get more friction. Being filled both ways has me panting, drooling onto his shirt."

  l "What a good boy..."
  a "Ahhh..."

  "He's kissing my cheek, my ear. It twitches and folds back against my head. I'm still rolling my hips, still moaning into his neck."

  l "What a good boy."
  a "Auuuuhhh..."

  "The kisses to my ear continue as he keeps the grip on my waist and guides me. I feel like I'm rutting into him, rolling my hips in circles, eyes watering from feeling his cock run so close against the toy, both of them filling me up so tightly."

  l "How is it? I can feel the vibrations too."
  a "Ahhh.... You can?"
  l "Mmhm. It feels good. How about you?"
  a "Ohhh... ahh... Dr. Kronauer, it feels really good."

  "I moan again, peeling myself away from him as my head tilts back and my spine arches."

  a "I love your dick... Ahhh..."
  l "You like being penetrated twice?"
  a "Yeeeessss... Auuuuhhh..."

  "I roll a bit faster, pushing down against his cock and the toy."
  "It's not often that I come before him, but my spine stiffens as I cry out, feeling the flesh between his dick and toy spasm."

  a "Ah- ah!"

  show white with flash
  hide white
  pause (.5)
  show white with flash
  hide white
  pause (.5)
  show white with longflash
  hide white

  l "Addy, that was quick."

  "His hands combs gently through my hair but all I can feel is the toy still buzzing inside of me. Even as he kisses me, taking my hips and rutting, it's all my mind is on. The buzzing and the trembling of my thighs."

  a "Doctor..."
  l "Do you think you can come again?"

  "I shake my head no, but feel myself trembling and struggling with pushing against him, feeling his dick move a little quicker inside of me. My whole body is shaking as if I was left in the cold."

  l "Just a little longer."

  "I nod, panting, eyes closed. The buzzing just wont stop and the stimulation is making it hard to think at all. My hands balled into fists at his shirt."

  l "Ah-"

  show white with flash
  hide white
  pause (.5)
  show white with flash
  hide white
  pause (.5)
  show white with longflash
  hide white

  "I feel him come, the semen only filling me further."
  "Finally he breaks away, the cum slowly drips out. I squirm, letting the toy fall to the floor before resting on his chest, taking deep breaths, finally my body emptied out."

  hide lukasride onlayer event
  with dissolve
  $ config.side_image_tag = "addison"
  show lukas happy

label skipride:

  "Putting my clothes back on, I wonder. It doesn't seem like Dr. Kronauer is going to eat, and maybe I've cheered him up enough? I'm not sure."

  play music musiclukas loop

  "It's probably going to be boring, but Dr. Kronauer is already hugging me from behind and rubbing his face into my back. I should probably stay."

  a happy "You okay?"
  l "Mmhm. You know I love you, right?"
  a thinking "Yeah, of course."
  l "Okay."
  a happy "Purrr~"

  "He lets go of me and I sit on the floor next to his legs, leaning against him, grinning as his hand runs through my hair. I occupy myself with just enjoying the feeling for awhile, but even the best trained Felixes get bored."
  "Squirming, I reposition myself. Dr. Kroanuer doesn't seem to mind, still typing with one hand."
  "I grab a spare pen from his desk and some paper from his recycle bin."

  show paper onlayer event
  with dissolve

  "I burn through a few of his recycled papers before pulling one out that already has something written in pen on the blank side."

  narrator_nvl """
  Just wanted to make sure you saw
  """

  $ nvl_hide(dissolve)
  nvl clear

  "Flipping it over, I'm a little surprised that I can make sense of it, no numbers or graphs at all."

  narrator_nvl """
  Finance Department

  Ticket #: 028159

  Submission: In Review
  """
  narrator_nvl """
  Notes: This time I think he has a point, and Addison is only going to get older. The pharmachemical department's ready to launch their mouse set-up. Might as well give this a chance,

  he said he's willing to pay.
  """

  $ nvl_hide(dissolve)
  nvl clear

  a thinking "?"

  "Weird. I put it back in the pile and pulled out a fresh sheet."

  hide paper onlayer event
  with dissolve

  "After too long though, I'm getting restless."

  a happy "I'm going to head out now."
  l confused "Huh? Oh shit- is it that late already? Sorry Addy, of course."

  show lukas sad smile
  with dissolve

  "I give him a kiss on the forehead before heading out."

  scene bg cafeteria
  with dissolve
  play audio bell
  "I talk to anyone I can at dinner, about anything. Letting the kittens ramble on about their new favorite toys or stories, it's calming to just nod and listen along. The way their faces light up is enough to feed me too."

  scene bg barracks
  with dissolve

  play music musicsleepy loop

  "Settling them in, I pick up where I left off in their bedtime book and I make sure everyone is quiet in bed before I leave."
  "-yawn-"
  "Even big brothers can get sleepy."

  scene bg hallway1
  with dissolve
  pause (2)
  scene bg bedroomlight
  with dissolve

  "The bed is soft and it feels nice to hide my face under the covers."

  scene bg bedroomdark
  with dissolve

  "Goodnight."

  scene bg bedroomdark
  with dissolve
  pause (1)

  cards open card4

  scene bg bedroomlight
  with fade
  jump day4
