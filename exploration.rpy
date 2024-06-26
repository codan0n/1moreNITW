#more labels

label dailyExploration:
    menu:
        "{cps=0}What should you do?{/cps}"
        "Explore home" if houseEventsDay:
            if exploredHouse == False:
                call unexploredHouse
            
            #if houseEvents is empty, you can no longer explore the house
            #if not houseEventsDay:
            #    $ houseFullyExplored = True
            #    "You've already explored the house enough."
            
            $ randomSelected = renpy.random.choice(houseEventsDay)
                
            call expression randomSelected
            #else:
            #    "You've already explored the house enough."
            #    $ houseFullyExplored = True
        
        "Explore town" if townEventsDay:
            scene bg roads_day with dissolve
        
            "You decide to explore Possum Springs and familiarize yourself with the area."
            
            $ randomSelected = renpy.random.choice(townEventsDay)
            
            call expression randomSelected
            
        "Return screwdriver" if screwdriverReturned == False:
            #could probably just have a $ hasScrewdriver variable and it would work more cleanly
            #day or night
            $ screwddriverReturned = True
            
            "You promised the hardware store girl that you'd return the screwdriver after you were done with it."
            "You have no more use for it so you should give it back as soon as possible."
            
            call returnScrewdriverScene 
        "Return library book" if haveOverdueBook == True:
            #daytime only
            "The book is more overdue than the screwdriver. You should return it first."
            
            call libraryVisit1 
        "Return wallet" if dayWalletFound > 0:
            call maeLoriSleepover
        "Do nothing":
            "Yeahhh you don't really feel like doing anything today."
            "You sit back and mindlessly stare at your phone for a few hours."
            
    return

label unexploredHouse:
    $ exploredHouse = True
    
    "The eerie emptiness of the house unsettles you as you look around."
    "This is the house your father lived in all alone after the divorce. You've been here a few times to visit, but now that he's gone, you've inherited it."
    "A desolate building, untouched for years. Dust has piled up on every surface and cobwebs spill from the ceiling, but everything is otherwise so tidy and neat."
    "It really is a tomb."
    "Your wistful memories conflict with the current reality."
    "The guest room you slept in is exactly like you remember it but the kitchen got all new tile and a fresh coat of paint."
    "There are a lot more bookshelves than you recall. Was that coffee table always there in the den?"
    #"A whirlwind of confusion and conflicting emotions makes your search for tools more difficult. You're not sure where to look. You've never even been in half the rooms."
    
    #jump continue
    
    return

