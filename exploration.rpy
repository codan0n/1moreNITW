#more labels

label unexploredHouse:
    #give a general description of the house to set the mood
    "The eerie emptiness of the house unsettles you as you look around."
    "A desolate building, untouched for years. Dust has piled up on every surface and cobwebs spill from the ceiling, but everything is otherwise so tidy and neat."
    "It really is a tomb."
    "Your memories conflict with the current reality."
    "The guest room you slept in is exactly like you remember it but the kitchen got all new tile and a fresh coat of paint."
    "There are a lot more bookshelves than you recall. Was that table always there in the den?"
    #"A whirlwind of confusion and conflicting emotions makes your search for tools more difficult. You're not sure where to look. You've never even been in half the rooms."
    
    #jump continue
    
    return

label houseOffice:
    # day or night
    $ officeQuestStarted = True
    
    scene bg home_office_day with fade

    "While searching the house you stumble upon an unfamiliar room: the office. You were never allowed in here."
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
    #daytime exclusive
    "After searching the house, you happen to notice something unusual through one of the windows: a rickety looking shed standing in the backyard, half buried under the snow."
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
    
    #the book contains part of the password?
    "You checked various nooks, crannies, shelves, drawers, and boxes but found nothing of note."
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
    
    $ libraryQuestStarted = True
    
    return

label houseKey:
    #day or night
    $ hasKey = True
    
    "Your search brings you to a spare bathroom where the sound of water dripping disturbs the otherwise still area every few seconds."
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
    
label afterLookingForTool:
    "You spent a few hours searching and have yet to find a tool to open that grate. At this rate, it'll be dark by the time you figure something out."
    "For all you know, there might not even be a wrench in this house anymore."
    "Your next best option is to see if the hardware store in town has what you need."
    
    jump intoTown
    


label intoTown:
    "You put on a jacket and boots and make your way towards the center of the town."
            
    scene bg roads_day
    
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
    
    
label townGerm1:
    #day exclusive
    
    "You go west toward the outskirts of town. There lies a barren parking lot next to an large abandoned building."
    "In the distance you can make out a figure. As you get closer you can see he's petting stray cats."
    "There are tins of cat food strewn about. You accidentally kick one, making a loud clattering sound."
    "The cats scatter and the figure looks to you."
    
    show germ neutral at center with dissolve
    
    germ "..."
    
    #if metGerm == True:
    
    #else:
    
    return
    
label townAngus1:
    #day exclusive
    
    "Walking along main street, you decide to sit on a bench for a rest. You push aside the snow and take a seat next to a statue commemorating old soldiers."
    
    show angus at center with dissolve
    
    #if met == True:
    
    #else:
    
    angus "Oh sorry, is this spot taken?"
    angus "I usually come here to feed the squirrels around this time. They've come to expect me."
    
    $ metAngus = True

    return


label townBridge1:
    #day or night
    "You visit the bridge to the east of town."
    
    
    
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