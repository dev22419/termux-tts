import os

os.system('termux-toast -b white -c black -g top termux-style by dgr22419 ')

x=str(input(": "))

os.system('termux-tts-speak '+ x +'')