label houseOffice:
    # day or night
    $ officeQuestStarted = True
    $ houseEventsDay.remove("houseOffice")
    $ houseEventsNight.remove("houseOffice")
    
    scene bg home_office_day with fade

    "While wandering around the house you stumble upon an unfamiliar room: the office. You were never allowed in here."
    "Books and binders are scattered along the shelves. Some of them look so old they'll fall apart if you picked them up."
    "A desk sits on the far end of the room with a computer on top of it. You wonder if it still runs."
    "But first you take a moment to play with the dial on the wall safe. You have no idea what the code might be but predictably you don't happen to guess it on your first try."
    "Heck."
    "There's probably some good loot in there too... Maybe there's a local locksmith who can crack it open."
    "You take a seat in the swivelling chair and press the power button on the desktop. The whirring of fans and disk drives fills the room for a few seconds before the monitor wakes up."
    "Immediately it asks for a password before even booting into the operating system. You try typing in a few common passwords but it won't let you in."
    "What a shame. This thing may be old but it could probably run some games."
    #"There must be a way to bypass this..."
    "There must be a way to bypass this... but you'd probably need someone to walk you through it so you don't break it."
    "You hold the power button to shut it off and slump in your seat. You glance at the photo frame beside the monitor."
    #"A thick layer of dust cakes the various books and binders on the shelves but the desk area remains relatively clean."
    #"You poke around the safe and the computer a bit, but you're unable to crack into either of them."
    #"Much like the wifi, the PC is locked behind a password."
    #"Your inheritance paperwork never mentioned any codes or passwords. You try a few random guesses to no avail."
    #you poke around the safe and then the computer before finding the photo
    
    
    #"In your idle spinning, you must have accidentally bumped the mouse, because you hear the computer suddenly turn on."
    #"You try a few common passwords but have no luck getting in."
    #"You'll need to figure out a way to get past the login screen sometime."
    #"You wander what could possibly be on the hard drive."
    #"It's probably just going to be full of vacation photos and spreadsheets. A cryptocurrency wallet or two if you're lucky."
    #"But you don't wanna wipe the drive until you've taken a look."

    # pause

    #"As you shut the computer down, you notice a photo frame next to the monitor."
    "Inside there's a faded photo of you as a kid. You're holding up a fish you caught and your father is kneeling beside you with a proud look on his face."
    "You vaguely remember when that photo was taken. It was many years ago in early spring, when all the leaves were bright green."
    "You got up early and spent the whole day fishing, just you and your dad. Then when the sun started going down you sat on the bank and fed the fish with the remainder of your bait."
    "Simpler times, those were. Your parents were still together back then."
    "It's hard to think he's been missing for five years."
    "Just vanished one day without a trace."
    "You feel a lump in your throat, but you push it down because adults aren't supposed to cry."
    #"With a heavy sigh, you look back at the monitor."
    #"You half-heartedly try a few random passwords until it locks you out."
    #might change back to the corrupt hard drive in recovery mode thing
    #"Dang, the disk is saying it's corrupt. It's starting a recovery procedure now."
    #"The estimated finish time is given in... days?!"
    #"Just how big is the hard drive?"
    #the code for the safe is in the files?
    #"Ugh, you'll deal with this later. You leave the machine running and prepare to head out."
    
    
    
    
    
    
        #"That's odd, the lamp is already on."
    #"The soft glow illuminates the tidy room and all its furnishings."
    #"You had called the utilities companies ahead of time to get things ready for your arrival, but apparently nobody took the time to turn off this one light."

    #hint that there's a mark where a book used to lie on the table
    #"Surprisingly this house hasn't been ransacked and vandalized in all the years it was sitting unoccupied, at least not from what you can tell."
    #"You're lucky this house you've inherited hasn't been broken into and vandalized in all the time it was sitting empty."
    #"At the very least the safe appears to be... safe. "
    #"No sign that anybody tried to break into that safe, so whatever it contains is probably... safe."
    #"Interestingly there's a safe built into one of the walls. You wonder what that's all about but there's no way you're getting it open without the combination."
    #maybe gregg can crack it
    #"You'll have to try and crack it later, right now you're more interested in cracking the wifi password."
    #"You follow the wires coming out of the computer under the desk, which leads you straight to the router."
    #"Jackpot!"
    #"You look all over the box but the default password has faded from the label."
    #"Damn cheap piece of shit ink."
    #"You desperately look around the room for any sticky notes with passwords scrawled on them to no avail."
    #"Even the computer is locked behind a password when you try turning it on."
    #"Why can't phones just come with ethernet ports? You could plug yours in directly and satisfy your internet addiction if people weren't so obsessed with having thin phones."
    #"If only your phone had an ethernet port."
    #"You step away and sigh."
    #"Now what are you gonna do?"
    #"Your inheritance hasn't hit your bank account yet so buying a new computer or router is out of the question."
    #"Especially when you haven't even bought groceries."
    #"Your stomach rumbles."
    #"You better find something to eat soon. Even a small town like Possum Springs must have a place to get breakfast, right? Hopefully some decent coffee too."
    #"That, and a restaurant is bound to have public wifi."
    #"That map of Possum Springs you snagged from the bus station yesterday should point you in the right direction."
    #"You put on a jacket and shoes and ventured out in search of food and internet."
    #"That's all the motivation you need to put on some shoes and head out the door and begin the hunt for food and internet."

    
    
    #"Your tour of the house concludes when you find yourself back in the office."
    #"Your tour of the building took you through different rooms filled with art, furniture, and books."
    #"Nothing out of the ordinary for a well-off boomer. You noted your father had a taste for antiques."
    #"But what stood out to you the most was what must have been your father's bedroom."
    #"Just thinking about it sends a chill up your spine and you're not sure why."
    #"The room smelled like old stale clothes, and neither of the two windows provided much light. There was nothing in there except a king sized bed, a nightstand, and a wardrobe."
    #"It didn't feel right to mess with anything so you shut the door and made a note to leave it be, like a tomb."
    #"Wandering over to the desk, you take a gander at the shelves stuffed with binders and books. They seem to be work related."
    #"You sit down in the leather chair and slowly spin around."
    #"It's actually really comfortable. You guess you'd splurge on a nice chair too if you were gonna sit in it for long periods of time."
    
    #"There's just one more room left to check out."
    
    return

label houseShed:
    $ houseEventsDay.remove("houseShed")
    #daytime exclusive
    "While exploring the house, you happen to notice something unusual through one of the windows: a rickety looking shed standing in the backyard, half buried under the snow."
    "You recall playing in the backyard but don't remember there ever being a shed. It must have been built after the last time you visted."
    "With some effort, you manage to dig through the snow to reach the door handle, but it's locked up tight with a rusty chain and padlock."
    if hasKey == True:
        "The key you found earlier looks like it might fit the lock."
        "You run inside to retrieve it, but when you insert it into the lock, the handle snaps off, rendering it impossible to open."
        "Nothing can ever be easy or straightforward, can it?"
        "With the door firmly stuck, you'll have to consider alternative methods of entry if you wanna see what's inside."
        #maybe you could glue the handle back on or something
        
        $ doorStuck = True
        #if you're past week 1, add bikequest part 2 to exploration scene list
    else:
        "Maybe there's a key somewhere inside. Otherwise you'll have to find... alternative methods of entry."
    $ bikeQuestStarted = True
    
    return
    
