#more labels

label houseOffice:
    "while searching the house you find a room you've never been in before, the office. You were never allowed in here."
    $ officeQuestStarted = True
    
    jump afterExploringHouse

label houseShed:
    "After searching the house, you come across a rickety looking shed outside."
    #must have been built after the last time you visted
    "Pushing the snow out of the way, you find the door is locked."
    if hasKey == True:
        "You recall you found a key earlier that looks like it might fit the lock."
        "You run inside to retrieve it, but it's so rusted it snaps off inside the lock. Damn!"
        $ doorStuck = True
    else:
        "Maybe there's a key somewhere inside. Or maybe you'll have to find... alternative methods of entry."
    $ bikeQuestStarted = True
    
    jump afterExploringHouse
    
label houseBook:
    "You decide to explore your home some more. You don't find a wrench but you do find an overdue library book"
    "You should return it to the library."
    $ libraryQuestStarted = True
    
    jump afterExploringHouse

label houseKey:
    "What's this? You find a rusty key in a dusty crevice behind some spider webs."
    "You wonder what it's for."
    
    jump afterExploringHouse
    
label afterExploringHouse:
    "You spent a few hours and have yet to find a wrench to open that grate. At this rate, it'll be dark by the time you figure something out."
    "Your next best option is to see if there's a hardware store in town."
    
    jump intoTown
    



label intoTown:
    "You put on a jacket and boots and make your way towards the center of the town."
            
    scene bg towncenter
    
    #"You try to follow the map but without GPS "
    #"Without GPS you get a bit lost but eventually stumble upon what must be the main street."
    "blah blah blah general description of the surroundings. i think the statue is between the shops?"

    "That looks like the hardware store over there, but the aroma from the nearby bakery draws you in."
    
    menu:
        "{cps=0}Where will you go first?{/cps}"
        "bear essentials":
            jump meetingAngus
            #gregg mentions he's on a long lunch break since it's a slow day, but that he is still clocked in  
            #if you visit 1st time after visitng pickaxe, you order 2 coffees
        
        "ol pickaxe":
            jump meetingBea
                            
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