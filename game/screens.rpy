################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    unscrollable "hide" # Prevents Ren'Py from showing a scrollbar when there's nothing to scroll


style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"



    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                frame:
                  background None #None hide background
                  area (100,10,178,91)#(x0,y0,xsize,ysize)
                  text who:
                    id "who"
                    color "#35b2c7"
                    #size 28
                    xalign 0.5
                    yalign 0.5
                    #font "fonts/ConcertOne-Regular.ttf"


        text what:
           id "what"
           #font "fonts/bucc.ttf"
    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0




## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos #410
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos #0
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos 455#415#gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## End Credits Scroll ############################################################
## ATL for scrolling screen object. In this case, credits roll.
## Speed is the time for object to move up from initial ypos to finish ypos.

## Code Source: https://lemmasoft.renai.us/forums/viewtopic.php?t=42667

transform credits_scroll(speed):
    ypos 4000
    linear speed ypos -4000
    ## Adjust these numbers to be the height of your end credits. Both numbers
    ## should be the same.

## Credits screen.

screen credits():

    ## Ensure that the game_menu screens don't appear and interrupt the credits.
    key "K_ESCAPE" action NullAction()
    key "K_MENU" action NullAction()
    key "mouseup_3" action NullAction()

    style_prefix "credits"

    ## If a player has seen the end credits before, this button appears.
    if persistent.credits_seen:

        textbutton _("Skip End Credits") action Jump("skip_credits") xalign 1.0 yalign 1.0

    timer 15.0 action Return()
    ## Adjust this number to control when the Credits screen is hidden and the game
    ## returns to its normal flow.
    ## Ideally, there is some wait time after the the credits reaches the end.

    frame at credits_scroll(10.0):
        ## Adjust this number to control the speed at which the credits scroll.
        background None
        xalign 0.5

        vbox:
            label "Credits" xalign 0.5

            null height 300

            text "Director" size 100
            null height 50
            text "Briarmae"

            #null height 200

            # text "Logo" size 100
            # null height 50
            # text "Lorem Ipsum"

            #null height 200

            text "Script" size 100
            null height 50
            hbox:

                xalign 0.5
                spacing 200

                text "Briarmae"

                text "HarukaNami" #ok

            null height 200

            text "Art" size 100
            null height 50

            text "Briarmae"

            null height 200

            text "Music and Sound Designer" size 100
            null height 50

            text "Fogheart, Joe Schwebke"

            null height 200

            # text "GUI Template" size 100
            text "Programming" size 100
            null height 50

            hbox:

                xalign 0.5
                spacing 200

                text "Tanix"

                text "Badanni"

            text "Also" size 100
            null height 50

            hbox:

                xalign 0.5
                spacing 200

                text "OP Voice Acting: Yuuna Saito"

                text "OP Motion Graphics: Vidveo and other CC0 motion graphics"

                text "Background Art: Unsplash, Pixabay, and other CC0 photography"

                text "Sound Effects: Freesound and other CC0 sound"

            null height 50
            hbox:
                xalign 0.5
                spacing 200

                text "Programs: Ren'py, Live2D, Ibispaint X, OpenShot, LogoMaker"
            null height 80
            text "Special Thanks To" size 100
            null height 50

            hbox:

                xalign 0.5
                spacing 200

                text "Rhin, Eric, Tomoka, Lemmasoft, and everyone else who helped us along"

            null height 50

            #hbox:

            #    xalign 0.5
            #    spacing 200

            #    text "minute"

            #    text "npckc"

            null height 200

            # text "Trailer" size 100
            # null height 50
            # text "Lorem Ipsum"

            # null height 200

            # text "Voiceover" size 100
            # null height 50

            # hbox:
            #     xalign 0.5
            #     spacing 250

            #     vbox:

            #         text "Lorem Ipsum"

            #     vbox:

            #         text "Lorem Ipsum"

            # null height 200

            # text "Backers" size 100
            # null height 50

            # hbox:

            #     xalign 0.5
            #     spacing 100
            #     style_prefix "backercredits"

            #     vbox:

            #         text "Lorem Ipsum"

            #     vbox:

            #         text "Lorem Ipsum"

            #     vbox:

            #         text "Lorem Ipsum"

            text "A Bikkuri Bunny Production" size 100

            null height 450

            text "Thanks for Playing!" size 100

style credits_hbox:
    spacing 40
    ysize 30

style credits_label_text:
    xalign 0.5
    size 200
    text_align 0.5

style credits_text:
    xalign 0.5
    size 80
    justify True
    text_align 0.5

style backercredits_text:
    xalign 0.5
    size 50
    justify True
    text_align 0.5

## Results Screen ############################################################
## A screen that displays how much of the game the player has seen.

