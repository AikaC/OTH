label nivel:
    call screen pagina01
    return
# Primeira fase

label lvl1:
    #permite bloquear botões de escolha do menu pre-programado
    #define config.menu_include_disabled = True

    "level 1"
    $ persistent.n2 = True
    call screen pagina01
    return

label lvl2:
    "level 2 [persistent.pp]"
    $ persistent.n3 = True
    call screen pagina01
    return

label lvl3:
    "level 3 here"
    $ persistent.n4 = True
    call screen pagina01
    return

label lvl4:
    "level 4 here"
    $ persistent.n5 = True
    call screen pagina01
    return

label lvl5:
    "level 5 here"
    $ persistent.n6 = True
    call screen pagina01
    return

label lvl6:
    "level 6 here"
    $ persistent.n7 = True
    call screen pagina01
    return

label lvl7:
    "level 7 here"
    hide screen pagina01
    return