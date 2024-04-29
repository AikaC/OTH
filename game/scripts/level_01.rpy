#tela de menu das fases
label nivel:
    call screen pagina01
    return
# Primeira fase

label listen_1:
    $ title_level = "Time of the day"
    $ words = ["Time", "Day", "Night", "Dawn", "Sunrise", "Early morning", "Morning",
    "Midday", "Noon", "Afternoon", "Sundown", "Evening", "Late night", "Midnight","Twilight"]
    call screen listening
    return

label explore_1:
    "Exploring"
    call screen pagina01
    return

label story_1:
    "Storytime"
    $ persistent.n2 = True
    $ persistent.n3 = True
    $ persistent.n4 = True
    $ persistent.n5 = True
    $ persistent.n6 = True
    $ persistent.n7 = True
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