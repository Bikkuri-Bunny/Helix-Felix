#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  achievements.rpy
#  
#  Copyright 2020 badanni <dannyvasconeze@gmail.com>
#  Copyright 2017 base code from imperf3kt (https://lemmasoft.renai.us/forums/viewtopic.php?t=47148#p472578)
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

init offset = -1
define locked_str=_("Locked")
define archievements_locked="gui/achievements/locked.png"

## Achievements screen ###############################################################
##

screen achievements():
    
    tag menu
    style_prefix "achievement_menu"
    add "images/BG/Cherryblosssoms1.png"
    add "gui/achievements/main_menu.png" at center
    
    vbox:
        text _("Achievements"):
          font "fonts/ConcertOne-Regular.ttf"
          size 40
          bold True
          color "#7f7ab1"
          ypos 150
          at spin(-3)
        xalign 0.5
        ypos 25
        
    vpgrid:
        xmaximum 500
        xfill True
        ysize 500#config.screen_height - 300
        xalign 0.5
        ypos 400
        cols 2
        spacing 50
        draggable True
        #scrollbars "vertical"
        
        text " "
        text " "

#########################################
##part 1 complete
        if achievement.has("part1"):
            add "gui/achievements/001.png"
            text _("part One: Family Complete") yalign 0.5
        else:
            add archievements_locked
            text "[locked_str]" yalign 0.5
#########################################
##part 2 complete
        if achievement.has("part2"):
            add "gui/achievements/002.png"
            text _("part Two: Friends Complete") yalign 0.5
        else:
            add archievements_locked
            text "[locked_str]" yalign 0.5
#########################################
##Completionist
        if achievement.has("Completionist"):
            add "gui/achievements/003.png"
            text _("Completionist") yalign 0.5
        else:
            add archievements_locked
            text "[locked_str]" yalign 0.5
#########################################
##easter egg - Bonus gallery
        if achievement.has("ee_bonus"):
            add "gui/achievements/004.png"
            text _("Fisrt Year!!!") yalign 0.5
        else:
            add archievements_locked
            text "[locked_str]" yalign 0.5
#########################################
##END
        text ""
        text ""
    frame:
          xalign 0.5
          ypos 900
          if main_menu_bt[20]:
            background im.Scale("gui/button_hover.png", 500, 100)
          else:
            background im.Scale("gui/button_idle.png", 500, 100)
          hbox:
            xalign 0.5
            textbutton _("R E T U R N"):
              action Return()
              hovered Function(hovered_main_menu_bt,20)
              unhovered Function(unhovered_main_menu_bt,20)
              xmaximum 500
              xminimum 500
              ypos 10


style achievement_menu_vbox:
    xmaximum 500#680
    
style achievement_menu_text:
    size gui.achievement_text_size
    color gui.achievement_text_color
