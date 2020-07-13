init python:
    def purring_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            ui.timer(15.0, Play("purring", "audio/purring_cat.ogg",loop=True))
        elif event == "end":
            renpy.sound.stop(channel="purring")
            pass

#config.say_attribute_transition = Dissolve (0.2, alpha = true)
#config.side_image_same_transform = same_transform

define flash = Fade(0.1, 0.0, 0.5, color="#ffffff")
define longflash = Fade(0.1, 0.2, 0.5, color="#ffffff")
transform myleft:
    xalign 0.3
    yalign 1.0
transform myright:
    xalign 0.7
    yalign 1.0

define a = Character(_("Addison"), who_color="#ffdb90", who_outlines=[ (1, "#733700") ], what_color="#ffdb90", what_outlines=[ (1, "#733700") ], image="addison",ctc="ctc_blink",ctc_position="nestled",callback=purring_voice)
#orange
define l = Character(_("Dr. Kronauer"), who_color="#a6f7e3", who_outlines=[ (1, "#004030") ], what_color="#a6f7e3", what_outlines=[ (1, "#004030") ], ctc="ctc_blink",ctc_position="nestled", callback=purring_voice)#"lukas"
#cyan
#Because names can be confusing when reading this script; Dr. Lukas Kronauer, usually referred to as Lukas ooc
define s = Character(_("Dr. Moore"), who_color="#fd9ebb", who_outlines=[ (1, "#57001b") ], what_color="#fd9ebb", what_outlines=[ (1, "#57001b") ], ctc="ctc_blink",ctc_position="nestled", callback=purring_voice)#"steven"
#pink
#Dr. Steven Moore, usually referred to as Steven ooc
define p = Character(_("Pumpkin"), who_color="#b2fa99", who_outlines=[ (1, "#0e3800") ], what_color="#b2fa99", what_outlines=[ (1, "#0e3800") ], ctc="ctc_blink",ctc_position="nestled", callback=purring_voice)#"pumpkin"
#green
define j = Character(_("Mr. Jesse"), who_color="#fbf896", who_outlines=[ (1, "#383600") ], what_color="#fbf896", what_outlines=[ (1, "#383600") ], ctc="ctc_blink",ctc_position="nestled", callback=purring_voice)#"jesse"
#yellow
define c = Character(_("Charlie"), who_color="#99a8ff", who_outlines=[ (1, "#000f63") ], what_color="#99a8ff", what_outlines=[ (1, "#000f63") ], ctc="ctc_blink",ctc_position="nestled", callback=purring_voice)#"charlie"
#blue
define g = Character(_("Ainsley"), who_color="#eba9ff", who_outlines=[ (1, "#3b004d") ], what_color="#eba9ff", what_outlines=[ (1, "#3b004d") ], ctc="ctc_blink", ctc_position="nestled", callback=purring_voice)#"ainsley"
#purple
#Note she had to be 'G' for 'Good Girl'
define o = Character(_("Staff"), who_color="#e6e6e6", who_outlines=[ (1, "#000000") ], what_color="#e6e6e6", what_outlines=[ (1, "#000000") ], ctc="ctc_blink", ctc_position="nestled", callback=purring_voice)
#grey
define narrator = Character(what_color="#ffffff", what_outlines=[ (1, "#000000") ],  ctc="ctc_blink", ctc_position="nestled", callback=purring_voice)
define narrator_nvl = Character(None, kind=nvl,what_outlines=[ (1, "#000000") ], ctc="ctc_blink", ctc_position="nestled", callback=purring_voice)
#CTC
image ctc_blink:
       "gui/CTC.png"
       linear 0.75 alpha 1.0
       linear 0.75 alpha 0.0
       repeat
#logo and splashscreen
image black = "#000"
image white = "#ffffff"

image logo2 = Composite(
    (662, 653+50),
    (0, 0), "gui/bikkuri_bunny_logo.png",
    (110, 680), Text("{color=#0000ffff}A Bikkuri Bunny Production{/color}"))

#transition
define bites = ImageDissolve(im.Tile("images/transitions/bites.jpg"), 2, 8)
define test_t = ImageDissolve(im.Tile("images/transitions/test.png"), 2, 8)
define test2_t = ImageDissolve(im.Tile("images/transitions/test2.png"), 2, 8)

