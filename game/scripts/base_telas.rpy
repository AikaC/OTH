# Tela listening
screen listening(words, views):
    add "gui/fases.png"
    text "{size=80}[title_level]" xalign 0.5 ypos 0.05

    # Define uma grid para os botões
    grid 3 2:
        xalign 0.5 ypos 0.7
        spacing 30

        # Cria um botão para cada palavra
        for word, image_path in zip(words, views):
            textbutton word:
                style_prefix "quick"
                idle_background Frame("gui/button/idle_listen.png")
                hover_background Frame("gui/button/hover_listen.png")
                action Show("image_screen", image_path=image_path)
            
    vbox:
        textbutton _("Níveis") action ShowMenu ("nivel")

# Tela para exibir a imagem
screen image_screen(image_path):
    add "gui/fases.png"
    text "{size=80}[title_level]" xpos 0.2 ypos 0.05
    add image_path xpos 0.13 ypos 0.2
    
    # Define uma grid para os botões
    grid 3 2:
        xalign 0.5 ypos 0.7
        spacing 30

        # Cria um botão para cada palavra
        for word, image_path in zip(words, views):
            textbutton word:
                style_prefix "quick"
                idle_background Frame("gui/button/idle_listen.png")
                hover_background Frame("gui/button/hover_listen.png")
                action Show("image_screen", image_path=image_path)

    vbox:
        textbutton _("Níveis") action ShowMenu ("nivel")