label houseBook:
    #day or night
    $ haveOverdueBook = True
    $ libraryQuestStarted = True
    $ houseEventsDay.remove("houseBook")
    $ houseEventsNight.remove("houseBook")
    
    #the book contains part of the password?
    "You looked through various nooks, crannies, shelves, drawers, and boxes but found nothing noteworthy."
    "Exhausted, you decide to take a break and recline on the living room sofa."
    "Ow!"
    "Something hard is digging into your spine."
    "You reach between the cushions and pull out a hardcover book with a library sticker on the side."
    "It's titled \"Cryptids of the Western Hemisphere.\""
    "Flipping it open, you note there's a slip of paper inside with the names of everyone who checked it out along with the dates."
    "The most recent is your father, dated five years ago. He must have checked out this book shortly before vanishing."
    "Maybe he skipped town to avoid the late fee?"
    "Haha..."
    "Okay, maybe comedy isn't a good coping mechanism for this."
    "Kind of a strange book to check out though."
    "You wonder what interest he would have had in mythological creatures."
    "Opening it up to the bookmarked page, you find an article on the Jersey Devil, a weird skinny goat thing with wings."
    "The paranormal sure loves its goats, doesn't it?"
    "There's not even anything particularly evil about him, he's just a winged goat with devil connotations that sometimes steals chickens."
    "Upon reading further, it appears this creature was nothing more than a fabrication by hysterical religious country bumpkins."
    "You should return this book to the library. They've probably been missing it."
    
    return

label houseKey:
    #day or night
    $ houseEventsDay.remove("houseKey")
    $ houseEventsNight.remove("houseKey")
    $ hasKey = True
    
    "Your tour of the house brings you to a spare bathroom where the sound of water dripping disturbs the otherwise still area every few seconds."
    "You pull back the curtain around the bathtub to reveal it's been filled almost to the brim, presumably from the leaky faucet over the years."
    "You turn the knob to prevent any more water from dripping and hesitantly stick your hand elbow-deep into the frigid tub to pull the stopper and drain it."
    "As the water spirals down the drain, the flow drags an object along the bottom, catching your eye."
    "You reach your hand into the water once more to grab it before it can fall through the drain. It turns out to be a rusty key."
    "You wonder how it got here and what it's for."
    
    if bikeQuestStarted == True:
        "Maybe it's for the shed out back?"
        "You run outside, eager to see what the shed contains, but when you insert the rusty key into the lock, the handle snaps off."
        "Nothing can ever be easy or straightforward, can it?"
        "With the door firmly stuck, you'll have to consider alternative methods of entry if you wanna see what's inside."
        #maybe you could glue the handle back on or something
        
        $ doorStuck = True
        #if you're past week 1, add bikequest part 2 to exploration scene list
    else:
        "You put it away somewhere safe and continue about your day, satisfied that you prevented imminent water damage and didn't have to fight a giant spider or something."
        
    return
    
#label afterLookingForTool:
#    "You spent a few hours searching and have yet to find a tool to open that grate. At this rate, it'll be dark by the time you figure something out."
#    "For all you know, there might not even be a wrench in this house anymore."
#    "Your next best option is to see if the hardware store in town has what you need."
#    
#    jump intoTown
    


label intoTown:
    "You put on a jacket and boots and make your way towards the center of the town."
            
    scene bg roads_day with dissolve
    
    #"You try to follow the map but without GPS "
    #"Without GPS you get a bit lost but eventually stumble upon what must be the main street."
    #"blah blah blah general description of the surroundings."
    "Old brick buildings line the streets as you approach your destination. Some of them look lived in, others look like they're about to crumble."
    "Some look like both."
    #i think the memorial statue is between the shops?
    #"pass by the trolley station but it's boarded up. You take a peek inside."

    "That looks like the hardware store up ahead, but the aroma from the nearby bakery draws you in."
    "Where will you go?"
    
    menu:
        "{cps=0}Where will you go?{/cps}"
        "Bakery":
            jump meetingAngus
            #gregg mentions he's on a long lunch break since it's a slow day, but that he is still clocked in  
        
        "Hardware store":
            jump meetingBea
                            
            #what about pliers?
            #where do i know her (mae) from? :flashback:
        
        #"underground":
            #minor event
        
        #"rooftops":
            #minor event
            
            
label nightlabel:
    "It'll get dark in a couple hours. Is there anything else you want to do today?"
    
    jump continue
    
