#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cds.rpy
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
# https://www.renpy.org/dev-doc/html/cds.html?highlight=statement
# renpy.error(message, submessage=None, label="front_page", **kwargs)
# layout.yesno_screen(message, yes=None, no=None)
# commom buscar como usar
# layout.__dict__
default pov_chara = None

python early:


    def parse_attrs_pov(lex):
        emotion = lex.rest()
        lex.expect_eol()
        return emotion
    def execute_attrs_pov(o):
        attrs=o
        old_attributes = renpy.game.context().say_attributes
        if store.pov_chara is None:
            return
        else: 
            who=store.pov_chara
        try:
            renpy.game.context().say_attributes = attrs
            who.resolve_say_attributes(predict=False,attrs=attrs.split(" "))
        finally:
            renpy.game.context().say_attributes = old_attributes
    def lint_attrs_pov(o):
        attrs=o
        try:
            #assert(who is ADVCharacter)
            who=store.pov_chara
            #assert(who is ADVCharacter)
            #eval(who attrs)
            eval(who)
        except:
            renpy.error("Character attrs not defined: %s" % attrs)
        if not store.pov_chara:
            return
    renpy.register_statement("pov attrs", parse=parse_attrs_pov, execute=execute_attrs_pov, lint=lint_attrs_pov)
    
    
    def parse_set_pov(lex):
        who = lex.simple_expression()
        lex.expect_eol()
        return who
    def execute_set_pov(who):
        """
        Sets the current POV character to ``who``, which may be ``None``.
        Also clears any attributes.
        """
        store.pov_chara = eval(who)
        if eval(who):
            config.side_image_tag = eval(who).image_tag
            #pov_attrs()
        else:
            config.side_image_tag = None
            renpy.game.context().say_attributes=None
            
    def lint_set_pov(who):
        try:
            eval(who)
            #assert((not who) or (who is ADVCharacter))
        except:
            renpy.error("Character not defined: %s" % who)
    renpy.register_statement("pov set", parse=parse_set_pov, execute=execute_set_pov, lint=lint_set_pov)
    
    def parse_smartline(lex):
        who = lex.simple_expression()
        what = lex.rest()
        return (who, what)

    def execute_smartline(o):
        who, what = o
        renpy.say(eval(who), what)

    def lint_smartline(o):
        who, what = o
        try:
            eval(who)
        except:
            renpy.error("Character not defined: %s" % who)

        tte = renpy.check_text_tags(what)
        if tte:
            renpy.error(tte)

    renpy.register_statement("line", parse=parse_smartline, execute=execute_smartline, lint=lint_smartline)
    
    def parse_minigame(lex):
       minigame=lex.simple_expression()
       aux=lex.simple_expression()
       id_draw=None
       if aux in ["start"]:
        xpos=None
        ypos=None
        id_draw=lex.simple_expression()
       elif aux in ["open"]:
        xpos=lex.simple_expression() #require(thing, name=None)
        ypos=lex.simple_expression()
        id_draw=lex.simple_expression()
       elif aux in ["close"]:
        xpos=None
        ypos=None
        id_draw=None
       else:
        renpy.error("only start,show,hide defined: %s" % aux)
       lex.expect_eol()
       return (minigame,aux,id_draw,xpos,ypos)
    def execute_minigame(o):
       minigame,option,id_draw,xpos,ypos=o
       if minigame in ["draw"] and option in ["start"]:
        config.mouse["default"]=config.mouse["minigame_draw"]
        hide_quick_menu(False) #unshow quickmenu not hide
        renpy.hide_screen("calendar_menu")
        menu_mini_game=True
        #call screen freehand_draw(0)
        renpy.call_screen("freehand_draw",id_draw)
        hide_quick_menu(False) #unshow quickmenu not hide
        menu_mini_game=False
        hide_quick_menu(True) #show quickmenu
        renpy.show_screen("calendar_menu")
        config.mouse["default"]=config.mouse["base"]
       elif minigame in ["draw"] and option in ["open"]:
        renpy.free_memory()
        renpy.show_screen("show_hand_draw",int(xpos),int(ypos),id_draw)
       elif minigame in ["draw"] and option in ["close"]:
        renpy.hide_screen("show_hand_draw")
       else:
        renpy.error("Minigame not defined: %s or inappropriate parameter %s" % (minigame,option))
    def lint_minigame(o):
        minigame,option,id_draw,xpos,ypos = o
        try:
            eval(minigame)
            
        except:
            renpy.error("Minigame not defined: %s" % minigame)

        tte = renpy.check_text_tags(id_draw)
        if tte:
            renpy.error(tte)
    renpy.register_statement("minigame", parse=parse_minigame, execute=execute_minigame, lint=lint_minigame)

    def parse_calendar(lex):
       aux=lex.simple_expression()
       id_draw=None
       if aux in ["day"]:
        val=lex.simple_expression()
       elif aux in ["add"]:
        val1=lex.string()
        val2=lex.string()
        val3=lex.string()
        val=[val1,val2,val3]
       elif aux in ["manual"]:
        val1=lex.string()
        val2=lex.string()
        val3=lex.string()
        val=[val1,val2,val3]
       elif aux in ["next"]:
        val=None
       else:
        renpy.error("only day, manual or next are defined, not %s" % aux)
       lex.expect_eol()
       return (aux,val)
    def execute_calendar(o):
       option, val=o
       if option in ["day"]:
        try:
          renpy.store.calendar_text = renpy.store.calendar_menu_text[int(val)]
        except:
          renpy.store.calendar_text = ["ERROR","VALUE",val]
       elif option in ["manual"]:
        renpy.store.calendar_text = val
       elif option in ["add"]:
        renpy.store.calendar_menu_text.append(val)
       elif option in ["next"]:
        try:
          index=renpy.store.calendar_menu_text.index(renpy.store.calendar_text)
          renpy.store.calendar_text = renpy.store.calendar_menu_text[index+1]
        except:
          renpy.store.calendar_text = ["ERROR","VALUE",index+1]
       else:
        renpy.error("calendar inappropriate parameter %s" % (option))
    def lint_calendar(o):
        option, val= o
        try:
            eval(option)
            renpy.store.calendar_menu_text[int(val)]
            
        except:
            renpy.error("calendar inappropriate parameter %s or value not int: %s" % (option,val))

        tte = renpy.check_text_tags(val)
        if tte:
            renpy.error(tte)
    renpy.register_statement("calendar", parse=parse_calendar, execute=execute_calendar, lint=lint_calendar)
    
    def parse_cards(lex):
       if lex.has_block():
        val_aux=[None,5.0,False,False]
        lex.expect_block("cards")
        lex.require(':')
        lex.expect_eol()
        ll = lex.subblock_lexer()
        while ll.advance():
          aux=ll.simple_expression()
          if aux in ["card"]:
            val=ll.simple_expression()
            val_aux[0]=val
          elif aux in ["with_in"]:
            val=ll.string()
            val_aux[1]=val
          elif aux in ["with_out"]:
            val=ll.string()
            val_aux[3]=val
          elif aux in ["delta_t"]:
            val=ll.float()
            val_aux[2]=val
          elif aux in ["start"]:
            pass
          else:
            renpy.error("only card, with_in, with_out anddelta_t are defined, not %s" % aux)
        ll.expect_eol()
       else:
        val_aux=[None,"dissolve",5.0,"dissolve"]
        lex.expect_noblock("cards")
        aux=lex.simple_expression()       
        if aux in ["open"]:
           val=lex.simple_expression()
           val_aux[0]=val
        elif aux in ["random"]:
           val_aux[0]=None
        else:
           renpy.error("only open or random are defined, not %s" % aux)
        lex.expect_eol()
       return (aux,val_aux)
    def execute_cards(o):
       option, val=o
       if option in ["open"]:
        config.allow_skipping = False
        config.side_image_tag = None
        hide_quick_menu(False) #unshow quickmenu not hide
        renpy.hide_screen("calendar_menu")
        #show card1 onlayer event with dissolve
        renpy.show(str(val[0]),layer="event")
        renpy.with_statement(dissolve)
        renpy.pause(float(val[2]), hard=True)
        renpy.hide(str(val[0]),layer="event")
        renpy.with_statement(dissolve)
        #hide card1 onlayer event with dissolve
        hide_quick_menu(True) #show quickmenu
        renpy.show_screen("calendar_menu")
        config.side_image_tag = "addison"
        config.allow_skipping = True 
       elif option in ["random"]:
        lista=renpy.list_files()
        renpy.error("In development. cards inappropriate parameter %s" % (option))
       elif option in ["start"]:
        config.allow_skipping = False
        config.side_image_tag = None
        hide_quick_menu(False) #unshow quickmenu not hide
        renpy.hide_screen("calendar_menu")
        #show card1 onlayer event with dissolve
        renpy.show(str(val[0]))
        if not str(val[1]) in ["False"]:
          pass
        else:
          renpy.with_statement(dissolve)
        renpy.pause(float(val[2]), hard=True)
        if not str(val[3]) in ["False"]:
          pass
        else:
          renpy.hide(str(val[0]))
          renpy.with_statement(dissolve)
        #hide card1 onlayer event with dissolve
        hide_quick_menu(True) #show quickmenu
        renpy.show_screen("calendar_menu")
        config.side_image_tag = "addison"
        config.allow_skipping = True 
       elif option in ["card","with_in","delta_t","with_out"]:
        pass
       else:
        renpy.error("cards inappropriate parameter %s" % (option))
    def lint_cards(o):
        option, val= o
        try:
            eval(option)
            
        except:
            renpy.error("cards inappropriate parameter %s or value not int: %s" % (option,val))

        tte = renpy.check_text_tags(val)
        if tte:
            renpy.error(tte)
    renpy.register_statement("cards", parse=parse_cards, execute=execute_cards, lint=lint_cards,block="possible")
