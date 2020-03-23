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

screen main_menu():
    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background
    add gui.main_menu_overlay
    add gui.logo xalign 1.0
    #Debug options
    if (renpy.exists('debug/debug.rpyc') or renpy.exists('debugger.rpa')):
        vbox:
            style_prefix "debug"
            textbutton _("Debugger"):
                action Show("_debuger")
    vbox:
        style_prefix "menu_button"
        spacing -5
        ypos 450
        xsize 570
        xalign 1.0
        xoffset -150
        ysize 600

        if LoadMostRecent().get_sensitive():
            fixed:
                xsize 570
                ysize 130
                imagebutton:
                    auto "gui/button/short_button_%s.png"
                    action [Play("sound", "audio/ding.ogg"), LoadMostRecent()]
                text _("Load"):
                    xalign 0.5
                    yalign 0.5
        fixed:
            xsize 570
            ysize 130
            imagebutton:
                auto "gui/button/short_button_%s.png"
                if LoadMostRecent().get_sensitive():
                    action [Play("sound", "audio/ding.ogg"), Confirm("Are you sure you want to restart the game?", yes=Start(), no=Return())]
                else:
                  action [Play("sound", "audio/ding.ogg"), Start()]
            text _("New Game"):
                xalign 0.5
                yalign 0.5

        fixed:
            xsize 570
            ysize 130
            imagebutton:
                auto "gui/button/short_button_%s.png"
                action ShowMenu("preferences")
            text _("Options"):
                xalign 0.5
                yalign 0.5

        fixed:
            xsize 570
            ysize 130
            imagebutton:
                auto "gui/button/short_button_%s.png"
                action ShowMenu("gallery")
            text _("Gallery"):
                xalign 0.5
                yalign 0.5
        ## The quit button is banned on iOS and unnecessary on Android and Web.
        if renpy.variant("pc"):
            fixed:
                xsize 570
                ysize 130
                imagebutton:
                    auto "gui/button/short_button_%s.png"
                    action Quit()
                text _("Quit"):
                    xalign 0.5
                    yalign 0.5

style debug_button_text:
    hover_color "#7f7ab1"
    color "#000000"
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
style menu_button_text:
    font gui.menu_button_text_font
    size 70
    color "#ffffffBF"
