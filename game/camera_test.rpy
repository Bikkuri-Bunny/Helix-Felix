#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  camera_test.rpy
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

label camera_test:
  # Resets the camera and layers positions
  $ camera_reset()
  # Instantly sets layer distances from the camera
  $ layer_move("background2", 2000)
  $ layer_move("middle", 1500)
  $ layer_move("forward", 1000)
  scene bg clinic onlayer background2
  # WARNING: The 'scene' command will reset the depth of whatever layer the image
  # is displayed on. Make sure you reset the depth after you call the 'scene' command.
  $ layer_move("background2", 2000)
  show addison happy onlayer middle
  show addison costume happy onlayer forward
  with dissolve
  "Moves the camera to (1800, 0, 0) in 1 second."
  $ camera_move(1800, 0, 0, 0, 1)
  "Moves the camera to (0, 0, 1600) in 5 seconds."
  $ camera_move(0, 0, 1600, 0, 5)
  "Moves the camera to (0, 0, 0) instantaneously."
  $ camera_move(0, 0, 0)
  "Rotates the camera 180 degrees in 1 second."
  $ camera_move(0, 0, 0, 180, 1)
  'Rotates the camera -180 degrees in 1 second and subsequently moves the camera to (-1800, 0, 500) in 1.5 seconds'
  $ camera_moves( ( (0, 0, 0, 0, 1, 'linear'), (-1800, 0, 500, 0, 1.5, 'linear') ) )
  'Continually moves the camera between (-1800, 0, 500) and (0, 0, 0), taking 0.5 seconds for the first move and 1 second for the second until the action is interrupted.'
  $ camera_moves( ( (0, 0, 0, 0, .5, 'linear'), (-1800, 0, 500, 0, 1, 'linear') ), loop=True)
  $ renpy.pause(5)
  $ camera_reset()
  hide addison happy onlayer middle
  hide addison costume happy onlayer forward
  $ renpy.scene(layer="background2")
  return
