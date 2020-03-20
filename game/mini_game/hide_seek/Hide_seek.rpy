#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  game.rpy
#  
#  Copyright 2020 badanni <dannyvasconeze@gmail.com>
#  Copyright 2015 http://renpyfordummies.blogspot.com/2015/07/blog-post.html
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


init python:

    class Hide_seek(object):
      def __init__(self,winner):
        self.oXY = []
        self.oN = []
        self.oLen = 0
        self.maxLen = 0
        self.oBg = ""
        self.winner=winner
        self.oLast = -1
        self.oTime = 0.0
        self.oMaxTime = 5.0
        self.needTimer = False
        self.oActive = False
        self.oRes = False
        self.need = False
        self.needTimer = False
      def InitGame(self,bg, time, *args):
        self.oBg = bg
        self.oTime = time
        self.oMaxTime = time
        self.oActive = True
        if self.oTime > 0.0:
            self.needTimer = True
        for xy, obj_name in zip(args[0::2], args[1::2]):
            self.oXY.append(xy)
            self.oN.append(obj_name)
            self.maxLen += 1
      def StartGame(self):
        self.oActive = True
        self.need = True
        while self.need:
            renpy.call_in_new_context("hs_diag%d"%(self.oLen))
            hide_quick_menu(False)
            renpy.call_screen("hs_minigame", self, _layer="screens")
            if self.oRes == False:
               self.need=True
               renpy.show_screen("hs_minigame",self, _layer="screens")
               renpy.call_in_new_context("hs_diag%d"%(self.oLen))
            else:
               self.need=False
               renpy.show_screen("hs_minigame",self, _layer="screens")
               renpy.call_in_new_context("hs_diag%d"%(self.oLen))
            #self.need = self.oRes == False
      def GameAsBG(self):
        self.oActive = False
        renpy.show_screen("hs_minigame",self, _layer="master")
      def o_click(self,i):
        if i >= 0:
            if self.oN[i]:
                temp = self.oN[i]
                self.oN[i] = ""
                self.oLen += 1
                #renpy.play("sounds/click.mp3", channel="sound")
                renpy.restart_interaction()
                if self.oLen == self.winner: #because variables are unicode 
                    self.oRes = True
                else:
                    self.oRes = False

screen hs_minigame(hide_seek):
    $ oClick = renpy.curry(hide_seek.o_click)
    modal True
    add hide_seek.oBg
    for i in range(0, len(hide_seek.oN)):
        if hide_seek.oN[i]:
            imagebutton:
                focus_mask True
                pos(hide_seek.oXY[i])
                idle hide_seek.oN[i]
                hover hide_seek.oN[i]+"_hover"
                mouse "minigame_hs"
                if hide_seek.oActive:
                    action [oClick(i), Return()]
                else:
                    action []
