#níveis a serem desbloqueados
default persistent.n2 = False
default persistent.n3 = False
default persistent.n4 = False
default persistent.n5 = False
default persistent.n6 = False
default persistent.n7 = False

# Declare os personagens usados nesse jogo. O argumento image, liga a imagem
# ao nome do personagem.

define t = Character("Teru", image = 'Teru')
define pp = Character([persistent.pp], image = 'PP')

# Declare as imagens aqui
##BG
image bgintro = "BG/BG_intro.png"

##PP
layeredimage PP:
 always:
  "PP/PP happy.png"

 group eyes:
  attribute P_normal default:
   "None.png"
  attribute P_bored:
   "PP/PP bored.png"

##Teru

layeredimage Teru:
 always:
  "Teru/Teru_body.png"

 group eyes:
  attribute T_open default:
   "Teru/Teru_openEyes.png"
  attribute T_close:
    "Teru/Teru_closeEyes.png"
  attribute T_angry:
    "Teru/Teru_angryEyes.png"

 group expressions:
  attribute none default:
    "Teru/None.png"
  attribute T_talk:
   "Teru/Exp_talk.png"
  attribute T_exc:
   "Teru/Exp_excl.png"

#ATL
transform floating:
 block:
        xalign 0.5 yalign 0.3
        linear 2.0 yalign 0.2
        linear 2.0 yalign 0.3
        repeat