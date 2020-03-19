#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  styles.rpy
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
transform spin(x):
    rotate x

transform jump_char:
    xalign 0.5
    linear 0 ypos 80
    linear 0.1 ypos 40 #img dimensions X,1000 heigth screen renpy 1080
    linear 0.1 ypos 80
transform zoom_in:
    ypos int(config.screen_height*1) zoom 1
    #yalign 1.5 xanchor -1.06 yanchor -0.26
    linear 0.5 ypos int(config.screen_height*1.1) zoom 1.1
    linear 0.5 ypos int(config.screen_height*1.3) zoom 1.3
    linear 0.5 ypos int(config.screen_height*1.5) zoom 1.5
transform zoom_off:
    ypos int(config.screen_height*1.5) zoom 1.5
    linear 0.5 ypos int(config.screen_height*1.3) zoom 1.3
    linear 0.5 ypos int(config.screen_height*1.1) zoom 1.1
    linear 0.5 ypos int(config.screen_height*1) zoom 1
transform zoom_out:
    linear 0 zoom 1
    yalign 1.0
    linear 0.5 zoom 0.75

#logo and splashscreen
transform transform_logo:
    on show:
        alpha 0 xalign 0.5 yalign 0.5
        linear 2.0 alpha 1
    on hide:
        linear 2.0 alpha 0
        
transform transform_white:
    on show:
        alpha 0 
        linear 2.0 alpha 1
    on hide:
        linear 2.0 alpha 0
