#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  gallery.rpy
#
#  Copyright 2020 badanni <dannyvasconeze@gmail.com>
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


init python:
    import math

    def generate_pos(val,max_page):
      serie=[val]
      for aux_page in range(max_page):
        serie.append(serie[aux_page]+9)
      return serie

    # Step 1. Create the gallery object.
    gal = Gallery()
    gal.locked_button = "gui/gallery/locked.png" #this is the thumbnail image for ALL LOCKED gallery previews, found in the images folder
    gal.transition = dissolve
    #gal.hover_border = "gui/newgallery/black.png"

    # Step 2. Add buttons and images to the gallery.
    # A button that contains an image that automatically unlocks.
    list_gal_bg=["bg playroom","bg playroom2","bg hallway1","bg hallway2","bg bedroomdark","bg bedroomlight","bg barracks","bg cafeteria","bg classroom","bg clinic","bg filmset","bg filmset2","bg filmset3","bg stevenoffice1","bg stevenoffice2","bg lukasoffice","bg cherryblossoms1","bg cherryblossoms2","bg outside1","bg outside2","bg officespace", "bg secretspace", "bg staffroom"]
    list_gal_bg_img=["/gui/gallery/BG/playroom.png", "/gui/gallery/BG/playroom2.png", "/gui/gallery/BG/hallway1.png", "/gui/gallery/BG/hallway2.png", "/gui/gallery/BG/bedroomdark.png", "/gui/gallery/BG/bedroomlight.png", "/gui/gallery/BG/barracks.png", "/gui/gallery/BG/cafeteria.png", "/gui/gallery/BG/classroom.png", "/gui/gallery/BG/clinic.png", "/gui/gallery/BG/filmset1.png", "/gui/gallery/BG/filmset2.png", "/gui/gallery/BG/filmset3.jpg", "/gui/gallery/BG/stevenoffice1.png", "/gui/gallery/BG/stevenoffice2.png", "/gui/gallery/BG/lukasoffice.png", "/gui/gallery/BG/cherryblossoms1.png", "/gui/gallery/BG/cherryblossoms2.png", "/gui/gallery/BG/outside1.png", "/gui/gallery/BG/outside2.png", "/gui/gallery/BG/officespace.png", "/gui/gallery/BG/secretspace.png", "/gui/gallery/BG/staffroom.jpg"]
    list_gal_aux=list_gal_bg
    list_gal_aux_img=list_gal_bg_img
    cantidad_paginas_bg=math.ceil(len(list_gal_bg)/float(9))
    list_gal_cg=["simonsays","mathclass","food","shot","pumpkin_model","secretspace","lukasride","showsteven","lesson","sparkle1","piggyback","pumpkin1","lukasblow1","lukasoral1","lukassleeping","artsupplies","giftsteven","lukasgift","giftpumpkin","ss2ahph","charliecrying","stevencrying1"]
    list_gal_cg_img=["/gui/gallery/CG/simon_says.png","/gui/gallery/CG/math_class.png","/gui/gallery/CG/food.png","/gui/gallery/CG/shot.png","/gui/gallery/CG/pumpkin_model.png","/gui/gallery/CG/secret_space.png","/gui/gallery/CG/lukas_ride.png","/gui/gallery/CG/showsteven.png","/gui/gallery/CG/lessons.png","/gui/gallery/CG/sparkle1.png","/gui/gallery/CG/piggy_back.png","/gui/gallery/CG/pumpkin1.png","/gui/gallery/CG/lukas_blow_1.png","/gui/gallery/CG/lukasoral.png","/gui/gallery/CG/lukassleeping.png","/gui/gallery/CG/artsupplies.png","/gui/gallery/CG/gift_steven.png","/gui/gallery/CG/lukasgift.png","/gui/gallery/CG/gift_pumpkin.png","/gui/gallery/CG/secretspace_Ahappy_Phappy.png","/gui/gallery/CG/Part_2/charliecrying.png","/gui/gallery/CG/Part_2/stevencrying1.png"]
    cantidad_paginas_cg=math.ceil(len(list_gal_cg)/float(9))

    list_gal_bonus=["thanks1year"]
    list_gal_bonus_img=["/gui/gallery/BONUS/thanks.png"]
    cantidad_paginas_bonus=math.ceil(len(list_gal_bonus)/float(9))

    def init_gallery(gal,list_gal,type_str=""):
      for i in list_gal:
        aux=i
        gal.button(i)
        gal.unlock_image(i)
    init_gallery(gal,list_gal_bg)
    init_gallery(gal,list_gal_cg,"cg_")
    init_gallery(gal,list_gal_bonus)

    #gal.button("bg playroom") #this is the name/label associated with your button for a particular image, can be modified
    #gal.condition("persistent.bg_playroom") #this is the requirement/condition that must be met for this gallery image to unlock
    #gal.image("bg playroom") #this creates a gallery image that overlaps a foreground on top of a bg, you can also use a single flattened image here

    #gal.button("bg playroom2")
    #gal.condition("persistent.bg_playroom2")
    #gal.image("bg playroom2")

    #gal.button("bg hallway1")
    #gal.condition("persistent.bg_hallway1")
    #gal.image("bg hallway1")

    #gal.button("bg hallway2")
    #gal.condition("persistent.bg_hallway2")
    #gal.image("bg hallway2")

