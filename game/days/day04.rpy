#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  day4.rpy
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

#Day 4
label day4:
  calendar day 4
  play audio bell
  a pajamas sleepy "-yawn-"
  a -pajamas happy "Ugh..."

  "Another morning and another big knot in my tail. This hair is so long it feels like ages to comb it out as I sit and brush it at my desk."
  "Did I have anything planned today? My half-awake mind wanders about."
  "It's been so busy here lately. The adoptions, Pumpkin getting a title, the new doctor..."
  "Oh, that's right. I'm supposed to help out the new doctor today. He said he needed help getting to know everyone, right? Well that's my specialty."

  play music musicneutral loop

  a sleepy "Mhh..."

  "But this knot just won't come out. Did I get food stuck in it yesterday? After a long while of teasing, finally my hair feels free and smooth."

  scene bg cafeteria
  with dissolve

  "I was a little late for breakfast but the staff don't seem to mind."
  "I pile the scrambled eggs filled with some leftover meat high on my plate and I take a seat."
  "Can I really handle doing three different jobs? I already have to be a Big Brother to the kittens, and of course I have to be the Staff Companion."
  "That already leaves my days pretty full; it's a lot of work. But he seemed so genuine when he said he asked for my help, and he seems like a really stoic person, so that smile must have meant extra."
  "I should at least give it my best shot. If I get too overwhelmed, I'm sure Dr. Moore would understand, wouldn't he?"

  scene bg hallway1
  with dissolve
  pause (2)
  scene bg clinic
  with dissolve
  pause (2)
  scene bg stevenoffice2
  with dissolve
  $ persistent.bg_stevenoffice2=True

  play music musicsteven loop

  a happy "Dr. Moore?"

  show steven happy
  with easeinleft

  s "Oh, Addison! Good morning. What can I do for you?"
  a thinking "You wanted me here, sir. You said I could help you?"
  s neutral "Oh, right. Yes, thank you for coming."

  "Dr. Moore nods and collects up papers to tidy his desk. It sure has gotten a lot more cozy in the last day or two. The new posters are up; I like them a lot. I sit down across from him, still glancing around."

  s "We can teach you how to fill out paperwork another day. For now, tell me about yourself. I want to get to know you."
  a thinking "That's not going to help you."
  s "Actually, it is."
  a "Ah, well, I guess..."

label menuday4:

  show steven neutral
  with dissolve

  play sound ding

  menu:
    "I was born as a girl.":
      a "Well, I was born as a girl."
      s "I saw that on your chart. It looks like everything is going well. Although, I noticed that you're not on hormones, would you like to be?"
      a smile "No, Dr. Collbreed said human hormones wouldn't work- and I don't want hormones anyways, I'm fine."
      s confused "Did he? I'll have to look into that... But if you don't want them, I guess that's fine."
      jump menuday4
    "I'm the Staff Companion.":
      $ steven_points -= 1
      a "I'm the Staff Companion, so I know almost everybody here, not just the kittens. I can introduce you to people if you wan-"
      "He cuts me off."
      s neutral "No, no thank you. I want to know about you, not your job."
      jump menuday4
    "I like art?":
      a "Ah, I guess I like art."
      s surprised "Art? So you draw?"
      a nod "I'm not good, but it's what I do in my free time."

label art:

  s smile "Could I see some, perhaps? Only if you're comfortable showing me."
  a thinking "See it? Ah-"

  play sound ding

  menu:
    "Yes":
      $ steven_points += 1
      jump artyes
    "No":
      a blush "Ah, I don't know, it's pretty embarrassing."
      s neutral "Oh- don't worry. I know it can be hard to show people."
      "He seems pretty disappointed, so I try and change the subject."
      jump artno

label artyes:

  a "Sure, it's in my room though. I'd have to go get it."
  s "I don't mind waiting."
  a surprised "!"

  hide steven
  with easeoutleft

  scene bg hallway1
  with dissolve
  pause (2)
  scene bg bedroomlight
  with dissolve

  "Was this a bad idea? I scan over my recent drawings and coloring book pages."
  "What is good? What should I show him? I end up grabbing a few haphazardly, with my cheeks and ears burning."
  "Why would he want to see them? Why should I be showing those to him?"

  scene bg hallway1
  with dissolve
  pause (2)
  scene bg stevenoffice2
  with dissolve

  show steven happy
  with easeinright

  a "Here you are..."
  s happy "Addison..."

  hide steven
  $ config.side_image_tag = "alfa"
  show showsteven onlayer event
  with dissolve
  $ persistent.cg_showsteven=True

  s "Addison, these are wonderful. You did these yourself? Where did you learn all this?"
  a "I didn't, I just looked at pictures and I tried to copy them..."
  s "You taught yourself all this? Addison, you must be very tallented. These are fantastic! You obviously worked hard on these and it really shows. Thank you for showing me."

  "I can't stand this. He sets my drawings down on the desk and I try to change the subject as fast as I can."

  hide showsteven onlayer event
  with dissolve
  $ config.side_image_tag = None
  show steven happy

