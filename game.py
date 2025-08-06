# NOTE THE USE OF TYPE HINGS HERE. The function accepts a str argument and
# returns a str (or None).
def get_input(options: str) -> str:
    # TODO: FIX THIS FUNCTION
    choice = input("CHOOSE: ")
    return choice


def intro():
    print(
"""
A GAME OF GROANS
================
Welcome to the lamest adventure game ever. You have woken up to find yourself,
well, in a bed. A familiar bed. In fact it's *YOUR* bed.

You feel compelled to leave the house. Yes, in fact, this is your quest. You
simply _**must**_ find a way out of your own house.

Being that it's your house, you'd think that you'd be quite familiar with it.
And in fact it's quite small being a "tiny house" with only a few rooms. But you
feel a bit groggy and your brain is numb for reasons you can't quite recall. So
you're going to have to "explore" your way out.

With a loud groan, you stumble out of bed and discover that you are in...wait
for it...your bedroom.

Do you want to wake up and play this game?
  * (Y)es
  * (N)o
"""
    )
    choice = get_input("yn")
    if choice == "y":
        return bedroom    # BE CAREFUL...DO NOT USE PARENS HERE...NOT return bedroom()
    else:
        print(
"""
You waste your one opportunity to escape and are trapped in your sad, tiny
little excuse for a home forever!!!! Mwa, ha, ha, ha, ha!!!!!!

GAME OVER!
"""
        )
        exit()


def bedroom():
    print("YOUR BEDROOM")
    print(
"""
You are standing in your bedroom. There are multiple windows tempting you with
the sweet, sweet goodness that is the outside. However, presumably this is a bad
neighborhood, so there are steel bars preventing you from using them to escape.

In addition to the bed, there's a dresser, a nightstand, a crap-ton of dirty
clothes, and a couple of doors. DOORS! OMG! You realize you can use those things
to explore other parts of the house.

A door to the East is ajar and you can just make out the shape of a toilet bowl
peeking through the hinge crack.

A door to the South is also ajar, but you're too blurry-eyed to see what
mysteries that room holds.
"""
    )

    print(
"""
You can:
  * Go (E)ast
  * Go (S)outh
  * (L)ay back down on your bed
"""
    )
    choice = get_input("esl")

    if choice == "e":
        return bathroom
    elif choice == "s":
        return living_room
    else:
        print(
"""
OH NO! NO! NO! As you go to lie down, you are overcome with nausea and make a
dash in the direction of that toilet bowl you glimpsed.

After a lot of really uncomfortable dry heaving and even more groaning, you
slowly stand and take in your surroundings.
"""
        )
        return bathroom


def bathroom():
    print("YOUR BATHROOM")
    print(
"""
Well. Yep. A bathroom. And a toilet bowl that does appear attached to a full-on
toilet. I would imagine your creative mind can come up with a better
description. So please do.
          
You currently have no choice but to go (W)est, back to the bedroom.
"""
    )
    get_input("w")
    return bedroom


def living_room():
    print(
"""
You enter the living room and are magically transported outside. You win.

GAME OVER!

Dude! This ending sucks! You need to make it better.
"""
    )
    exit()

################################################################################
# The main game loop. Look but don't touch!!

def game_loop():
    scene = intro
    while True:
        next_scene = scene()
        if callable(next_scene):
            scene = next_scene
        else:
            print("SILLY CODE ERROR")
            print("It appears you returned something other than a function from one of your scene functions.")
            exit()


if __name__ == "__main__":
    game_loop()
