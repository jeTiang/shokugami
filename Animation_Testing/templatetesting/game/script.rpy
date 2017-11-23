# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init python:
    vpuncht = Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=.275)
    hpunch = Move((15, 0), (-15, 0), .10, bounce=True, repeat=True, delay=.275)

define e = Character("Eileen")

#image bg tempRailtransarvo = "tempRailtransarvo.png"

# The game starts here.
image backgroundTrain:
    contains:
        "sky"
        xalign 1.0


    contains:
        choice:
            pause 20.0
        choice:
            pause 15.0
        choice:
            pause 10.0
        xalign 1.0
        "bar"
        linear 2.0 xpos-1.0

        repeat
    contains:

        subpixel True
        xalign 0.0
        yalign 0.0
        "bg test"
        zoom 1.06

        choice:
            linear 0.01 xpos 0 ypos 10
            linear 0.01 xpos 0 ypos 0
        choice:
            pause 7.0
        choice:
            pause 12.0

        repeat
#        with vpuncht

#        choice:
#            pass
#        choice:
    #        linear 0.01 yalign 0.97
    #        linear 0.01 yalign 0.0

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene backgroundTrain
    #image img  = Image("bg test.png", xpos = 0, ypos = 0)
    #show img vpuncht
    #show img with dissolve:
        #linear 2.0 xpos 200 ypos 200
        #linear 2.0 xpos 0 ypos 0
        #repeat

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    "Hello, world."

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.
    jump choice

    return

label choice:
    $ drank_tea = False

    menu:
        "What should I do?"

        "Drink coffee.":
         "I drink the coffee, and it's good to the last drop."
         $ drank_tea = True

        "Drink tea.":
         "I drink the tea, trying not to make a political statement as I do."

    menu:
        "Go left.":
            "gass gass gass"
        "Go right.":
            "gass gass gass"
        "Fly above." if drank_tea:
            "coffev"
