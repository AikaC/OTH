#tela de menu das fases
label nivel:
    call screen pagina01
    return

#Listening

label listen_1:
    $ title_level = "Time of the day pt. 1"
    $ words = ["Time", "Day", "Night", "Dawn", "Sunrise", "Morning"]
    $ views = ["gui/viewports/view_time.png", "gui/viewports/view_day.png", "gui/viewports/view_night.png", 
    "gui/viewports/view_dawn.png", "gui/viewports/view_sunrise.png","gui/viewports/view_morning.png"]
    call screen listening(words, views)
    return

label listen_2:
    $ title_level = "Time of the day pt. 2"
    $ words = ["Midday", "Afternoon", "Sundown", "Evening", "Midnight","Twilight"]
    $ views = ["gui/viewports/view_midday.png", "gui/viewports/view_afternoon.png", "gui/viewports/view_sundown.png",
    "gui/viewports/view_evening.png", "gui/viewports/view_midnight.png", 
    "gui/viewports/view_twilight.png"]
    call screen listening(words, views)
    return

label listen_3:
    $ title_level = "Bye-bye"
    $ words = ["Goodbye", "See you later", "Take care", "Until next time", "Have a good day", "Bye-bye"]
    $ views = ["gui/viewports/view_midday.png", "gui/viewports/view_afternoon.png", "gui/viewports/view_sundown.png",
    "gui/viewports/view_evening.png", "gui/viewports/view_lnight.png", "gui/viewports/view_midnight.png"]
    call screen listening(words, views)
    return

label listen_4:
    $ title_level = "Points in time"
    $ words = ["Before", "Now", "Present", "After", "Future", "Past"]
    $ views = ["gui/viewports/view_midday.png", "gui/viewports/view_afternoon.png", "gui/viewports/view_sundown.png",
    "gui/viewports/view_evening.png", "gui/viewports/view_lnight.png", "gui/viewports/view_midnight.png"]
    call screen listening(words, views)
    return

label listen_5:
    $ title_level = "Be polite pt.1"
    $ words = ["Thank you", "Thanks", "Thanks a lot", "I appreciate it", "You're the best",
    "I am grateful"]
    $ views = ["gui/viewports/view_midday.png", "gui/viewports/view_afternoon.png", "gui/viewports/view_sundown.png",
    "gui/viewports/view_evening.png", "gui/viewports/view_lnight.png", "gui/viewports/view_midnight.png"]
    call screen listening(words, views)
    return

label listen_6:
    $ title_level = "Be polite pt.2"
    $ words = ["No problem", "You are welcome", "My pleasure", "Happy to help", "Of course", "No, thank you"]
    $ views = ["gui/viewports/view_midday.png", "gui/viewports/view_afternoon.png", "gui/viewports/view_sundown.png",
    "gui/viewports/view_evening.png", "gui/viewports/view_lnight.png", "gui/viewports/view_midnight.png"]
    call screen listening(words, views)
    return

label listen_7:
    $ title_level = "Quantity"
    $ words = ["Lot", "Much", "Many", "Few", "Handful", "A couple"]
    $ views = ["gui/viewports/view_midday.png", "gui/viewports/view_afternoon.png", "gui/viewports/view_sundown.png",
    "gui/viewports/view_evening.png", "gui/viewports/view_lnight.png", "gui/viewports/view_midnight.png"]
    call screen listening(words, views)
    return

label intro2:
    "Level 2 soon"
    call screen pagina01
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
    $ persistent.n8 = True
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