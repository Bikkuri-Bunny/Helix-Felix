style draw_ui:
    spacing 2

init python:
    #import pygame
    #import pygame_sdl2.image
    
    def guardar_pantalla(id_img):
       renpy.game.interface.save_screenshot(renpy.config.gamedir+"/draw"+str(id_img)+".png")
    #def acomodar_lienzo():
       #vr=im.Crop("draw.png", (160, 126, 880, 480))
       #surf=im.load_surface(vr)
       #surf=pygame.image.load(vr)
       #pygame_sdl2.image.save(surf,renpy.config.gamedir+"/test.png")
       
       #pygame.image.save(surf,renpy.config.gamedir+'/draw22.png')
       
    colours = ['#FFFFFF', '#000000', '#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#00FFFF', '#FF00FF', '#FF7F7F', '#FBEFE3']
    default_colour = '#000'
    freehand_canvas = FreehandCanvas(default_colour, 1336, 716)

    # Quick and dirty hover icons
    pencil_hover_icon = Fixed(
        Image("mini_game/draw/pencil_icon.png"),
        Transform(Frame(Solid("#FFF"), 5, 5), alpha=0.5),
        xysize=(32, 32),
    )
    
    line_hover_icon = Fixed(
        Image("mini_game/draw/line_icon.png"),
        Transform(Frame(Solid("#FFF"), 5, 5), alpha=0.5),
        xysize=(32, 32),
    )

    circle_hover_icon = Fixed(
        Image("mini_game/draw/circle_icon.png"),
        Transform(Frame(Solid("#FFF"), 5, 5), alpha=0.5),
        xysize=(32, 32),
    )
  
    circle_fill_hover_icon = Fixed(
        Image("mini_game/draw/circle_icon_fill.png"),
        Transform(Frame(Solid("#FFF"), 5, 5), alpha=0.5),
        xysize=(32, 32),
    )
  
    thickness_hover_icon = Fixed(
        Image("mini_game/draw/thickness.png"),
        Transform(Frame(Solid("#FFF"), 5, 5), alpha=0.5),
        xysize=(32, 32),
    )
    
    thickness_2_hover_icon = Fixed(
        Image("mini_game/draw/thickness_2.png"),
        Transform(Frame(Solid("#FFF"), 5, 5), alpha=0.5),
        xysize=(32, 32),
    )
  
    thickness_3_hover_icon = Fixed(
        Image("mini_game/draw/thickness_3.png"),
        Transform(Frame(Solid("#FFF"), 5, 5), alpha=0.5),
        xysize=(32, 32),
    )
  
    thickness_4_hover_icon = Fixed(
        Image("mini_game/draw/thickness_4.png"),
        Transform(Frame(Solid("#FFF"), 5, 5), alpha=0.5),
        xysize=(32, 32),
    )
  
