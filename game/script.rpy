# O jogo começa aqui.

label start:
    if persistent.n2 == True:
        jump nivel
        return
    
    else:
        jump intro
        return

label intro:
    # Quando False, as opções de escolha deixam de aparecer na próxima rodada
    $ o1 = True
    $ o2 = True

    #sfx aeronave
    scene bgintro
    with hpunch
    pause 0.6

    show PP P_bored
    with dissolve
    "Ugh... {w}Que queda feia..."

    hide PP
    with dissolve
    show Teru T_exc at floating
    pause 1.0

    #sfx giberish
    show Teru T_talk at floating
    pause 3.0

    hide Teru
    show PP P_bored
    with dissolve
    
    "Quê?"

    hide PP
    show Teru at floating

    t "Teru."

    hide Teru
    show PP
    with dissolve

    $ persistent.pp = renpy.input("My name is...{p}{size=30}(Escreva um nome.)", length = 10)
    $ persistent.pp = persistent.pp.strip()
    if persistent.pp == "":
        $ persistent.pp = "Galaxy"

    hide PP with dissolve
    show Teru at floating

    t T_close "Hello, [persistent.pp]."

    hide Teru with dissolve

    menu:
        "Hello!":
            show Teru at floating

            t "Hi! Friends!"

            hide Teru
            jump friends
        "Bye-bye!":
            show Teru at floating

            t T_close "Bye-bye!"

            hide Teru with pixellate
            pause 0.6
            show Teru at floating

            t T_angry "No...{w} No bye-bye!{p}Hello!"

            hide Teru
            show PP P_bored
            with dissolve

            persistent.pp "Hello..."

            hide PP with dissolve
            show Teru at floating

            t T_close "Friends?"

            hide Teru
            jump friends

    # This ends the game.
    return

label friends:
    menu:
        "O que significa \'friends\'?"
        "Olá!" if o1:
            show Teru at floating

            t T_angry "No,{w} no hello.{p} Friends!"
            $ o1 = False
            jump friends
            return
        "Amigos!":
            show Teru at floating

            t T_open "Yes!{w} Teru, [persistent.pp], friends!"
            t T_close "Teru, [persistent.pp], friends!"
            t T_open "[persistent.pp], follow me."

            hide Teru
            show PP
            with dissolve

            persistent.pp "Acho que é para seguir ele."
            hide Teru
            call screen pagina01
            return
        "Ajuda!" if o2:
            show Teru at floating

            t T_angry "No,{w} no help.{p} Friends!"
            $ o2 = False
            jump friends
            return