label townLoriTracks1:
    $ townEventsDay.remove("townLoriTracks1")
    ####to be added in a future version
    #$ townEventsDay.append("townLoriTracks2")
    
    $ loriAP = loriAP + 1
    
    #outline - find lori between the tracks, from a distance think she's a dead animal that got hit by a train, but no she's just chilling and says you should try it. option to stay away or sit with her. kind of an awkward scene. no train comes, disappointing lori. she says she used to do this all the time but there's no trains near her university. she says she was excited to leave possum springs but she's more happy to be back. player says they miss their city but not their situation. thinks possum springs is better than they expected. Lori gives you a penny to put on the tracks.
    
    scene bg roads_day with dissolve
    
    "Today you decide to follow the train tracks to see if they lead anywhere cool."
    "You mostly just get a view of the backside of old buildings and empty fields though."
    "Lame."
    "You're about to call it quits when you notice something in the distance between the tracks."
    "What is that?"
    "When you get closer, you can tell it's a person lying on their back. Are they ok?"
    "Please don't be a dead body."
    "Their ears perk up when you get closer."
    
    show lori breath at center with dissolve
    
    lori "*Squeak!*"
    
    show lori neutral
    
    lori "Oh, it's just you. I heard footsteps in the snow running towards me and I thought you were gonna like stab me or something."
    
    player "Uh no. I thought you were a dead animal that got hit by the train at first."
    
    lori "So you came running?"
    
    player "I only started running when I realized it was a person! What are you doing lying in the middle of the tracks anyway?"
    
    lori "Just chilling."
    
    player "In the most dangerous spot you could pick?"
    
    lori "It's safer than the streets. The trains give a lot of warning before they show up. And I like seeing them."
    
    player "You do this often?"
    
    lori "I used to. There's no trains near my university, but I usually come out here whenever I visit Possum Springs. You should try it!"
    
    player "What?"
    
    "You look around, suddenly feeling like a train is about to sneak up on you."
    
    player "I feel weird just standing on the tracks."
    
    lori "There's plenty of space between them. Just be sure to move your feet away from the tracks when a train is coming."
    
    menu:
        "Sit between the tracks":
            $ loriAP = loriAP + 1
            $ bold = bold + 1
            
            "If she can do it so fearlessly, so can you. But you're getting away the moment you hear a train."
            
            player "Fine, I'll do it. I don't see what's so cool about it though."
            
            show lori happy
            
            lori "You'll understand when you get up here!"
            
            "You climb up the rocky hill to the tracks and sit beside Lori, just far enough so she can't push you in front of an oncoming train."
            
            show lori neutral
            
            player "...I don't get it."
            
            lori "Give it a while. Might have to wait for a train to come first."
            lori "It's supposed to feel exciting doing something you're not supposed to do. Just a little bit of harmless mischief."
            lori "That's how it was when I started doing it, but I guess I got used to it and now it's a relaxing comfort activity."
            
            "Lori lies down with her arms behind her head as a pillow. You follow suit."
            
            player "Hmm. I just feel like I'm gonna get hit by a piece of metal hanging off a train and die."
            
            lori "Then we'd both die! Hahahaha!"
            
            player "Hahaha... wait, that's not funny!"
            
            lori "It made you laugh though."
            
            player "You tricked me into laughing."
            
            lori "Just like how I tricked you into sitting between the train tracks?"
            
            player "Haha yeah..."
            
            "You suddenly sit up."
            
            player "Wait, was this all just a trick?"
            
            #lori "Only if you think I could manipulate you into stumbling upon this particular section of track at this specific time on this exact day."
            lori "Hehehe not really! I had no idea you'd be here today. You seem cool and I just thought you might wanna hang out between some tracks."
            
            menu:
                "Me? Cool?":
                    player "Me? Cool? No one's ever said that before."
                    
                    lori "Nobody thought I was cool either until I met the right people."
                    
                    player "I guess you just have to be in the right place at the right time."
                    
                    lori "Like on the train tracks in the afternoon."
                    
                    player "Yeah."
                    
                    lori "Well... I'm here pretty often whenever I'm in town, so if you ever wanna hang out just follow the tracks."
                    
                    player "I'll think of you every time I see roadkill."
                    
                    lori "Hehehe!"
                "It's kinda fun":
                    player "I mean, it's kinda fun?"
                    player "It's a new experience at least. I never would have thought to do something like this back in the city."
                    player "I'd probably provoke a gang war or get shot by police for trespassing just doing this."
                    
                    lori "I'm glad my college isn't like in a huge city."
                    lori "I don't think I could get used to it if it was."
                    lori "It's bigger than Possum Springs, sure, but it's not like 'city living' you know? *huff huff*"
                    
                    player "Yeah... I don't miss the traffic and noise and trash everywhere."
                    player "Possum Springs makes me feel like I'm on a different planet."
                    player "Like I'm on some Mars colony far away from everything else."
                    
                    lori "That's a good way of putting it. Vast and empty and you need to take a shuttle to get back to civilization."
                    lori "Gotta watch out for the Martians lurking under the soil too."
                    
                    player "Oh nooo, don't eat me! I taste bad, I'm full of corn syrup!"
                    
                    lori "Hehehe!"
                "I guess it was fate":
                    player "I guess it was fate that we'd both end up here at the same time."
                    
                    lori "Maybe! But I'm here pretty often to be honest, so fate is pretty lenient I guess."
                    lori "Perhaps there's a reason why we keep bumping into each other, like in the grand scheme of things."
                    
                    player "Like a supernatural reason or...?"
                    
                    lori "Yeah!"
                    lori "Like two strangers keep seeing each other on the street and then it's revealed that they have some sort of mystical connection that they have to use to discover some hidden secret and defeat the big bad evil guy!"
                    lori "*Huff huff* sorry, I read too many stories."
                    
                    player "Haha well I don't think it's quite that deep, but I'd be down for an adventure. I've already had to do some low level quests since moving into town."
                    
                    lori "Really? Like what?"
                    
                    player "Just some mundane fetch quests to get key items to progress the plot. Trade a coffee for a screwdriver to fix the furnace and so on."
                    
                    lori "Ohh like one of those old computer games."
                    
                    player "Pretty much."
                    
                    lori "I used to love playing those!"
                    lori "Granted, I didn't have many games when I was younger so I had to make the most of the ones I could get."
                    lori "Some of those puzzles were really obtuse and I think that permanently affected how I approach problem solving."
                    
                    player "I'll come to you if I ever get stuck on a quest then."
                    
                    lori "Hehehe sure!"
            
            
        "Stay off to the side":
            $ mature = mature + 1
            
            player "I'll just stay over here, thank you very much."
            
            "Lori shrugs."
            
            lori "Suit yourself!"
            lori "What if there's a piece of metal hanging off a train and hits you though?"
            
            player "Does that happen??"
            
            "You take a step backward and look around for any oncoming trains."
            
            lori "Hehehehe! It's not gonna happen. Trains have to go through tunnels and pass other trains so they can't just have random stuff hanging off the sides."
            
            player "That's reassuring... but I'm still staying away just in case."
            
            lori "Maybe a train will come soon and you'll see how safe it is between the tracks..."
            lori "Or you'll see my mangled bloody body after being dragged a couple hundred feet."
            lori "Hehehehe!"
            
            player "Hahaha yeah..."
            player "Wait, that's not funny!"
            
            lori "It made you laugh though."
            
            player "Only because you laughed!"
            
            lori "Well I thought it was funny."
            
            #player "Country people sure have an odd sense of humor."
            player "You sure have an odd sense of humor."
            
            #lori "Do I? Sorry it's not normie humor."
            lori "Sorry... *huff huff*"
            
            player "It's cool. You're cool."
            
            lori "Really???"
            
            player "What?"
            
            lori "You said I'm cool?"
            
            player "Uhh, yeah? You're a lot more interesting than the people I knew back in the city."
            
            lori "Wow. I thought I was kinda boring."
            
            player "If anything I'm the boring one here. Too scared to even sit between the tracks."
            
            lori "Scary things are fun. I like being scared."
            lori "This doesn't scare me anymore but it did when I started doing it."
            lori "Which is kinda why I wanted to do it in the first place."
            
            player "I guess I can kinda see the appeal. Like watching a horror movie or riding a roller coaster."
            
            lori "Hehehe exactly!! I love those too!"
            
            #player ""
    
    hide lori with dissolve
    
    "You hang out with Lori for a while until the sun starts to go down."
    "No trains came by, which Lori noted was odd but happens sometimes."
    "She seemed disappointed by that, but said she was glad to have some company while she waited."
    
    return