screen freehand_draw(draw_num):
 frame:
    background "gui/background_draw.jpg"#"images/CG/artsupplies.png"
    vbox:
        xpos 110
        ypos 200
        hbox:
            vbox:
                style "draw_ui"
                imagebutton idle "mini_game/draw/pencil_icon.png" hover pencil_hover_icon selected_idle pencil_hover_icon action SetField(freehand_canvas, 'mode', FreehandCanvas.PENCIL)
                imagebutton idle "mini_game/draw/line_icon.png" hover line_hover_icon selected_idle line_hover_icon action SetField(freehand_canvas, 'mode', FreehandCanvas.LINE)
                imagebutton idle "mini_game/draw/circle_icon.png" hover circle_hover_icon selected_idle circle_hover_icon action SetField(freehand_canvas, 'mode', FreehandCanvas.CIRCLE)
                imagebutton idle "mini_game/draw/circle_icon_fill.png" hover circle_fill_hover_icon selected_idle circle_fill_hover_icon action SetField(freehand_canvas, 'mode', FreehandCanvas.CIRCLE_FILL)
            vbox:
                style "draw_ui"
                imagebutton idle "mini_game/draw/thickness.png" hover thickness_hover_icon selected_idle thickness_hover_icon action SetField(freehand_canvas, 'line_width', 1)
                imagebutton idle "mini_game/draw/thickness_2.png" hover thickness_2_hover_icon selected_idle thickness_2_hover_icon action SetField(freehand_canvas, 'line_width', 2)
                imagebutton idle "mini_game/draw/thickness_3.png" hover thickness_3_hover_icon selected_idle thickness_3_hover_icon action SetField(freehand_canvas, 'line_width', 4)
                imagebutton idle "mini_game/draw/thickness_4.png" hover thickness_4_hover_icon selected_idle thickness_4_hover_icon action SetField(freehand_canvas, 'line_width', 8)
            
            vbox:
                style "draw_ui"
                for colour in colours:
                   button:
                      xsize 32
                      ysize 32
                      background colour
                      action SetField(freehand_canvas, 'colour', colour)
         
    frame:
      background "#FFF"
      padding (0, 0)
      xpos 264
      ypos 200
      xsize 1336
      ysize 716
      add freehand_canvas
    hbox:
       xmaximum 1920#1280
       xminimum 1500
       ypos 950
       xalign 0.5
       frame:
          style_prefix "freehand_draw"
          background im.Scale("gui/button.png", 500, 100)
          hbox:
            textbutton _("Clear Canvas"):
              action Function(freehand_canvas.clear)
              xmaximum 500
              xminimum 500
              xalign 0.5
              ypos 10
       frame:
          style_prefix "freehand_draw"
          background im.Scale("gui/button.png", 500, 100)
          hbox:
            textbutton _("Done"):
              action [Function(guardar_pantalla,draw_num),Return()]
              xmaximum 500
              xminimum 500
              xalign 0.5
              ypos 10

style freehand_draw_button is gui_button
style freehand_draw_button_text:# is gui_button_text
  color "#7f7ab1"
  hover_color "#b1ddff" 
  selected_color "#ff0"
  bold True
  size 50
  xalign 0.5

label dibujar:
    #freehand_draw(id_draw) id_draw unique value dont repeat only numbers
    scene bg bedroomlight with test2_t
    a happy"Let's go to the drawing board"
    #$ rv=renpy.roll_forward_info()
    #$ renpy.checkpoint(rv) # Store the result of the interaction.
    scene bg bedroomlight
    minigame draw start 0
    a happy "My first drawing"
    p happy "show me your drawing"
    minigame draw open 160 40 0
    a happy "My first drawing"
    minigame draw close
    show screen show_gift_steven(0)
    " "
    hide screen show_gift_steven
    show screen show_gift_pumpkin(0)
    " "
    hide screen show_gift_pumpkin
    return

screen show_hand_draw(x=160,y=40,id_img=0):

  frame:
    xpos x
    ypos y
    #top_margin 15
    #left_margin 15
    #right_margin 15
    #bottom_margin 15
    xmaximum 1100#852
    ymaximum 600#471
    background "mini_game/draw/show_draw.png" #852,471
    add lienzo_fondo(id_img):
       xpos 20
       ypos 10

transform draw_gift_steven:
    rotate 45
    xzoom 0.3531
    yzoom 0.4531 #0.5031

screen show_gift_steven(id_img=0):
  add lienzo_fondo(id_img):
      xpos 580
      ypos -50
      at draw_gift_steven
  frame:
    xpos 0
    ypos 0
    background "images/CG/gift_steven_draw.png"


transform draw_gift_pumpkin:
    rotate 90
    xzoom 0.3531
    yzoom 0.4531 #0.5031

screen show_gift_pumpkin(id_img=0):
  add lienzo_fondo(id_img):
      xpos 1435
      ypos 70
      at draw_gift_pumpkin
  frame:
    xpos 0
    ypos 0
    background "images/CG/gift_pumpkin_draw.png"
