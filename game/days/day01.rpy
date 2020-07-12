#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  day1.rpy
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

label day1:
  #Day 1
  calendar day 1
  $ config.side_image_tag ="addison"
  pov attrs pajamas sleepy
  play audio bell
  "The sound of the wake-up bell is faint in my room. Sometimes I sleep right through it, but today it wakes me up. I rub my eyes, getting ready for the day with a big, wide stretch."

  a "-yawn-"

  "Still a while before breakfast..."

  a -pajamas happy "Now then..."

  "I brush my hair, and then I sit down to comb out my tail."
  "It always takes a long time; now and again I wish I had lovely sleek short hair like the other kittens do."
  "My long hair captures so much dust and dirt around my tail, sometimes it looks like I've been trying to sweep all of it up off the floor."
  "When that's done, I sit at my desk, stretching, and think about drawing for a bit. A warm-up practice would be good for me, and who knows what I'll find when I get to breakfast."
  "If yesterday was any indication, this may be the only time I get to draw today."

  play music musiclukas

  play sound ding

  menu:
    "Practice anatomy":
      jump hands
    "Interpret last night's dream":
      jump dream
    "Relax with a coloring book":
      jump coloringbook

label hands:
  
  $ config.side_image_tag = "alfa"
  show drawing1 onlayer event
  with dissolve
  $ persistent.cg_drawing1=True

  "I don't often do figure drawing, and hands are the most frustrating to get right. My warm-up sketches look more like noodles for now. Fingers curl unnaturally or separate uncomfortably."
  hide drawing1 onlayer event
  with dissolve
  show drawing3 onlayer event
  with dissolve
  
  "It's only practice, but my eyebrows scrunch together as I turn my eyes back and forth between my own hand and the paper."
  
  hide drawing3 onlayer event
  with dissolve
  show drawing5 onlayer event
  with dissolve 
  
  "It feels nice once I can produce something at least recognizable. But soon enough the breakfast bell rings and I have to put away my pencils and tend to my rumbling stomach."
  hide drawing5 onlayer event
  with dissolve
  $ config.side_image_tag = "addison"
  
  jump breakfastday1

label coloringbook:

  $ config.side_image_tag = "alfa"
  show drawing1 onlayer event
  with dissolve
  $ persistent.cg_drawing1=True
  
  "Dr. Kronauer has given me a few coloring books recently. I've always liked coloring books, but these new ones have shapes that are really small."
  hide drawing1 onlayer event
  with dissolve
  show drawing2 onlayer event
  with dissolve
  
  "I really like coloring in details and being slow with my pencils."
  hide drawing2 onlayer event
  with dissolve
  show drawing3 onlayer event
  with dissolve
  "One book contains birds, another is all kinds of animals, but my favorite so far has been the 'Mandala' coloring book, which is full of swirling circles with lovely mirrored patterns."
  hide drawing4 onlayer event
  with dissolve
  show drawing5 onlayer event 
  with dissolve
  
  "The abstract shapes are friendly and those circles always invite any color I choose."
  "Since it's morning and I don't have much time to spare, but I pull out the last mandala I was working on and fill in a few more spots with diferent kinds of purples and blues."
  hide drawing5 onlayer event
  with dissolve
  $ config.side_image_tag = "addison"
  
  jump breakfastday1

label dream:
  
  $ config.side_image_tag = "alfa"
  show drawing1 onlayer event
  with dissolve
  $ persistent.cg_drawing1=True

  "I had a strange dream last night. I usually don't remember much about them, but I do remember this one, even though I don't understand it."
  hide drawing1 onlayer event
  with dissolve
  show drawing2 onlayer event
  with dissolve
  
  "It had something to do with going outside. Maybe I'm just really excited for the field trip we're having in a week or so."
  hide drawing2 onlayer event
  with dissolve
  show drawing3 onlayer event
  with dissolve
  "I color haphazardly on a blank page, a large swath of blue and another of green. Something red in the middle."
  hide drawing3 onlayer event
  with dissolve
  show drawing4 onlayer event
  with dissolve
  
  "It doesn't make much sense, but it's just a warmup."
  hide drawing4 onlayer event
  with dissolve
  $ config.side_image_tag = "addison"
  
  jump breakfastday1

