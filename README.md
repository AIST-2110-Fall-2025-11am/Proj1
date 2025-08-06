# Project 1: The Adventure Begins

This week, we're embarking on our adventure game adventure. It's not going to be
much of a game, yet, but you have to start somewhere.

## Learning Objectives

1. Start exploring the basics of the adventure game project
2. Practice working with string objects and methods including:
   - strip()
   - lower()
3. Practice using the len() function
4. Practice using the isinstance() function
5. Practice raising exceptions

## Introduction

The game is divided up into multiple scenes. Scenes can be places to go, things
to see, specific encounters, etc. The game tells a story, so a scene is just a
part of the story that (likely) concludes with some kind of decision that needs
to be made by the player.

Technically, we're using Python functions to model each individual scene. And
for this week, you'll create the scenes that are defined in this README. Though
for your actual project, you are going to take this in an ENTIRELY NEW direction
of your choosing. But that's fun for a later assignment.

For now, look at the sample code. Note that each function does something
similar. It describes the scene and then it either exits the program or returns
the next scene (i.e., it returns the next function to call). And most of the
time the next scene is determined based on a user choice.

> Feel free to examine the `game_loop()` function at the bottom. It's extremely
> simple. Basically it just loops forever, calling each scene function and then
> calling whatever scene that function returns. This will stay mostly the same
> for the duration of this project.

## Tasks

You have a few tasks this week. Most are fun, but let's treat this like a
mullet: business up front and party in the back.

So first, you need to implement the `get_input()` function. This is somewhat
similar to earlier get_something() functions, but this time there's a lot more
input validation. Instead of just getting ANY input, you are getting ONE
character from the user. And that character MUST be one of a few specified by a
parameter. And even more, you are making the function so that it protects you
from yourself. So you'll "raise" exceptions if the arguments passed in are bad.

> A `raise Exception()` statement raises a _generic_ exception. But you can (and
> should) raise more specific kinds of exceptions. `raise ValueException()`
> generally means that someone passed in a bad argument to a Python function.
> Note that this is the **_opposite_** of exception _handling_. You as the
> developer of your super-cool function are now telling some other schmuck coder
> that they used your function incorrectly. And THEY have to either handle it
> with a try/except or (in this case) fix their code.

`get_input()` takes one argument (`options`). This will be a string of letters.
Each letter represents ONE of the valid choices. So `get_input("esl")` means
the user must enter either `e` or `s` or `l`. To meet these requirements, the
function needs to do the following (probably in this order):

  1.  Validate the `options` parameter value:
      - Use `isinstance()` to ensure `options` is a `str` object. If not raise a
        `ValueException()`.
      - Use `.lower()` and `.strip()` to remove any extra spaces and lowercase
        the `options`.
      - Use `len()` to make sure that there is at least one character in
        `options`. If not raise a `ValueException()`.
  2.  Enter into an infinite loop to ask for user input:
      - Prompt the user to "CHOOSE: " (this is the only part that is unchanged)
      - Use `.lower()` and `.strip()` to remove any extra spaces and lowercase
        the user's choice.
      - If the user's choice is exactly one character long and is one of the
        options (i.e. it is "`in options`"), then return their choice. (this
        exits the infinite loop)
      - Otherwise, print "INVALID CHOICE" and allow the loop to iterate.

Two steps, but they are pretty tricky steps. They are also pretty common for
input validation, so a very useful (and "business-like") exercise.

> NOTE: the automated testing ONLY tests the above. Everything below is going to
> be evaluated by running each of your games. So, yes, I WILL see your story.

NOW, on to the fun. The "scenes" in this silly example adventure game/story are
as follows:
```
    ┌─────────┐     ┌──────────┐
    │ Bedroom ├─────┤ Bathroom │
    └────┬────┘     └──────────┘
         │
  ┌──────┴──────┐    ┌─────────┐   ┌────────┐
  │ Living Room ├────┤ Kitchen ├───┤ Garage │
  └──────┬──────┘    └─────────┘   └───┬────┘
      LOCKED!                          │
                                ┌──────┴────┐
        N                       │  OUTSIDE  │
      W + E                     │ game over │
        S                       └───────────┘
```
There's also an introductory scene that shows only once. `intro()` and
`bedroom()` are pretty much done. And `bathroom()` and `living_room()` have some
placeholder text and logic in them. But writing the rest of the scenes to tell
the rest of this oh-so-riveting choose-your-own-adventure story...that's where
you come in.

You need to:

  - add the missing scene functions
  - "finish" any unfinished (or lame) functions
  - the scene-to-scene navigation must follow the above map
    + but the scene descriptions, other choices, etc. are all up to you
    + so...make me laugh

Yes the game currently is quite small. And silly. And pointless. It's called "A
Game of Groans" because it's so lame. But it's the very first sample. We'll
get better over time.

> NOTE: In living_room(), they should have the option to go south, but since the
> door is locked, they should be informed of the locked door and `return` back
> to `living_room` (since they didn't actually move).

For this and all of the project assignments, the highest-scoring submissions
will demonstrate creativity. Technical function is still necessary, but will not
be sufficient by itself. For this assignment, this can include:

  - unique descriptions (e.g., specific, vivid objects)
  - intriguing choices (e.g., story prompts instead of just directions)

Lower-scoring submissions might look like this lackluster example:
```
This is a bedroom.

You can:
  Go (W)est
  Go (N)orth
  Open (T)rapdoor
```
I don't need you to be Stephen King or Octavia Butler or J. K. Rowling, but
effort and creativity will count. Engage your players' imaginations.

The numbers may change as we progress, but for this assignment, expect scoring
to be be allocated as follows:

  - 75% functionality
  - 25% creativity and effort

> TIP: Visual Studio Code in your Codespace has a new extension installed called
> Rewrap. This can be used to easily perform word wrapping in multi-line
> strings. If you format long text passages as demonstrated in the sample code,
> then you can place your text cursor anywhere in a paragraph and press `Alt+Q`
> to automatically wrap the text at a comfortable width.

Write a bit. Test a bit. Chuckle. Have fun. Repeat until thoroughly cooked.

## Assignment Completion Procedures

You will complete and submit this assignment in a similar way to prior
assignments. To avoid cluttering up this README with the same instructions each
time, they have been broken out into a separate file. Please reference
[PROCEDURES.md](PROCEDURES.md) to see the details if you have forgotten.

In summary:

  1. Complete the code per the instructions
  2. Run the game to test and debug interactively
  3. Execute the automated tests to ensure expected functionality

When finished, do not forget to:

1. Commit and Sync:
    - Switch to version control tab
    - Stage all changed files
    - _**Enter a commit message**_
    - Click Commit
    - Click Sync
2. Validate your submission in GitHub
3. Submit the final commit ID in D2L
