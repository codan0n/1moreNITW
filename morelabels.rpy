#more labels

label unexploredHouse:
    #give a general description of the house to set the mood
    "The eerie emptiness of the house unsettles you as you look around."
    "A desolate building, untouched for who knows how long."
    "Dust has piled up on every surface and cobwebs spill from the ceiling, but everything is otherwise so tidy and neat."
    "It really is a tomb."
    "Your memories conflict with the current reality."
    "The room you slept in is exactly like you remember it. The kitchen got all new tile. Was that table always there in the den?"
    "A whirlwind of confusion and conflicting emotions makes your search for tools more difficult. You're not sure where to look. You've never even been in half the rooms."
    
    #jump continue
    
    return

label houseOffice:
    $ officeQuestStarted = True
    
    scene bg home_office_day with fade

    "While searching the house you stumble upon an unfamiliar room, the office. You were never allowed in here."
    "Books and binders are scattered along the shelves. Some of them look so old they'll fall apart if you picked them up."
    "A desk sits on the far end of the room with a computer on top of it. You wonder if it still runs."
    "But first you take a moment to play with the dial on the wall safe. You have no idea what the code might be but predictably you don't happen to guess it on your first try."
    "Heck."
    "There's probably some good loot in there too... Maybe there's a local locksmith who can crack it open."
    "You take a seat in the swivelling chair and press the power button. The whirring of fans and disk drives fills the room for a few seconds before the monitor wakes up."
    "Immediately it asks for a password before even booting into the operating system. You try typing in a few common passwords but it won't let you in."
    "What a shame. This thing may be old but it could probably run some games."
    #"There must be a way to bypass this..."
    "There must be a way to bypass this... but you'd probably need someone to walk you through it so you don't break it."
    "You hold the power button to shut it off and slump in your seat. The photo frame next to the monitor catches your attention."
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
    "Inside there's a faded picture of you as a kid. You're holding up a fish you caught and your father is kneeling beside you with a proud look on his face."
    "You vaguely remember when that photo was taken. It was in early spring, when all the leaves were bright green."
    "You got up early and spent the whole day fishing, just you and your dad. Then when the sun started going down you sat on the bank and fed the fish with the remainder of your bait."
    "Simpler times, those were. Your parents were still together back then."
    "It's hard to think of the fact that he's been missing for five years."
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
    
    
    
    
    
    
    jump afterExploringHouse

label houseShed:
    "After searching the house, you come across a rickety looking shed in the back yard, half buried under the snow."
    "You don't recall there ever being a shed. It must have been built after the last time you visted."
    "After digging through the snow to reach the door handle, you realize that it's locked up tight with a chain and padlock."
    if hasKey == True:
        "You recall you found a key earlier that looks like it might fit the lock."
        "You run inside to retrieve it, but it's so rusted it snaps off inside the lock. Nothing can ever be easy and straightforward, can it?"
        $ doorStuck = True
    else:
        "Maybe there's a key somewhere inside. Otherwise you'll have to find... alternative methods of entry."
    $ bikeQuestStarted = True
    
    jump afterExploringHouse
    
label houseBook:
    #the book contains part of the password?
    "You checked various nooks, crannies, shelves, drawers, and boxes but no wrenches."
    "You did however come across a book with a library sticker on it. Inside there's a slip of paper dated five years ago with your father's name next to it."
    "He must have checked out this book shortly before vanishing. Maybe he skipped town to avoid the late fee?"
    "Haha..."
    "Okay, comedy isn't making you feel better."
    "You should probably return this to the library though. They've probably been missing it."
    
    $ libraryQuestStarted = True
    
    jump afterExploringHouse

label houseKey:
    "What's this? You find a rusty key in a dusty crevice behind some spider webs."
    "You wonder what it's for."
    
    
    jump afterExploringHouse
    
label afterExploringHouse:
    "You spent a few hours searching and have yet to find a wrench to open that grate. At this rate, it'll be dark by the time you figure something out."
    #for all you know, there might not even be a wrench in this house
    "Your next best option is to see if there's a hardware store in town."
    
    jump intoTown
    


label intoTown:
    "You put on a jacket and boots and make your way towards the center of the town."
            
    scene bg towncenter
    
    #"You try to follow the map but without GPS "
    #"Without GPS you get a bit lost but eventually stumble upon what must be the main street."
    "blah blah blah general description of the surroundings."
    #i think the memorial statue is between the shops?

    "That looks like the hardware store over there, but the aroma from the nearby bakery draws you in."
    "Where will you go?"
    
    menu:
        "{cps=0}Where will you go?{/cps}"
        "Bakery":
            jump meetingAngus
            #gregg mentions he's on a long lunch break since it's a slow day, but that he is still clocked in  
            #if you visit 1st time after visitng pickaxe, you order 2 coffees
        
        "Hardware store":
            jump meetingBea
                            
            #what about pliers?
            #maybe need to make the bolt an allen screw
            #where do i know her (mae) from? :flashback:
            #if you didn't explore the house in the morning, you automatically do it at night after fixing the heater
        
        #"underground":
            #minor event
        
        #"rooftops":
            #minor event
            
            
label midday:
    "It'll get dark in a couple hours. Is there anything else you want to do today?"
    
    jump continue
    
label continue:
    #continues to next scene
    #keep this at the end of file
    "continuing..."