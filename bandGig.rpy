label bandGig1:
    #considerations
    #at this point you may not have met Lori and Mae
    #maybe only trigger this scene if you've met them

    #outline
    #As they're cleaning up, lori hangs out with the band, they notice you and invite you over, then get dinner at clik clak

    "You're running late but as you approach the bakery, you can see the lights are still on and the thumping of bass hangs in the air."
    "You quicken your pace and reach for the door handle."
    
    scene bg bakery with fade
    
    "Inside there's a small crowd formed around the stage. You can hardly see who's on it due to the dim lighting, but you recognize the voice on the microphone."
    
    show angus neutral at center with dissolve
    
    angus "Thank you again for coming out tonight! Since you've been such a wonderful crowd, we have one last song for you!"
    
    hide angus with dissolve
    
    "The crowd gives a pathetic cheer and the lights go out."
    "One by one spotlights shine on the band members as they begin their next song."
    "To your shock, you know them already."
    "Grocery clerk on guitar, hardware store girl on keyboard, weird avoidant cat playing bass, and bakery guy is the singer."
    "They're surprisingly not bad. Not amazing but not bad."
    "They get your foot tapping at least."
    "When they're finished playing, the crowd gives an applause, with one overly enthusiastic high pitched shriek beind heard above all."
    
    show lori neutral at right with dissolve
    
    lori "WOOOOOO!!! I LOVE YOU MAE!!!!"
    
    show mae blush2 at left with dissolve:
        xzoom -1
    
    mae "Heh. I know you do. Thanks for coming out and listening, guys!"
    
    hide mae
    hide lori
    with dissolve
    
    show gregg neutral at left:
        xzoom -1
    show bea neutral at right
    with dissolve
    
    gregg "Thank you!! You all rock!"
    gregg "Be sure to follow Bea on bandcloud! She writes all our shit!"
    
    bea "Oh shut up."
    bea "But yeah, it's b-e-a underscore tunes."
    bea "Tunes as in music, not cartoons ok whatever you get the idea."
    
    hide bea
    hide gregg with dissolve
    
    show angus neutral at center with dissolve
    
    angus "Thank you all again! We hope you enjoyed our music!"
    
    "Someone in the crowd responds."
    
    show raccoon neutral at right with dissolve
    
    raccoon "I just came here for the free cookies."
    
    angus "Well I hope you enjoyed those too! I baked them myself!"
    
    raccoon "Yeah they're pretty good."
    
    hide raccoon 
    hide angus
    with dissolve
    
    "The crowd begins to dissipate as almost everyone leaves and the band starts packing their equipment and cleaning up."
    "A couple of them stay behind and help out."
    
    show germ neutral at left with dissolve:
        xzoom -1
        
    germ "Hey sorry guys, I can't stick around. I have to take care of some things at home."
    
    show gregg neutral at right with dissolve
    
    gregg "No problem dude. We're just glad you could come at all."
    
    #mae "Yeah! Where would we be without our most loyal fan?"
    mae "Take care, Germ! We'll see you next time, right?"
    
    germ "Wouldn't miss it!"
    
    show lori at right with dissolve
    
    lori "Bye Germ! Give your pet possum hugs and kisses for me!"
    
    germ "Will do. Later guys!"
    
    hide germ with dissolve
    
    show bea at left with dissolve:
        xzoom -1
    
    bea "So. Are we getting dinner or what?"
    
    gregg "Of course we are! 'Tis a tradition after a gig!"
    
    angus "Clik Clak?"
    
    mae "Dude, what else is open at this hour?"
    
    angus "Clik Clak it is."
    
    "By now everyone has left aside from the band, their one groupie, and you."
    "One of them happens to notice you awkwardly standing in the corner of the room eavesdropping on their conversation."
    
    $ highestAP = max(loriAP, greggAP, angusAP, beaAP)
    
    if highestAP == loriAP:
        "Lori excitedly waves for you to come over."
        
        lori "Hey [name]! Fancy seeing you here! How'd you enjoy the band?"
        
        player "They were good. I got in late and only heard the last song though."
        
        lori "Guys, this is [name]! [name], that's Gregg, Angus, and Bea!"
        
        player "I've already met everyone, actually."
        
        lori "What? Really?? You all know each other?"
        
        bea "[heshethey] came into my store bothering me about a screwdriver a few days ago."
        
        if screwdriverReturned == False
            bea "I still haven't gotten that back by the way."
            
            player "Sorry, I'll bring it back ASAP."
            
            bea "You better."
        
        gregg "Saw [himherthem] at the Ham Panther earlier this week."
        
        angus "And they swung by the bakery at some point too."
        
        lori "I guess introductions aren't neccessary then!"
        lori "We were just about to go to the local diner."
        
        "Lori turns to the others."
        
        lori "Would it be cool if [name] joined us?"
    elif highestAP == beaAP:
        "Bea gives you a wave and you take that as your cue to join the circle."
        
        bea "Hey there."
        bea "... Did you enjoy the music?"
        
        player "Yeah, it was pretty good. I got in late and only heard the last song though."
        
        bea "Ah well, it's not our best one."
        bea "Guys, this is [name]. [name] this is Gregg, Angus, Mae, and Lori."
    elif highestAP = greggAP:
        "gregg is best boy"
    elif highestAP = angusAP:
        "angus is best boy"

    
    
    
    return