## Code for Read Percentage: https://lemmasoft.renai.us/forums/viewtopic.php?t=39859
## Official Documentation of function: https://www.renpy.org/doc/html/other.html#renpy.count_dialogue_blocks

## This creates a percentage based on how much of the game the player has seen.
init python:
    numblocks = renpy.count_dialogue_blocks()
    def percent():
        global readtotal
        readtotal = renpy.count_seen_dialogue_blocks()* 100 / numblocks

default readtotal = 0

## Code for Total Playtime: https://lemmasoft.renai.us/forums/viewtopic.php?t=40407
## Official Documentation of function: https://www.renpy.org/doc/html/other.html#renpy.get_game_runtime

default playtime = 0

init 2 python:

    def total_playtime(d):
        renpy.store.playtime += renpy.get_game_runtime()
        #renpy.clear_game_runtime()
        d["playtime"] = renpy.store.playtime

    #config.save_json_callbacks = [total_playtime]

## Actual results screen itself
screen results():

    zorder 200

    vbox:
        xalign .5
        yalign .2
        spacing 45

        text "Script Seen: [readtotal]%"

        ## Calculates how long a player has taken to reach this screen in a single playthrough.
        $ minutes, seconds = divmod(int(playtime), 60)
        $ hours, minutes = divmod(minutes, 60)

        text "[hours:02d]:[minutes:02d]:[seconds:02d]"

        null height 450

        text "Fin"

## For a screen that updates in real time, use the following:
## show screen _progress

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items,badge=True):
    style_prefix "choice"
    vbox:
        for j,i in enumerate(items):
            #$ badge = i.kwargs.get("badge", None)
            textbutton i.caption:
              action [i.action,Function(reset_choice_menu_bt)]
              hovered Function(hovered_choice_menu_bt,j)
              unhovered Function(unhovered_choice_menu_bt,j)
              if badge:
                     if choice_menu_bt[j]:
                         foreground None
                     else:
                         foreground Transform("badge", xpos=0, yalign=.5)




## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 505
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is button:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    outlines  [(1, "#330000", 0, 0)]
    yalign 0.5
## Calendar screen #############################################################
##
##
##
screen calendar_menu():
    zorder 110
    if True:
      frame:
        background "gui/calendar.png"
        xpos 1575
        frame:
            background None #"#000000AA"
            area (80, 225, 178, 91)#(1392,37,176,91)
            text calendar_text[0]:
              color "#7c8cc6"
              size 50
              xalign 0.5
              yalign 0.5
              font "fonts/endutt.otf"

        frame:
            background None
            area (70,75,113,91)#(1589,40,113,84)
            text calendar_text[1]:
              color "#7c8cc6"
              size 125
              xalign 0.5
              yalign 0.5
              font "fonts/Chewy.ttf"
        frame:
            background None
            area (150,155,112,91)
            text calendar_text[2]:
              color "#7c8cc6"
              size 125
              xalign 0.5
              yalign 0.5
              font "fonts/Chewy.ttf"


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():
    ## Ensure this appears on top of other screens.
    zorder 100

    if (renpy.exists('debug/debug.rpyc') or renpy.exists('debugger.rpa')):
      use renedit_overlay
    if quick_menu:
      if not menu_mini_game:
        hbox:
          style_prefix "quick"
          xalign 0.5
          yalign 1.0
          textbutton _("Save") action QuickSave()
          textbutton _("Load") action QuickLoad()
          textbutton _("Auto") action Preference("auto-forward", "toggle")
          textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
          textbutton _("Back") action Rollback()
          textbutton _("History") action ShowMenu("history")
          textbutton _("Menu") action ShowMenu("preferences")

    else:
        if menu_mini_game:
          imagebutton auto "gui/open_menu_%s.png" action Function(hide_quick_menu,**{"var":True})
        else:
          pass
        #if not renpy.android or not renpy.ios:
        #  imagemap:
        #    idle "gui/main_menu_all_small_close.png"
        #    hover "gui/main_menu_all_small_close_hover.png"
        #    ground "gui/main_menu_all_small_close.png"
        #    hotspot (1594,692,71,66) action Function(hide_quick_menu,**{"var":True})
        #else:
        #  imagebutton auto "gui/open_menu_%s.png" action Function(hide_quick_menu,**{"var":True})



## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "menu_button"

        #yalign 0.5
        ypos 424
        xmaximum 500
        xminimum 500
        xalign 0
        xoffset 60
        #ysize 600
        if not main_menu:
            fixed:
                xsize 570
                ysize 130
                imagebutton:
                    auto "gui/button/short_button_%s.png"
                    action ShowMenu("save")
                text _("Save"):
                    xalign 0.5
                    yalign 0.5
            fixed:
                xsize 570
                ysize 130
                imagebutton:
                    auto "gui/button/short_button_%s.png"
                    action ShowMenu("load")
                text _("Load"):
                    xalign 0.5
                    yalign 0.5
        fixed:
            xsize 570
            ysize 130
            imagebutton:
                auto "gui/button/short_button_%s.png"
                action ShowMenu("preferences")
            text _("Preferences"):
                xalign 0.5
                yalign 0.5
        if not main_menu:
            fixed:
                xsize 570
                ysize 130
                imagebutton:
                    auto "gui/button/short_button_%s.png"
                    action ShowMenu("gallery")
                text _("Gallery"):
                    xalign 0.5
                    yalign 0.5
            fixed:
                xsize 570
                ysize 130
                imagebutton:
                    auto "gui/button/short_button_%s.png"
                    action ShowMenu("achievements")
                text _("Achievements"):
                    xalign 0.5
                    yalign 0.5
        if not main_menu:
          fixed:
            xsize 570
            ysize 130
            imagebutton:
                auto "gui/button/short_button_%s.png"
                action MainMenu()
            text _("Main Menu"):
                xalign 0.5
                yalign 0.5
        else:
          fixed:
            xsize 570
            ysize 130
            imagebutton:
                auto "gui/button/short_button_%s.png"
                action Return()
            text _("Return"):
                xalign 0.5
                yalign 0.5
        if main_menu:
         frame:
          if main_menu_bt[18]:
            background im.Scale("gui/button_hover.png", 500, 100)
          else:
            background im.Scale("gui/button_idle.png", 500, 100)
          hbox:
            textbutton _("A B O U T"):
              action ShowMenu("about")
              hovered Function(hovered_main_menu_bt,18)
              unhovered Function(unhovered_main_menu_bt,18)
              xmaximum 500
              xminimum 500
              xalign 0.5
              ypos 10

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")



## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame:# is empty
    background Frame("gui/overlay/background_menu.png",25,25)
    xpos 200
    left_padding 15
    right_padding 15
    top_padding 15
    bottom_padding 20
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1150 #1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:
            label "[config.name!t]":
              xalign 0.5
            text _("Version [config.version!t]"):
              xalign 0.5
            null height 40
            text _("Thank you for trying this pre-release version! It is only the first 1/3rd of the story, so I hope you come back for the rest!")
            null height 80
            text _("Credits"):
              xalign 0.5
            text _("""
Director/Story/Art/Script: Briar
Script Edit and Polish: HarukaNami
Programming: Tanix, Badanni
Art Director: Kimopoleis
General Nonsense: PruJo
Background Art and Reference Photos: Unsplash, Pixabay, and other CC0 photography
Music: Fogheart, Joe Schwebke
Sound Effects: Freesound and other CC0 sound
OP Voice Acting: Yuuna Saito
OP motion graphics: Videvo and other CC0 graphics
Programs used: Live2D, IbisPaint X, OpenShot, and of course,
""")

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].") at delayed_blink(0.0, 1.0)
            null height 20
            text _("[renpy.license!t]")


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            xsize 1100
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    predict False

    frame:

        style_prefix "history"

        label _("History")

        left_margin 200
        right_margin 200
        top_margin 50
        bottom_margin 50

        left_padding 50
        right_padding 100
        top_padding 150
        bottom_padding 100

        vpgrid:

            cols 1
            yinitial 1.0

            draggable True
            mousewheel True
            scrollbars "vertical"

            for h in _history_list:

                window:

                    ## This lays things out properly if history_height is None.
                    has fixed:
                        yfit True

                    if h.who:

                        label h.who + ":":
                            style "history_name"

                            ## Take the color of the who text from the Character, if
                            ## set.
                            if "color" in h.who_args:
                                text_color h.who_args["color"]

                    $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    text h.what:
                        color h.what_args["color"]



            if not _history_list:

                text "The dialogue history is empty." line_spacing 10
                ## Adding line_spacing prevents the bottom of the text
                ## from getting cut off. Adjust when replacing the
                ## default fonts.

        textbutton _("Return") action Return() yalign 1.1 xalign 1.0


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5
    ypos -100
    size gui.label_text_size

## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:
        background Frame("gui/overlay/confirm_box.png", 650, 300)
        xpos 1530
        ypos 250
        xmaximum 600
        vbox:
            xalign 1.0
            yalign 0#.5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5
            hbox:
               xalign 0.5
               spacing 150

               textbutton _("Yes"):
                 action yes_action
               textbutton _("No"):
                 action no_action


    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text:# is gui_prompt_text
  color "#ffffff"
  #bold True
  # "fonts/ChildWriting-Regular.ttf"
style confirm_button is gui_medium_button
style confirm_button_text:# is gui_medium_button_text
  color "#ffffff"#color "#7f7ab1"
  #bold True
  hover_color "#b1ddff"
  selected_color "#ff0"
  #font "fonts/ChildWriting-Regular.ttf"

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skipping.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png",gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 900