image logo = "gui/logo.png"

#badge
image badge = "gui/button/paw.png" #badge for choice menu
#cards
image card1 = "images/cards/card1.webp"
image card2 = "images/cards/card2.webp"
image card3 = "images/cards/card3.webp"
image card4 = "images/cards/card4.webp"
image card5 = "images/cards/card5.webp"
image card6 = "images/cards/card6.webp"
image card7 = "images/cards/card7.webp"
image partone = "images/cards/partone.webp"
image parttwo = "images/cards/parttwo.webp"

#backgrounds

#backgrounds
image gallocked = "gui/newgallery/black.png"
image bg playroom = "images/BG/playroom.webp"
image bg playroom2 = "images/BG/playroom2.webp"
image bg hallway1 = "images/BG/hallway1.webp"
image bg hallway2 = "images/BG/hallway2.webp"
image bg bedroomdark = "images/BG/bedroomdark.webp"
image bg bedroomlight = "images/BG/bedroomlight.webp"
image bg barracks = "images/BG/barracks.webp"
image bg cafeteria = "images/BG/cafeteria.webp"
image bg classroom = "images/BG/classroom.webp"
image bg clinic = "images/BG/clinic.webp"
image bg filmset = "images/BG/filmset1.webp"
image bg filmset2 = "images/BG/filmset2.webp"
image bg filmset3 = "images/BG/filmset3.webp"
image bg stevenoffice1 = "images/BG/stevenoffice1.webp"
image bg stevenoffice2 = "images/BG/stevenoffice2.webp"
image bg lukasoffice = "images/BG/lukasoffice.webp"
image bg cherryblossoms1 = "images/BG/cherryblossoms1.webp"
image bg cherryblossoms2 = "images/BG/cherryblossoms2.webp"
image bg outside1 = "images/BG/outside1.webp"
image bg outside2 = "images/BG/outsdie2.webp"
image bg officespace = "images/BG/officespace.webp"
image bg secretspace = "images/BG/secretspace.webp"
image bg staffroom = "images/BG/Staffroom.webp"
image bg hideandseekclosed = "images/BG/unchecked.webp"
image bg hideandseekopen = "images/BG/checked.webp"

#event pictures, they're called 'CGs'
image warning = "images/CG/warning.webp"
image simonsays = "images/CG/simon_says.webp"
image mathclass = "images/CG/math_class.webp"
image food = "images/CG/food.webp"
image shot = "images/CG/shot.webp"
image lesson = "images/CG/lessons.webp"
image drawing1 = "images/CG/drawing1.webp"
image drawing2 = "images/CG/drawing2.webp"
image drawing3 = "images/CG/drawing3.webp"
image drawing4 = "images/CG/drawing4.webp"
image drawing5 = "images/CG/drawing5.webp"
image pumpkinmodel = "images/CG/pumpkin_model.webp"
image secretspace = "images/CG/secret_space.webp"
image lukasride = "images/CG/lukas_ride.webp"
image paper = "images/CG/paper.webp"
image showsteven = "images/CG/showsteven.webp"
image pumpkin1 = "images/CG/pumpkin1.webp"
image lukasblow1 = "images/CG/lukas_blow_1.webp"
image lukasblow2 = "images/CG/lukas_blow_2.webp"
image lukasgift = "images/CG/lukasgift.webp"
image lukasoral1 = "images/CG/lukasoral.webp"
image piggyback = "images/CG/piggy_back.webp"
image glitterballcuddle = "images/CG/glitterballcuddle.webp"
image sparkle1 = "images/CG/sparkle1.webp"
image lukassleeping = "images/CG/lukassleeping.webp"
image artsupplies = "images/CG/artsupplies.webp"
image giftpumpkin = "images/CG/gift_pumpkin.webp"
image giftlukas = "images/CG/giftlukas.webp"
image giftsteven = "images/CG/gift_steven.webp"
image ss2ahph = "images/CG/secretspace_ahappy_phappy.webp"
image ss2acpch = "images/CG/secretspace_asad_pclosed_happy.webp"
image ss2acpcs = "images/CG/secretspace_aclosed_pclosed_sad.webp"
image ss2asps = "images/CG/secretspace_asad_psad.webp"
image ss2aspc = "images/CG/secretspace_asad_pclosed_sad.webp"
image ss2asph = "images/CG/secretspace_asad_phappy.webp"
image ss2abph = "images/CG/secretspace_ablush_phappy.webp"
#part 2
image charliecrying="images/CG/Part_2/charliecrying.webp"
image stevencrying1="images/CG/Part_2/stevencrying1.webp"