label townGerm1:
    $ townEventsDay.remove("townGerm1")
    ####to be added in a future version
    #$ townEventsDay.append("townGerm2")

    #day exclusive
    
    "You venture west toward the outskirts of town. There lies a barren parking lot next to a large abandoned building."
    "In the distance you can make out a silhouette of a bird fellow in against the sun. As you get closer you can see him petting stray cats."
    "As you creep forward, your foot accidentally sends one of the empty cat food tins flying. It makes a loud clattering sound when it hits the asphalt."
    "The cats scatter in all directions and the figure turns to you."
    
    show germ neutral at center with dissolve
    
    germ "..."
    
    if metGerm == True:
        player "Oh hey... Germ, right? These your cats?"
        
        germ "Nah."
        germ "But I look after them."
        
        #player "That's nice of you."
        
        #germ "I guess."
        
        "One of them brushes against Germ's leg and glares at you."
        "You crouch down and hold your hand out but it doesn't come any closer."
        
        #player "Good kitty?"
        
        #germ "They're curious about you but don't trust you."
        germ "You gotta feed them to gain their trust."
        
        player "Oh."
        
        germ "Bring food next time if you want to befriend them."
        
        hide germ with dissolve
        
        "Germ begins to walk towards a bicycle resting against a lamp post. There's a plastic bag hanging from one of the handle bars that appears to be full of more cat food."
        
        player "Er, see you later I guess?"
        
        "He either didn't hear you or purposely ignores you as he hops on the bike and rides away."
        
        
    else:
        player "Sorry, I didn't mean to scare you all. These your cats?"
    
        germ "Nah."
        germ "But I look after them."
        
        player "There sure are a lot of them here."
        
        germ "Yeah."
        
        player "..."
        
        germ "..."
        
        player "Do they have names?"
        
        germ "Nope."
        
        "A cat approaches and brushes against the stranger's leg while glaring at you."
        
        #player "That's nice of you."
        
        #germ "I guess."
        
        "You crouch down and hold your hand out but it doesn't come any closer."
        
        #player "Good kitty?"
        
        #germ "They're curious about you but don't trust you."
        germ "You gotta feed them to gain their trust."
        
        player "Oh."
        
        hide germ with dissolve
        
        "The mysterious bird begins to walk towards a bicycle resting against a lamp post. There's a plastic bag hanging from one of the handle bars that appears to be full of more cat food."
        
        player "Er, see you later I guess?"
        
        "He either didn't hear you or purposely ignores you as he hops on the bike and rides away."
    
    
    
    $ metGerm = True
    
    return
    