label artno:

  a "Dr. Moore, had you ever seen a Felix before?"
  s thinking "What do you mean? Before I came here?"
  a nod "Yes, before you came here, had you ever seen one? When we first met, you just looked so... confused."

  "'Confused' isn't the right word, but it will work. I don't want to say 'mean' or 'scary' or anything like that."

  s sad "No, I hadn't. There are only maybe 10,000 of you. I had only seen Felixes in pictures until I came here for the first time."
  a thinking "So that means we're really rare outside?"
  s sigh "There are about 12 billion humans on Earth. That would be more than one million people for every single Felix."
  a "... How many is a million?"

  "He leans forward at his desk, that frown of his coming back. Oh no, did I say something wrong?"

  s angry "A lot. Quite a lot. So yes, you're very rare outside of this building."
  a "Oh..."
  s "... Don't worry though. I didn't mean to make you uncomfortable."
  a "No, I was just wondering."
  s happy "Well, that's good."
  a "Actually, is it okay if I go to lunch now? I can come back after that."
  s thinking "Of course. You don't have to stay here with me if you don't want to. I'd never want to keep you here."
  a happy "Okay. I'll be back."

  scene hallway1
  with dissolve

  "I ran off. Dr. Moore is nicer than he looks, but it's embarrassing trying to explain myself to someone new."
  "Dr. Kronauer might understand. Maybe he can explain how many a million is too."

  play music musiclukas loop

  scene officespace
  with dissolve
  pause (2)
  scene lukasoffice
  with dissolve

  show lukas happy
  with easeinleft

  a happy "Hello!"
  l "Hey Addy, how are you doing?"
  a "Okay- what do you have?"
  l "Nothing special. Beans, rice and chicken."

  "We settle down easily. It's certainly a good feeling to be with someone who knows you very well and can have a comfortable silence with."
  "He taps at his computer a bit while we sit, but he's not as distracted as the last time."

  a "How many is a million?"
  l confused "Hm?"
  a "How many is a million? Dr. Moore said there's a million humans for every Felix."
  l "Really?"

  "He sits and thinks about it."

  l "I guess that's right... It feels like there's more of you."
  l happy "But I get to see you every day, so I'm biased."
  a "But does that mean we're really rare?"
  l "You're special. Rare, yes, like... Like diamonds. You know what a diamond is?"

  l "You're rare, special and valuable. It's a good thing."
  a "Oh, okay."
  l happy "Why are you worried about that?"
  a "Just because Dr. Moore looked at me funny the from first time we met."
  l "Right- I remember you saying that. He doesn't look at you funny anymore, right?"
  a "No."
  l "Good. Or he'd get a stern talking to."
  a laugh "Don't scare him away."

  "I need that laugh. It had been awhile since we sat,talked and laughed. Dr. Kronauer joked around for a while until it was time to go again. I'm glad he's feeling better today."

  l "I have to get back to work."

  "He kisses me on the forehead."

  l "I'll see you later."
  a happy "Okay."

  scene officespace
  with dissolve
  pause (2)
  scene bg hallway1
  with dissolve

  "To be honest though, I think I'm excited to be learning things from Dr. Moore. I finished classes a long time ago, so learning new things is a treat. I wonder what it will be."

  scene bg clinic
  with dissolve

  play music musicsteven loop

  show steven happy
  with dissolve

  s "Welcome back, Addison. I thought we would start with something fun."

  hide steven
  $ config.side_image_tag = "alfa"

  show lesson onlayer event
  with dissolve
  $ persistent.cg_lesson=True

  "He teaches me how to take my pulse with my fingers and the clock, which I probably learned how to do at some point, but I've forgotten when."
  "The stethoscope is fun, and I end up laughing while I'm trying to get it right."

  s "Don't worry, you'll get it."
  a "Okay."

  "It doesn't take me too long, he's a good teacher."

  s "Do you want to learn how to take blood pressure, too?"
  a "Sure!"

  "He shows me how to place the cuff right above the elbow. Puffing it up and sliding the stethoscope underneath, I can listen to my own blood moving."

  a "Wow."
  s "Mhm. Your body works really hard to keep you alive and healthy."

  hide lesson onlayer event
  with dissolve
  $ config.side_image_tag = None
  show steven happy

  "He shows me a few more things before sending me off so that he can get his own work done. I didn't realize how late it had gotten! So I scamper off to dinner."

  scene bg cafeteria
  with dissolve
  play audio bell
  pause (2)
  scene bg hallway1
  with dissolve
  pause (2)
  scene bg bedroomlight
  with dissolve

  play music musicsleepy loop

  a sleepy "-yawn-"

  "As much fun as it is getting to learn new things, it's a lot of work."
  "My bed sounds fantastic right about now, but it's still too early to go to sleep, or even to put the kittens to sleep. Instead, I sprawl out with my colored pencils and coloring books, picking a page with an abstract swirling circle to keep me occupied."
  "Today feels like a red and blue day. As I color the small shapes, I stretch out, wiggling my toes and kicking my heels. Soon enough, I'm lost to the outside world."

  play sound dooropen

  scene bg bedroomlight with hpunch #why background

  a surprised "Huh? Come in?"
  l "Just me."

  show lukas happy
  with easeinleft

  a happy "Oh, hey!"

  "I scramble up to sit, wiggling back and forth."

  a "What's up? Shouldn't you be going home soon?"

  show lukas sad smile
  with dissolve

  l "Probably. But I have some medicine I need you to try out first."

  a sad "Medicine? The medicine you're working on? But I'm not in heat yet..."
  l "Come on Addy, I didn't say it was for 'that'."
  a "But--"

  show lukas angry
  with dissolve

  l "Come on, give me your arm and stop pouting. You know you're not allowed to know what it's supposed to do."
  a "Yessir..."

  "I raise my arm, pulling my sleeve back a bit."
  "Dr. Kronauer has gotten a lot better at giving shots over the years, and now I can barely feel a thing. He used to end up accidentally making my arm purple with bruises."
  "It's okay, we all have to learn somehow."
  "He sets his bag on the bed, then pulls out a packaged needle and a vial labeled 'AM4-3.'"
  "I shouldn't be peeking, but I am already."

  a "I was really hoping it would be something that would help..."

  show lukas sad smile
  with dissolve

  l "It will, you just can't know with what. I can neither confirm nor deny."
  a excited "Wait, so it could be?"

  l nod "Like I said, I can neither confirm nor deny. I just need to test it first."

  "I kick my feet happily. Maybe it will make my heat die out? Or maybe it will make it hurt less?"
  "I am due to start sometime next week... So it really could be it after all! "
  "Dr. Kronauer sits on the bed next to me."

  l "I brought you something to make up for the trouble."

  a surrpised "Oh, another coloring book?"
  l "No..."

  "He's digging through his bag, and when he turns to face me he's holding a silver ball in the palm of his hand."

  a thinking "Huh?"

  play music musictender loop

  hide lukas
  $ config.side_image_tag = "alfa"

  show sparkle1 onlayer event
  with dissolve
  $ persistent.cg_sparkle1=True

  "But the more I look at it, I realize inside must be water- the silver liquid is swirling and moving by itself, glitter catching the light and moving like the whirlpool that forms at the end of a bath."

  a "Wow..."
  l "I thought you might like it."
  a "What is it?"
  l "Just a pretty ball. But I remembered you liked that kaleidoscope a while back, so it reminded me of you."

  "I take it in my hands, turning it back and forth. The glitter takes too long to respond to my movements, as if it doesn't realize the ball has turned until it's too late."

  a "It's so neat..."
  l "I'm glad you like it."

  hide sparkle1 onlayer event
  with dissolve
  $ config.side_image_tag = None
  show lukas happy

  "He wraps an arm around my shoulder, pulling me into him. There's no resistance as I grin and cuddle up beside him, shaking the ball and twirling it to see how else the glitter might react."

  l "Tell me about your day."
  a "Hmm... I spent a lot of time with Dr. Moore. He wants me to help him in the clinic so he can get to know all the Felixes better."
  l "Ah, what did he teach you then?"
  a "Today he taught me how to take somebody's pulse."

  "I reach up, pressing two fingers against Dr. Kronauer's neck, just the way Dr. Moore showed me."

  show lukas blush
  with dissolve

  a happy "Right, like this."

  "I wait for a few seconds."

  a thinking "Your pulse is really high."
  l "Is it?"

  show lukas sad smile
  with dissolve

  a "Yeah, or maybe I counted wrong?"
  l happy "Don't worry about it."

  "He takes my wrist, pulling my hand away from his neck while he leans in, stealing himself a kiss."

  a blush "..."

  "The ball rolls from my hand to the bed, bouncing once on the floor as Dr. Kronauer guides me back to lay down, still kissing as I find him on top of me."

  a "Mmm..."

  "It's not unusual for him to kiss me like this. He has the biggest soft spot for me out of everyone at the facility, and he's probably my favorite, too."
  "I return the kisses, letting myself relax into the bed as he straddles over me, one hand still around my wrist, the other finding its way to my hair."
  "It makes me feel gooey inside, like a warm cookie."

  hide lukas
  with dissolve

  $ config.side_image_tag = None

  show black onlayer event
  with dissolve

  "It makes my mind go all fuzzy."

  l "I love you, Addy."

  hide black onlayer event
  with dissolve
  pause (2)
  scene bg bedroomdark
  with dissolve
  pause (1)

  cards open card5

  scene bg bedroomlight
  with fade
  jump day5