#BONUS imgs
image thanks1year="images/BONUS/thanks.png" #easter egg to show in gallery this bonus image

#sound effects
define audio.knock = "audio/knock.ogg"
define audio.dooropen = "audio/door open.ogg"
define audio.marker = "audio/marker.ogg"
define audio.ding = "audio/ding.ogg"
define audio.bell = "audio/HelixBell.ogg"

#music
define audio.musicneutral = "audio/a cats life.ogg"
define audio.musictender = "audio/another meeting.ogg"
define audio.musicsteven = "audio/blue water.ogg"
define audio.musicsecretspace = "audio/heart of snow.ogg"
define audio.musichappy = "audio/holiday3.mp3"
define audio.musicsleepy = "audio/oyasuminasai.ogg"
define audio.musiclukas = "audio/promise.ogg"
define audio.musictheme = "audio/theme.ogg"
define audio.musicupbeat = "audio/wonder snow.ogg"

#sprites
#Movie(play="images/sprites/charfolder/outfit/",mask="images/sprites/charfolder/outfit/",loop=False,image="images/sprites/charfolder/outfit/",start_image="images/sprites/charfolder/outfit/")

layeredimage side addison:
    group anim:
        attribute idle default:
            Movie(play="images/sprites/Addison/Uniform/addison_idle_color.webm", mask="images/sprites/Addison/Uniform/addison_idle_alpha.webm", loop=True)
        attribute happy:
            Movie(play="images/sprites/Addison/Uniform/addison_happy_color.webm", mask="images/sprites/Addison/Uniform/addison_happy_alpha.webm", loop=False, image="images/sprites/Addison/Uniform/addison_happy.png", start_image="images/sprites/Addison/Uniform/addison_happy_000.png")
        attribute blush:
            Movie(play="images/sprites/Addison/Uniform/addison_blush_color.webm", mask="images/sprites/Addison/Uniform/addison_blush_alpha.webm", loop=False, image="images/sprites/Addison/Uniform/addison_blush.png",start_image="images/sprites/Addison/Uniform/addison_blush_000.png")
        attribute confused:
            Movie(play="images/sprites/Addison/Uniform/addison_confused_color.webm", mask="images/sprites/Addison/Uniform/addison_confused_alpha.webm", loop=False, image="images/sprites/Addison/Uniform/addison_confused.png", start_image="images/sprites/Addison/Uniform/addison_confused_000")
        attribute laugh:
            Movie(play="images/sprites/Addison/Uniform/addison_laugh_color.webm", mask="images/sprites/Addison/Uniform/addison_laugh_alpha.webm", loop=False, image="images/sprites/Addison/Uniform/addison_laugh.png",start_image="images/sprites/Addison/Uniform/addison_laugh_000.png")
        attribute surprised:#is a placeholder static image
            "sprites/Addison/addison_surprised.png"
        attribute sad:
            Movie(play="images/sprites/Addison/Uniform/addison_sad_color.webm", mask="images/sprites/Addison/Uniform/addison_sad_alpha.webm", loop=False, image="images/sprites/Addison/Uniform/addison_sad.png",start_image="images/sprites/Addison/Uniform/addison_sad_000.png")
        attribute sleepy:
            Movie(play="images/sprites/Addison/Uniform/addison_sleepy_color.webm", mask="images/sprites/Addison/Uniform/addison_sleepy_alpha.webm", loop=False, image="images/sprites/Addison/Uniform/addiso_sleepy.png",start_image="images/sprites/Addison/Uniform/addison_sleepy_000.png")
        attribute excited:
            Movie(play="images/sprites/Addison/Uniform/addison_excited_color.webm", mask="images/sprites/Addison/Uniform/addison_excited_alpha.webm", loop=False, image="images/sprites/Addison/Uniform/addison_excited.png",start_image="images/sprites/Addison/Uniform/addison_excited_000.png")
        attribute thinking:
            Movie(play="images/sprites/Addison/Uniform/addison_thinking_color.webm", mask="images/sprites/Addison/Uniform/addison_thinking_alpha.webm", loop=False, image="images/sprites/Addison/Uniform/addison_thinking.png",start_image="images/sprites/Addison/Uniform/addison_thinking_000.png")
        attribute mad:
            Movie(play="images/sprites/Addison/Uniform/addison_angry_color.webm", mask="images/sprites/Addison/Uniform/addison_angry_alpha.webm", loop=False, image="images/sprites/Addison/Uniform/addison_angry.png",start_image="images/sprites/Addison/Uniform/addison_angry_000.png")
        attribute sad_smile:
            Movie(play="images/sprites/Addison/Uniform/addison_sad_smile_color.webm", mask="images/sprites/Addison/Uniform/addison_sad_smile_alpha.webm", loop=False, image="images/sprites/Addison/Uniform/addison_sad_smile.png",start_image="images/sprites/Addison/Uniform/addison_sad_smile_000.png")
        attribute nervous:
            Movie(play="images/sprites/Addison/Uniform/addison_nervous_color.webm", mask="images/sprites/Addison/Uniform/addison_nervous_alpha.webm", loop=False, image="images/sprites/Addison/Uniform/addison_nervous.png",start_image="images/sprites/Addison/Uniform/addison_nervous_000.png")
