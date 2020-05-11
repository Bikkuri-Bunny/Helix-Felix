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
    gal.idle_border = "gui/gallery/frame.png"
    gal.hover_border = "gui/gallery/framehover.png"
    thumbnailx = 400
    thumbnaily = 300


    # Step 2. Add buttons and images to the gallery.
    # A button that contains an image that automatically unlocks.
    list_gal_bg=["bg playroom","bg playroom2","bg hallway1","bg hallway2","bg bedroomdark","bg bedroomlight","bg barracks","bg cafeteria","bg classroom","bg clinic","bg filmset","bg filmset2","bg filmset3","bg stevenoffice1","bg stevenoffice2","bg lukasoffice","bg cherryblossoms1","bg cherryblossoms2","bg outside1","bg outside2","bg officespace", "bg secretspace", "bg staffroom"]
    list_gal_bg_img=["/images/BG/playroom.webp", "/images/BG/playroom2.webp", "/images/BG/hallway1.webp", "/images/BG/hallway2.webp", "/images/BG/bedroomdark.webp", "/images/BG/bedroomlight.webp", "/images/BG/barracks.webp", "/images/BG/cafeteria.webp", "/images/BG/classroom.webp", "/images/BG/clinic.webp", "/images/BG/filmset1.webp", "/images/BG/filmset2.webp", "/images/BG/filmset3.webp", "/images/BG/stevenoffice1.webp", "/images/BG/stevenoffice2.webp", "/images/BG/lukasoffice.webp", "/images/BG/cherryblossoms1.webp", "/images/BG/cherryblossoms2.webp", "/images/BG/outside1.webp", "/images/BG/outside2.webp", "/images/BG/officespace.webp", "/images/BG/secretspace.webp", "/images/BG/staffroom.webp"]
    list_gal_aux=list_gal_bg
    list_gal_aux_img=list_gal_bg_img
    cantidad_paginas_bg=math.ceil(len(list_gal_bg)/float(9))
    list_gal_cg=["simonsays","mathclass","food","shot","pumpkin_model","secretspace","showsteven","lesson","sparkle1","piggyback","lukassleeping","artsupplies","giftsteven","lukasgift","giftpumpkin","ss2ahph","charliecrying","stevencrying1"]
    list_gal_cg_img=["/images/CG/simon_says.png","/images/CG/math_class.png","/images/CG/food.png","/images/CG/shot.png","/images/CG/pumpkin_model.png","/images/CG/secret_space.png","/images/CG/showsteven.png","/images/CG/lessons.png","/images/CG/sparkle1.png","/images/CG/piggy_back.png","/images/CG/lukassleeping.png","/images/CG/artsupplies.png","/images/CG/gift_steven.png","/images/CG/lukasgift.png","/images/CG/gift_pumpkin.png","/images/CG/secretspace_Ahappy_Phappy.png","/images/CG/Part_2/charliecrying.png","/images/CG/Part_2/stevencrying1.png"]
    cantidad_paginas_cg=math.ceil(len(list_gal_cg)/float(9))
    list_gal_r18=["lukasride", "pumpkin1", "lukasblow1", "lukasoral1",]
    list_gal_r18_img=["/images/CG/lukas_ride.png", "/images/CG/pumpkin1.png", "/images/CG/lukas_blow_1.png", "/images/CG/lukasoral.png",]
    cantidad_paginas_r18=math.ceil(len(list_gal_r18)/float(9))


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
    init_gallery(gal,list_gal_r18)



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
    if page_title in ["R18"]:
      $ max_page=int(cantidad_paginas_r18)
      $ list_gal_aux=list_gal_r18
      $ list_gal_aux_img=list_gal_r18_img
    if page_title in ["BG"] and page_gallery>cantidad_paginas_bg:
      $ page_gallery = int(cantidad_paginas_bg)
    if page_title in ["CG"] and page_gallery>cantidad_paginas_cg:
      $ page_gallery = int(cantidad_paginas_cg)
    if page_title in ["BONUS"] and page_gallery>cantidad_paginas_bonus:
      $ page_gallery = int(cantidad_paginas_bonus)
    if page_title in ["R18"] and page_gallery>cantidad_paginas_bonus:
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
    add gui.gallery_background
    add gui.logo size 750, 400 xoffset -20 yoffset -20



    # A grid of buttons.

    vbox:
        style_prefix "menu_button"
        yalign 0.8
        xsize 500
        xalign 0.0
        xoffset 60
        ysize 400
        fixed:
            xsize 570
            ysize 120
            imagebutton:
                auto "gui/button/short_button_%s.png"
                action SetScreenVariable("page_title", "BG")
            text _("Backgrounds"):
                xalign 0.5
                yalign 0.5

        fixed:
            xsize 570
            ysize 140
            imagebutton:
                auto "gui/button/short_button_%s.png"
                action SetScreenVariable("page_title", "CG")
            text _("CGs") xalign 0.5 yalign 0.5
        fixed:
            xsize 570
            ysize 130
            imagebutton:
                auto "gui/button/short_button_%s.png"
                action SetScreenVariable("page_title", "BONUS")
            text _("Bonus") xalign 0.5 yalign 0.5
        if persistent._legal_age == True:
            fixed:
                xsize 570
                ysize 130
                imagebutton:
                    auto "gui/button/short_button_%s.png"
                    action SetScreenVariable("page_title", "R18")
                text _("R{font=fonts/chewy.ttf}18{/font}") xalign 0.5 yalign 0.5
        fixed:
            xsize 570
            ysize 130
            imagebutton:
                auto "gui/button/short_button_%s.png"
                action Return()
            text _("Back") xalign 0.5 yalign 0.5


    ####Imgs
    grid 3 3:

        area (728,58,1200,900)
        xfill True
        yfill True

        # Call make_button to show a particular button.
        #add im.Scale(img_path, 385, 217) ubicr en posicion de fondo adecuada
        # validar con serias (mas 4) para cada elemento de la galeria
        # verificar si existe posicion antes de graficar
        if 0<=img1[page_gallery-1]<len(list_gal_aux):
          add gal.make_button(list_gal_aux[img1[page_gallery-1]], im.Scale(list_gal_aux_img[img1[page_gallery-1]], thumbnailx, thumbnaily), xalign=0.5, yalign=0.5) # 0,4,8,12,16,20,24
        else:
          null
        if 0<=img2[page_gallery-1]<len(list_gal_aux):
          add gal.make_button(list_gal_aux[img2[page_gallery-1]], im.Scale(list_gal_aux_img[img2[page_gallery-1]], thumbnailx, thumbnaily), xalign=0.5, yalign=0.5) # 1,5,9,13,17,21,25
        else:
          null
        if 0<=img3[page_gallery-1]<len(list_gal_aux):
          add gal.make_button(list_gal_aux[img3[page_gallery-1]], im.Scale(list_gal_aux_img[img3[page_gallery-1]], thumbnailx, thumbnaily), xalign=0.5, yalign=0.5) # 2,6,10,14,18,22,26
        else:
          null
        if 0<=img4[page_gallery-1]<len(list_gal_aux):
          add gal.make_button(list_gal_aux[img4[page_gallery-1]], im.Scale(list_gal_aux_img[img4[page_gallery-1]], thumbnailx, thumbnaily), xalign=0.5, yalign=0.5) # 3,7,1115,19,23,27
        else:
          null
        if 0<=img5[page_gallery-1]<len(list_gal_aux):
          add gal.make_button(list_gal_aux[img5[page_gallery-1]], im.Scale(list_gal_aux_img[img5[page_gallery-1]], thumbnailx, thumbnaily), xalign=0.5, yalign=0.5) # 3,7,1115,19,23,27
        else:
          null
        if 0<=img6[page_gallery-1]<len(list_gal_aux):
          add gal.make_button(list_gal_aux[img6[page_gallery-1]], im.Scale(list_gal_aux_img[img6[page_gallery-1]], thumbnailx, thumbnaily), xalign=0.5, yalign=0.5) # 3,7,1115,19,23,27
        else:
          null
        if 0<=img7[page_gallery-1]<len(list_gal_aux):
          add gal.make_button(list_gal_aux[img7[page_gallery-1]], im.Scale(list_gal_aux_img[img7[page_gallery-1]], thumbnailx, thumbnaily), xalign=0.5, yalign=0.5) # 3,7,1115,19,23,27
        else:
           null
        if 0<=img8[page_gallery-1]<len(list_gal_aux):
            add gal.make_button(list_gal_aux[img8[page_gallery-1]], im.Scale(list_gal_aux_img[img8[page_gallery-1]], thumbnailx, thumbnaily), xalign=0.5, yalign=0.5) # 3,7,1115,19,23,27
        else:
            null
        if 0<=img9[page_gallery-1]<len(list_gal_aux):
          add gal.make_button(list_gal_aux[img9[page_gallery-1]], im.Scale(list_gal_aux_img[img9[page_gallery-1]], thumbnailx, thumbnaily), xalign=0.5, yalign=0.5) # 3,7,1115,19,23,27
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
        text "{font=fonts/endutt.otf}{color=#767777}Page {font=fonts/Chewy.ttf}[page_gallery]{/font}{/color}{/font}" xalign 0.5 yalign 0.5
        if page_gallery!=max_page:
          textbutton ">>" action SetScreenVariable("page_gallery", page_gallery+1) xalign 0.5 yalign 0.5
        else:
          text "{color=#FFFFFF00}>>{/color}"
style gallery_text:
    font gui.gallery_text_font
    size gui.gallery_text_size
style menu_button_text:
    font gui.menu_button_text_font
    size 70
    color "#ffffffBF"