screen gallery():
    # Ensure this replaces the main menu.
    default page_gallery=1
    default page_title="BG"
    default img1=[0]
    default img2=[1]
    default img3=[2]
    default img4=[3]
    default img5=[4]
    default img6=[5]
    default img7=[6]
    default img8=[7]
    default img9=[8]
    if page_gallery<=0:
      $ page_gallery=1
    if page_title in ["BG"]:
      $ max_page=int(cantidad_paginas_bg)
      $ list_gal_aux=list_gal_bg
      $ list_gal_aux_img=list_gal_bg_img
    if page_title in ["CG"]:
      $ max_page=int(cantidad_paginas_cg)
      $ list_gal_aux=list_gal_cg
      $ list_gal_aux_img=list_gal_cg_img
    if page_title in ["BONUS"]:
      $ max_page=int(cantidad_paginas_bonus)
      $ list_gal_aux=list_gal_bonus
      $ list_gal_aux_img=list_gal_bonus_img
    if page_title in ["BG"] and page_gallery>cantidad_paginas_bg:
      $ page_gallery = int(cantidad_paginas_bg)
    if page_title in ["CG"] and page_gallery>cantidad_paginas_cg:
      $ page_gallery = int(cantidad_paginas_cg)
    if page_title in ["BONUS"] and page_gallery>cantidad_paginas_bonus:
      $ page_gallery = int(cantidad_paginas_bonus)
    $ img1=generate_pos(0,max_page)
    $ img2=generate_pos(1,max_page)
    $ img3=generate_pos(2,max_page)
    $ img4=generate_pos(3,max_page)
    $ img5=generate_pos(4,max_page)
    $ img6=generate_pos(5,max_page)
    $ img7=generate_pos(6,max_page)
    $ img8=generate_pos(7,max_page)
    $ img9=generate_pos(8,max_page)

    tag menu

    zorder 100
    # The background.
    add "gui/gallery/gallery_menu.png" #this is the bg image for the gallery; found in the images folder
    $ textImagen=At(Text(gui.text_version_menu), Transform(rotate=-2))
    image textImagen:
       xpos gui.text_version_leftX#1280
       ypos gui.text_version_leftY



    # A grid of buttons.

    vbox:
        style_prefix "navigation_main"

        xpos gui.navigation_xpos
        #yalign 0.5
        ypos 424
        xsize 500
        xalign 0.0
        ysize 400

        #spacing gui.navigation_spacing
        frame:
            background None
            ysize 55
            imagebutton:
                auto "gui/button/short_button_%s.png"
                action SetScreenVariable("page_title", "BG")
                hovered Function(hovered_choice_menu_bt,1)
                unhovered Function(unhovered_choice_menu_bt,1)
                if choice_menu_bt[1]:
                    foreground None
                else:
                    foreground Transform("badge", xpos=0, yalign=.5)
            text _("Backgrounds"):
                xalign 0.5
                yalign 3.5

        frame:
            ysize 55
            imagebutton:
                auto "gui/button/short_button_%s.png"
                action SetScreenVariable("page_title", "CG")
                hovered Function(hovered_choice_menu_bt,2)
                unhovered Function(unhovered_choice_menu_bt,2)
                if choice_menu_bt[2]:
                    foreground None
                else:
                    foreground Transform("badge", xpos=0, yalign=.5)
            text _("CGs") xalign 0.5 yalign 3.5
        frame:
            ysize 55
            imagebutton:
                auto "gui/button/short_button_%s.png"
                action SetScreenVariable("page_title", "BONUS")
                hovered Function(hovered_choice_menu_bt,3)
                unhovered Function(unhovered_choice_menu_bt,3)
                if choice_menu_bt[3]:
                    foreground None
                else:
                    foreground Transform("badge", xpos=0, yalign=.5)
            text _("Bonus") xalign 0.5 yalign 3.5
        frame:
            ysize 55
            imagebutton:
                auto "gui/button/short_button_%s.png"
                action Return()
                hovered Function(hovered_choice_menu_bt,4)
                unhovered Function(unhovered_choice_menu_bt,4)
                if choice_menu_bt[4]:
                    foreground None
                else:
                    foreground Transform("badge", xpos=0, yalign=.5)
            text _("Back") xalign 0.5 yalign 3.5

    #    frame:
        #    if main_menu_bt[7]:
        #        background im.Scale("gui/button_hover.png", 500, 100)
        #    else:
        #        background im.Scale("gui/button_idle.png", 500, 100)
        #    hbox:
        #        textbutton _("B G"):
        #            action SetScreenVariable("page_title", "BG")
        #            hovered Function(hovered_main_menu_bt,7)
        #            unhovered Function(unhovered_main_menu_bt,7)
        #            xmaximum 500
        #            xminimum 500
        #            xalign 0.5
        #            ypos 10
        #frame:
         # if main_menu_bt[8]:
        #    background im.Scale("gui/button_hover.png", 500, 100)
         # else:
        #    background im.Scale("gui/button_idle.png", 500, 100)
         # hbox:
        #    textbutton _("C G"):
        #      action SetScreenVariable("page_title", "CG")
        #      hovered Function(hovered_main_menu_bt,8)
        #      unhovered Function(unhovered_main_menu_bt,8)
        #      xmaximum 500
        #      xminimum 500
        #      xalign 0.5
        #      ypos 10
        #frame:
         # if main_menu_bt[9]:
        #    background im.Scale("gui/button_hover.png", 500, 100)
         # else:
        #    background im.Scale("gui/button_idle.png", 500, 100)
         # hbox:
        #    textbutton _("B O N U S"):
        #      action SetScreenVariable("page_title", "BONUS")
        #      hovered Function(hovered_main_menu_bt,9)
        #      unhovered Function(unhovered_main_menu_bt,9)
        #      xmaximum 500
        #      xminimum 500
        #      xalign 0.5
        #      ypos 10
        #frame:
         # if main_menu_bt[10]:
        #    background im.Scale("gui/button_hover.png", 500, 100)
         # else:
        #    background im.Scale("gui/button_idle.png", 500, 100)
         # hbox:
        #    textbutton _("B A C K"):
        #      action Return()
        #      hovered Function(hovered_main_menu_bt,10)
        #      unhovered Function(unhovered_main_menu_bt,10)
        #      xmaximum 500
        #      xminimum 500
        #      xalign 0.5
        #      ypos 10
    ####Imgs
    grid 3 3:

        area (728,58,1162,868)
        xfill True
        yfill True

        # Call make_button to show a particular button.
        #add im.Scale(img_path, 385, 217) ubicr en posicion de fondo adecuada
        # validar con serias (mas 4) para cada elemento de la galeria
        # verificar si existe posicion antes de graficar
        if 0<=img1[page_gallery-1]<len(list_gal_aux):
          add gal.make_button(list_gal_aux[img1[page_gallery-1]], list_gal_aux_img[img1[page_gallery-1]], xalign=0.5, yalign=0.5) # 0,4,8,12,16,20,24
        else:
          null
        if 0<=img2[page_gallery-1]<len(list_gal_aux):
          add gal.make_button(list_gal_aux[img2[page_gallery-1]], list_gal_aux_img[img2[page_gallery-1]], xalign=0.5, yalign=0.5) # 1,5,9,13,17,21,25
        else:
          null
        if 0<=img3[page_gallery-1]<len(list_gal_aux):
          add gal.make_button(list_gal_aux[img3[page_gallery-1]], list_gal_aux_img[img3[page_gallery-1]], xalign=0.5, yalign=0.5) # 2,6,10,14,18,22,26
        else:
          null
        if 0<=img4[page_gallery-1]<len(list_gal_aux):
          add gal.make_button(list_gal_aux[img4[page_gallery-1]], list_gal_aux_img[img4[page_gallery-1]], xalign=0.5, yalign=0.5) # 3,7,1115,19,23,27
        else:
          null
        if 0<=img5[page_gallery-1]<len(list_gal_aux):
          add gal.make_button(list_gal_aux[img5[page_gallery-1]], list_gal_aux_img[img5[page_gallery-1]], xalign=0.5, yalign=0.5) # 3,7,1115,19,23,27
        else:
          null
        if 0<=img6[page_gallery-1]<len(list_gal_aux):
          add gal.make_button(list_gal_aux[img6[page_gallery-1]], list_gal_aux_img[img6[page_gallery-1]], xalign=0.5, yalign=0.5) # 3,7,1115,19,23,27
        else:
          null
        if 0<=img7[page_gallery-1]<len(list_gal_aux):
          add gal.make_button(list_gal_aux[img7[page_gallery-1]], list_gal_aux_img[img7[page_gallery-1]], xalign=0.5, yalign=0.5) # 3,7,1115,19,23,27
        else:
           null
        if 0<=img8[page_gallery-1]<len(list_gal_aux):
            add gal.make_button(list_gal_aux[img8[page_gallery-1]], list_gal_aux_img[img8[page_gallery-1]], xalign=0.5, yalign=0.5) # 3,7,1115,19,23,27
        else:
            null
        if 0<=img9[page_gallery-1]<len(list_gal_aux):
          add gal.make_button(list_gal_aux[img9[page_gallery-1]], list_gal_aux_img[img9[page_gallery-1]], xalign=0.5, yalign=0.5) # 3,7,1115,19,23,27
        else:
          null


    hbox:
        style_prefix "navigation_main"
        area (728,944,1162,100)
        xalign 0.5
        #return to main menu
        if page_gallery!=1:
          textbutton "<<" action SetScreenVariable("page_gallery", page_gallery-1) xalign 0.5 yalign 0.5
        else:
          text "{color=#FFFFFF00}<<{/color}"
        text "{font=fonts/endutt.otf}{color=#7f7ab1}Page {font=fonts/Chewy.ttf}[page_gallery]{/font}{/color}{/font}" xalign 0.5 yalign 0.5
        if page_gallery!=max_page:
          textbutton ">>" action SetScreenVariable("page_gallery", page_gallery+1) xalign 0.5 yalign 0.5
        else:
          text "{color=#FFFFFF00}>>{/color}"