layeredimage side addison costume:
    group anim:
        attribute idle default:
            Movie(play="images/sprites/Addison/Costume/addison_costume_idle_color.webm", mask="images/sprites/Addison/Costume/addison_costume_idle_alpha.webm", loop=True)
        attribute happy:
            Movie(play="images/sprites/Addison/Costume/addison_costume_happy_color.webm",mask="images/sprites/Addison/Costume/addison_costume_happy_alpha.webm",loop=False,image="images/sprites/Addison/Costume/addison_costume_happy.png",start_image="images/sprites/Addison/Costume/addison_costume_happy_000.png")
        attribute blush:
            Movie(play="images/sprites/Addison/Costume/addison_costume_blush_color.webm", mask="images/sprites/Addison/Costume/addison_costume_blush_alpha.webm", loop=False, image="images/sprites/Addison/Costume/addison_costume_blush.png",start_image="images/sprites/Addison/Costume/addison_costume_blush_000.png")
        attribute confused:
            Movie(play="images/sprites/Addison/Costume/addison_constume_confused_color.webm",mask="images/sprites/Addison/Costume/addison_costume_confused_alpha.webm",loop=False,image="images/sprites/Addison/Costume/addison_costume_confused.png",start_image="images/sprites/Addison/Costume/addison_costume_confused_000.png")
        attribute laugh:
            Movie(play="images/sprites/Addison/Costume/addison_costume_laugh_color.webm", mask="images/sprites/Addison/Costume/addison_costume_laugh_alpha.webm", loop=False, image="images/sprites/Addison/Costume/addison_costume_laugh.png",start_image="images/sprites/Addison/Costume/addison_costume_laugh_000.png")
        attribute surprised:#is a placeholder static image; does not have a costume version
            "sprites/Addison/addison_surprised.png"
        attribute sad:
            Movie(play="images/sprites/Addison/Costume/addison_costume_sad_color.webm", mask="images/sprites/Addison/Costume/addison_costume_sad_alpha.webm", loop=False, image="images/sprites/Addison/Costume/addison_costume_sad.png", start_image="images/sprites/Addison/Costume/addison_costume_sad_000.png")
        attribute sleepy:
            Movie(play="images/sprites/Addison/Costume/addison_costume_sleepy_color.webm", mask="images/sprites/Addison/Costume/addison_costume_sleepy_alpha.webm", loop=False, image="images/sprites/Addison/Costume/addison_costume_sleepy.png",start_image="images/sprites/Addison/Costume/addison_costume_sleepy_000.png")
        attribute excited:
            Movie(play="images/sprites/Addison/Costume/addison_costume_excited_color.webm", mask="images/sprites/Addison/Costume/addison_costume_excited_alpha.webm", loop=False, image="images/sprites/Addison/Costume/addison_costume_excited.png", start_image="images/sprites/Addison/Costume/addison_costume_excited_000.png")
        attribute thinking:
            Movie(play="images/sprites/Addison/Costume/addison_costume_thinking_color.webm", mask="images/sprites/Addison/Costume/addison_costume_thinking_alpha.webm", loop=False, image="images/sprites/Addison/Costume/addison_costume_thinking.png", start_image="images/sprites/Addison/Costume/addison_costume_thinking_000.png")
        attribute mad:
            Movie(play="images/sprites/Addison/Costume/addison_costume_mad_color.webm", mask="images/sprites/Addison/Costume/addison_costume_mad_alpha.webm", loop=False, image="images/sprites/Addison/Costume/addison_costume_mad.png", start_image="images/sprites/Addison/Costume/addison_costume_mad_000.png")
        attribute sad_smile:
            Movie(play="images/sprites/Addison/Costume/addison_costume_sad_smile_color.webm", mask="images/sprites/Addison/Costume/addison_costume_sad_smile_alpha.webm", loop=False, image="images/sprites/Addison/Costume/addison_costume_sad_smile.png", start_image="images/sprites/Addison/Costume/addison_costume_sad_smile_000.png")
        attribute nervous null #need this
