#tela listening
screen listening():
    add "gui/fases.png"
    text "{size=80}[title_level]" xpos 0.2 ypos 0.05

    viewport:
        add "gui/textbox.png"
        xpos 0.05 ypos 0.3
        
    grid 3 5:
        spacing 30
        xpos 0.15 ypos 0.7
        for i in words:
            textbutton"{size=30}[i]":
                action MainMenu()