label breakfastday1:

  play music musicneutral loop

  scene bg hallway1
  with dissolve
  pause (2)
  scene bg cafeteria
  with dissolve

  "The cafeteria is already bustling with kittens, the chatter of their voices and the delicious smell of maple mingling together. I bet that today will be just as sweet as these pancakes."

  show ainsley happy
  with easeinright

  g "Good morning, Addy!"
  a happy "Good morning, Ainsley."

  hide ainsley
  with easeoutright

  "Most of the kittens are bushy tailed and bright, having gotten a rest after yesterday's loss, and eagerly shoveling down the tasty breakfast. There's no way I wouldn't follow suit."
  "Chatting idly with the kittens at my table and stuffing my face with some fluffy pancakes makes me a little slow to notice the tone of their chatters changing so suddenly."
  "Eventually the air turns a little cold and I raise my head to look around. Someone else has been adopted. My heart squeezes."

  play music musictender loop
  pov attrs sad

  "We only know when they don't show up for breakfast. I'll have to find out who it is, and help the kittens feel comfortable without their friend again today."
  "I feel guilty as my shoulders fall. This is my responsibility, I shouldn't avoid it. Usually one of us is adopted at least once or twice a month."
  "But we never know who, and we never know when. It makes it hard for the kittens who have grown close over the years."

  a "Oh no..."

  scene bg hallway1
  with dissolve
  pause (2)
  scene bg playroom
  with dissolve

  a "Okay, it looks like today we get to be happy for Ali."

  a happy "He was adopted this morning and went home with a Master. Everyone will get to have their turn eventually. We shouldn't be impatient or envious, remember?"

  "The kittens shuffle around but nod, knowing what I say is true but they are still upset about losing their friend."

  scene bg hallway1
  with dissolve

  a sad "-sigh-"

  "I know it's wrong, but I can't hold out all day like this again. Lunch break couldn't come fast enough."
  "When it finally does, I quickly slip away from the kittens and scamper down the hallway in the other direction."

  play music musiclukas loop

  "Every weekday when I can, at exactly 11:45 AM, I trot up the north stairwell and down the office hallway to room 244, where I have lunch with Dr. Kronauer."
  "Dr. Kronauer has been my friend since I became the staff companion ten years ago."
  "He's the head of the pharmaceutical department and sometimes has to test his medicine on me. I don't mind a lot of the time. Every day we get to talk and share lunch with each other."
  "I wonder what he's brought today. Technically I don't think I'm supposed to have food from the outside, but Dr. Kronauer wouldn't let me get in trouble."

  a sleepy "-yawn-"

  scene bg lukasoffice
  with dissolve
  $ persistent.bg_lukaoffice=True
  show lukas happy
  with easeinleft

  l "There you are, I just nuked lunch. Today is spaghetti."

  show lukas sad
  with dissolve

  l "What's wrong? You look worn out."
  a "Ali was adopted this morning, some of the kittens are sad about it. It's nothing new."
  l "Oh, alright. Well take a break for a while. You know you're not responsible for them. You don't have to baby them day and night. They have other people they can talk to, like Jesse. It's not all on you."
  a "No, but it's... I feel like I should."
  l "That's because your heart is so big."

  show lukas happy
  with dissolve

  a blush "Ha..."

  "He grins and hastily ruffles my hair before leaning back in his chair."

  l "But I don't want you to make yourself sick over it or anything like that. Too much stress can make you physically ill or it'll give you lots of pain, and as a Felix you really shouldn't have to deal with that. Please be careful."
  a "O-Okay."
  l "Mmhm- someone new is starting tomorrow and he's going to tell you the same thing."
  a surprised "Someone new?"

  "Dr. Kronauer nods enthusiastically."

  l "Mmhm. Dr. Collbreed's replacement. He'll be the new medical doctor for you all."

  "That's right. We had Dr. Collbreed's retirement party a couple weeks ago. Maybe a new face will do everyone some good. Dr. Kronauer echoes my thoughts."

  l "I think the kittens will be very happy to have someone new down there. Maybe it'll make your job a little easier too."

  "I nod, nibbling on the spaghetti."

  a "Have you met him yet?"
  l "Just for his interview. I'm excited for him to start. I think we'll get along well."
  a "Well, other than that, has anything new happened for you?"

  show lukas neutral
  with dissolve

  l "Just a lot of work needs to be done."
  a "What do you mean?"
  l "Ah- The medicine I'm working on- there's a lot of Felixes who need it. But it's still not done yet."
  a "Is it one I've tested yet?"
  l "No, not yet. I'll probably need your help for that soon."

  show lukas sad
  with dissolve

  a "Are they getting sick after they get adopted?"
  l "-sigh- Sort of. It's nothing for you to worry about though. It's my job, and the medicine will be ready soon. I'm sorry I brought it up."
  a "... Wait. Is it to help with heat?"
  a excited "I know I'm not supposed to know, but is it? Is it?"

  "Something that would help with heat would be a miracle."
  "Every three months, female Felixes go into heat for around six or seven days. Sometimes it's like a tingling that feels nice, but other times it hurts so badly it feels like nothing else exists."
  "It only happens to mature Felixes, so I don't have to worry about the kittens while they're here."
  "But it really is a pain for me to go through it."
  "I'm a boy, but I was born female and still go into heat. It's the worst."

  show lukas sad smile
  with dissolve

  l "I can't tell you. You know that. It would-"
  a "It would 'ruin the test', I know."

  "But my heart is still fluttering! Dr. Kronauer is always the one to help me with my heat when I really need it, but if he could make a new medicine that helps everyone, I would be so happy!"

  l "Well, give me your bowl, don't you want to go back downstairs?"
  a confused "Huh?"
  l "Isn't it class time?"
  a "Is it? Oh- I guess it is. It's math today, so I'm not a big help..."
  l "Math is important."

  "Dr. Kronauer is getting our dirty dishes together into a pile and then he stands up from his chair."

  scene bg officespace
  with dissolve
  $ persistent.bg_officespace=True

  show lukas happy
  with dissolve
  pov attrs happy

  "We walk down the hall to the break room to wash out the bowls and clean the forks. A few employees stop to say 'hello' and pet my head a little."

  a "Hello!"
  o "Addison, you're cute as ever today!"
  a "Thank you!"

  show lukas sad smile
  with dissolve

  l "I'm very glad you're here, Addy. I hope you know that."
  a "Huh? It is because everyone gets to see me?"

  show lukas sad smile
  with dissolve

  l "Yeah, something like that. I'm really glad you're here and I--I mean, we--can take care of you."
  a excited "Of course! I like being here, too."

  pov attrs happy

  "I've talked to Dr. Kronauer about not having a Master. I've even cried to him about it a couple times."
  "He would always listen to me when I was little and I'm still so self-conscious about the whole thing. He knows it still hurts."
  "I wonder if he knows I still think about it."

  a "See you later!"

  show lukas happy
  with dissolve

  l "See you later, Addy."

  scene bg hallway1
  with dissolve
  pause (2)
  scene bg classroom
  with dissolve
  $ persistent.bg_classroom=True

  play music musicneutral loop

  a thinking "..."

  "Class has already started. The classes are only for 5-12-year-old kittens, since everyone graduates from the care center to the adoption center when they're 4. Then most of them are adopted by the time they're 12."
  "They teach a lot of things, knowing how to read and how to write are important skills to help out our future masters as best we can. The kittens are working on math today--it's important, too."
  "There are other, more fun classes, like physical education, dance class, and music class. There are also harder classes, like how how the body works, how to cook, and so on."
  "Really, they teach us how to be good Felixes so that the kittens can be adopted and serve their masters and make them happy."

  show pumpkin thinking
  with easeinleft

  "It's strange when I walk in today and see Pumpkin sitting at the back of the class."#Why?
  "I don't say anything, but I wait until the lesson is over when and it's work time. Then I can go help out anyone who raises their hand."
  "I'm not very good at math, so I'm not as much help today as I am sometimes. But I'll always do my best."

  hide pumpkin
  with easeoutleft
  show charlie confused
  with easeinright

  hide charlie
  $ config.side_image_tag = "alfa"
  show mathclass onlayer event
  with dissolve
  $ persistent.cg_mathclass=True

  a "What is it, Charlie?"
  c "I don't remember what's 8x9."
  a "Those are big numbers. But there's a trick for nines."

  "I hold my hands out in front of myself to show Charlie, counting my fingers in front of him"

  a "One, two, three, four, five, six, seven, eight."

  "I fold my eighth finger down."

  a "How many fingers are on the right side?"
  c "Uh...Seven."
  a "Okay, write that down. Now how many are on the left side?"
  c "Uh... Two."
  a "Yep, now write that down."
  c "Seven and two? 8x9 is seven and two?"
  a "No, it's Seven-TY two."

  hide mathclass onlayer event
  with dissolve
  $ config.side_image_tag = "addison"

  show charlie excited

  c "Really??"
  a "Yep. And it works for any number multiplied by nine. You can try it with the other equations too, okay?"
  c "Okay!"

  hide charlie
  with easeoutleft

  "I help out a few other kittens with a few more questions, some harder than others. But when class gets out at five, I can't help but try to and find Pumpkin to talk to him."

  a surprised "Huh?"

  "He must have already left. I can't see him anywhere."

  scene bg hallway1
  with dissolve
  pause (2)
  scene bg cafeteria
  with dissolve
  play audio bell
  "Today's dinner is dinner rolls, meatloaf with tomato sauce, and steamed vegetables. The smell of the tomato sauce and pepper tickles my nose, but my tummy doesn't mind at all."
  "The kittens seem pretty tired after two of their friends were adopted two days in a row. It takes a lot out of them. It takes a lot out of me too."

  scene bg hallway1
  with dissolve
  pause (2)
  scene bg barracks
  with dissolve

  play music musicsleepy loop

  "Tucking them into bed is easy. I also finally spot Pumpkin again, but I decided not to bother him this late. He slides into bed just like the other kittens are doing, and I turn out the lights as I leave."

  scene bg hallway1
  with dissolve
  show jesse happy
  with easeinright

  j "Always doing my job for me."
  a "I'm just trying to help."
  j "No Addy, you're a big help. Thank you."

  hide jesse
  with easeoutright

  scene bg bedroomlight
  with dissolve

  a pajamas happy "-yawn-"

  "Today was... okay. I avoided the kittens more than I should have. But Dr. Kronauer tried to cheer me up."
  "Oh, right--the new doctor will be here tomorrow. I wonder what he'll be like. I hope he’s cute. I should get plenty of sleep so I’ll be ready to meet with him~"

  scene bg bedroomdark
  with dissolve
  pause (1)

  window hide
  cards open card2

  scene bg bedroomlight
  with fade

  jump day2