layeredimage side addison pajamas:
    group anim:
        attribute idle default:
            Movie(play="images/sprites/Addison/Pajamas/addison_idle_pajamas_color.webm", mask="images/sprites/Addison/Pajamas/addison_idle_pajamas_alpha.webm", loop=True)
        attribute happy:
            Movie(play="images/sprites/Addison/Pajamas/addison_happy_pajamas_color.webm", mask="images/sprites/Addison/Pajamas/addison_happy_pajamas_alpha.webm", loop=False, image="images/sprites/Addison/Pajamas/addison_happy_pajamas.png",start_image="images/sprites/Addison/Pajamas/addison_happy_pajamas_000.png")
        attribute sad:
            Movie(play="images/sprites/Addison/Pajamas/addison_sad_pajamas_color.webm", mask="images/sprites/Addison/Pajamas/addison_sad_pajamas_alpha.webm", loop=False, image="images/sprites/Addison/Pajamas/addison_sad_pajamas.png", start_image="images/sprites/Addison/Pajamas/addison_sad_pajamas_000.png")
        attribute sleepy:
            Movie(play="images/sprites/Addison/Pajamas/addison_sleepy_pajamas_color.webm", mask="images/sprites/Addison/Pajamas/addison_sleepy_pajamas_alpha.webm", loop=False, image="images/sprites/Addison/Pajamas/addison_sleepy_pajamas.png", start_image="images/sprites/Addison/Pajamas/addison_sleepy_pajamas_000.png")
layeredimage pumpkin:
    group emotions:
        attribute neutral default:
            "images/sprites/Pumpkin/Uniform/pumpkin_neutral.png"
        attribute happy:
            "images/sprites/Pumpkin/Uniform/pumpkin_happy.png"
        attribute thinking:
            "images/sprites/Pumpkin/Uniform/pumpkin_thinking.png"
        attribute nervous:
            "images/sprites/Pumpkin/Uniform/pumpkin_nervious.png"
        attribute excited:
            "images/sprites/Pumpkin/Uniform/pumpkin_excited.png"
        attribute sad:
            "images/sprites/Pumpkin/Uniform/pumpkin_sad.png"
        attribute blush:
            "images/sprites/Pumpkin/Uniform/pumpkin_blush.png"
        attribute laugh:
            "images/sprites/Pumpkin/Uniform/pumpkin_laugh.png"
        attribute angry:
            "images/sprites/Pumpkin/Uniform/pumpkin_angry.png"
        attribute surprised:
            "images/sprites/Pumpkin/Uniform/pumpkin_surprised.png"
        attribute confused:
            "images/sprites/Pumpkin/Uniform/pumpkin_confused.png"
        #attribute makeup_excited:
            #"images/sprites/Pumpkin/Uniform/pumpkin_makeup_excited.png"
