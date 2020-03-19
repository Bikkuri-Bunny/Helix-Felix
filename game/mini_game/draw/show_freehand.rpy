#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  show_freehand.rpy
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
    
    class lienzo_fondo(renpy.Displayable):
        '''
        the MapDisplayable class which inherits from renpy.Displayable
        '''
        def __init__(self,id_img=0):
            renpy.Displayable.__init__(self)
            self.width=822
            self.height=441
            self.vr=im.Crop("draw"+str(id_img)+".png", (166, 127, self.width, self.height))

        def render(self, width, height, st, at):
            # Main render and blit
            render_obj = renpy.render(self.vr, self.width, self.height,st, at)
            render = renpy.Render(self.width, self.height)
            #self.moves_to_image(moves_image_render, render) #permite que se mueva las imagenes
            render.blit(render_obj, (0,0))
            
            return render

            def visit(self):
                return [ 1, 2 ]
