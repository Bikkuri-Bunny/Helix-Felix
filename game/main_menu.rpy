#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main_menu.rpy
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

## Navigation main screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation_main():
    
    if (renpy.exists('debug/debug.rpyc') or renpy.exists('debugger.rpa')):

              vbox:
                style_prefix "debug"
                textbutton _("Debugger"):
                  action Show("_debuger")
    vbox:
        style_prefix "navigation_main"

        #xpos gui.navigation_xpos
        #yalign 0.5
        xpos 1474#1134
        ypos 504
        xsize 578#500
        xalign 0.5
        ysize 600

        #spacing gui.navigation_spacing


        #frame:
        #    background None
        #    imagebutton:
        #        auto "gui/button/short_button_%s.png"
        #        action Start()
        #    hbox:
        #      textbutton _("Start"):
        #        action NullAction()
        #        xmaximum 500
        #        xminimum 500
        #        xalign 0.5
        #        ypos 10

        if LoadMostRecent().get_sensitive():
         frame:
          if main_menu_bt[4]:
             background "gui/button/short_button_idle.png"#im.Scale("gui/button/short_button_hover.png", 500, 100)
          else:
             background "gui/button/short_button_hover.png"#im.Scale("gui/button/short_button_idle.png", 500, 100)
          hbox:
             textbutton _("Continue"):
              action [Play("sound", "audio/ding.ogg"), LoadMostRecent(), Function(reset_main_menu_bt)] #[ShowMenu("load"), Function(reset_main_menu_bt)]
              hovered Function(hovered_main_menu_bt,4)
              unhovered Function(unhovered_main_menu_bt,4)
              xsize 570
              xalign 0.5
              ysize 117
              yalign 0.5

        frame:
         if main_menu_bt[0]:
            background "gui/button/short_button_idle.png"#im.Scale("gui/button/short_button_hover.png", 500, 100)
         else:
            background "gui/button/short_button_hover.png"#im.Scale("gui/button/short_button_idle.png", 500, 100)
         hbox:
            textbutton _("New Game"):
              if LoadMostRecent().get_sensitive():
               action [Play("sound", "audio/ding.ogg"), Confirm("Are you sure you want to restart the game?", yes=Start(), no=Return()), Function(reset_main_menu_bt)] #[ShowMenu("load"), Function(reset_main_menu_bt)]
              else:
               action [Play("sound", "audio/ding.ogg"), Start(), Function(reset_main_menu_bt)] #[ShowMenu("load"), Function(reset_main_menu_bt)]
              hovered Function(hovered_main_menu_bt,0)
              unhovered Function(unhovered_main_menu_bt,0)
              xsize 570
              xalign 0.5
              ysize 117
              yalign 0.5

        frame:
          if main_menu_bt[1]:
            background "gui/button/short_button_idle.png"
          else:
            background "gui/button/short_button_hover.png"
          hbox:
            textbutton _("Options"):
              action [ShowMenu("preferences"), Function(reset_main_menu_bt)]
              hovered Function(hovered_main_menu_bt,1)
              unhovered Function(unhovered_main_menu_bt,1)
              xsize 570
              xalign 0.5
              ysize 117
              yalign 0.5

        frame:
          if main_menu_bt[2]:
            background "gui/button/short_button_idle.png"
          else:
            background "gui/button/short_button_hover.png"
          hbox:
            textbutton _("Gallery"):
              action [ShowMenu("gallery"), Function(reset_main_menu_bt)]
              hovered Function(hovered_main_menu_bt,2)
              unhovered Function(unhovered_main_menu_bt,2)
              xsize 570
              xalign 0.5
              ysize 117
              yalign 0.5

        #remember this variable --> persistent.draw_mode
        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            frame:
              if main_menu_bt[3]:
                background "gui/button/short_button_idle.png"
              else:
                background "gui/button/short_button_hover.png"
              hbox:
                textbutton _("Quit"):
                  action Quit(confirm= main_menu)
                  hovered Function(hovered_main_menu_bt,3)
                  unhovered Function(unhovered_main_menu_bt,3)
                  xsize 570
                  xalign 0.5
                  ysize 117
                  yalign 0.5

style debug_button_text:
  hover_color "#7f7ab1"
  color "#9ba9a5"
  size 50
  xalign 0.5
style navigation_main_button is gui_button
style navigation_main_button_text:# is gui_button_text
  hover_color "#7f7ab1"
  color "#b1ddff"
  selected_color "#ff0"
  #bold True
  size 50
  xalign 0.5


style navigation_button:
    size_group "navigation_main"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")

## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background

    ## This empty frame darkens the main menu
    frame:
        pass

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation_main



style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 430
    yfill True

    #background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)


style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    #properties gui.text_properties("version")
    #xpos 1280
    #ypos 322
    color "#7f7ab1"
