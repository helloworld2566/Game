# The script of the game goes in this file.
default peek = False
default tookPhoto = False

label start:
    scene 1
    # 18+ Age Confirmation
    "This game is intended for players 18 years or older."
    "Are you 18 years or older?"
    
    menu:
        "Yes":
            "Thank you for confirming. Let's proceed."
            jump game_start
        "No":
            "Sorry, you need to be 18 or older to play this game."
            return  # Ends the game

label game_start:
    if not _in_replay:
        $ m = "Landlady"
        $ m_name = "Maria"
        $ s = "Tenant"
        $ cr = "Older Roommate"
        $ cr_name = "Cristina"
        $ lu = "Roommate"
        $ lu_name = "Luna"
        $ ch = "Friend"
        $ ch_name = "Chris"
        $ th = "Therapist"
        $ fa = "Group"
        $ y = "John"
        $ tmp = ""
        $ npc1 = "Guy 1"
        $ npc2 = "Guy 2"

        scene 1 
        play music "playfull.mp3"

        show mc-bg with dissolve
        $ tmp = renpy.input ("What is your name? (Default: John)")
        if tmp != "":
            $ y = tmp.strip()
        $ persistent.y = y
        hide mc-bg

        show maria-bg with dissolve
        $ tmp = renpy.input ("What is she to you? (Default: Landlady)")
        if tmp != "":
            $ m = tmp.strip()
        $ persistent.m = m 

        $ tmp = renpy.input ("What is her name? (Default: Maria)")
        if tmp != "":
            $ m_name = tmp.strip()
        $ persistent.m_name = m_name

        $ tmp = renpy.input ("What are you to her? (Default: Tenant)")
        if tmp != "":
            $ s = tmp.strip()
        $ persistent.s = s
        hide maria-bg

        show cristina-bg with dissolve
        $ tmp = renpy.input ("What is she to you? (Default: Older Roommate)")
        if tmp != "":
            $ cr = tmp.strip()
        $ persistent.cr = cr

        $ tmp = renpy.input ("What is her name? (Default: Cristina)")
        if tmp != "":
            $ cr_name = tmp.strip()
        $ persistent.cr_name = cr_name
        hide cristina-bg

        show luna-bg with dissolve
        $ tmp = renpy.input ("What is she to you? (Default: Roommate)")
        if tmp != "":
            $ lu = tmp.strip()
        $ persistent.lu = lu

        $ tmp = renpy.input ("What is her name? (Default: Luna)")
        if tmp != "":
            $ lu_name = tmp.strip()
        $ persistent.lu_name = lu_name
        hide luna-bg

        "WARNING!!! I don't take any responsibility on how you name your relationships with the girls."

        jump family_introduction

label family_introduction:
    "Let's introduce the characters based on your input."

    show mc-bg with fade
    "This is you [y], our main character."
    hide mc-bg

    show maria-bg  with fade
    "This is [m_name], your [m]."
    hide maria-bg

    show cristina-bg with fade
    "This is [cr_name], your [cr]."
    hide cristina-bg

    show luna-bg with fade
    "This is [lu_name], your [lu]."
    hide luna-bg

    "Now that you know everyone, let's start the story."
    scene black with fade
    centered "Incestous - Chapter 1"
    jump ep1