label townAngus1:
    #day exclusive
    
    #if you've met angus already, he is alreaded sitting there
    #if you haven't met angus, he comes up after you sit down
    
    $ townEventsDay.remove("townAngus1")
    ####to be added in a future version, also to need to be on week 2+
    #$ townEventsDay.append("townAngus2")
    
    scene bg roads_day with dissolve
    
    if metAngus == True:
        "As you wander through main street, you eyes are drawn to a statue standing atop a tall pillar. It appears to be a war monument."
        "While you're reading the plaque, a you hear a familiar voice. You turn and are greeted by the bakery bear."
        
        show angus neutral at center with dissolve
        
        angus "Hello there. It's nice to see you again."
        
        player "Ah, it's you. Mind if I sit with you?"
        
        angus "Not at all."
        
        "You brush aside the snow that's accumulated on the bench and sit next to the baker."
        
        angus "What brings you here today?"
        
        player "Thought I might hop back into the bakery but it's closed."
        
        angus "Haha sorry about that! It's just me working there and I need to take breaks from time to time."
        angus "I like to come out here and feed the squirrels around this time every day. They've grown to expect me."
        
        "Angus pulls some bread from a paper bag. The crinkling sound attracts the attention of several nearby squirrels and they come running over."
        "He tears off small pieces of bread and the squirrels either wait patiently for him to toss them or snatch it directly out of his claws."
        
        menu:
            "Did you train them to do that?":
                player "Whoa I've never had a squirrel come so close to me. Did you train them to do that?"
            
                angus "Not really, they sort of trained themselves."
                angus "Animals will do anything for food."
                
                #player "So will I."
                
            "Do they ever bite you?":
                "You flinch as a squirrel skitters across your lap toward the bread."
                
                player "Whoa! Do they bite?"
                
                angus "No?"
                angus "Not yet at least."
                angus "They like to grab their food with their tiny hands before nibbling on it."
                #angus "Thankfully they haven't bitten me yet. I hear they have a pretty nasty bite. Those teeth are made to crack walnuts after all."
                
                "You shudder at the thought of being bitten by those walnut cracking teeth."
        
        "Angus offers the loaf of bread to you."
        
        angus "You wanna try?"
        
        "Might as well see what the fuss is all about."
        "You take hold of the loaf and tear off a bit. The squirrels are more apprehensive towards you but seem eager for more bread."
        "You toss it onto the snow and a few of them gather around it until one takes it and hops away."
        "You watch him gnaw on it as you rip another piece and start the process over again."
        
        player "I have to admit, they are pretty cute."
        
        angus "They can get fierce when they fight. They usually play nice though as long as there's enough food."
        #I usually bring enough food for all of them though."
        
        "You tear off pieces of bread and distribute them until there's none left and the squirrels disperse."
        
        player "Well, that was fun while it lasted."
        
        angus "Indeed."
        
        "Angus stands up."
        
        angus "I should get back to work now but you're more than welcome to join me in feeding the squirrels anytime."
        
        player "For sure. I think I'll sit here and watch them a bit longer. See you around!"
        
        angus "Later!"
        
        hide angus with dissolve
        
        "You hang around for a few minutes before getting up and moving along with your day."
        
        
        #angus "Haha they get impatient if I'm late to feed them. "
        #angus "I like to view them as my friends."
        
        #angus "it gets hot and stuffy in the bakery"
    
    else:
        #have not met angus before
        
        "Walking along main street, you decide to sit on a bench for a quick rest. You push aside the snow and take a seat next to some kind of old war monument."
        "Distracted watching squirrels burying nuts in the snow, you don't notice when somebody approaches."
        
        show angus neutral with dissolve
        
        angus "Oh sorry, is this spot taken?"
        
        player "No no, I'm just sitting by myself. I can move if you want."
        
        angus "It's fine. I usually come here to feed the squirrels around this time of day. They've come to expect me."
        
        "The bear sits beside you and the squirrels gather around as he pulls a loaf of bread out from a paper bag."
        "You watch as he tears chunks from it and tosses them to the little critters."
        
        player "This your hobby or something?"
        
        angus "Not exactly. I work at the bakery so I often end up with stale bread. Not that these guys seem to mind."
        
        "One brave squirrel comes up and snatches the bread piece out of his paw."
        
        menu:
            "Did you train them to do that?":
                player "Whoa I've never had a squirrel come so close to me. Did you train them to do that?"
            
                angus "Not really, they sort of trained themselves."
                angus "Animals will do anything for food."
                
                #player "So will I."
                
            "Do they ever bite you?":
                "You flinch as a squirrel skitters across your lap toward the bread."
                
                player "Whoa! Do they bite?"
                
                angus "No?"
                angus "Not yet at least."
                angus "They like to grab their food with their tiny hands before nibbling on it."
                #angus "Thankfully they haven't bitten me yet. I hear they have a pretty nasty bite. Those teeth are made to crack walnuts after all."
                
                "You shudder at the thought of being bitten by those walnut cracking teeth."
                
        "He offers the loaf of bread to you."
        
        angus "You wanna try?"
        
        "Might as well see what the fuss is all about."
        "You take hold of the loaf and tear off a bit. The squirrels are more apprehensive towards you but seem eager for more bread."
        "You toss it onto the snow and a few of them gather around it until one takes it and hops away."
        "You watch him gnaw on it as you rip another piece and start the process over again."
        
        player "I have to admit, they are pretty cute."
        
        angus "They can get fierce when they fight. They usually play nice though as long as there's enough food."
        #I usually bring enough food for all of them though."
        
        "You tear off pieces of bread and distribute them until there's none left and the squirrels disperse."
        
        player "Well, that was fun while it lasted."
        
        angus "Indeed."
        angus "I'm Angus by the way. Are you new in town?"
        
        player "I'm [name]. And yeah, I just moved here."
        
        angus "In that case, welcome to Possum Springs! It's a small town but there's always stuff to do if you look hard enough."
        
        player "Like feeding squirrels?"
        
        angus "Like feeding squirrels!"
        
        "Angus stands up."
        
        angus "I'd love to stay and chat more but I need to get back to work."
        
        player "Fair enough. It was nice meeting you."
        
        angus "Same! You should stop by the bakery sometime. We've got more than just squirrel food."
        
        player "For sure! I was planning on checking it out anyway."
        
        angus "I'll have it open in just a few minutes if you wanna come in!"
        
        player "Cool, I'll just chill here until then."
        
        angus "See you soon!"
        
        player "Later!"
        
        hide angus with dissolve
        
        "You hang around for a few minutes before getting up and moving along with your day."
        
        
    $ metAngus = True

    return
    
