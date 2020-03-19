#image titlesplash: #zoom out effect
#    "img"
#    alpha 0 zoom 4
#    linear 1 alpha 1 zoom 0.335
init -20 python:
    import discord_rpc
    import time
    
    def readyCallback(current_user):
        print('Our user: {}'.format(current_user))

    def disconnectedCallback(codeno, codemsg):
        print('Disconnected from Discord rich presence RPC. Code {}: {}'.format(
            codeno, codemsg
        ))

    def errorCallback(errno, errmsg):
        print('An error occurred! Error {}: {}'.format(
            errno, errmsg
        ))


label splashscreen:
    scene warning
    $ renpy.pause(float(3.0), hard=True)
    if not persistent._legal_age:
      call screen confirm(message=_("Are you of legal age in your country?"), yes_action=Return(), no_action=Quit(confirm=False))
      $ persistent._legal_age=True
    scene black
    $ renpy.pause(1, hard=True)

    show white at transform_white
    $ renpy.pause(2, hard=True)

    show logo2 at transform_logo
    $ renpy.pause(6, hard=True)

    hide logo2
    $ renpy.pause(2, hard=True)

    hide white
    $ renpy.pause(3, hard=True)

    $ renpy.movie_cutscene('movies/intro.ogv') # https://www.youtube.com/watch?v=afKvS95MvhI&feature=youtu.be
    return

label start:
  python:
        callbacks = {
            'ready': readyCallback,
            'disconnected': disconnectedCallback,
            'error': errorCallback,
        }
        discord_rpc.initialize('684141775019180197', callbacks=callbacks, log=False)
        start = time.time()
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
        discord_rpc.update_presence(
            **{
                'details': 'Part I: Family',
                'state': 'day 0',
                'large_image_key': 'big-image',
                'start_timestamp': start
            }
        )

        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
  $renpy.scene()
  $ hide_quick_menu(True)
  play music musicneutral loop
  show screen calendar_menu
  calendar day 0
  $ config.window_title=u'Part I - Family'
  jump day0

label before_main_menu:
    #test discord v1
  python:
        # Note: 'event_name': callback
        callbacks = {
            'ready': readyCallback,
            'disconnected': disconnectedCallback,
            'error': errorCallback,
        }
        discord_rpc.initialize('684141775019180197', callbacks=callbacks, log=False)
        start = time.time()
        print(start)
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()
        discord_rpc.update_presence(
            **{
                'details': 'Main Menu',
                'start_timestamp': start,
                'large_image_key': 'big-image'
            }
        )
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()

  
  $ minutes, seconds = divmod(int(playtime), 60)
  $ hours, minutes = divmod(minutes, 60)
  #easter egg to show in gallery this bonus image
  if not (renpy.exists('thanks.png') or persistent.thanks1year):
    $persistent.thanks1year=True
    if not achievement.has("ee_bonus"):
      $ achievement.grant("ee_bonus")
    scene bg playroom
    a sad "Why do you do that???"
    window hide
    $renpy.scene()
  elif persistent.myuuid_node != myuuid_node:
    #playing with the code, for this to happen you must play with a save on another computer (using MAC address)
    $ persistent.myuuid_node=myuuid_node
    scene bg playroom
    a mad "This is a new house?"
    a happy "You are my new owner?"
    window hide
    $renpy.scene()
  elif hours>=3 and not persistent.ee_more3hours:
    #playing with the code, for this to happen you must play three hours or more
    $ persistent.ee_more3hours=True
    scene bg playroom
    a happy "You've been playing for over three hours!"
    window hide
    $renpy.scene()
  return

label credits:

    # End Credits

    ## We hide the quickmenu for the End Credits so they don't appear at the bottom.
    $ hide_quick_menu(False)

    scene black with fade

    ## Find "End Credits Scroll" in screens.rpy to change text.
    call screen credits

    $ persistent.credits_seen = True

    # $ _game_menu_screen = "save"

    scene black
    with fade

    # Players can skip the credits in subsequent playthroughs of the game.
    label skip_credits:

        pass

    ## Makes [result] work. This needs to be near the end of the game
    ## for it to work properly.
    $ percent()

    ## We display a screen that shows how much the player has seen and played of the game.
    show screen results

    if persistent.game_clear:

        pass

    else:

        if readtotal == 100:

            $ achievement.grant("Completionist")

            $ persistent.game_clear = True

            ## The game will show our text displayable so the player can read it
            ## And only continue when there is input
            pause

    ## The game will show our text displayable so the player can read it
    ## And only continue when there is input
    pause

    # This ends the game.
    return
