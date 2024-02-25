label meetingMae:
    #include an option to visit the bakery while you're here. Either that or force a bakery visit if you haven't already been.
    $ townEvents.append("townMaeWallet")
    $ townEvents.append("townMaeLoriRooftop1")
    $ townEvents.append("townLoriTracks1")
    
    scene bg olpickaxe with dissolve
    
    "No one is at the counter when you arrive at the hardware store."
    "You ring the bell and only after a few minutes does the cashier shuffle over."
    
    show bea apron neutral at center with dissolve
    
    bea "*Yaawwwwn*"
    bea "Welcome to the Ol' Pickax. You want it, we probably got it."
    #bea "Welcome to the Ol' Pickax, what is it that ya need?"
    bea "Oh it's you. You got my wrench?"
    
    player "Yup. Thanks for letting me borrow it. My heater was broken and I needed to loosen the bolts to-"
    
    bea "Fascinating. I guess I won't be needing to sic a collection agency on you after all."
    bea "Will that be all?"
    
    player "I think so."
    
    bea "Good. Have a nice day."
    
    hide bea with dissolve
    
    "She looks like she's sleepwalking as she returns to the backroom. You'd be tired too if you spent all day hauling heavy stuff."
    
    show lori neutral at offscreenleft
    show mae neutral at offscreenleft
    
    "You decide not to bother her any further and try to quietly leave the store but someone bursts through the door as you reach out to the handle."
    
    play sound "sound/storebell.mp3"
    
    show mae:
        xzoom -1
        xpos 800
    show lori:
        xzoom -1
        xpos 950
    with move

    #"Wait a minute, you recognize her as the same cat who picked up the mouse girl at the bus station the other day!"
    #"You didn't notice it at the time, but one of her ears is torn and she has subtle red highlights in her fur."
    #"She frantically looks around the store before coming up to you."
    "The cat frantically looks around turning to you."

    mae "Hey, do you know if Bea here right now?"

    #player "Is that the cashier?"
    player "That's the cashier, right?"

    mae "More like owner but yes."

    player "She went into the back room."

    mae "Ok cool thanks."

    show mae skeptical at left

    "She narrows her eyes at you."

    mae "Do I know you from somewhere?"
    
    "A girl steps out from behind the cat. She had practically been clinging to her but now that you get a good look at her, you recognize her from a few days ago."
    
    show lori with move:
        xpos 1100
     
    lori "I know [himherthem]!"
    lori "We met on the bus, remember?"

    #player "I don't think so?"
    
    #mae "I thought I saw you at the bus station the other day."
    
    #"You think back to a few days ago when you first arrived in Possum Springs."
    #n "The memory comes flooding back to you."
    
    #(flashback to day 0, nov 29/30 tuesday)
    #lori is back from school early due to weather
    
    scene bg bus_interior with fade
    play sound "sound/bus_onboard.mp3" fadein 1.0
    play music "music/deathterrors_v2loop.mp3" fadein 1.0
    
    "You were startled awake by a high pitched shriek."
    "The bus was eerily empty, save for the driver and the pair of ears sticking up from the seat in front of you."
    "Taking a peek over it, there's a mouse slumped back watching a movie on her phone and doodling in a notepad."
    "Thankfully she has earphones but sounds were still leaking through."
    #"You sit back, starting to relax"
    "It's already dark out but the reflections off the snow illuminate the surrounding hills."
    "You tap your phone to check the time. It's only 6:15."
    "Your phone signal dies as soon as you pass by the 'Welcome to Possum Springs' sign."
    "Great."
    "At least you'll arrive at your destination soon."
    "Amid the engine sounds and muffled horror movie screams, you hear a pencil fall to the floor and roll back towards you."
    
    menu:
        "Pick it up":
            $ sympathetic = sympathetic + 1
            "You pick up the pencil and pass it over the top of the seat to the mouse girl."
            
            player "You drop this?"
            
            show lori neutral at center with dissolve
            
            loriunknown "Ohmygosh *huff huff* you startled me!"
            
            player "Sorry."
            
            loriunknown "It's alright! I just thought I was the last one on the bus."
            
            "She takes her earphones out and grabs the pencil."
            
            loriunknown "Thanks~ *huff huff*"
            
            "The bus driver clears his throat before sputtering out an announcement."
            
            driver "Next stop *cough cough WHEEEEZE* ...Possum Springs!"
            
            loriunknown "Oop, that's my stop!"

            player "Really? It's mine too!"

            loriunknown "No way! No one else ever gets off at Possum Springs!"

            player "Yeah, I'm moving in today."
            
            loriunknown "It's quite a small and uneventful town! Only a couple murders in the past few years!"
            
            player "That's uh, reassuring."
            
            loriunknown "I lived there my whole life until recently. I'm going to college now but it's not too far away so I visit as much as I can."
            
            player "Oh? What are you studying?"

            loriunknown "Film! Like movies and stuff."
            
            player "I see. Studying for a test?"
            
            "You gesture to the movie paused on her screen."
            
            loriunknown "Something like that!"
            
            "She flips to a page and shows you some of her drawings. They're all of creatures and monsters with bloody knives, elongated claws, jagged teeth or some combination of those."
            
            loriunknown "I'm working on monster design right now. I mean I kinda always have been but it's something I'm focusing on at the moment."
            
            menu:
                "Reminds me of some of my own sketches":
                    $ loriAP = loriAP + 1
                    
                    player "Reminds me of my own sketches."
                    
                    lori "Really? I'd love to see them sometime!"
                "Looks scary":
                    $ loriAP = loriAP + 1
                    
                    player "Looks pretty scary"
                    
                    lori "Thanks! I wanna make movies that frighten people. Really unnerve them, ya know?"
                "2spooky4me":
                    player "Too spooky for me. Good sketches though."
                    
                    lori "Thanks. They're not spooky enough for me but I'm glad they scare someone."
            
            #player "Nice. Those are some pretty cool sketches."
            
            #lori "Thanks! I'm Lori by the way!"
            lori "I'm Lori by the way!"
            
            player "[name]. Nice meeting you!"
            
            driver "Here we are! Final stop -*cough cough WHEEEEZE*- ...Possum Springs!"
            
            player "I guess this is where we get off."
            
            lori "Yup! But don't worry, I have a feeling we'll meet again~"
            
            hide lori with dissolve
            
            "The bus pulls into the station. Grafitti covers the walls and windows, and dead plants sprout from every crack."
            "If the lights weren't on, you'd think it was abandoned."
            
            "Lori stands up and starts walking toward the exit. You check your pockets to make sure you got everything and head out yourself."
            
            scene bg bus_station with fade
            
            #"After grabbing your luggage from "
            "You enter the bus terminal building, hoping the restroom is cleaner than the exterior. It's surprisingly welcoming inside."
            #"Your new friend apparently had someone to pick her up and was waiting indoors."
            
            show mae neutral at right
            show lori neutral at left:
                xzoom -1
            with dissolve
            
            maeunknown "Lori!"

            lori "Mae!"

            mae "Welcome home!"
            
            "The two embrace each other tightly."

            lori "Haha it's good to be back!"

            mae "Glad to see you again! I was starting to think you'd never show up!"
            
            #lori "The bus was delayed because of the snow"
            lori "Thanks for coming to pick me up on such short notice. The school let us out early 'cause of the blizzard!"
            
            #mae "Haha it's no trouble at all! You ready to go home?"
            mae "Anytime! Got everything?"
            
            lori "Yeah, let's go!"

            hide lori
            hide mae
            with dissolve
            
            "Lori gives you a parting wave as she leaves with her cat friend. You watch through the window as she loads her bags into the trunk of a car and they drive away."
            "The wind picks up, rattling the building and pushing snow down faster than before."
            "You should have asked if you could bum a ride."
            
            #you get your luggage and go inside to use the restroom. inside, mae is waiting for lori
            
            
            #lori "Maybe I'll see you around town later~"
                           
            #you're going to possum springs too?
            #yup! i live here! or at least used to. I'm visiting for winter break
            #ah i'm just moving there myself
            #my name's lori
            #blah blah blah film school, what movie was that
            
            #lori mentions to mae sorry for the short notice, they let us out early for winter break due to the blizzard
            
            #lori thanks you and you ask about her movie and sketches
        "Nudge it towards her":
            $ introverted = introverted + 1
            
            "You see a paw blindly reaching under the seat for the lost pencil."
            "You decide to nudge it over in her direction."
            "A moment later her ears pop up over the seat, followed by two curious looking eyes staring back at you."
            "She holds up the pencil she had dropped and smiles at you."
            
            show lori neutral at center with dissolve
            
            loriunknown "Thanks."
            
            "The bus driver clears his throat before sputtering out an announcement."
            
            driver "Next stop *cough cough WHEEEEZE* ...Possum Springs!"
            
            loriunknown "Oop, that's my stop!"

            player "Mine as well."

            loriunknown "No way! No one else ever gets off at Possum Springs!"

            player "Yeah, I'm moving in today."
            
            loriunknown "It's quite a small and uneventful town! Only a couple murders in the past few years!"
            
            player "That's uh, reassuring."
            
            loriunknown "I lived there my whole life until recently. I'm going to college now but it's not too far away so I visit as much as I can."
            
            player "Oh? What are you studying?"

            loriunknown "Film! Like movies and stuff."
            
            player "I see. Studying for a test?"
            
            "You gesture to the movie paused on her screen."
            
            loriunknown "Something like that!"
            
            "She flips to a page and shows you some of her drawings. They're all of creatures and monsters with bloody knives, elongated claws, jagged teeth or some combination of those."
            
            loriunknown "I'm working on monster design right now. I mean I kinda always have been but it's something I'm focusing on at the moment."
            
            menu:
                "Reminds me of some of my own sketches":
                    $ loriAP = loriAP + 1
                    
                    player "Reminds me of my own sketches."
                    
                    lori "Really? I'd love to see them sometime!"
                "Looks scary":
                    $ loriAP = loriAP + 1
                    
                    player "Looks pretty scary"
                    
                    lori "Thanks! I wanna make movies that frighten people. Really unnerve them, ya know?"
                "2spooky4me":
                    player "Too spooky for me. Good sketches though."
                    
                    lori "Thanks. They're not spooky enough for me but I'm glad they scare someone."
            
            #player "Nice. Those are some pretty cool sketches."
            
            #lori "Thanks! I'm Lori by the way!"
            lori "I'm Lori by the way!"
            
            player "[name]. Nice meeting you!"
            
            driver "Here we are! Final stop -*cough cough WHEEEEZE*- ...Possum Springs!"
            
            player "I guess this is where we get off."
            
            lori "Yup! But don't worry, I have a feeling we'll meet again~"
            
            hide lori with dissolve
            
            "The bus pulls into the station. Grafitti covers the walls and windows, and dead plants sprout from every crack."
            "If the lights weren't on, you'd think it was abandoned."
            
            "Lori stands up and starts walking toward the exit. You check your pockets to make sure you got everything and head out yourself."
            
            scene bg bus_station with fade
            
            #"After grabbing your luggage from "
            "You enter the bus terminal building, hoping the restroom is cleaner than the exterior. It's surprisingly welcoming inside."
            #"Your new friend apparently had someone to pick her up and was waiting indoors."
            
            show mae neutral at right
            show lori neutral at left:
                xzoom -1
            with dissolve
            
            maeunknown "Lori!"

            lori "Mae!"

            mae "Welcome home!"
            
            "The two embrace each other tightly."

            lori "Haha it's good to be back!"

            mae "Glad to see you again! I was starting to think you'd never show up!"
            
            #lori "The bus was delayed because of the snow"
            lori "Thanks for coming to pick me up on such short notice. The school let us out early 'cause of the blizzard!"
            
            #mae "Haha it's no trouble at all! You ready to go home?"
            mae "Anytime! Got everything?"
            
            lori "Yeah, let's go!"

            hide lori
            hide mae
            with dissolve
            
            "Lori gives you a parting wave as she leaves with her cat friend. You watch through the window as she loads her bags into the trunk of a car and they drive away."
            "The wind picks up, rattling the building and pushing snow down faster than before."
            "You should have asked if you could bum a ride."
            
            #you get your luggage and go inside to use the restroom. inside, mae is waiting for lori
            
            
            #lori "Maybe I'll see you around town later~"
                           
            #you're going to possum springs too?
            #yup! i live here! or at least used to. I'm visiting for winter break
            #ah i'm just moving there myself
            #my name's lori
            #blah blah blah film school, what movie was that
            
            #lori mentions to mae sorry for the short notice, they let us out early for winter break due to the blizzard
            
            #lori thanks you and you ask about her movie and sketches
        "Kick it away":
            $ chaotic = chaotic + 1
            
            "A paw blindly reaches for the pencil. You kick it away, but a moment later a whole mouse comes crawling out from under the seat to retrieve it."
            
            show lori neutral at center with dissolve
            
            loriunknown "Ohmygosh sorry! *Huff huff* I didn't realize someone was sitting here!"
            
            player "Uhh, it's fine?"
            
            loriunknown "I thought I was the last one on the bus."
            loriunknown "Excuse me..."
            
            "She grabs her pencil and awkwardly returns to her own seat."
            "Suddenly the bus driver clears his throat before sputtering out an announcement."
            
            driver "Next stop *cough cough WHEEEEZE* Possum Springs!"
            
            "The mouse takes an earbud out."
            
            loriunknown "Did he say Possum Springs?"
            
            player "Yeah. You getting off there too?"
            
            loriunknown "Depends, are you a serial killer?"
            
            player "Haven't reached serial status yet."
            player "I'm kidding. I only asked because I'm moving there today and could use some directions."
            
            loriunknown "Ah, that makes sense. I dunno if I can be much help but they have maps of the town at the station."
            
            player "That's good to know."
            player "*You* wouldn't happen to be a serial killer, would you?"
            
            #loriunknown "Only in my dreams."
            loriunknown "Only in my film projects."
            
            player "Your what?"
            
            loriunknown "My films! I did short films for fun. And now I do them for grades."
            loriunknown "After I graduate I wanna work on horror movies."
            
            player "I guess that explains your drawings."
            
            "You point down to the notebook in her lap."
            "The page is filled with creatures and monsters with bloody knives, elongated claws, jagged teeth or some combination of those."
            
            loriunknown "Oh these? I'm working on monster design right now. I mean I kinda always have been but it's something I'm focusing on at the moment."
            
            menu:
                "Reminds me of some of my own sketches":
                    $ loriAP = loriAP + 1
                    
                    player "Reminds me of my own sketches."
                    
                    lori "Really? I'd love to see them sometime!"
                "Looks scary":
                    $ loriAP = loriAP + 1
                    
                    player "Looks pretty scary"
                    
                    lori "Thanks! I wanna make movies that frighten people. Really unnerve them, ya know?"
                "2spooky4me":
                    player "Too spooky for me. Good sketches though."
                    
                    lori "Thanks. They're not spooky enough for me but I'm glad they scare someone."
            
            #player "Nice. Those are some pretty cool sketches."
            
            #lori "Thanks! I'm Lori by the way!"
            lori "I'm Lori by the way!"
            
            player "[name]. Nice meeting you!"
            
            driver "Here we are! Final stop -*cough cough WHEEEEZE*- ...Possum Springs!"
            
            player "I guess this is where we get off."
            
            lori "Yup! But don't worry, I have a feeling we'll meet again~"
            
            hide lori with dissolve
            
            "The bus pulls into the station. Grafitti covers the walls and windows, and dead plants sprout from every crack."
            "If the lights weren't on, you'd think it was abandoned."
            
            "Lori stands up and starts walking toward the exit. You check your pockets to make sure you got everything and head out yourself."
            
            scene bg bus_station with fade
            
            #"After grabbing your luggage from "
            "You enter the bus terminal building, hoping the restroom is cleaner than the exterior. It's surprisingly welcoming inside."
            #"Your new friend apparently had someone to pick her up and was waiting indoors."
            
            show mae neutral at right
            show lori neutral at left:
                xzoom -1
            with dissolve
            
            maeunknown "Lori!"

            lori "Mae!"

            mae "Welcome home!"
            
            "The two embrace each other tightly."

            lori "Haha it's good to be back!"

            mae "Glad to see you again! I was starting to think you'd never show up!"
            
            #lori "The bus was delayed because of the snow"
            lori "Thanks for coming to pick me up on such short notice. The school let us out early 'cause of the blizzard!"
            
            #mae "Haha it's no trouble at all! You ready to go home?"
            mae "Anytime! Got everything?"
            
            lori "Yeah, let's go!"

            hide lori
            hide mae
            with dissolve
            
            "Lori gives you a parting wave as she leaves with her cat friend. You watch through the window as she loads her bags into the trunk of a car and they drive away."
            "The wind picks up, rattling the building and pushing snow down faster than before."
            "You should have asked if you could bum a ride."
            
            #you get your luggage and go inside to use the restroom. inside, mae is waiting for lori
            
            
            #lori "Maybe I'll see you around town later~"
                           
            #you're going to possum springs too?
            #yup! i live here! or at least used to. I'm visiting for winter break
            #ah i'm just moving there myself
            #my name's lori
            #blah blah blah film school, what movie was that
            
            #lori mentions to mae sorry for the short notice, they let us out early for winter break due to the blizzard
            
            #lori thanks you and you ask about her movie and sketches
    
    
    #lori drops her pencil, you can return it for her, or she crawls under the seat for it. can maybe kick it away or pull it closer?
    #you can ask what lori is watching or what she's drawing
    
    
    #"There's nobody else on the bus."
    #"It's just you, the mouse and the driver."
    
    
    #wake up, pass by welcome to possum springs sign and suddenly your phone signal goes out. maybe you woke up because your music stream stopped? maybe lori is watching a movie on her phone and a scream was loud enough to wake you. either way you're the last ones on the bus

    #"You wake up to the sound of some unusual music coming from nearby."
    #"It takes you a while to realize where you are and recall why you're here."
    #"You're on a bus to Possum Springs, a small town your father lived in after your parents split up."
    #"That was ages ago and you'd rarely seen him since."
    #"In fact, nobody's seen him in the past four years. He just vanished one day without a trace."
    #"Normally it takes seven years for a missing person to be legally declared dead but apparently your father was not the most patient man."
    #"He had written in his will that if he disappeared for just four to go ahead and hand all his belongings down to you."
    #"His cash assets would be distributed to you over time though. Guess he didn't want you spending his fortune all in one place."
    #"He did however leave behind a house for you to move into immediately."
    #"Your previous living conditions were not ideal to say the least, so you jumped at the chance to move anywhere else, even if it was in some nowhere town."
    #"You check the time on your phone. It's only 6:15. You'd never know that by looking outside though. It's pitch black out already."
    #"Well, Longest Night is drawing near after all."
    #"Thankfully you hadn't missed your stop."
    #"There's quite a few more people on board now. They must have come on while you were asleep."
    #"Apparently one of them likes loud music."
    #"You can see a pair of ears sticking up over a seat with wires trailing down from them. That must be whoever's earphones making that noise."
    #"At least they have the decency not to blast it through their phone speakers."

    #menu:
    #    "{cps=0}What will you do?{/cps}"
    #    "Ask her what she's listening to.":
    #        $ inquisitive = inquisitive + 1
    #        $ loriAP = loriAP + 1
    #        $ loriInteractionBold == True

            #"It actually sounds like something you'd listen to so she must be pretty cool. You decide to strike up a conversation before #she slips away, never to be seen again."
            #"Moving up to the empty seat beside her, you can't help but take a peak at what she's writing in her notebook."
            #"It's hard to read from this angle but it looks to be a story, with horrific doodles in the margins."
            #"Jagged-toothed monsters, devilish demons, intestines spilling out of the innocent..."
            #"Strange, she doesn't look the type to draw stuff like that."

            #show lori neutral at right with dissolve:
            #    yalign loriheight

            #"She doesn't seem to have noticed you yet so you clear your throat, a bit louder than you need to."

            #player "*Ahem*"

            #show lori breath

            #"The mouse glances up from her journal and nearly jumps out of her seat."
            #"In a flash, she clutches her notebook and scrambles away from you until her back is pressed against the window."
            #"The poor thing's rapidly breathing in and out as she watches you with fear in her eyes."
            #"You hold your hands up to show you meant no harm."

            #player "Whoa, didn't mean to startle you."

            #"Easing back into her seat, she takes her earphones out and makes a concentrated effort to slow her breathing."

            #loriunknown "Oh goodness, you scared me! Hah hah... hah..."

            #"You chuckle lightheartedly."

            #player "I guess that makes us even. Pretty cool music by the way."

            #show lori neutral

            #"The girl looks confused for a moment then realizes her earphones still playing and are audible from a distance."

            #loriunknown "Oh gosh, you could hear that? I'm so sorry!"

            #stop music fadeout 2.0

            #"She mashes the volume down button on her phone in a panicked, embarrassed fashion."

            #loriunknown "*Huff huff*"

            #player "No, it's fine. Actually I wanted to get the name of it before one of us got off the bus."

            #"You confidently smile as you reassure her. She looks at you like you're crazy for a second then smiles back, scooting closer to you."

            #loriunknown "Well uh, it's called Deathterrors. The album, that is. It's by Kerosinners."

            #player "Nice. I'll check it out once I get to my place."

            #"She seems excited to talk more about it, but the bus driver cuts your conversation short as he announces you'll be arriving in Possum Springs momentarily."

            #loriunknown "Oop, that's my stop!"

            #player "Really? It's mine too!"

            #loriunknown "No way! No one else ever gets off at Possum Springs!"

            #player "Yeah, I'm moving in today."

            #loriunknown "Cool! Maybe I'll see you around town later... Whoops!"

            #"She reaches down to grab her pen that had just rolled off her notebook, but you get to it first and hand it back."

            #loriunknown "Hah, thanks! Guess I better pack up before our stop, huh?"

            #player "Yeah, that might be a good idea haha."

            #hide lori with dissolve

            #"While she gathers her things and stuffs them in her backpack, you take a look outside."
            #"The forest has opened up into a hilly countryside. Aside from the train track and an old factory, there's hardly anything noteworthy out there. Just miles and miles of emptiness."
            #"A short time later, the bus pulls up to an abandoned-looking station and stops by an empty bench."
            #"The whole area has fallen into disrepair. Plants sprout from the multitude of cracks in the walls and sidewalk, and graffiti marks nearly every vertical surface."
            #"It looks like a ghost town."
            #"At least some of the lights are on, even if most of them are flickering or have cracked face plates."
            #"You let the mouse girl stand up and start walking toward the exit first, then check your pockets to make sure you got everything and head out yourself."

            #stop sound fadeout 1.0

            #this is supposed to be an exterior background but we didn't have one available :/
            #scene bg busstation with dissolve

            #$ renpy.sound.set_volume(.3, 0, channel='sound')
            #play sound "sound/crickets.mp3" fadein 1.0

            #"The air outside is chillier than expected, in contrast to the surprisingly warm interior of the bus."
            #"You can see your breath forming thick clouds that rapidly rise into the overcast sky as you shuffle over to the storage compartment, shivering."
            #"It's just you and her waiting out here under a streetlight, both with your hands in your pockets and hunched over to cope with the cold."
            #"Your eyes meet at one point and you exchange friendly smiles and subtle nods."

            # brief pause

            #"Jeez, how long is the driver gonna make you wait?"
            #"He takes his sweet time before finally waddling out and unlocking the storage door."
            #"Gesturing for her to go first, you patiently wait for the girl to retrieve her bags, then reach in to dig out your own stuff."

            #show lori neutral at right with dissolve:
            #    yalign loriheight

            #loriunknown "See you around!"

            #"You look up to see the mouse waving goodbye to you with her free hand as she totes her suitcase to a car that had just pulled up to the curb."
            #"You take a break from pulling your bags out to wave back."

            #player "See ya!"

            #"You're rewarded with a wide grin before she runs into the arms of the black-furred cat who had just stepped out of the vehicle, giggling and embracing her fondly."

            # hug scene
            #show mae neutral flip at left with dissolve:
            #    yalign maeheight

            #maeunknown "Lori!"

            #lori "Mae!"

            #mae "Welcome back to Possum Springs!"

            #lori "Haha it's good to be back!"

            #mae "Glad to see you again! Here, lemme get those for you."

            #"The cat takes Lori's luggage and hoists it into the trunk of her car, but the mouse chooses to hold onto her backpack."

            #lori "Hang on, I wanna keep my notebook close by."

            #mae "Gotchya. Ready to go?"

            #lori "Yeah!"

            #hide lori
            #hide mae
            #with dissolve

            #"Lori hops into the passenger seat while her friend closes the trunk and goes back around to the driver side."
            #"The car revs to life and begins to drive away as you drag your things from the bus."
            #"One heavy backpack and two suitcases filled to the brim. All of your belongings in one place."
            #"The bus driver wordlessly closes the compartment and locks it, then returns to his helm of his vessel. With a final roar, the engine hauls its passengers to their next destination."


        #"Ask her to turn it down.":
        #    $ loriAP = loriAP - 1
        #    $ bold = bold + 1
        #    $ loriInteractionRude == True

        #    "You don't wanna hear any more of that creepy music, and you're sure everyone else on the bus would appreciate some peace and quiet."
        #    "Moving up to the empty seat beside her, you can't help but take a peak at what she's writing in her notebook."
        #    "It's hard to read from this angle but it looks to be a story, with horrific doodles in the margins."
        #    "Jagged-toothed monsters, devilish demons, intestines spilling out of the innocent..."
        #    "What kind of person draws stuff like this?"

        #    show lori neutral at right with dissolve:
                #yalign loriheight

            #player "Excuse me."

            #$ cynical = cynical + 1

            #show lori anxious3:
            #    yalign loriheight

            #"She jumps a little when she notices you, knocking her pen to the floor."
            #"She hastily picks it back up then takes out her earphones. Her movement is kinda jittery and she's breathing heavily."

            #show lori breath

            #loriunknown "Um, hey? Huff huff... Did you need something?"

            #"You point to her earphones lying on her journal."

            #player "Would you mind turning that down?"

            #"She glances down at her earphones then back up to you with a panicked, embarrassed expression."

            #loriunknown "Oh gosh, you could hear that? I'm so sorry, hang on!"

            #stop music fadeout 2.0

            #"She mashes the volume down button on her phone."

            #loriunknown "Huff huff... Huff huff..."

            #player "Appreciate it."

            #hide lori with dissolve

            #"With that out of the way, you decide to look out the window and admire the countryside."
            #"Hills, a train track, a factory, and more hills. So this is it, huh? It's quite... plain."
            #"The driver announces you'll be arriving in Possum Springs shortly, and a few minutes later you pull up to an empty bench near an abandoned-looking station."
            #"The whole place has fallen into disrepair. Plants sprout from the multitude of cracks in the walls and sidewalk, and graffiti marks most vertical surfaces."
            #"It looks like a ghost town."
            #"At least some of the lights are on, even if most of them are flickering or have cracked face plates."
            #"The mouse girl hurriedly stands up and starts walking toward the exit, looking a bit distressed."
            #"Is she angry because you asked her to turn down her music?"
            #"Regardless, you check your pockets to make sure you got everything and head out yourself."

            #stop sound fadeout 1.0

            #scene bg busstation with dissolve

            #$ renpy.sound.set_volume(.3, 0, channel='sound')
            #play sound "sound/crickets.mp3" fadein 1.0

            #"The air outside is chillier than expected, in contrast to the surprisingly warm interior of the bus."
            #"You can see your breath forming thick clouds that rapidly rise into the overcast sky as you shuffle over to the storage compartment, shivering."
            #"It's just you and that girl waiting out here under a streetlight, both with your hands in your pockets and hunched over to cope with the cold."
            #"She avoids eye contact with you."

            # brief pause

            #"Jeez, how long is the driver gonna make you wait?"
            #"He takes his sweet time before finally waddling out and unlocking the storage door."
            #"Gesturing for the mouse to go first, you patiently wait for her to retrieve her bags, then reach in to dig out your own stuff."
            #"Out of the corner of your eye, you can see her walk up to a car as it pulls up to the curb."
            #"A black-furred cat steps out to happily greet her with a nice big hug."

            #show lori neutral at right:
            #    yalign loriheight
            #show mae neutral flip at left
            #with dissolve

            #maeunknown "Lori!"

            #lori "Mae!"

            #mae "Welcome back to Possum Springs!"

            #lori "Haha it's good to be back!"

            #mae "Glad to see you again! Here, lemme get those for you."

            #"The cat takes hold of Lori's luggage and hoists it into the trunk of her car, but the mouse opts to keep her backpack with her."

            #lori "Hang on, wanna keep my notebook close."

            #mae "Gotchya. Ready to go?"

            #lori "Yeah!"

            #hide lori
            #hide mae
            #with dissolve

            #"Lori hops into the passenger seat while her friend closes the trunk and goes back around to the driver side."
            #"The car revs to life and begins to drive away as you drag your things from the bus."
            #"One heavy backpack and two suitcases filled to the brim. All of your belongings in one place."
            #"The bus driver comes and locks the compartment, then wordlessly returns to his helm of his vessel. With a final roar, the engine hauls its passengers to their next destination."


        #"Move away from her.":
        #    $ loriInteractionNull = True
        #    $ cynical = cynical + 1

        #    "You don't wanna bother her. You'll be off this bus soon anyway."
        #    "You move over to a seat further away from her and take a look out the window, losing yourself in thought."
        #    "The forest has opened up into a hilly countryside."
        #    "Aside from the train track and an old factory, there's hardly anything noteworthy out there. Just miles and miles of emptiness. So this is it huh? It seem so... plain."
        #    "The driver announces you'll be arriving in Possum Springs shortly, and a few minutes later you pull up to an empty bench near an abandoned-looking station."
        #    "The whole place has fallen into disrepair. Plants sprout from the multitude of cracks in the walls and sidewalk, and graffiti marks most vertical surfaces."
        #    "It looks like a ghost town."
        #    "At least some of the lights are on, even if most of them are flickering or have cracked face plates."
        #    "The mouse girl stands up and walks toward the exit before you do. You wonder if she lives here."
        #    "Seems she's the only one besides yourself getting off at this stop. You check your pockets to make sure you got everything and head out yourself."

        #    stop music fadeout 2.0
        #    stop sound fadeout 1.0

        #    scene bg busstation with dissolve

        #    $ renpy.sound.set_volume(.3, 0, channel='sound')
        #    play sound "sound/crickets.mp3" fadein 1.0

        #    "The air outside is chillier than expected, in contrast to the surprisingly warm interior of the bus."
        #    "You can see your breath forming thick clouds that rapidly rise into the overcast sky as you shuffle over to the storage compartment, shivering."
        #    "It's just you and her waiting out here under a streetlight, both with your hands in your pockets and hunched over to cope with the cold."
        #    "Your eyes meet at one point and you exchange friendly smiles and subtle nods."
        #    "She still has her earphones in, and you can overhear all the cries and moans and screams that she doesn't seem to mind at all."

            # brief pause

        #    "Jeez, how long is the driver gonna make you wait?"
        #    "He takes his sweet time before finally waddling out and unlocking the storage door."
        #    "Gesturing for her to go first, you patiently wait for the girl to retrieve her bags, then reach in to dig out your own stuff."
        #    "Out of the corner of your eye, you can see her remove her earphones then excitedly run up to a car as it pulls up to the curb."
        #    "A black-furred cat steps out to happily greet the mouse and give her a nice big hug."

        #    show lori neutral at right:
        #        yalign loriheight
        #    show mae neutral flip at left:
        #        yalign maeheight
        #    with dissolve

        #    maeunknown "Lori!"

        #    lori "Mae!"

        #    "Welcome back to Possum Springs!"

        #    lori "Haha it's good to be back!"

        #    mae "Glad to see you again! Here, lemme get those for you."

        #    "The cat takes hold of Lori's luggage and hoists it into the trunk of her car, but the mouse opts to keep her backpack with her."

        #    lori "Hang on, wanna keep my notebook close."

        #    mae "Gotchya. Ready to go?"

        #    lori "Yeah!"

        #    "Lori hops into the passenger seat while her friend closes the trunk and goes back around to the driver side."

        #    hide mae
        #    hide lori
        #    with dissolve

        #    "The car revs to life and begins to drive away as you drag your things from the bus."
        #    "One heavy backpack and two suitcases filled to the brim. All of your belongings in one place."
        #    "The bus driver comes and wordlessly locks the compartment, then returns to his helm of his vessel. With a final roar, the engine hauls its passengers to their next destination."

    # restore default music volume
    #$ renpy.music.set_volume(0.7, 0, channel='music')

    scene bg olpickaxe with fade
    
    show lori neutral at offscreenleft
    show mae neutral at offscreenleft

    #"From there you remember walking through the woods to get to your new home."

    show mae neutral:
        xzoom -1
        xpos 900
    show lori neutral:
        xzoom -1
        xpos 1300

    "A look of realization dawns on the cat."

    mae "Oh yeah! I do remember seeing you! At the bus station!"
    mae "It's not every day someone new arrives in Possum Springs!"

    player "Ah right, I saw you for just a moment. I just moved into town the other day. My name's [name]."

    mae "Mae. Mae Borowski. Nice to meet you!"

    player "Same!"

    mae "So what made you decide to come all the way out to Possum Springs?"

    player "You know, the relaxing countryside, the fresh air, peace and quiet... oh and inheriting a house up past the train tracks."
    player "The old man was nice enough to put it in my name before he died a few years back."

    show mae sad1

    "Mae looks away and mumbles to herself."

    mae "Died...?"

    show mae panic at left
    
    mae "Err how many years ago? If you don't mind my asking...?"
    
    player "Like five I think?"

    "She suddenly looks like she's seen a ghost."

    mae "Uhh, look at the time Ihavetogobye!"
    mae "Come on Lori, I just remembered we have to be somewhere."
    
    show mae at offscreenleft with move
    
    lori "Mae! Wait up!"
    lori "Sorry to run off so quickly, [name]. I'll see you around though, I'm sure."
    
    show lori at offscreenleft with move
    
    "You look out the window and watch the pair run through the streets just as the crocodile cashier comes back."

    show bea apron at right with dissolve

    bea "Was that Mae and Lori just now?"

    "You're still processing what just happened. You snap out of it and turn to the shop owner."

    player "Uh, yeah. You know them?"

    bea "You could say that. What did they want?"

    player "I dunno. They just came in, asked if you were here, then left."

    bea "Huh. Weird."
    bea "Anyway, is there anything else you needed?"

    player "Hm? Oh, no I was just leaving."

    bea "See you around."

    player "Later gator."
    
    "She bares her teeth at you."
    "You'll take that as your cue to finally get out of here."
    
    hide bea with dissolve

    stop music fadeout 2.0

    return