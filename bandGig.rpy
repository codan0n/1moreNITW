label bandGig1:
    $ bandGig1Complete = True
    #considerations
    #at this point you may not have met Lori and Mae
    #maybe only trigger this scene if you've met them

    #outline
    #As they're cleaning up, lori hangs out with the band, they notice you and invite you over, then get dinner at clik clak
    
    scene bg bakery_exterior with fade

    "You're running late but as you approach the bakery, you can see the lights are still on and the thumping of bass hangs in the air."
    "You quicken your pace and reach for the door handle."
    
    scene bg bakery_interior with fade
    
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
    
    show lori neutral at right with dissolve
    
    lori "Bye Germ! Give your pet possum hugs and kisses for me!"
    
    germ "Will do. Later guys!"
    
    hide germ with dissolve
    
    show bea neutral at left with dissolve:
        xzoom -1
    
    bea "So. Are we getting dinner or what?"
    
    gregg "Of course we are! 'Tis a tradition after a gig!"
    
    angus "Clik Clak?"
    
    mae "Dude, what else is open at this hour?"
    
    angus "Clik Clak it is."
    
    "By now everyone has left aside from the band, their one groupie, and you."
    "One of them happens to notice you awkwardly standing in the corner of the room eavesdropping on their conversation."
    
    $ highestAP = max(loriAP, beaAP)
    
    if highestAP == loriAP:
        "Lori excitedly waves for you to come over."
        
        lori "Hey [name]! Fancy seeing you here! How'd you enjoy the band?"
        
        player "They were good. I got in late and only heard the last song though."
        
        lori "Guys, this is [name]! [name], that's Gregg, Angus, and Bea!"
        
        player "I've already met everyone, actually."
        
        lori "What? Really?? You all know each other?"
        
        bea "[heshethey] came into my store bothering me about a screwdriver a few days ago."
        
        if screwdriverReturned == False:
            bea "I still haven't gotten that back by the way."
            
            player "Sorry, I'll bring it back ASAP."
            
            bea "You better."
        
        gregg "Saw [himherthem] at the Ham Panther earlier this week."
        
        angus "And they swung by the bakery at some point too."
        
        lori "I guess introductions aren't neccessary then!"
        lori "We were just about to go to the local diner."
        
        "Lori turns to the others."
        
        lori "Would it be cool if [name] joined us?"
        
        "The band looks at each other. Bea shrugs."
        
        bea "Sure."
        
        player "Cool. I've never been to this diner before."
        
        bea "Don't get your hopes up. It sucks."
        
        gregg "But it has S O U L!!!"
        
        angus "It also costs twice as much as it did 5 years ago."
        
        bea "Are we going or not?"
        
        gregg "Yeah, let's just finish packing away everything here first."
    elif highestAP == beaAP:
        "Bea gives you a wave and you take that as your cue to join the circle."
        
        bea "Hey there."
        bea "... Did you enjoy the music?"
        
        player "Yeah, it was pretty good. I got in late and only heard the last song though."
        
        bea "It's not our best one."
        
        lori "It's my favorite... Oh and hi [name]!"
        
        mae "Yeah Bea, don't sell yourself short. That song rocks!"
        
        bea "Eh. I think it could use some work."
        
        angus "Welcome back to my bakery, [name]. Shame you missed out on the free cookies."
        
        gregg "Sorry, I ate like half of them."
        gregg "Also hi [name]. You coming to Constellation Conquest next week?"
        
        player "Haven't decided yet."
        
        gregg "Aww..."
        
        bea "Cool, it sounds like you already know everyone so I don't have to introduce you."
        bea "We're about to get some chow at the local diner. Wanna come with?"
        
        player "Sure!"
        
        gregg "Sweet! Just let us finish packing away everything here first then we'll head out."
    #elif highestAP = greggAP:
        #"gregg is best boy"
    #elif highestAP = angusAP:
        #"angus is best boy"
        
        #gregg "Yeah I know [himherthem], we already met. At Ham Panther. Remember?"

    
    "After everyone finishes cramming their guitars and amps in the storage closet, Bea folds the legs under her keyboard setup and tucks it under her arm."
    
    bea "Everything's packed up. You ready to go?"
    
    player "Yup!"
    
    "You all file out through the doorway and into the cold dark street."

    scene bg bakery_exterior with dissolve

    show bea neutral at right with dissolve

    "Bea turns toward the group and does a headcount."

    bea "There's too many of us to fit in my car, so I guess we're walking."

    show gregg neutral at left:
        xzoom -1
    with dissolve

    gregg "I volunteer to sit in Angus's lap to make space."

    bea "That would work if I didn't have a big box of records in the passenger seat and a keyboard soon to be occupying the back."

    gregg "Aww."
    
    bea "I'm gonna throw this in my car real quick."
    bea "Be right back."
    
    "Bea starts heading toward the Ol' Pickaxe where her car is parked."

    show mae panic at left:
        xzoom -1
    with dissolve

    mae "I'll go with you!"

    "Mae spontaneously runs off to catch up to Bea."
    
    hide mae
    hide bea
    with dissolve
    
    gregg "Hurry up! My nuts are freezing out here!"
    
    "Gregg pulls out a bag of pistachios and munches on them."
    
    angus "You're gonna spoil your appetite."
    
    gregg "It was worth it for the pun."
    
    "Mae and Bea take their time. Everyone's shivering and Lori is pacing back and forth to keep herself warm. Angus wraps his arm around Gregg and holds him tight."
    "When the two do return, Mae looks like something's bothering her and that she doesn't want to be here."
    "Bea whispers something to her and Mae puts on a smile like nothing's wrong."
    
    show bea neutral at right
    show mae neutral at right
    with dissolve
    
    bea "Sorry that took so long, we had to move a bunch of junk around. We all ready?"
    
    gregg "We are so ready."
    
    scene bg clikclak
    
    "The diner turns out to only be a few blocks away. It's a repurposed train car with an orange neon sign reading \"CLIK CLAK DINER\"."
    
    "Gregg holds the door open for everyone. Inside, you're met with a cramped, cluttered space, vaguely reminiscent of Art Deco design, covered with photos, paintings, and other artwork on the walls."
    "You're seated at a booth and given a menu that has typical diner offerings."
    "Pizza, burgers, bacon and eggs, club sandwiches, and even pierogies. You all make your selections and chat while the food is prepared."
    
    show bea neutral at right with dissolve
    
    bea "So, [name]. I heard you moved here recently? What made you come to Possum Springs?"
    
    player "Eh, just wanted to get away from home, ya know? Move out, be independent, all that stuff."
    player "I have to say, I'm enjoying Possum Springs a lot more than I thought I would."

    bea "Really? Almost everyone I know can't wait to escape from here."

    "A subtle hush falls over the group. Bea quickly changes the topic."

    bea "Anyway, you got a job yet?"

    player "Nope. Living off of savings at the moment. Why, you know anybody who's hiring?"

    show lori neutral at right
    
    lori "I could scrounge something together and pay you a little if you help me work on my movie."

    player "You're making a movie?"

    lori "Yup! It's partly a school project, but it's also something I just wanna do."
    lori "I'm out in the woods or by the tracks nearly every day if you wanna come and watch or set up equipment. Or maybe you could even act in it?"
    
    bea "I could use a hand at the shop if you're interested. Backbreaking work, but decent, untaxed, under-the-table pay."
    
    player "What do I have to do?"

    bea "Lift heavy stuff, sometimes direct a customer to said heavy stuff, and on rare occasion, move the heavy stuff to their car."
    
    show angus neutral at left:
        xzoom -1
    show gregg neutral at left:
        xzoom -1
    
    gregg "I could try putting in a good word for you at Ham Panther. I don't think they're hiring right now, though."
    
    angus "I've got my claws full just trying to pay myself at the bakery, so..."
    
    gregg "Maybe Mae could get you something at the arts council if you're into that?"
    
    "All eyes turn toward an unsuspecting Mae. She looks like she wasn't paying much attention to the conversation and was caught off guard by the mention of her name."

    show mae panic at right with dissolve
    
    mae "Oh! Uh, yeah. I teach art stuff at the Deep Hollow County Arts Council on Fridays and Saturdays. Painting, clay sculpting, photography..."
    
    lori "She's really good at it!"
    lori "Mae's the one who taught me how to use a camera!"
    
    show mae sad1

    "Mae shrugs."

    mae "At this point, Lori's more familiar with cameras than I am. I just know enough to teach the basics."

    player "I'll check it out if I'm feeling artsy."
    
    show mae neutral

    "Mae flashes you a forced smile. Luckily, the awkward moment is interrupted by the waitress coming by with your orders."
    "Food has a way of lightening the mood. Mae relaxes and even becomes more talkative as the evening goes on."
    "Even though your meal isn't very good, you still have a pleasant time with your new friends."
    "When it comes time to pay the bill, Gregg insists that he cover for you. You politely decline, but you were surprised he'd even do such a thing."
    "Funny enough, Gregg doesn't even pay for his own meal. Angus covers him."
    "Bea pays for herself, and Mae asks the waitress to put hers and Lori's meals on one bill."
    
    show mae curious2

    "Lori wordlessly expresses her gratitude by wrapping her arm around Mae and embracing her in a hug. For the first time tonight, you see Mae smile in earnest."
    
    scene bg street with fade
    
    "Once you're outside, you all crowd around under a streetlight and discuss your plans for the rest of the night."

    gregg "This was great! We should do this again."

    lori "Yeah, it was awesome seeing you guys playing as a band again!"

    "Bea pulls out her electronic cigarette."

    bea "Always a joy. But I think I'm gonna go home, relax, and watch some TV with my dad now."

    lori "Yeah, I should get home too before my dad starts worrying about where I am so late."

    mae "I'll drive you home so you don't have to walk back in the dark, Lori."

    lori "Thanks!"

    gregg "Me and Angus'll probably watch some streams, then go to sleep."

    player "Yeah, sleep sounds good right about now. But it was fun hanging out with you all!"
        
    "Everyone says their goodbyes and goes their own way for the night."
    
    return