label townRooftops1:
    #"scene where you see Lori and Mae running along the rooftops and mae drops her wallet."
    #"set timer for when you've acquired the wallet and later do a check if it hasn't been too long. Something like if currentDay - dayFoundWallet > 15"
    
    $ townEventsDay.remove("townRooftops1")
    ####to be added in a later version
    #$ townEventsDay.append("townRooftops2")
    $ dayWalletFound = currentDay
    
    scene bg roads_day
    
    "You take a stroll through main street, doing some window shopping and trying not to slip on frozen sections of sidewalk."
    "Strangely you keep hearing giggling but can't make out where it's coming from until a pile of snow falls on your head."
    "Above you are two kids prancing around on the rooftops, leaping from building to building."
    "\'Tag, you're it!'\ one of them shouts after catching up to the other."
    "\'Not for long!\' her friend replies and begins chasing after her."
    "By chance something falls from her pocket right in front of you. You pick it up and call out."
    
    player "Hey! You dropped your..."
    
    "Seemingly unaware of your presence, they run along a rooftop out of your sight but you can still hear their laughs and hollars bouncing off the brick walls."
    
    player "...wallet."
    
    "No way you'll be able to catch up to them now."
    
    menu:
        "Finder's keepers":
            "You open the wallet hoping to find some cash but the money pocket is empty. Even the debit cards are expired."
            "Well, this is no use to you."
            "Or anyone else for that matter."
            "You're tempted to just throw it away but you might as well see if you can return it and get some good karma."
            "You pull an ID card from a pouch and read the name."
        "Check ID":
            "Your first thought is to check if there's an ID card inside. If there is, it should help you track down the owner and return their wallet."
            "You flip through the cards in various pouches until you find the one."
            
    "Margaret Borowski...?"
    
    if metMae == True:        
        "You recognize the cat in the photo, it's Mae!"
        "Good god she's lost a lot of weight since this shot was taken."
        
    else:
        "According to the birth date listed, she's 25!"
        
    "Guess it wasn't kids playing tag up there, it was a couple of fully grown adults!"
    "You wonder who the other one was. You didn't get a good look at either of them."
    "Nevertheless, there's an address printed on the card for you to go and return this to... whenever you have a moment of course."

    return


