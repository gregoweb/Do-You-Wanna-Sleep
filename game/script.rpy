# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define g = Character("Game Master", color="#b55088")
define audio.lovesong = "music/love-Song.mp3"


# Skill

# The game starts here.

label start:
    play music lovesong fadeout 1.0 fadein 1.0
    # Nombre de personne ayant dormi dans votre chambre
    $score = 0

    $charm = 0
    $eloquence = 0

    # 0 kind 1 kinky
    $kinky = False

    # jour en cours
    $day=1
    $dayMax=3

    # Action Point
    $apMax=3
    $ap= apMax
    
    $bedroomCapacity=1
    # 16 = 8B + 8G
    $names =['Barack','Sarah','Bill','Elisabeth','Bobby','Sakura','George','Hilary','Jenny','John','Ronald','Rosy','Sergei','Charlotte','Greg','Eileen']
    $namesMax = 15
    #$characters = [Character("Lucy", color="#ffcccc"),Character("Clea", color="#aaaaff")]

    #guest[id][Name][charm][eloquence]
    $guest = []
    $nbGuests = 0

    # est-ce que le bonus de multiplication des ap a ete utilise
    $limitedSpaceBonus=False

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg style

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    python:
            name = renpy.input("Hi, what's your name ?")
            name = name.strip() or "Cloud" 
    scene bg style
    
    menu:
        "Quick game 6 turns":
            $dayMax = 6
        "Quick game 15 turns":
            $dayMax = 15
        "Quick game 30 turns":
            $dayMax = 30

    play sound "audio/select.wav"

    "Dear {color=#B55088}[name]{/color} I challenge you to full your bedroom with as many {color=#B55088}Guest{/color} as possible in [dayMax] of days . To achieve that you have to choose your style"
    # TODO menu maxDay (en combien de jours 6 15 30)
    # These display lines of dialogue.

    menu:
        "{color=#0099DB}Z - Kind style - Z{/color}":
            $kinky = False
            $color = '0099DB'
        "{color=#F04}❤️ - Kynky style - ❤️{/color}":
            $kinky = True
            $color = 'F04'
    play sound "audio/select.wav"

    "An advice for you {color=[color]}[name]{/color} : just remember to be sure to have enough Skills and Bedroom Capacity before inviting a {color=#B55088}Guest{/color}"
    while day < dayMax+1:
        scene bg city
        "{color=[color]} Good morning {/color}"
        while ap > 0:
            label day:
            "Day : [day] - Score : [score]\n {color=#FEAE34}Action Point : [ap]{/color} - Bedroom Capacity :[bedroomCapacity]\n {color=#F04} ❤️ : [charm]{/color} - {color=#0099DB}Z : [eloquence]{/color}"

            if limitedSpaceBonus:
                menu:
                    "Move":
                        play sound "audio/select.wav"
                        jump move
                    "Invite":
                        play sound "audio/select.wav"
                        jump invite
            else:
                menu:
                    "Move : choose a place to upgrade your Skills or Bedroom Capacity":
                        play sound "audio/select.wav"
                        jump move
                    "Invite : try to invite some guest in your bedroom":
                        play sound "audio/select.wav"
                        jump invite
                    "{color=#FEAE34}Space : Space-Time limited bonus can only be used once APx2 for the day{/color}":
                        play sound "audio/jump.wav"
                        $ap = ap * 2
                        $limitedSpaceBonus = True
                        jump day
                        
            label move:
            menu:
                "Littery store : Bedroom Capacity +1 ":
                    scene bg littery
                    show bed2:
                        xalign 0.7
                        yalign 0.7
                    show sbed:
                        xalign 0.3
                        yalign 0.7
                    
                    $bedroomCapacity += 1
                "{color=#0099DB}Library{/color} +ZZ":
                    scene bg library
                    $eloquence +=2
                "{color=#B55088}Cinema +❤️ +Z{/color}":
                    scene bg cinema
                    $eloquence +=1
                    $charm +=1
                "{color=#B55088}Beach +❤️ +Z{/color}":
                    scene bg plage 
                    $eloquence +=1
                    $charm +=1
                "{color=#F04}Love Store +❤️❤️{/color}":
                    scene bg love 
                    $charm +=2
                #"Fitness Sport cours de diction AP +1"
                #   $ap +=1
            play sound "audio/powerup.wav"
            "Day : [day] - Score : [score]\n {color=#FEAE34}Action Point : [ap]{/color} - Bedroom Capacity :[bedroomCapacity]\n {color=#F04} ❤️ : [charm]{/color} - {color=#0099DB}Z : [eloquence]{/color}"
            jump nextPA
            
            label invite:

            $guestA = names[renpy.random.randint(0, namesMax)]
            $guestAc = renpy.random.randint(0,day)
            $guestAe = renpy.random.randint(0,day)
            $guestB = names[renpy.random.randint(0, namesMax)]
            $guestBc = renpy.random.randint(0,day)
            $guestBe = renpy.random.randint(0,day)
            $guestC = names[renpy.random.randint(0, namesMax)]
            $guestCc = renpy.random.randint(0,day)
            $guestCe = renpy.random.randint(0,day)

            
            $success = False
            menu:
                "{color=#B55088}[guestA]{/color} {color=#F04}❤️:[guestAc]{/color} - {color=#0099DB}Z:[guestAe]{/color}":
                    if guestAc <= charm:
                        if guestAe <= eloquence:
                            if nbGuests < bedroomCapacity:
                                $score +=1
                                $nbGuests +=1
                                $success = True
                    if success:
                        play sound "audio/coin.wav"
                        "{color=#B55088}[guestA]{/color}" "{color=#11EE11}Good idea let me see your Bedroom{/color}"
                    else:
                        play sound "audio/hit.wav"
                        "{color=#B55088}[guestA]{/color}" "{color=#EE1111}No way{/color}"
                "{color=#B55088}[guestB]{/color} {color=#F04}❤️:[guestBc]{/color} - {color=#0099DB}Z:[guestBe]{/color}":
                    if guestBc <= charm:
                        if guestBe <= eloquence:
                            if nbGuests < bedroomCapacity:
                                $score +=1
                                $nbGuests +=1
                                $success = True
                    if success:
                        play sound "audio/coin.wav"
                        "{color=#B55088}[guestB]{/color}" "{color=#11EE11}Good idea let me see your Bedroom{/color}"
                    else:
                        play sound "audio/hit.wav"
                        "{color=#B55088}[guestB]{/color}" "{color=#EE1111}No way{/color}"
                "{color=#B55088}[guestC]{/color} {color=#F04}❤️:[guestCc]{/color} - {color=#0099DB}Z:[guestCe]{/color}":
                    if guestCc <= charm:
                        if guestCe <= eloquence:
                            if nbGuests < bedroomCapacity:
                                $score +=1
                                $nbGuests +=1
                                $success = True
                    if success:
                        play sound "audio/coin.wav"
                        "{color=#B55088}[guestC]{/color}" "{color=#11EE11}Good idea let me see your Bedroom{/color}"
                    else:
                        play sound "audio/hit.wav"
                        "{color=#B55088}[guestC]{/color}" "{color=#EE1111}No way{/color}"

            label nextPA:
            $ap -= 1
        #endwhile ap>0

        $ap = apMax
        $nbGuests = 0
        $day += 1
        
        if kinky:
            scene bg kinky
            if bedroomCapacity <=1:
                show bed
            elif bedroomCapacity <=3:
                show bed2
            else:
                show bed3
            "{color=[color]}❤️ Good night ❤️{/color}"
        else:
            scene bg blue
            if bedroomCapacity <=1:
                show bed
            elif bedroomCapacity <=2:
                show sbed
            elif bedroomCapacity <=4:
                show sbed:
                    xalign 0.7
                    yalign 0.7
                show sbed2:
                    xalign 0.3
                    yalign 0.7
            else:
                show sbed:
                    xalign 0.6
                    yalign 0.7
                show sbed2:
                    xalign 0.3
                    yalign 0.7
                show sbed3:
                    xalign 0.8
                    yalign 0.7
            "{color=[color]}Time to sleep Zzz{/color}"
            

    # This ends the game.
    play sound "audio/coin.wav"
    "Well done {color=[color]}[name]{/color} you manage to full your bedroom with {color=#[color]}[score]{/color} {color=#B55088}Guests{/color} in [dayMax] days"
    return
