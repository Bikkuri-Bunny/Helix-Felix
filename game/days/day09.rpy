#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  day9.rpy
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

#Day 9
label day9:
  if (pumpkin_points<2):
    jump day10

  calendar day 9
  play music musicupbeat loop

  a pajamas happy "Ah!"

  "Mmmmm, happy Saturday! Saturdays and Sundays, almost all of the staff are gone, and us Felixes basically have free reign. I take a biiiiig stretch to wiggle the sleep from my body and then I do my usuall morning routine."

  a happy "..."

  scene bg hallway1
  with dissolve
  pause (2)
  scene bg playroom
  with dissolve

  "The kittens want to play a game of hide and seek, so naturally I'm 'it'."
  "This makes it hard, some of the younger ones are bad at hiding and I'm not sure if I should pretend that they're good, or let them know I can see their ears over the couch."
  "As we're winding down from the morning games, I take everyone down to the cafeteria for lunch. Soon Pumpkin links arms with me."

  show pumpkin happy
  with dissolve

  p "Happy Saturday."
  a "Happy Saturday, what's up?"
  p "Nothin'."

  "He leans his head on my shoulder as we wait in line for lunch."

  p "That's what's nice. ‘Nothing,’ I mean. Last weekend, they had me work all day, both days."

  show pumpkin sad
  with dissolve

  a "I was wondering where you were."

  "I pull away and pick up a tray, loading it up with an apple, milk and nuts,"

  a surprised "Pumpkin, -whisper- you can't take two bags of nuts."

  "Pumpkin puts the extra into his pocket and winks."

  p "It's okay, no one will know."
  a blush "Okay..."

  "Isn't he going to gain weight if he does that? I saw him take extra lolipops from Dr. Moore before too. But Dr. Moore let him, so I didn't say anything."
  "I guess as long as he doesn't get in trouble..."
  "As we sit and eat quietly, I can feel Pumpkin watching me, his eyes narrow."

  a "Wh-what?"
  p "Really, it's going to be okay."
  a nervous "Okay."
  p "Hey, let's do something fun."

  "He shoves the rest of his lunch in his pockets."

  a surprise "What."
  p "Come on."

  "My lunch is fair game as he fills his pockets and then he grabs my arm."

  p "Don't act weird, and it won't be weird if we leave."

  show pumpkin nervous
  with dissolve

  a "Oh- okay."

  "The kittens are busy eating and they didn't notice me slip out with Pumpkin. He takes my hand, guiding me down the twisting hallways."

  scene bg hallway1
  with dissolve
  scene bg hallway2
  with dissolve

  a "Are we going to your secret space?"

  show pumpkin angry
  with dissolve

  p "Shhhhh!!!! Yeah, but first is something special."

  "He looks over his shoulder before opening the door that is clearly labeled as the 'Staff Room'."

  show pumpkin happy
  with dissolve

  a "Hey, we're not allowed in here..."
  p "Shhh! Nobody's here. Come on."

  scene bg staffroom
  with dissolve
  $ persistent.bg_staffroom=True

  "I nervously pad in behind him. It's not a big room: there were a couple couches and a table. But Pumpkin is in the corner playing with a machine."

  a "What's that?"
  p "A drink machine. I'm getting us some hot cocoa."
  a excited "COCOA!?"
  p angry "Shhhh!!!!"

  "Cocoa was a big treat, and he was just pulling some from a machine?"

  a "How?! How are you doing it?"
  p happy "This machine makes hot drinks. Most of them are not good, but it makes cocoa, too. Here you are."

  "He hands me a ceramic mug. It feels hot to the touch, almost too hot to hold in between my hands."

  a "Wow..."
  p "We'll have to wash and bring the mugs back when we're done, but we'll be fine. Come on, let's go."

  "I sip the drink as we head to his spot- ouch. Still too hot."

  scene bg hallway2
  with dissolve
  pause (2)
  scene bg secretspace
  with dissolve

  play music musicsecretspace loop

  p "There. I like having cocoa when I'm in here. Now you can, too."
  a "Yeah!"

  "I lean halfway against the wall and halfway against Pumpkin's shoulder. It really does feel nice in here- like a nest, or a warm and safe hug."

  hide pumpkin
  $ config.side_image_tag = "alfa"

  show ss2ahph onlayer event
  with dissolve
  $ persistent.cg_ss2ahph=True

  a "-sigh-"

  play sound ding

  menu:
    "Relax and cuddle":
      jump cuddleday9
    "Talk to Pumpkin":
      $ pumpkin_points += 1
      jump talkday9