label townBridge1:
    #day only (for now? night scene later?)
    $ townEventsDay.remove("townBridge1")
    #$ townEventsNight.remove("townBridge1")
    $ townEventsDay.append("townBridge2")
    #$ townEventsNight.append("townBridge2")
    
    "You continue walking until the buildings of downtown give way to smaller residences, and beyond that, sparse trees."
    "Cotton-like snowflakes fall infrequently around you, drifting so slowly it feels like time is coming to a gradual halt."
    "Before long, it's just you, the main road and the woods. The trees aren't so sparse anymore."
    "The air is cold, and a chill mist lowers visibility slightly within the denser patches of trees."
    "As you pass through the barren landscape, you reflect on the recent changes to your life. The folks you've met seem… eccentric, but friendly enough."
    "But it's been refreshing to meet new people and change up your life a bit. Possum Springs is an entirely new flavour of existence, though you still aren't sure what the future holds, or even what you want it to hold."
    "The melancholy reflection ends as you realise that you can't even see a building in any direction anymore, only the grasping grey trees are left to detail the landscape."
    "Since you're walking on a road, and there isn't really a danger of getting lost, you forge ahead."
    "Being used to city life, it's strange not seeing a convenience store every hundred steps or so. There aren't even any streetlights!"
    "Just as you start feeling like nothing interesting will ever show up, you come upon a small steel bridge over what can only be described as a large ditch."
    "You vaguely remember crossing it on your way into town, may as well check it out while you're here."
    "The bridge is constructed of large, solid metal girders, and painted a dull red. The paint is peeling, showing several layers of paint underneath and revealing bare metal in places."
    "Rust weeps in long, thin strands from the bolts and fasteners holding the steel construction together, and there's as much graffiti as you'd expect."

    "Class of 14"

    "Class of 09"

    "Danny is a azz"

    "Seems like people come here semi-regularly to dick around at least, nobody is here at the moment though."
    "You exhale towards the sky, your breath condensing and floating up and away towards the clouds before you stuff your hands in your pockets and look at the pavement."
    "Huh. You didn't notice before, but there are footprints leading from the edge of the ravine to the center of the bridge before stopping at the handrail and doubling back."
    "Curiously, snow is cleared off the handrail and you can see boot prints ON TOP OF the rail."
    "Damn, that's hardcore. It's not a very deep ravine but a fall like that would still likely kill you."
    "At least the boot prints lead back the way they came so you know whatever crazy bad-ass came out here to do that didn't fall. It was probably one of those hooligan children from town, with no sense of self-preservation."
    "You can't believe someone would actually risk their life for fun like that. No way you'd do that. No matter how cool that is."

    menu:
        "Fuck it we ball":
            $ bold = bold + 1
            $ chaotic = chaotic + 1
            $ railingclimb = True

            "In a moment of manic carelessness, you put one hand on the girder and hoist yourself shakily up onto the railing."
            "The world tilts around you with vertigo, but for a split second, you are flooded with a powerful feeling of freedom and elation."
            "Your life is in your own hands!"
            "Then you slip and almost fall."
            "You windmill your arms for a frantic moment before regaining your tenuous balance."
            "Holy shit."
            "You step off the railing and catch your breath. Fuck."
            "Well it was cool for a second."


        "Pussy out":
            "Yeah you'd definitely slip and die, nobody would find your broken corpse at the bottom of the ditch for days, if not weeks. Maybe months."
            "You wonder if anyone would actually miss you if you did fall."
            "The thought depresses you."

    "Well, that's enough for today. Probably time to head back."

    "It couldn't hurt to return every so often, you might meet the railing daredevil at some point if you do."
    "But for now, your fingers are cold and your nose is freezing, better to keep walking and stay warm than stand here and freeze until the sun goes down, then you'd really be in trouble."

    "There aren't any... Wolves or something around here, are there?"

    "You quicken your pace and get back to town, mercifully without being mauled."
    
    
    return
    
    
label townTrolley1:
    #day or night
    "You descend the stairway into what appears to be an underground trolley station."
    "It's like the small town version of the metro."
    "not sure what to put here. maybe talking with a minor character"
    
    return
    
    
label continue:
    #continues to next scene
    #keep this at the end of file
    "continuing..."