layeredimage pumpkin costume:
    group emotions:
        attribute neutral default:
            "images/sprites/Pumpkin/Costume/pumpkin_costume_neutral.png"
        attribute happy:
            "images/sprites/Pumpkin/Costume/pumpkin_costume_happy.png"
        attribute thinking:
            "images/sprites/Pumpkin/Costume/pumpkin_costume_thinking.png"
        attribute nervous:
            "images/sprites/Pumpkin/Costume/pumpkin_costume_nervous.png"
        attribute excited:
            "images/sprites/Pumpkin/Costume/pumpkin_costume_excited.png"
        attribute sad:
            "images/sprites/Pumpkin/Costume/pumpkin_costume_sad.png"
        attribute blush:
            "images/sprites/Pumpkin/Costume/pumpkin_costume_blush.png"
        attribute laugh:
            "images/sprites/Pumpkin/Costume/pumpkin_costume_laugh.png"
        attribute angry:
            "images/sprites/Pumpkin/Costume/pumpkin_costume_angry.png"
        attribute confused:
            "images/sprites/Pumpkin/Costume/pumpkin_costume_confused.png"
layeredimage steven:
    group emotions:
        attribute neutral default:
            "images/sprites/Steven/steven_neutral.png"
        attribute happy:
            "images/sprites/Steven/steven_happy.png"
        attribute thinking:
            "images/sprites/Steven/steven_thinking.png"
        attribute angry:
            "images/sprites/Steven/steven_angry.png"
        attribute angry2:
            "images/sprites/Steven/steven_angry2.png"
        attribute sigh:
            "images/sprites/Steven/steven_sigh.png"
        attribute sad:
            "images/sprites/Steven/steven_sad.png"
        attribute excited:
            "images/sprites/Steven/steven_excited.png"
        attribute laugh:
            "images/sprites/Steven/steven_laugh.png"
        attribute sad_smile:
            "images/sprites/Steven/steven_sad_smile.png"
        attribute surprised:
            "images/sprites/Steven/steven_surprised.png"
layeredimage lukas:
    group emotions:
        attribute neutral default:
            "images/sprites/Lukas/lukas_neutral.png"
        attribute happy:
            "images/sprites/Lukas/lukas_happy.png"
        attribute laugh:
            "images/sprites/Lukas/lukas_laugh.png"
        attribute sad:
            "images/sprites/Lukas/lukas_sad.png"
        attribute angry:
            "images/sprites/Lukas/lukas_angry.png"
        attribute sad_smile:
            "images/sprites/Lukas/lukas_sad_smile.png"
        attribute confused:
            "images/sprites/Lukas/lukas_confused.png"
        attribute surprised:
            "images/sprites/Lukas/lukas_surprised.png"
        attribute sleepy:
            "images/sprites/Lukas/lukas_yawn.png"
        attribute blush:
            "images/sprites/Lukas/lukas_blush.png"
layeredimage ainsley:
    group emotions:
        attribute happy:
            "images/sprites/Ainsley/ainsley_happy.png"
        attribute sad:
            "images/sprites/Ainsley/ainsley_sad.png"
layeredimage charlie:
    group emotions:
        attribute happy default:
            "images/sprites/Charlie/charlie_happy.png"
        attribute sad:
            "images/sprites/Charlie/charlie_sad.png"
        attribute excited:
            "images/sprites/Charlie/charlie_excited.png"
        attribute confused:
            "images/sprites/Charlie/charlie_confused.png"
layeredimage jesse:
    group emotions:
        attribute neutral default:
            "images/sprites/Jesse/jesse_neutral.png"
        attribute happy:
            "images/sprites/Jesse/jesse_happy.png"
        attribute thinking:
            "images/sprites/Jesse/jesse_thinking.png"
        attribute mad:
            "images/sprites/Jesse/jesse_mad.png"

#side sprite
image side alfa = "#ffffff00" #dont erase, its used for all characters

#hide seek minigame
image hs1 = "mini_game/hide_seek/hs1.png"
image hs2 = "mini_game/hide_seek/hs2.png"
image hs3 = "mini_game/hide_seek/hs3.png"
image hs4 = "mini_game/hide_seek/hs4.png"
image hs5 = "mini_game/hide_seek/hs5.png"
image hs1_hover = "mini_game/hide_seek/hs1_hover.png"
image hs2_hover = "mini_game/hide_seek/hs2_hover.png"
image hs3_hover = "mini_game/hide_seek/hs3_hover.png"
image hs4_hover = "mini_game/hide_seek/hs4_hover.png"
image hs5_hover = "mini_game/hide_seek/hs5_hover.png"
#coding notes
#rpy monologue single

default giftsteven = False
default giftlukas = False
default giftpumpkin = False #this name is used in image
default candy = False
default stickers = False
default test = False
default kissedsteven = False