label talkday9:

  a "Was there anything you wanted to talk about?"

  "Pumpkin is fidgeting with his mug, eyes halfway closed and distant as I glance up at him."

  show ss2asps onlayer event
  hide ss2ahph onlayer event
  with dissolve

  p "Yeah, I guess. It's still really strange, not getting adopted. I think I just wanted to talk to you about it. I know it was a long time ago, but what was it like when you first found out that you wouldn't be adopted?"
  a "Ah... It was scary. I don't know if I've talked about it before."

  "At least, not with anyone but Dr. Kronauer."

  a "I thought it wasn't fair. I wanted a Master, since I'd been told-, we all were-, that we would all get one. It felt ripped away from me."
  p "Yeah... yeah."
  a "... Eventually, I tried not to think about it. I have other jobs to do, like taking care of the little ones, and this life isn't unhappy."
  p "It's fun, and it's still nice to be here... It's just not what I thought I would be doing."
  a "Yeah."

  "We sit in silence for awhile."

  p "What kind of Master did you imagine you would have?"
  a "Hm..."

  show ss2ahph onlayer event
  hide ss2asps onlayer event
  with dissolve

  play sound ding

  menu:
    "Someone who would always take care of me.":
      $ lukas_points += 1
      jump nextday9
    "Someone who would push me towards my goals.":
      $ steven_points += 1
      jump nextday9
    "Someone who I could try new things with.":
      $ pumpkin_points += 1
      jump nextday9

label nextday9:

  a "What about you? What did you dream about when you would think about having a Master?"
  p "Hm. It's dumb, but I always wanted to go to school- to learn about math."
  a "Math????"
  p "Yeah! Math is really fun. They stop teaching it after you turn 10- but I kept reading the books and playing with the work sheets. I really like numbers and stuff like that. Sorry, that's really weird."
  a "No- I just had no idea! I remember you being really smart and good in classes. I didn't know you kept going."
  p "Well you kept going with art, right? It's like that!"

  "His smile is so genuine. He really is cute."

  a "That doesn't answer the question though!"
  p "Huh?"
  a "What would you want from your Master?"
  p "Oh- uh. I guess someone really smart, who wanted to teach me things. I think he'd be cute in glasses... And he'd have a hobby you wouldn't expect... like gardening."
  a "Hmmm, he sounds really sweet."

  "It was a beautiful dream, but that'll never happen..."
  "So I gave out a big sigh."

  a "Well..."

  "Pumpkin cuts me off before I can finish."

  p "What if we had the same Master?"
  a "The same Master?"
  p "Yeah, what if we got adopted together? What do you think it would be like? Living together outside."

  "I sit quietly, trying to think about it."

  a "Uh..."

  "To be honest, I haven't thought about living outside for a long time."

  p "You could paint ducks at the park, and our Master would get us some ice cream... We would all hold hands, take a trolley to the market... Oh! And maybe we'd live in Paris! I'd have lots of pretty clothes and I would take trips to the beach..."
  a "You got this all planned out, huh?"
  p "No. They're just ideas."
  a "Well, we kinda are adopted together. We've got each other."
  p "Yeah..."

  "He looks around the small space."

  p "Yeah. I'm glad I don't have to do this alone. I'm already confused and scared enough."

  a "... Do you want to talk about it?"
  p "It's just lots of little things."

  "Then that's a yes."

label heavyday9:

  show ss2asps onlayer event
  hide ss3ahph onlayer event
  with dissolve

  p "Even my pretend Masters, they're going to keep changing I think. I've already had four. I just want to get to know them. And sex is nice-, it's really nice-, but sometimes I feel bad, because I might not be able to see them again. It just feels like it's going so fast."
  a "I never thought of that. I guess I was lucky..."
  p "What do you mean?"
  a "Well, I know everyone. And sometimes people have to leave the company and it hurts, but... I get to be slow. I never thought of it that way."
  p "... Do you have sex with everyone?"
  a "No. But with a lot of people. But not often... some people come talk to me. Other people would like to pet me, or brush me. But usually the same person wouldn't want to have sex with me more than... twice a year? People like to be in a certain mood for it."
  p "Except Dr. Kronauer."
  a "Except Dr. Kronauer. He really, really likes me. "
  p "... Do you think of him as your Master?"
  a "Uh- well- no, I've never... thought of that. Before."
  p "Hmm. Well, do you know why he likes you? Other than you being ~so cute~."
  a "Hey. Well, we're friends. When I found out I couldn't be adopted because I was trans, I was 12. They put Dr. Kronauer in charge of me, so that I could test his medicines. He just liked to talk to me, and I trusted him when I was scared or sad."
  a "In the beginning, I was sad a lot. And when I turned 18 and they said I could have sex, I was really nervous and scared. He was the one who told me I could say 'no', and wait as long as I needed, or never do it at all."
  a "And then one night when I was in heat, it just felt... right. I trusted him ever since."

  p "Sometimes I forget you still go into heat."
  a "Yeah. It sucks. Augh, it'll start soon too..."
  p "I'm glad you have someone like that you can trust."

  "Oh, whoops. That was really rude of me to say that, Pumpkin doesn't have anyone like that."

  show ss2asph onlayer event
  hide ss2asps onlayer event
  with dissolve

  a "I'm sorry- I didn't even think-"
  p "No, it's okay. I have you!"
  a "Yeah. Yeah! I'll be here for you then."

  "He settles into my shoulder a little more."

  p "Yeah... You know, even with your picture, my new room feels so empty. It's hard to sleep with everything so quiet. I miss hearing the kittens sleeping around me."

  a "It took me a while after I moved from the barracks to get used to that too."
  p "I almost wish I could sleep in here. It's a little cozier..."

  play sound ding

  menu:
    "Why don't you sleep with me tonight?":
      $ pumpkin_points += 1
      jump saturdaysleep
    "Why don't we decorate your room with this?":
      $ pumpkin_points -= 1
      jump movethings

