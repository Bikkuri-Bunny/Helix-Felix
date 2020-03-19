#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  debug.rpy
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
init +1:
    python hide:
        config.developer = True
        config.console = True

screen _simple_director:
    #para ver los archivos rpym cargados en renpy en los menus
    $ archivo_linea=str(renpy.get_filename_line())
    text archivo_linea
screen _debuger:

    zorder 1001
    modal True

    frame:
        style_prefix ""

        has side "t c b":
            spacing gui._scale(10)

        label _(u"Debugger Menu")

        fixed:
            vbox:

                textbutton _("Label Launcher"):
                    action [Hide("_debuger"),Call("_label_picker")]
                textbutton _("Variable Viewer"):
                    action ui.callsinnewcontext("_debugger_screen")

                if not renpy.get_screen("_simple_director"):
                    textbutton _("Simple interactive director"):
                        action Show("_simple_director")
                else:
                    textbutton _("Hide Simple interactive director"):
                        action Hide("_simple_director")
                if not renpy.get_screen("_image_load_log"):
                    textbutton _("Show Image Load Log (F4)"):
                        action Show("_image_load_log")
                else:
                    textbutton _("Hide Image Load Log (F4)"):
                        action Hide("_image_load_log")

                textbutton _("Image Attributes"):
                    action ui.callsinnewcontext("_image_attributes")

        hbox:
            spacing gui._scale(25)

            textbutton _(u"Return"):
                action Hide("_debuger")
                size_group "developer"


screen _label_start:

    default filter = ""

    frame:
        style_prefix ""

        has side "t c b":
            spacing gui._scale(10)

        vbox:
            label _(u"Label Launcher")
            text _("Be careful, this is only to validate the logic in the label.\n")

            hbox:
                text _("Label: ")
                input value ScreenVariableInputValue("filter")

        viewport:
            xfill True
            yfill True
            scrollbars "both"
            mousewheel True

            has vbox

            for fn in [ i for i in renpy.get_all_labels() if filter.lower() in i.lower() ]:

                textbutton "[fn!q]":
                    action [Hide("_debuger"),Start(fn)]#,ui.callsinnewcontext(fn) ] renpy.call_in_new_context(
                    style_suffix "small_button"

        hbox:
            spacing gui._scale(25)

            textbutton _(u"Return"):
                action Return(False)

#renpy.add_python_directory(path)
# import <module>

label _label_picker:

    call _enter_game_menu

    scene black

    python hide:

        xadjustment = ui.adjustment()
        yadjustment = ui.adjustment()

        while True:

            rv = renpy.call_screen("_label_start")

            if rv is False:
                renpy.jump("_label_done")

            # Now, allow the user to pick the image.

            ui.keymap(game_menu=ui.returns(True))
            ui.add(_label_start)
            ui.interact()

        renpy.jump("_label_picker")

label _label_done:
    return