default debug_test=False #in development dont eraser
default menu_mini_game=False

default pumpkin_points = 0
default steven_points = 0
default lukas_points = 0

default persistent.secrets = False

default main_menu_bt=[True]*23 #by the code of the previous GUI
default choice_menu_bt=[True]*10

##### calendar text #########
define calendar_menu_text=[]
#############################

######### layers #############
#define config.layers = [ 'background', 'master', 'event', 'transient', 'screens', 'overlay' ]
define config.layers = ['background','master', 'background2', 'middle', 'forward','event', 'transient', 'screens', 'overlay']
init python:
    register_3d_layer('background2', 'middle', 'forward')
##############################

######### icon for app.exe ##########
define config.windows_icon="icon.ico"
#####################################

###### Cursor #############
init -1 python hide:
    config.mouse = {"default": [("images/cursors/icon.cur", 0, 0)],"menu": [("images/cursors/icon_menu.cur", 0, 0)], "minigame_draw":[("images/cursors/nat1035.cur", 0, 0)], "minigame_hs":[("images/cursors/icon_hs.cur", 0, 0)],"base": [("images/cursors/icon.cur", 0, 0)]}
###########################

###### days ###############
init:
  calendar add "Sun" "7" "3" #day0
  calendar add "Mon" "8" "3" #day1
  calendar add "Tues" "9" "3" #day2
  calendar add "Wed" "10" "3" #day3
  calendar add "Fri" "13" "3" #day4
  calendar add "Mon" "16" "3" #day5
  calendar add "Wed" "18" "3" #day6
  calendar add "Thur" "19" "3" #day7
  calendar add "Fri" "20" "3" #day8
  calendar add "Sat" "21" "3" #day9
  calendar add "Mon" "23" "3" #day10
  calendar add "Wed" "25" "3" #day11
  calendar add "Thur" "26" "3" #day12

###########################

init python:
  import functools, os
  name_pc_user=player = os.environ.get( 'USERNAME', os.environ.get( 'USER', os.environ.get( 'LNAME', os.environ.get( 'LOGNAME', 'Player' ))))

  say_speak = functools.partial(renpy.display.tts.speak, force=True)
  say_speak(_("Welcome, ")+str(name_pc_user))
  #time.sleep(1)
  #renpy.display.tts.speak("hola",force=True)
  import uuid

  myuuid_node = uuid.getnode()#uuid.uuid1()
  if not persistent.myuuid_node:
    persistent.myuuid_node=myuuid_node

  #load custom module from renpy
  renpy.exports.load_module("core/_errorhandling")
  renpy.exports.load_module("core/_accessibility")

  #purring channel
  renpy.music.register_channel("purring", "sfx", True)
  #config.speaking_attribute = "speaking"
  #addison side allways
  config.side_image_tag = "addison"
  #narrator.image_tag = "addison"
  config.tag_layer['bg'] = 'background'
  config.tag_layer['cg'] = 'event'
  def hide_quick_menu(var):
   if var:
    renpy.store.quick_menu=True
   else:
    renpy.store.quick_menu=False
   return None
  def hovered_choice_menu_bt(var):
    renpy.store.choice_menu_bt[var]=False
    return None
  def unhovered_choice_menu_bt(var):
    renpy.store.choice_menu_bt[var]=True
    return None
  def reset_choice_menu_bt():
    renpy.store.choice_menu_bt=[True]*10
    return None

  def hovered_main_menu_bt(var):
    renpy.store.main_menu_bt[var]=False
    return None
  def unhovered_main_menu_bt(var):
    renpy.store.main_menu_bt[var]=True
    return None
  def reset_main_menu_bt():
    renpy.store.main_menu_bt=[True]*23 #by the code of the previous GUI
    return None
  def crop_scale(d,area):
    #area=(x,y,x_SIZE,y_SIZE)
    b= renpy.easy_displayable(d)
    #b=im.Crop(b,(x,y,x_SIZE,y_SIZE)) x+x_SIZE<=width y+y_SIZE<=height
    b=im.Crop(b,area) 
    return b

init +1 python:
    class LoadMostRecent(Action):

        def __init__(self):
            self.slot = renpy.newest_slot("[^_]") #this way for mac

        def __call__(self):
            renpy.load(self.slot)

        def get_sensitive(self):
            return self.slot is not None