label saturdaysleep:

  a "Why don't you sleep with me tonight? It'll be better than sleeping alone."
  p "Really? You'd be okay with that?"
  a "Of course!!"

  show ss2ahph onlayer event
  hide ss2asph onlayer event
  with dissolve

  "He gives me a tight squeeze. We're both giggling now. That conversation had been heavy, so we needed the air to clear up."

  p "Thank you."

  hide ss2ahph onlayer event
  with dissolve

  scene bg hallway2
  with dissolve
  $ config.side_image_tag = None
  show pumpkin happy

  "We wash and return our mugs, still chatting and giggling down the hallway."

  scene bg bedroomlight
  with dissolve
  pause (2)
  scene bg bedroomdark
  with fade

  play music musicsleepy loop

  "My bed is a little small for two, but we curled into each other and I'm struck with a memory from a long, long time ago, there were some nap times where we curl into each other like this on the floor."
  "I don't remember doing it with Pumpkin specifically, but we fit together so well, and it brings a smile to my face."

  a happy "Goodnight, Pumpkin."
  p happy "Night, Addy."

  cards open card3
  jump day10

label cuddleday9:

  a "You must be really tired with everything going on lately. And it's really nice and cozy here, especially with the hot cocoa. You do a good job."
  p "Haha, thanks. I'm glad you think so. Yeah, they had me do a lot, but it's pretty fun."

  "Pumpkin goes on, telling me about his photo shoots, the fun clothes he gets to wear and model. He talks about the sex with a tired smile as I listen and nod. The warmth of the hot chocolate and our body heat begins to coax my eyelids down."

  p "You're falling asleep."
  a "Huh- oh- I'm sorry."
  p "Ha, no it's okay. Let's take a nap. Like you said, I'm pretty tired too."

  "We curl into each other, and I'm enjoying the warm cozy feeling."

  a "Okay."

  show ss2acpch onlayer event
  hide ss2ahph onlayer event
  with dissolve

  "I don't know how long it was, but we tangled into each other for a while. Holding Pumpkin against me, this reminds me that he's only 18 now. That's old for Felixes who live here, but... He's going through a lot right now."
  "Being 18 was hard for me too, but looking back, it feels like forever when it's only been four years since then."
  "I kiss his forehead softly, then we drift off."
  "Suddenly I wake up when I can feel something... shaking?"

  show ss2aspcs onlayer event
  hide ss2acpch onlayer event
  with dissolve

  a "Pumpkin? Pumpkin, Pumpkin wake up! It's only a dream."
  p "Huh!? Oh- Addy?"

  show ss2asps onlayer event
  hide ss2aspcs onlayer event
  with dissolve

  "He looks around the room, remembering where he is."

  a "Yeah, it's just me. I'm right here. What's wrong?"

  "His shoulders tense a bit as he sighs."

  p "It's... nothing. I've just been having bad dreams. Well, a bad dream that I've been having over and over. It's making it hard to sleep."
  a "What's it about?"
  p "Mhh... Like I said, it's nothing... It's like I get lost and I can't find anyone."
  a "Oh..."

  "That makes a lot of sense actually. It sounds like it's about..."

  a "Do you think it's about not having a Master?"
  p "Well..."

  jump heavyday9

label movethings:

  a "Why don't we move all this stuff up to your room?"

  "I motion at the walls around us. They're draped in cloth, streamers, decorations, holiday lights... Countless things that would make his bedroom feel more comfortable."

  p "This stuff?"

  "He hesitates, looking around."

  show ss2asps onlayer event
  hide ss2asph onlayer event
  with dissolve

  p "I guess that would work... It would be empty in here though."
  a "We don't have to do it, it was just a thought."
  p "... Yeah, I'll think about it, but I don't think I want to. I want to keep this space for me. It's very important."
  a "Sure."

  hide ss2asps onlayer event
  with dissolve
  $ config.side_image_tag = None
  show pumpkin neutral

  a thinking "..."

  "I think I might have offended him, so I changed the topic and we chitter away for a while longer, eventually crawling out to wash and put away the mugs we had 'borrowed'. It's getting late and I need to check on the kittens again."

  scene bg hallway1
  with dissolve

  play music musicsleepy loop

  a "Thanks for the treat, and I'm always here to talk to."

  "He gives me a half-hearted nod and heads back to his room. I'm worried about him, but what can I do?"

  hide pumpkin
  with easeoutright

  "I check on the kittens – they're all sleeping soundly in their beds, so I head to mine to crash for the night."

  scene bedroomlight
  with dissolve
  pause (2)
  scene bedroomdark
  with dissolve

  a pajamas tired "..."

  "I crawl under the covers, thinking about Pumpkin. How can I make him feel more comfortable? I don't have any supply of decorations like he does."
  "Maybe tomorrow the answer will come to me."
  "For now, goodnight."

  cards open card3

  jump day10
