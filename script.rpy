# This is the main script called upon when a new game is selected

# Define characters
define mae = Character("Mae", color="#ff3f54")
define bea = Character("Bea", color="#4f7175")
define gregg = Character("Gregg", color="#e8971a")
define angus = Character("Angus", color="#6fbc92")
define lori = Character("Lori", color="#c1e0fc")
define germ = Character("Germ", color="#a384e5")
define selma = Character("Selmers", color="#d15384")
define narrator = Character("")
define player = Character("Wayfarer")
define candy = Character("Candy")
define stan = Character("Stan")
define name = Character("Avery")
define cafebird = Character("Trish")
define driver = Character("Driver")
define loriunknown = Character("???", color="#c1e0fc")
define maeunknown = Character("???", color="#ff3f54")
define selmaunknown = Character("???", color="#d15384")
define trishunknown = Character("???")
define trish = Character("Trish")
define greggunknown = Character("???", color="#e8971a")
define beaunknown = Character("???", color="#4f7175")
define angusunknown = Character("???", color="#6fbc92")
define harleyunknown = Character("???")
define harley = Character("Harley")
define receptionist = Character("???")
define marcie = Character("Marcie")
define kid = Character("Kid")
define cashier = Character("Cashier")
define pa = Character("PA")
define raccoon = Character("Raccoon")
define danny = Character("Danny")
define citycouncil1 = Character("City Council 1")
define citycouncil2 = Character("City Council 2")
define citycouncil3 = Character("City Council 3")
define citycouncil4 = Character("City Council 4")
define saleem = Character("Saleem")
define sadie = Character("Sadie")
define man = Character("Man")
define madamespectre = Character("Madame Spectre")


label start:

    # variables and definitions

    $ currentDate = "December 1"
    $ currentDay = 1
    $ gender = ""

    # keeps track of how much the characters like the player (AP = affinity points)
    $ maeAP = 0
    $ beaAP = 0
    $ greggAP = 0
    $ angusAP = 0
    $ loriAP = 0
    $ selmaAP = 0
    $ germAP = 0

    # personality values. they correspond to defining traits of each character and act as a secondary way to appeal to them. unlocks some dialogue options.
    #lori
    $ introverted = 0

    #gregg
    $ bold = 0
    
    #germ
    $ sympathetic = 0
    
    #bea
    $ cynical = 0
    
    #mae
    $ chaotic = 0
    
    #angus
    $ gentle = 0
    
    #selma
    $ mature = 0

    # scene specific variables
    $ beenToChurch = False
    $ chosendrink = ""
    $ wentWithGregg = ""
    $ confectionChoice = "treat"
    $ loriInteractionRude = False
    $ loriInteractionNull = False
    $ loriInteractionBold = False
    $ loriInteractionNotBold = False
    $ loriInteractionNeutral = False
    $ firstWander = True
    $ audiencepoet = ""
    $ selmaNeutral = False
    $ selmaGood = False
    $ selmaBad = False

    # Scene completion status (as in, has the player experienced this scene on their playthrough)
    $ beaSelmaPoetryCompleted = False
    $ maeLoriSleepoverCompleted = False
    $ maeChurch1Completed = False
    $ maeLoriSleepoverCompleted = False
    $ beaAntiqueCompleted = False
    $ workingWithBeaCompleted = False
    $ angusTownCompleted = False
    $ greggTownCompleted = False
    $ selmaLibraryReadingCompleted = False
    $ loriFilmCompleted = False
    $ dragonsDungeons1Completed = False
    $ artsCouncilCompleted = False

    # note: if you want to quickly test a scene, put "jump [sceneName]" right below this line



    ####################
    
    # Start day 1 (technically 2nd day in possum springs, you arrived the night of nov 29)
    #november 30 2022 (2017 nitw release year + 5 years) (wednesday)

    #scene bg black with fade

    #play music "music/americano_loop.mp3" fadein 1.0
    #add walking in snow sound effect
    
    #"This must be the place."
    #"You could smell the roasted coffee beans from a few blocks away."

    scene bg cafe with dissolve

    play sound "sound/storebell.mp3"
    
    ###to do: mention lack of internet at home and bad cell service

    #"Finally, you made it."
    #"A bell on the door chimes as you walk into a cozy little cafe."
    #"The sign on the door read:\nPosspresso\nEST. 2020"
    #"The smell of roasted coffee beans guided you here from a couple blocks away."
    #""
    "Finally."
    "You were starting to think you'd never make it, but the smell of roasted coffee beans pointed you in the right direction."
    #"You were starting to think you'd never make it, but the smell of roasted coffee beans helped you find the right place."
    #"You could smell the roasted coffee beans from a few blocks away."
    "You brush the snow off your jacket and take a moment to bask in the warmth of the cafe you just stepped into."
    "The distance you travelled to get here, along with the frigid weather have left you drained of energy."
    "What better place to rest and warm up than a coffee shop?"
    "Posspresso... It's no chain you've ever heard of. Your home city had no shortage of local restaurants but this small town cafe is as authentic as it gets."
    "While fairly clean and new looking, the place has a rustic country charm to it."
    "No overly dramatic lighting, no artificially weathered hardwood, no hipster whiskers, no cheesy messages about coffee being the most important thing in life."
    #"The chairs look like leftovers from whatever this place used to be, the out-of-place picnic table is covered in knife etchings new and old, the walls are adorned with bad painting that must come from the locals."
    "Rather, Posspresso has mastered the art of furnishing on a budget."
    "The chairs look like leftovers from whatever this place used to be, with the fake leather cushions being cracked and torn in a few places."
    "You'd bet that picnic table was rescued from being sent to a landfill. As you pass by it, you can make out knife etchings both new and old."
    #"one of them is from the 1970s"
    "One would be wise to check for rusty nails before trying to sit on it."
    #"The picnic table in the center takes up a bit too much room"
    #"the out-of-place picnic table is covered in knife etchings new and old, the walls are adorned with bad painting that must have been made by the locals."
    "The local artists' amateur paintings and cheap grandma tier wallpaper really brings it all together."
    #nuke possum springs carved into table
    "Soul."
    #"This must be what they refer to as 'soul.'"
    #quaint and unassuming
    #"This quaint local "
    #finally a modern cafe in possum springs!
    #"It's the only one in Possum Springs if that map you got from the bus station is to be believed."
    #running joke about how every door in possum springs has a bell, even people's residences surprisingly ("it's just for the holidays. it's festive!")
    #"Hardwood flooring, homely wallpaper, a chalkboard menu, the works."
    #"Crude paintings adorn the walls, no doubt bought on the cheap from local artists."
    #"You wonder how the hell they fit that giant picnic table through the door."
    #"There's even a large picnic table occupies the center of the room."
    #"How did they even fit that through the door, you wonder?"
    "Behind the counter, a young bird lady with brick red feathers smiles and waves at you."

    show trish neutral at right with dissolve

    trishunknown "Hi there, welcome to Posspresso! I'll be with you in just a minute!"
    
    #hide trish with dissolve

    "She's busy helping another customer at the moment, giving you time to look over the menu."
    #"There's a variety of breakfast-y food and drinks to choose from as well as some sweets."

    #show trish neutral at right
    show selma neutral at left:
        xzoom -1
    with dissolve
    
    selmaunknown "Crazy snow we're havin' today, huh?"
    
    trishunknown "I know right! Perfect day for a hot drink though!"
    #trishunknown "Perfect day for a coffee!"

    #selmaunknown "I'll drink to that"
    selmaunknown "For real."
    selmaunknown "Hmm, I'm feelin' a salted caramel mocha today."

    trishunknown "Ya want whipped cream on top?"

    selmaunknown "Hell yeah."

    trishunknown "Hahaha will that be all for you, Selmers?"

    #selma "Throw in a cinnamon roll too please."
    selma "Throw in a strawberry waffle too please."
    
    trishunknown "Alright, that'll be... seven dollars and eighty five cents!"

    #trishunknown "Alright, that'll be... six dollars and sixy six cents!"
    
    #selma "What a lucky number..."
    
    #trishunknown "Hahaha I know, right? Hopefully it's not like a bad omen or something!"

    "The bear pulls a crumpled $10 bill out of her pocket and slides it over."

    selma "Keep the change."

    trishunknown "Thank you very much!"

    hide selma with dissolve
    
    show trish neutral at center with move

    "The bear steps aside and the barista looks over to you."

    trishunknown "Ain't seen you around before!"
    trish "Welcome to Posspresso! You can call me Trish!"
    trish "Have you decided what you'd like?"

    menu:
        "{cps=0}I'll have uh...{/cps}"
        "What she had":
            $ selmaAP = selmaAP + 1
            $ chosendrink = "mocha"
            "Not sure what else to get, you just order the same thing the previous customer got."
        
        "Posspresso Special":
        #surprise me
            $ bold = bold + 1
            $ chosendrink = "posspressospecial"
            "You order the Posspresso Special. There's no description for it, but you wanted to try something new and local."
            "You also get an everything bagel with cream cheese to go along with it."

        "Americano":
            $ cynical = cynical + 1
            $ chosendrink = "americano"
            "You order an americano and a blueberry bagel with honey butter spread to go along with it."
            "Gotta have something sweet to balance out the bitterness."

        "You're not sure...":
            $ introverted = introverted + 1
            $ chosendrink = "cappuccino"
            "You can't really decide."
            "The barista suggests a cappuccino. You go with that and order a chocolate chip waffle on the side."

    trish "Oki doki!"

    "The barista taps on her tablet a few times and reads out your total."
    "Seeing that you've got your debit card ready, she turns the machine around to you. You swipe your card and hit confirm."
    "It asks if you would like to give a tip."
    
    menu:
        "{cps=0}It asks if you would like to give a tip.{/cps}"
        "15\%":
            $ sympathetic = sympathetic + 1
            "A standard tip for standard service. Gotta pay the \"Please don't spit in my coffee\" tax."
        
        "30\%":
            $ gentle = gentle + 1
            "Eff it, you're feeling generous today. Maybe she'll throw in an extra shot of espresso for you too."
        
        "No tip":
            $ chaotic = chaotic + 1
            "The barista is just doing what's expected of her job, right? It's her employer's responsibility to pay her, not you."
            "Right?"

    trish "And can I get a name for you?"

    $ povnameValid = False
    $ player = Character("[name]")
    jump namescript1
    label namescript1:

        python:
            name = renpy.input("Oh shoot, what's your name again?", length = 14)
            name = name.strip()
            povnameValid = True
            # prevents the player from naming themselves certain names and names them Avery if nothing is input
            if name.upper() == "MAE":
                "Choose another name."
                povnameValid = False
            if name.upper() == "MARGARET":
                "Choose another name."
                povnameValid = False
            if name.upper() == "BEA":
                "Choose another name."
                povnameValid = False
            if name.upper() == "BEATRICE":
                "Choose another name."
                povnameValid = False
            if name.upper() == "GREGG":
                "Choose another name."
                povnameValid = False
            if name.upper() == "GREG":
                "Choose another name."
                povnameValid = False
            if name.upper() == "ANGUS":
                "Choose another name."
                povnameValid = False
            if name.upper() == "GERM":
                "Choose another name."
                povnameValid = False
            if name.upper() == "JEREMY":
                "Choose another name."
                povnameValid = False
            if name.upper() == "LORI":
                "Choose another name."
                povnameValid = False
            if name.upper() == "SELMA":
                "Choose another name."
                povnameValid = False
            if name.upper() == "SELMERS":
                "Choose another name."
                povnameValid = False
            if name.upper() == "STAN":
                "Choose another name."
                povnameValid = False
            if name.upper() == "CANDY":
                "Choose another name."
                povnameValid = False
            if name.upper() == "TRISH":
                "Choose another name."
                povnameValid = False
            if name.upper() == "MARCIE":
                "Choose another name."
                povnameValid = False
            if not name:
                #default name in case you don't type anything
                name = "Avery"
                povnameValid = True

        if povnameValid == True:
            "Your name is [name]?"
        else:
            "Choose another name."
            jump namescript1
            "Your name is [name]?"

    menu:
        "{cps=0}Your name is [name]?{/cps}"
        "That's right":
            player "That's right!"
        "That's wrong":
            jump namescript1

    trish "Alright, I'll have that ready for y'all in just a minute!"
    
    player "Thanks."

    hide trish with dissolve

    "You look around for a place to sit. That bear girl already found a table near the wall and plugged a laptop into a power outlet."
    "Taking a seat by a window, you gaze at the blinding white landscape."
    "Winter decided to come early this year. You heard there was a blizzard on its way and but you didn't think it would be this intense."
    #"It's been snowing nonstop since you arrived in Possum Springs last night and your new home was colder than the innermost circle of Hell when you woke up."
    "It's been snowing nonstop since you arrived in Possum Springs last night. You lack a proper windbreaker for this kind of weather but all the walking you've been doing has warmed you well enough."
    "The town seems ill-prepared as well. You lost count of how many abandoned cars you saw on the way here, stuck in a ditch and buried under a foot of snow."
    "A few people were shovelling snow off the streets but at the rate it's coming down, they need a snow plow and a few metric tons of rock salt."
    #. Most of the roads on the way here weren't plowed and you saw a couple of abandoned cars that had slid into ditches, now buried under a foot of snow."
    "You're lucky Posspresso even decided to open on a day like this."
    "Your eyes come to focus on your reflection in the glass, noticing you still have some snow on your..."
    
    menu:
        "{cps=0}Your eyes come to focus on your reflection in the glass, noticing you still have some snow on your...{/cps}"
        "Scales":
            $ animaltype = "reptile"
            "...scales. Because you're a reptile, of course."
            "Oh god how long have you been walking around with that bit of shed skin stuck to your face? How embarassing."
        "Fur":
            $ animaltype = "mammal"
            "...fur. Because you're a mammal, of course."
            "You pat down a patch of fur that the wind blew out of place but it keeps sticking up."
        "Feathers":
            $ animaltype = "bird"
            "...feathers. Because you're a bird, of course."
            "You try to pat down a few that are sticking up, but they are refusing to cooperate."
            
    #"Guess you should have done a better job grooming yourself this morning, but you really needed to get something to eat ASAP."
    "You look like a wreck."

    menu:
        "{cps=0}You look like a wreck.{/cps}"
        "A masculine wreck":
            $ gender = "masculine"
            $ heshethey = "he"
            $ guygirlperson = "guy"
            $ manladycreature = "man"
            $ hishertheir = "his"
            $ hisherstheirs = "his"
            $ himherthem = "him"
            "Yeah, a real macho manly wreck."
        "A feminine wreck":
            $ gender = "feminine"
            $ guygirlperson = "girl"
            $ heshethey = "she"
            $ manladycreature = "lady"
            $ hishertheir = "her"
            $ hisherstheirs = "hers"
            $ himherthem = "her"
            "A wreck fit for a lady such as yourself."
        "A gender neutral wreck":
            $ gender = "neutral"
            $ guygirlperson = "person"
            $ heshethey = "they"
            $ manladycreature = "one"
            $ hishertheir = "their"
            $ hisherstheirs = "theirs"
            $ himherthem = "them"
            "It's hard to tell where you lie on the gender scale. Just the way you like it."

    "Whew, glad you got that identity crisis out of the way."
    "Now you can focus on more important things like getting online. You look around for the wifi password and type it into your phone."
    "The shoddy cell signal you get in this town can't even stay connected long enough to load a webpage."
    #"The past few days have been really chaotic. It's nice to slow down for a moment and relax."
    
    show trish neutral at right with dissolve
    
    trish "Selmers!"

    #"The barista's voice pulls you out of your flashback, conveniently right as it was about to end anyway."
    #"Now you remember! You were on your way to buy groceries and you stopped by this cafe on the way for breakfast!"
    "The bear waits to finish typing something on her laptop before going up to the counter to collect her drink."

    show selma neutral at left with dissolve:
        xzoom -1

    selma "Thanks!"
    
    trish "Of course!"
    trish "How's the writin' going?"
    
    selma "Eh. Havin' a hard time with this chapter. But I'll figure it out."
    
    trish "You got this!"
    
    selma "Heh. Of course I do."
    
    hide trish
    hide selma
    with dissolve

    "You can't resist taking a glance at her drink as she passes by your table. It looks as good as it smells."
    "It's in a glass mug so you can see the thick chocolaty treat with a layer of froth topped by a generous helping of whipped cream with caramel sauce drizzled upon it."
    #"You eagerly wait for your own drink to be ready."

    #hide selma with dissolve

    "After a while, the barista calls you up to the counter."
    
    show trish neutral at center with dissolve
    
    trish "[name]!"
    trish "Here ya go, hun. Enjoy!"
    
    hide trish with dissolve

    if chosendrink == "posspressospecial":
        #"You walk up to the counter and grab your breakfast"
        "You fetch your bagel and steaming hot beverage from the counter and head back to your seat."
        "The mug contains a dark concoction with a layer of light foam, topped with dark chocolate shavings."
        "You blow on it then take a sip."
        "..."
        #"This is the most bitter thing you've ever tasted."
        "It's a mixture of overwhelming bitterness and sweetness."
        "The flavor is earthy and potent with a burnt chocolate aftertaste."
        "It's an exceptionally strong drink that leaves you wanting more of it."
        "You can't resist taking another satisfying sip before moving on to your bagel."
        "Nothing special here, just an ordinary bagel topped with seeds and herbs with ample cream cheese stuffed between its halves."
    
    elif chosendrink == "americano":
        "You fetch your bagel and steaming hot beverage from the counter and head back to your seat."
        "The mug contains a plain dark brew with a few bubbles on the surface."
        "You blow on it then take a sip."
        "..."
        "So bitter. So good."
        "No fancy flavors required, just a couple shots of espresso and good old fashioned water. The way god intended."
        #"Nothing says \"I hate myself\" more than drinking straight espresso with nothing but a little extra water to make it tolerable."
        #"It's incredibly smooth and gently massages your taste buds with a light, warming flavor."
        "You can't resist taking another satisfying sip before moving on to your bagel."
        "It's full of juicy blueberries and the honey butter spread oozes pure sweetness. Good thing you have a strong drink to wash down this sugar overdose."

    elif chosendrink == "cappuccino":
        "You fetch your waffle and steaming hot beverage from the counter and head back to your seat."
        "The mug contains a gradient of different flavors. A dark espresso mixture on the bottom that turns into a milky white cream the further up you go, topped with a layer of foam."
        "You blow on it then take a sip."
        "..."
        "It gives you two distinct flavors of steamed milk and espresso. One is light and the other is strong, neither overpowering the other."
        "Can't go wrong with a classic drink like this, even if it is kinda plain."
        "You can't resist taking another satisfying sip before moving on to your waffle."
        #"You cut a slice and pop it into your mouth."
        "The sweet chocolate chips combined with the melted butter send your taste buds to heaven with a first class ticket."
    
    elif chosendrink == "mocha":
        "You fetch your waffle and steaming hot beverage from the counter and head back to your seat."
        "The glass mug reveals a light brown mixture with a layer of chocolate on the bottom. Up top is a layer of whipped cream, with a drizzle of caramel and sea salt"
        "You lick away some of the cream then take a sip of the actual drink."
        "..."
        "The salt contrasts with the sugary taste of chocolate and caramel, which balance the bitterness of espresso."
        "All the flavors combine into an exquisite beverage that gives you everything you could want in a drink."
        "You can't resist taking another satisfying sip before moving on to your waffle."
        #"You slice off a chunk and pop it into your mouth."
        "Juicy strawberries are baked right into it, offering a sweet sensation with nearly every bite of the savory buttermilk waffle."

    "Meanwhile, the bear on the other side of the room taps away on her keyboard, her claws making quite a racket."
    "You can hear a lot of frustrated backspacing after she types a long block of text."
    #"You pull out your phone and get up to date on all your internet needs between bites and sips."
    "That reminds you, you're connected to the internet now."
    
    
    #"You couldn't get online at home, so now's the perfect time to get up to date on your internet addiction."
    "You pull out your phone and alternate between poking the screen and devouring your breakfast."
    "It may be a while before you get internet again, so you should download something to keep yourself busy later on."
    
    $ chosenHobby = ""
    
    menu:
        "{cps=0}It may be a while before you get internet again, so you should download something to keep yourself busy later on.{/cps}"
        "Download movies":
            $ chosenHobby = "movies"
            $ loriAP = loriAP + 1 #because she's known for liking movies
            #$ greggAP = greggAP + 1 #because choosing movies over books is something gregg would relate to, idk
            "This will give you something to pass the time. Hopefully the TV at home is modern enough for you to stream from your phone, you don't wanna get stuck watching these on a 5 inch screen."
            "You spend some time curating which movies you're interested in and finding working links."
        
        "Download books":
            $ chosenHobby = "books"
            $ mature = mature + 1
            $ selmaAP = selmaAP + 1
            "Books will last longer than movies and are more enjoyable anyway. Plus you can brag about being an adult who reads, an endangered species in the modern age."
            "You spend some time curating which books you're interested in and finding working links."
            
        "Download music":
            $ chosenHobby = "music"
            $ beaAP = beaAP + 1
            #$ maeAP = maeAP + 1
            "You'd rather not suffer in silence. Even if you've got nothing else to do you can always rock out to something."
            "You spend some time curating which albums you're interested in and finding working links."
    
    "Hours go by and the setting sun reminds you that you still need to go shopping to stock your pantry, preferably before it gets dark."
    
    # It will get dark soon so you better hit the road."
    #"You're in dire need of food to stock your pantry, so you look up a route to the nearest grocery store and memorize it before you're cut off from the internet."
    "You look up a route to the nearest grocery store and memorize it before you're cut off from the internet."
    "The map app says they're open today but you're skeptical. You guess you'll find out when you get there."
    "You rise from your seat and put away your dishes."
    "It seems the bear is still furiously typing away, concentrated on whatever she's writing."
    "You've both been here for a long time. You wonder how much longer she'll stay here."
    "As you're heading out the door, the barista chirps."
    
    show trish neutral at center with dissolve

    trish "Thanks for coming in! Have a nice day!"

    player "You too!"
    
    hide trish with dissolve
    
    "You step out into the snowy landscape and begin your lone march."
    #fade to white
    
    #"Feeling energized from the coffee, you set out on the next leg of your journey."
    "Now that your belly is filled and your veins are pulsating with caffeine, you're ready to set out on the next leg of your journey."
    #"You push away the snow that had accumulated at the door"

    stop music fadeout 2.0

    #scene bg woods_day

    #"Now that you've had your morning coffee, you're in a position to get things done."
    #"Now that your belly is filled and your veins are pulsating with caffeine, you're in a position to get things done."
    #"Next stop: Ham Panther."
    "The nearest store right at the limit of what you'd call walking distance. Better get a move on while there's still daylight."
    #"It's almost noon already judging by the position of the sun. Best hurry if you want to make it home before dark."
    #"Best hurry if you want to make it home before dark. Longest Night is coming up soon, which means you don't have a lot of daylight to work with."
    #Longest Night is in just a few weeks so you don't have much daylight to burn."
    
    scene bg ham_panther with fade

    play music "music/itsadrag_loop.mp3" fadein 1.0

    "Now here's a familiar place. The soulless, sterile, yet gross corporate chain grocery store, Ham Panther."
    "You kick the snow off your boots and venture in. You're just shopping for the basics so you grab a basket and get to work."
    #"Ham Panthers are basically the same everywhere. And man are they everywhere."
    #"Except a couple miles closer to your house apparently."
    "Rice, beans, lentils... The shelves are damn near empty but you manage to get what you need."
    #You pass by some townsfolk whose shopping carts are filled to the brim in response to the storm, though it's mostly junk food.
    "You pass by some townsfolk whose shopping carts are filled to the brim, no doubt in response to the snowstorm."
    "Two of them were arguing so aggressively over the last carton of eggs, you thought you were about to witness a murder."
    "These small towns really are something."
    #"Should you pick up milk as well?"
    "Miraculously there are a few milk jugs left."
    "Which one should you get, almond milk or normal milk?"
    
    menu:
        "{cps=0}Which one should you get, almond milk or normal milk?{/cps}"
        "Almost milk":
            $ sympathetic = sympathetic + 1
            "You'd think packaging the runoff water from washing almonds would be cheaper than raising a cow but somehow it's always the more expensive option."
            "Oh well, at least you've grown accustomed to the taste and it doesn't upset your tummy."
            "Better hope it doesn't freeze on the way home and make the container explode."
            "Moving on, you pass by the deli counter. You weren't really planning on getting anything from it but the jolly old man behind the counter calls out to you."
            
            show stan working at right:
                yalign .5
            with dissolve
            
            stan "Ahoy! I don't see any meats in that basket of yours. Why don't you take a gander at my wares to see if anything interests you!"
            
            "You give him the courtesy of at least pretending to be interested, even though you don't see anything you want."
            
            stan "Ahahaha, sorry, an old man's gotta entertain himself somehow standing back here all day. Anything catch your eye?"
            
            player "Not really..."
            
            stan "Not interested in meats? Perhaps you should check out the garden section har har har!"
            #Well I reckon you're in the wrong aisle, the garden section is on the other side of the store har har har!"
            stan "Really though, we do have a selection of tofu and vegetable sushi if that's more your style."
            
            player "Sushi huh? Who would have thought there'd be sushi in a small town like this."
            
            stan "Well... don't tell my supervisor I said this but you're better off being a vegetarian if you're eyeing the sushi here."
            stan "I wouldn't trust the definition of \"fresh\" they use for the fish here."
            stan "But the ones that are just veggies wrapped in rice should still be edible!"
            
            player "That's comforting..."
            
            "You pick up one of the packages, not entirely convinced."
            "You shrug and place it in your basket. Can't be that bad. At least it's cheap."
            
            stan "Hope you enjoy it! Let me know how it is!"

            player "Sure thing. Have a nice day."
            
            stan "You do the same!"

            hide stan with dissolve
            
        "Moo cow milk":
            "Where else are you supposed to get your calcium? You need strong bones for... well you just need them, okay?"
            "At least you don't have to worry about it spoiling on the walk back home since it's more likely to freeze."
            "Alright, what's next?"
            "You grab a few more things then swing by the deli where an old cat in an apron and paper hat stands behind the counter."
            "He catches you looking at the meats on display and bellows out a jolly greeting that startles you."

            show stan working at right:
                yalign .5
            with dissolve

            stan "Howdy!"
            stan "Let me know if you need anything and I'd be happy to assist you."

            "You give him a nod of acknowledgement then go back to deliberating which meat to get."

            player "Hey there..."

            "You glance at his nametag."

            player "...Stan."
            player "Can I get some..."
            
            "You pick out a few meats to stock your freezer with so you won't have to make frequent trips back here."

            stan "Sure thing! I'll have that ready for you in a jiffy!"

            "You shift your weight from one foot to the other while the clerk prepares the meats."
            "Once he's finished, he slides the packaged product toward you and you cross it off your shopping list."

            stan "Have a nice day!"

            player "Thanks, you too!"

            hide stan with dissolve

    "You go down a few more aisles, tossing some extras into your basket until it's nearly overflowing, then proceed to the check out."

    show gregg apron at center with dissolve:

    greggunknown "Heya!"

    "A chipper fox greets you as you approach the register."
    #"A fox with amber orange fur mans the register you wandered up to."
    #"He sports a dark grey turtleneck sweater underneath his apron, along with a chipper attitude."
    "The name tag pinned to the apron reads \"Gregg\", with a tiny, crude portrait of himself drawn next to it."

    player "Hey."

    "You start unloading the contents of your basket onto the conveyor belt. The cashier rings them up with ease, not even looking at what he's scanning."

    gregg "You find everything alright?"

    player "Mhm."

    "You mutter a response as you try to get your debit card out."

    gregg "So where ya headed?"

    "You look up from your wallet and blink a couple times."

    player "Huh?"

    gregg "Lots of people passing through from Bright Harbor lately, goin' to visit family for the holidays."

    player "Oh uh, I just moved into Possum Springs actually."

    "The cashier stops scanning your groceries and his eyes go wide."

    gregg "What, really?!"
    gregg "Nobody ever just like, comes here to live."
    gregg "Have you tried the pierogies at the diner yet? They're *amazing!*~"

    player "I just arrived yesterday. I tried that coffee shop this morning, what was it called... Posspresso?"

    gregg "Oh yeah that one's pretty good. You should check out Bear Essentials sometime. It's a bakery on main street. Serves pretty good coffee too."
    #as long as you don't need anything fancy
    
    player "I'll be sure to pop in sometime."
    
    gregg "This town ain't much but there's plenty of stuff to do if you know where to look!"
    
    player "I'll uh, keep an eye out I guess?"
    
    gregg "There's a ton of abandoned buildings to explore, the lake should be frozen enough for ice skating by now, uhhh some people go fishing in the old trolley station but it smells like somebody died down there so I don't often go, oh and my band is getting together to do this-"
    
    player "Haha yeah that sure sounds exciting! Can I pay for my groceries now?"
    
    gregg "Oh sorry about that."
    
    "He presses a button on the register and you can finally swipe your card."
    
    gregg "Have a nice day!"
    
    player "Thanks, you too."
    
    hide gregg with dissolve
    
    "You grab your bagged groceries and begin the long journey back home as the sun descends into the hilly landscape."
    
    scene bg home_interior_night with fade
    
    "You've had enough of the cold by the time you reach your house. You crank the heat up to the max but the air coming through the vents is hardly any warmer than it is outside."
    #"What the hell, it was doing this last night too."
    #"In fact, it feels colder!"
    #"You better not wake up to find yourself frozen to death because this machine "
    "You're gonna be so mad if you freeze to death in your sleep."
    "Exhausted from trudging through snow all day, you put away your groceries as quickly as possible then wrap yourself in several blankets."
    if chosenHobby == "movies":
        "With your face pressed against a cold pillow, you watch a movie until you fall asleep."
    elif chosenHobby == "music":
        "With your face pressed against a cold pillow, you listen to music until you fall asleep."
    elif chosenHobby == "books":
        "With your head pressed against a cold pillow, you read a book until you fall asleep."

    # Day 2, thursday
    $ currentDay = 2
    $ currentDate = "December 2"
    
    #code stuff
    $ metLori = False
    $ metMae = False
    $ metBea = False
    $ metAngus = False
    $ metSelma = False
    $ metGerm = False
    
    $ beaQuestStarted = False
    $ bikeQuestStarted = False
    $ libraryQuestStarted = False
    $ selmaQuestStarted = False
    $ officeQuestStarted = False
    
    $ beaQuestBakery = False
    $ beaQuestPosspresso = False
    
    $ beaQuestComplete = False
    $ bikeQuestComplete = False
    $ libraryQuestComplete = False
    $ selmaQuestComplete = False
    $ officeQuestComplete = False
    
    $ libraryVisits = 0
    $ posspressoVisits = 0

    $ hasKey = False
    $ doorStuck = False
    $ hasCoffee = False    
    $ hasShedKey = False
    $ seenFlyer = False
    $ tabletopInvitation = False
    $ foundBandGig = False
    
    scene bg home_interior_day with fade
    
    "You awaken just as warm as you were when you went to bed."
    "Which is to say you've been in cryogenic sleep. You'd have a better time sleeping in the fridge."
    "Seriously, you need to figure out what is up with the heater."
    "It's been a long time since you were last in this house but you can recall some details from the times you visited."
    "You remember watching your father fiddle with the heater once or twice when it wasn't blasting enough heat."
    "Unfortunately the inner workings are blocked by a grate that's screwed in tight."
    "You try to unscrew the bolts with your fingers but they're rusted and stuck in place."
    "Maybe there's a wrench somewhere in this house."
    "Your old man left behind a ton of stuff. There's gotta be a toolbox around here."
    "You haven't got a clue where to look though. This house is like a labrynth and there's no lack of boxes and drawers to search through."
    "It might be faster to just go out and buy a new wrench."
    "The map you downloaded at the cafe says there's a hardware store nearby you could try."
    "What should you do?"
    
    $ haveOverdueBook = False
    $ cinnamonRoll = False
    
    $ exploredHouse = False
    $ houseEvents = ["houseOffice", "houseBook", "houseKey"]
    
    menu:
        "{cps=0}What should you do?{/cps}"
        "Explore home":
            call unexploredHouse from _call_unexploredHouse
        
            #minor event
            #random whether you find the library book, office, or shed
            
            #if houseEvents is empty, you can no longer explore the house
            if not houseEvents:
                $ houseFullyExplored = True
                "You've already explored the house enough."
            
            $ randomSelected = renpy.random.choice(houseEvents)
            
            $ exploredHouse = True
            
            if randomSelected == "houseOffice":
                $ houseEvents.remove("houseOffice")
                call houseOffice
            #elif randomSelected == "houseShed":
            #    $ houseEvents.remove("houseShed")
            #    call houseShed
            elif randomSelected == "houseBook":
                $ houseEvents.remove("houseBook")
                call houseBook
            elif randomSelected == "houseKey":
                $ houseEvents.remove("houseKey")
                call houseKey
            else:
                "You've already explored the house enough."
                $ houseFullyExplored = True
            
            jump afterExploringHouse
            
        "Go into town":
            jump intoTown
            
            
            
        #"Posspresso":
            #minor event
            #can meet with characters you've met before here at random, if they're available
            #"You don't see how a coffee shop is gonna have what you need but a bit of caffeine never killed anyone."
    
        #"Town outskirts":
            #minor event
            #"To hell with this, you'll wander around outside somewhere."
            
            
label day2Evening:
    scene bg roads_day with fade
    
    "The sky is already turning dark. You should hurry home."
        
    scene bg home_interior_night with fade
        
    #to do: elaborate    
    "You fix the heater and go to bed."
    
    
label day3:    
    "day3"
    "For the first time in a while, you awaken feeling rested and comfortable."
    "The heater does a good job of warming you up when it actually works."
    "You make breakfast and sit watching the snow."
    "Now to decide what to do today."
    
    #options: stay home and explore (minor event), go into town and return the wrench (minor event), library if you have the book (major event), posspresso (minor event), visit bakery (non event), explore random part of town (minor event) [current available options are  exploring the underground and uhhhhh, seeing germ feeding wild cats at the food donkey, maybe merge random posspresso meets into this list]
    
    
    $ townEvents = ["townGerm1", "townAngus1", "townBridge1"]
    
    $ wrenchReturned = False
    $ midDay = False
    
    menu:
        "{cps=0}What should you do?{/cps}"
        "Explore home":
            #minor event
            #need to add to list of available house exploration options if you found the key earlier
            #re-add house description if you haven't already explored the house
            #if exploredHouse == False:
            
            if exploredHouse == False:
                call unexploredHouse
            
            $ midDay = True
            
            #if houseEvents is empty, you can no longer explore the house
            if not houseEvents:
                $ houseFullyExplored = True
                "You've already explored the house enough."
            
            $ randomSelected = renpy.random.choice(houseEvents)
            
            $ exploredHouse = True
            
            $ houseEvents.append("houseShed")
            
            if randomSelected == "houseOffice":
                $ houseEvents.remove("houseOffice")
                call houseOffice
            elif randomSelected == "houseShed":
                $ houseEvents.remove("houseShed")
                call houseShed
            elif randomSelected == "houseBook":
                $ houseEvents.remove("houseBook")
                call houseBook
            elif randomSelected == "houseKey":
                $ houseEvents.remove("houseKey")
                call houseKey
            else:
                "You've already explore the house enough."
                $ houseFullyExplored = True
        "Explore town":
            $ midDay = True
            
            "You should explore Possum Springs to familiarize yourself with the area."
            
            $ randomSelected = renpy.random.choice(townEvents)
            
            if randomSelected == "townAngus1":
                #to do: move remove and append statements into appropriate label
                $ townEvents.remove("townAngus1")
                $ townEvents.append("townAngus2")
                call townAngus1
            elif randomSelected == "townGerm1":
                $ townEvents.remove("townGerm1")
                $ townEvents.append("townGerm2")
                call townGerm1
            elif randomSelected == "townBridge1":
                $ townEvents.remove("townBridge1")
                $ townEvents.append("townBridge2")
                call townBridge1
            #add one more event to the pool
            
            
        "Return wrench":
            $ wrenchReturned = True
            "You promised the hardware store girl that you'd return the wrench after you were done with it."
            "You have no more use for it so you should give it back as soon as possible."
            
            call meetingMae
        "Return library book" if haveOverdueBook == True:
            "The book is more overdue than the wrench. You should return it first."
            
            call libraryVisit1
        
    if midDay == True:
        "There's still some light in the day. What else should you do with your time?"
        $ midDay = False

    
    "You return home and go to sleep."
    
    #day4
    
    "Day 4 start"
    "What will you do today?"
    
    $ midDay = False
    
    menu:
        "{cps=0}What should you do?{/cps}"
        "Explore home":
            #minor event
            #need to add to list of available house exploration options if you found the key earlier
            
            if exploredHouse == False:
                call unexploredHouse
            
            $ midDay = True
            
            #if houseEvents is empty, you can no longer explore the house
            if not houseEvents:
                $ houseFullyExplored = True
                "You've already explored the house enough."
            
            $ randomSelected = renpy.random.choice(houseEvents)
            
            $ exploredHouse = True
            
            $ houseEvents.append("houseShed")
            
            if randomSelected == "houseOffice":
                $ houseEvents.remove("houseOffice")
                call houseOffice
            elif randomSelected == "houseShed":
                $ houseEvents.remove("houseShed")
                call houseShed
            elif randomSelected == "houseBook":
                $ houseEvents.remove("houseBook")
                call houseBook
            elif randomSelected == "houseKey":
                $ houseEvents.remove("houseKey")
                call houseKey
            else:
                "You've already explore the house enough."
                $ houseFullyExplored = True
        "Explore town":
            $ midDay = True
            
            "You should explore Possum Springs to familiarize yourself with the area."
            
            $ randomSelected = renpy.random.choice(townEvents)
            
            if randomSelected == "townAngus1":
                #to do: move remove and append statements into appropriate label
                $ townEvents.remove("townAngus1")
                $ townEvents.append("townAngus2")
                call townAngus1
            elif randomSelected == "townGerm1":
                $ townEvents.remove("townGerm1")
                $ townEvents.append("townGerm2")
                call townGerm1
            elif randomSelected == "townBridge1":
                $ townEvents.remove("townBridge1")
                $ townEvents.append("townBridge2")
                call townBridge1
            #add one more event to the pool
            
            
        "Return wrench" if wrenchReturned == False:
            $ wrenchReturned = True
            "You promised the hardware store girl that you'd return the wrench after you were done with it."
            "You have no more use for it so you should give it back as soon as possible."
            
            call meetingMae
        "Return library book" if haveOverdueBook == True:
            "The book is more overdue than the wrench. You should return it first."
            
            call libraryVisit1
            
    if midDay == True:
        "There's still some light in the day. What else should you do with your time?"
        $ midDay = False

    
    "You return home and go to sleep."
    
    
    
    #day5
    #optional dnd with gregg and co
    
    "What will you do today?"
    
    $ midDay = False
    
    menu:
        "{cps=0}What should you do?{/cps}"
        "Explore home":
            #minor event
            #need to add to list of available house exploration options if you found the key earlier
            
            if exploredHouse == False:
                call unexploredHouse
            
            $ midDay = True
            
            #if houseEvents is empty, you can no longer explore the house
            if not houseEvents:
                $ houseFullyExplored = True
                "You've already explored the house enough."
            
            $ randomSelected = renpy.random.choice(houseEvents)
            
            $ exploredHouse = True
            
            $ houseEvents.append("houseShed")
            
            if randomSelected == "houseOffice":
                $ houseEvents.remove("houseOffice")
                call houseOffice
            elif randomSelected == "houseShed":
                $ houseEvents.remove("houseShed")
                call houseShed
            elif randomSelected == "houseBook":
                $ houseEvents.remove("houseBook")
                call houseBook
            elif randomSelected == "houseKey":
                $ houseEvents.remove("houseKey")
                call houseKey
            else:
                "You've already explore the house enough."
                $ houseFullyExplored = True
        "Explore town":
            $ midDay = True
            
            "You should explore Possum Springs to familiarize yourself with the area."
            
            $ randomSelected = renpy.random.choice(townEvents)
            
            if randomSelected == "townAngus1":
                #to do: move remove and append statements into appropriate label
                $ townEvents.remove("townAngus1")
                $ townEvents.append("townAngus2")
                call townAngus1
            elif randomSelected == "townGerm1":
                $ townEvents.remove("townGerm1")
                $ townEvents.append("townGerm2")
                call townGerm1
            elif randomSelected == "townBridge1":
                $ townEvents.remove("townBridge1")
                $ townEvents.append("townBridge2")
                call townBridge1
            #add one more event to the pool
            
            
        "Return wrench" if wrenchReturned == False:
            $ wrenchReturned = True
            "You promised the hardware store girl that you'd return the wrench after you were done with it."
            "You have no more use for it so you should give it back as soon as possible."
            
            call meetingMae
        "Return library book" if haveOverdueBook == True:
            "The book is more overdue than the wrench. You should return it first."
            
            call libraryVisit1
            
        "Play DnD with Gregg" if tabletopInvitation == True:
            "Tonight is when Gregg said he's gathering people to play Conquests and Constellations."
            "You spend the day relaxing and preparing for an epic evening."
            
    if midDay == True:
        "There's still some light in the day. What else should you do with your time?"
        $ midDay = False
    
    
    
    #day6
    #if you haven't already seen the poster for the band gig, you stumble upon it somehow and decide to check it out that night.
    
    if foundBandGig = False:
        "As you wonder through town, a sheet of paper flutters through the wind. By chance it flies directly in your face."
        "You see it's a flyer for some sort of band gig happening... tonight?!"
        
    
    #day7
    #church scene?
    
    
    
    
    
    
    

    play sound "sound/birds.mp3"
    "After a restless sleep, you awaken to the sound of birds chirping outside."
    #"Even underneath this thick blanket, you feel frostbitten."
    #"What the hell, is the heater working properly?"
    #"Ugh, guess you have to get up and check."
    #"Drawing in a deep breath, you stretch your limbs and loosen up a few stiff muscles."
    #"Your bones crackle and you let out a contented sigh when your spine finally pops into place."
    #"Ahh... that felt good."
    #"You crawl out from under the covers and pull back the curtains draping the window to let some light in."
    "You crawl out from under the covers and make your way to the kitchen to make breakfast."

    play sound "sound/curtains.mp3"
    #transition to background of view from window
    play music "music/whenskiesclear_loop.mp3" fadein .5

    #"To your surprise, snow has appeared in full force overnight!"
    #"Snowflakes plummet to the earth, covering the landscape in fluffy whiteness. Your eyes sting from how white it is but you can't look away."
    #"Everything's so different, your backyard is hardly even recognizable."
    #"The ground that had been littered with autumn leaves is now a clean blank slate, broken only by the dark tree trunks growing out of it."
    #"Even the treetops are frosted white, matching the bright cloudy sky."
    #"It's not like you've never seen snow before, but something about it makes you feel nice."
    #play sound "sound/stomach growl.mp3"
    #"As much as you'd like to spend the morning admiring the scenery, your stomach's growling is getting to be too much to ignore."
    #"You need to get something to eat after skipping dinner again last night."
    #"After turning up the thermostat, you make your way to the kitchen and see what you've got."

    #scene bg home_interior_day with fade

    #"...Not much, but you can at least make a bowl of oatmeal."
    "Wrapped in a blanket, you watch the snow fall outside as you eat. You make a note to buy hot cocoa mix next time you're at the store for maximum comfiness."
    "You never noticed before, but there's a shed on this property you can see from this window."
    #"Leaving the dishes in the sink to wash later, you take a trip to the bathroom to get ready for the day."

    #scene bg bathroom with fade
    
    #"You dry yourself off and put on some clothes, deliberating what to do today."
    #"Do you want to stay in or go out?"
    #"You've done a lot of walking lately so you're inclined to stay here and relax."
    #"You haven't really explored your new home yet. You should at least familiarize yourself with the general layout before you start wandering around town."
    "Curiosity gets the better of you and, after eating, you put on a coat and head out to investigate it."

    #scene bg home_office_day with fade

    
    #stop music fadeout 1.0

    scene bg shed with fade

    play music "music/woulditmatter_loop.mp3" fadein 1.0
    
    "It's pretty large for a shed. It's more like a garage, really."
    "It's cold and echoey and smells like gasoline in here. Old leaves crunch under your feet as you explore and dodge cobwebs."
    #"Judging by the debris and tools strewn about, it hasn't been cleaned in a while. Nobody even bothered to sweep the leaves from the floor."
    "In the darkness you make out a tarp covering something big."
    "Probably a lawnmower"
    #"A pile of skeletons, used for a demon-summoning ritual perhaps?"
    #"Or maybe it's a stockpile of cocaine. Never know when you might need a couple hundred pounds of that stuff."
    "Nothing makes an old man happier than mowing the lawn at the crack of dawn on weekends."
    "Bracing yourself for disappointment, you grab a corner of the tarp and take a peek."
    "..."
    "No way."
    "Your hand reaches out to touch it. The cold metal stings your fingertips."
    "You pull aside the rest of the tarp, revealing a gorgeous classy motorcycle."
    "Shiny chrome contrasts with the leathery black upholstery. You just need a pair of aviators and you can become a biker."
    "You take back what you thought about your dad being a lame boomer, he was in fact a cool boomer."
    "Now you can ride around town instead of having to walk everywhere *and* you can do so stylishly!"
    #"You can't wait to feel the wind on your face when you take her for a spin."
    "You look around for a spare key. The original is probably long gone, wherever your dad ended up."
    "Luckily you found it relatively quickly. It was just inside the nearby toolbox, which has been left open for who knows how long. Thankfully nobody stole it."
    "The engine makes a weird noise when you insert the key."
    "You try again and it makes another pathetic dying noise."
    "Heck."
    "Welp, time to roll up your sleeves and mess around with an engine you've never seen before and no access to documentation."
    "You spend a few hours tinkering with it trying everything you can think of but you're hindered by a lack of tools."
    "The one wrench size you need is missing from the tool box. You searched everywhere for it, even inside the house, but it's nowhere to be found."
    #you break the tool you needed?
    "You recall seeing a hardware store on the map that's within walking distance. Surely they'd have what you need, right?"
    "They damn well better if you're going through all this trouble."
    "You grab your wallet and a pair of mittens before setting out toward town, trudging through the snow."
    
    
    #"Still nothing. Out of fuel maybe?"
    #"You pop off the cap and look inside the gas tank, using the light on your phone to see into the darkness."
    #"Empty."
    #"A nearby gas can remedies this issue, but the engine still refuses to start."
    #"Hmm."
    #"You look around for the repair manual, remembering you saw something like it on the workbench."
    #"You skim through it and get the gist on how to check the engine and oil and troubleshoot common problems."
    #"Oil seems ok, but you're not sure if sitting around for so long has done it any favors."
    #"You grab a few tools, get on the floor, and get to work opening her up."
    #"Ugh, it's grimy as Hell down here."
    #"It just gets worse the more you work on it."
    #"As you pry off a covering, a gear comes loose and falls to the ground, shattering into pieces."
    #"That's not good."
    #"Was that what was wrong with it? You look around for any spare gears but fail to find any."
    #"Well damn, there's no way you can fix it now."
    #"With a frustrated sigh, you wipe your hands on a towel before checking your phone to look up any nearby auto shops."
    #"As fate would have it, the nearest one is even further out than Ham Panther."
    #"One of the related results however is a local hardware store in town, not that much further away than the cafe. Maybe they have what you need?"
    

    stop music fadeout 2.0

    scene bg park with fade


    "Ah here it is, the Ol' Pickaxe."
    "You ascend the couple of steps leading to the front door and head inside."

    
    
    
    
    scene bg ol pickax with fade
    

    #scene bg park with fade
    
    #if you still have your treat, add the squirrel scene below
    
    
    #"Taking your bag, you leave the store and decide to rest at the park lodged in between the bakery and hardware store."
    #"You brush aside the snow that has accumulated on one of the stone benches next to some sort of monument."
    #"Names are carved into a pillar, which houses a statue depicting a soldier carrying a rifle with a bayonet."
    #"They must have been locals who served in some war a century or so ago."
    #"You read a few names as you mindlessly open up your bag and pull out your cinnamon bun, but you don't recognize anyone on there."
    #"You munch on your snack in peace until a particularly curious squirrel hops onto the far edge of the bench, staring at you."
    #"The animals in this town seem to have no fear of people and walk right past you, close enough you could touch one."
    #"You watched them on your walk here as they scrambled to get last minute errands done before the real cold hits."
    #you're sure they were caught off guard by the blizzard like everyone else
    #"Burying food, fetching nesting materials, that sort of thing."
    #"This one here comes closer and sniffs at the treat in your hand."
    #"Squirrels like cinnabuns, right? You break off a piece and set it on the bench."
    #"He hesitantly comes over and picks it up with its little hands then shoves it into its mouth before skittering off."
    #"You're welcome."

    scene bg home_interior_night with fade
    
    "After the long walk back home, you crashed on the sofa and mulled over everything."
    #"You walk out the door and take a few aimless steps down the street, mulling over everything."
    #"Well that sure was disappointing."
    #"Not getting any of the parts you need, that is."
    "You're too tired to try fixing your bike, even though you finally got the tool you needed."
    "Hardly matters anyway since you've got Gregg coming over to fix your bike, and he can probably do it better than you can."
    if wentWithGregg == True:
        "That's two favors you owe him now."
    "Was it you or was he especially friendly with that baker, Angus?"
    "Maybe he has a crush on him or something."
    "At least you successfully bartered with that angry goth crocodile."
    "But then there was that chat with Mae that sure felt strange."
    "Maybe you should stop parading the fact that your dad died. It's probably freaking people out."
    "..."
    "No, it's definitely freaking people out. You should stop doing that."
    "Lost in thought and exhausted from today's quest, you end up falling asleep right there on the couch."
    
    
    "You crawl under the covers and think about your future here."
    "You need to get a job at some point. Sooner or later you'll need the income."
    "You wouldn't mind making some friends too while you're here."
    "It's been so long since you've hung out with anyone, you can hardly remember what it's like."
    "At least Gregg is coming over tomorrow. He seems like a nice guy."
    "You yawn and turn over, clutching your pillow as sleep overtakes you."

    scene bg black with fade
    
    # Day 3, friday
    $ currentDay = 3
    $ currentDate = "December 3"
    
    
    
    #"You're internally cringing at yourself when a delightfully sweet smell reaches your nose through the bitterly cold air."
    #"It draws you to the source, a shop called Bear Essentials Bakery."
    #"After the long walk here, you might as well grab a snack for the road."
    
    scene bg home_interior_day with fade
    
    "The following morning, you get up and walk around the house, stretching your legs and awaiting Gregg's arrival."
    
    scene bg home_office_day with dissolve
    
    
    "The sound of a motor revving in the distance fills the air and gradually gets louder as it approaches."
    
    play sound "sound/motorbike arriving.mp3"
    
    "That must be Gregg!"
    "You pull yourself together and go to the front door to meet him."
    
    scene bg home_interior_day with dissolve
    
    "*Knock knock knock*"
    
    show gregg neutral at center with dissolve
    
    play music "music/cozycidersipping_loop.mp3" fadein 1.0
    
    gregg "Heya!"
    
    player "Hey! Glad you could make it!"
    
    gregg "I only have an hour before I have to be at work."
    gregg "Well? Where's the bike?"
    
    player "Oh uh, right this way."
    
    "You slip on your shoes and show him to the shed."
    
    scene bg shed with fade
    
    "Gregg's eyes go wide at the sight of the motorcycle as you open the door."
    
    show gregg neutral at center with dissolve:
        xzoom -1
        
    gregg "She's beautiful. I love her."
    
    #if male do the sex joke bit
    
    player "I'd love her more if I could turn her on."
    
    gregg "*Snrk*"
    
    player "What?"
    
    gregg "Nothing ahahaha!"
    
    player "I tried fiddling around underneath, but I guess I just didn't have the right tool for the job."
    
    gregg "Pffft hahahaha!"
    
    player "What??"
    
    gregg "You're doing that on purpose aren't you?"
    
    player "Doing what?"
    
    gregg "Ah forget it. Do you have a wrench I can use?"
    
    #player "Yeah but it just wasn't big enough..."
    #mine wasn't big enough so I had to borrow one from the hardware store
    "You pull out the wrench you got from Bea and hand it to him."
    
    player "Here. I went through a whole ordeal to borrow this from the hardware store yesterday."
    player "Because apparently my own equipment wasn't the right size."
    
    #player "Or at least I didn't have one big enough"
    
    #something something maybe you just need the right tool
    #in just the perfect size
    
    "Gregg busts out laughing hysterically and only then do you realize the inadvertent innuendos you've been saying."
    
    player "I mean uhh..."
    
    #gregg "Hahaha don't worry dude, I'll get her running and you can ride her to your heart's content!"
    gregg "Hahaha I get what you mean! Don't worry though, I'll get her running and you can ride her to your heart's content!"
  
    player "You didn't have to say it like that..."
    
    gregg "I know, but it's more fun that way."
    
    "Gregg gets to work on the engine while you hold a light for him."
    #"He takes out a few pieces and disconnects some wires"
    "You can't really see what he's doing but he works pretty fast. He soon has a pile of bolts, wires and random engine parts strewn around him."
    
    gregg "There! That should do it!"
    gregg "Hopefully!"
    
    "He just as quickly puts it all back together, turning back to you with a proud grin and an oil stain on his fur."
    
    player "You got a little something on your cheek."
    
    gregg "Huh? This one?"
    
    "He wipes the wrong cheek with his paw."
    
    player "Other one."
    
    "He manages to wipe his face everywhere except the stain."
    
    menu:
        "Wipe it off for him":
            player "Here, let me just..."
            
            "You grab a nearby towel and rub at the oil, trying not to spread it further."
            "Gregg freezes like a deer in headlights while you clean his fur in the most awkward way possible."
            
            player "There. Sorry if I pulled some whiskers. Just didn't want you going in to work looking like that."
            
            gregg "Hahaha thanks? I think?"
            
            player "And I guess it was the least I could do since you just fixed my bike."
            
            gregg "Correction: probably fixed your bike!"
            gregg "We still have to test it first!"
            
            "You insert the key into the ignition and look to Gregg as you start to turn it, praying it doesn't explode."
            
            #engine noises
            play sound "sound/motorcycle start.mp3"
            
            "You're pleasantly surprised when it starts up just fine."
            
            gregg "Yes!"
            
            ###your reaction should be different depending on your personality points
            
            
            "FROM THIS POINT ON IS VERY OLD AND UNFINISHED STUFF"
            
            
            
            ###unfinished
            
            
            
            gregg "I had something similar happen to my bike before so this was a piece of cake!"
            
            
            
            gregg "And you'll probably wanna take it to a real mechanic sometime."

            player "At least now I can drive it to one."

            gregg "Yup!"
            gregg "Well, I better get going before I'm late for work."

            player "Ok! Thanks so much for fixing my bike!"

            gregg "No problem! It was more exciting than standing around scanning groceries all day, that's for sure!"
            gregg "Oh that reminds me, we're having a little get together at the bakery this evening if you wanna come. Me, Angus, and a friend of ours."
            
            player "Sure, I'm not doing anything tonight anyway."

    #        gregg "Cool, we're meeting at six."

    #        player "Sounds good. See ya then!"
            
            
            gregg "Alright, see ya later!"

    #        "He jogs over to his own bike and rides off into the sunrise."
            
            
        "Give him a towel":
            "FROM THIS POINT ON IS VERY OLD AND UNFINISHED STUFF"
            ###unfinished
    
    
    
    
    
    
    
    
    
    
    ###tell gregg about the computer you can't get into, he recommends gettng angus to fix it. he also invites you to hang out and play tabletop games with him angus selma and germ tonight. at the hangout angus mentions you should switch to a phone provider that works here and offers to fix your computer. you can decline and say you'll go to the library to download an iso to fix the computer yourself the next day (does selma comment on that or has she left already?) and that you'll look up a cell provider on the library computers while you're there. before you leave the next day you find an overdue book in your house and take it along with you.

    #"You had managed to get used to the train and its blaring horn passing by several times each night but now your slumber is disturbed by a new sound."
    #"It's the rumbling of a motor approaching, followed by tires digging into the ground just outside the front door."
    #"You quickly become alert once you realize that must be Gregg coming over to fix your bike."
    #"You scramble out of bed but before you can change out of your pajamas he's already knocking on the front door. You have no choice but to answer it like this."

    #scene bg home_interior_night with fade

    #"It's not even daylight out yet."
    #"You flip on the lights and open the door to find Gregg standing there proudly with an overstuffed backpack in his hand."
    #"He seems oblivious to the fact that you've just woken up."


    #gregg "Morning, [name]! I brought all my tools and a bunch of parts."

    #player "Uh, morning Gregg. I didn't expect you so early."


    #"You put on some slippers and lead him to the shed."
    

    #player "I'd love her more if she didn't leak fuel."

    #"You point at the puddle of gas soaking into the concrete floor."

    #gregg "Ooh, yeah that's a big problem."

    #show gregg sad3 flip

    #gregg "Hmm."

    #"He drops to the ground and gets an up close look at the engine."

    #show gregg neutral flip

    #gregg "You got a towel?"

    #"You grab a towel from the workbench and hand it to him."

    #gregg "Thanks."

    #"He wipes off some of the grime, then pulls his backpack close and rummages around until he finds a flashlight."
    #"Lighting up the area underneath the bike, he pokes and prods at a few parts then furrows his brow."

    #gregg "Hrmmm..."

    #player "What is it?"

    #gregg "Not sure yet."

    #player "Can I get you anything? A drink?"

    #gregg "Nah, I'm good."

    #"He pulls a wrench from his bag and starts unscrewing nuts and bolts while you stand by, just observing."
    #"You wish you could help, but you're really at a loss at what to do and you don't want to get in his way."
    #"He takes off quite a few bits and pieces, and at times looks like he's confused by what he's working with, but he continues working with confidence."

    #gregg "Hey how much fuel is in the tank, do you know?"

    #player "Um."

    #"Suddenly a valve clanks against the floor and the entire gas tank empties itself onto Gregg's sleeve."
    #"He recoils in surprise and falls back on his rear."

    #gregg "AAAAAAAH!"

    #player "Oh shit!"

    #gregg "Haha don't worry, it's fine! Didn't get much on me."

    #"Gregg flicks his arm to get the remaining droplets off."
    #"Thankfully most of it had slid off his leather jacket and splattered onto the floor instead of soaking into his fur."

    #player "Still..."

    #menu:
    #    "Wipe down his jacket":
    #        #+1 greggAP
    #        #+1 understanding

    #        "You grab a spare cloth and wipe the excess liquid off his jacket, noticing he got a smudge of oil on his face too."

    #        player "Hold still."

    #        gregg "Wha-?"

    #        "You scrub the oil spot off as gently as you can. He freezes in place as you clean his fluff."

    #        player "There. You had something on your face."

    #        gregg "O-oh!"
    #        gregg "Haha thanks! I wouldn't wanna show up to work with a big splotch on my face! Hahaha!"

    #        "His lighthearted laughter is contagious, at least enough to put a smile on your face."

    #    "Hand him a clean towel":
    #        #+1 cynical

    #        player "Sorry, I should have warned you ahead of time..."

    #        "You hand him a spare cloth."

    #        gregg "Nah, it's alright."

    #        "He wipes the excess liquid off his jacket."

    #        gregg "See? No harm done."

    #        player "You got a bit of oil on your face too. Right there."

    #        "You point in the general area where the splotch is on his face. He roughly scrubs at the area."

    #        gregg "Did I get it?"

    #        "Not really..."

    #        player "Yeah."

    #gregg "Alright, let me finish working on this. I think I can get her running soon."

    #"Gregg goes back to operating on your bike, wiping down gunked up parts, reseating pieces, and duct taping components."
    #"Time flies by as you watch him. He really seems like he's having a good time fixing your bike and making idle chit chat."
    #"Before you know it he stands and claps his paws together."

    #gregg "That should do it!"
    #gregg "Hopefully!"
    #gregg "Let's roll her out of here and see if she starts!"

    #menu:
    #    "I'm so excited!":
    #        $ greggAP = greggAP + 1

    #        player "I'm so excited!"

    #        gregg "Come on come on come on let's push her out onto the yard!"

    #        "You flip up the kickstand and the both of you wheel the bike through the garage door and out into the snow."
    #        "Gregg looks at you eagerly as you put the key into the ignition and give it a turn."

    #        play sound "sound/motorcycle fail.mp3"

    #        "..."

    #        "Another turn."

    #        play sound "sound/motorcycle fail.mp3"

    #        "..."

    #        play sound "sound/motorcycle start.mp3"

    #        "Just as you're losing hope, the engine comes to life."

    #        player "Hahaha yeah!!!"

    #        "Gregg looks so relieved. He's flailing his arms and howling."

    #        gregg "AWOOOOOOOOOOOOOOO!"

    #        "And then the engine dies."

    #        gregg "Huh?"
    #        gregg "Oh yeah, we never replaced the gas!"

    #        "You glance at the near-empty gas canister in the garage."

    #        player "I have a little bit left inside still. It's kinda old though."

    #        gregg "That's fine, just make sure you put some fresh fuel in there soon."
    #        gregg "And you'll probably wanna take it to a real mechanic sometime."

    #        player "At least now I can drive it to one."

    #        gregg "Yup!"
    #        gregg "Well, I better get going before I'm late for work."

    #        player "Ok! Thanks so much for fixing my bike!"

    #        gregg "No problem! It beats bagging groceries at the Ham Panther all day!"
    #        gregg "Oh that reminds me, we're having a little get together this evening if you wanna come. Me, Angus, and a friend of ours."

    #        player "Sure, that sounds fun! I'm not doing anything tonight anyway."

    #        gregg "Cool, we're meeting at six. We live on the floor above the bakery."

    #        player "Sounds good. See ya then!"

    #        gregg "Hey do you have Chattrbox? You should add me!"

    #        "You haven't used Chattrbox in quite a while."
    #        "Regardless, you get his account name and make a note to reinstall the app later."

    #        gregg "Alright, see ya later!"

    #        "He jogs over to his own bike and rides off as the sun begins to rise."

    #    "I'll be surprised if this works.":
    #        #(-1 Gregg AP, +1 cynicism)

    #        player "I'll be surprised if this works."

    #        "Gregg's ears droop."

    #        show gregg sad2 flip

    #        gregg "Hey man, don't doubt my abilities. At least it can't run *worse* now after all that work I put into it."

    #        "You flip up the kickstand and the both of you wheel the bike through the garage door and out into the snow."
    #        "Gregg looks at you with anticipation in his eyes as you put the key into the ignition and give it a turn."

    #        play sound "sound/motorcycle fail.mp3"

    #        "..."

    #        "Another turn."

    #        play sound "sound/motorcycle fail.mp3"

    #        "..."

    #        "Just as you thought, he couldn't fix-"

    #        play sound "sound/motorcycle start.mp3"

    #        "*VROOOOOM*"

    #        "The engine comes to life, much to Gregg's relief."

    #        show gregg neutral flip

    #        gregg "Yes!"

    #        player "Well this is a pleasant surprise."

    #        "And then the engine dies."

    #        gregg "Huh?"
    #        gregg "Oh yeah, we never replaced the gas!"

    #        "You glance at the near-empty gas canister in the garage."

    #        player "I have a little bit left inside still. It's kinda old though."

    #        gregg "That's fine, just make sure you put some fresh fuel in there soon."
    #        gregg "And you'll probably wanna take it to a real mechanic sometime."

    #        player "At least now I can drive it to one."

    #        gregg "Yup!"
    #        gregg "Well, I better get going before I'm late for work."

    #        player "Ok! Thanks for fixing my bike!"

    #        gregg "No problem! It beats bagging groceries at the Ham Panther all day!"
    #        gregg "Oh that reminds me, we're having a little get together this evening if you wanna come. Me, Angus, and a friend of ours."

    #        player "Sure, I'm not doing anything tonight anyway."

    #        gregg "Cool, we're meeting at six. We live on the floor above the bakery."

    #        player "Sounds good. See ya then!"

    #        gregg "Hey do you have Chattrbox? You should add me!"

    #        "You haven't used Chattrbox in quite a while."
    #        "Regardless, you get his account name and make a note to reinstall the app later."

    #        gregg "Alright, see ya later!"

    #        "He jogs over to his own bike and rides off as the sun begins to rise."

    #    "What was wrong with it?":
    #        #+1 Gregg AP, +1 inquisitive)

    #        player "What was wrong with it?"

    #        gregg "Not enough duct tape. It's the most important part in making things work."

    #        player "Riiiight..."
    #        player "Well, what did you do about the missing gear?"

    #        gregg "Huh? There was a missing gear?"
    #        gregg "Eh, don't worry about it. Now come on, let's see if it works now!"

    #        "You flip up the kickstand and the both of you wheel the bike through the garage door and out into the snow."
    #        "Gregg looks at you eagerly as you put the key into the ignition and give it a turn."

    #        play sound "sound/motorcycle fail.mp3"

    #        "..."

    #        "Another turn."

    #        play sound "sound/motorcycle fail.mp3"

    #        "..."

    #        play sound "sound/motorcycle start.mp3"

    #        "Just as you're losing hope, the engine comes to life."

    #        player "It works!"

    #        "Gregg looks so relieved. He's flailing his arms and howling."

    #        gregg "AWOOOOOOOOOOOOOOO!"

    #        "And then the engine dies."

    #        gregg "Huh?"
    #        gregg "Oh yeah, we never replaced the gas!"

    #        "You glance at the near-empty gas canister in the garage."

    #        player "I have a little bit left inside still. It's kinda old though."

    #        gregg "That's fine, just make sure you put some fresh fuel in there soon."
    #        gregg "And you'll probably wanna take it to a real mechanic sometime."

    #        player "At least now I can drive it to one."

    #        gregg "Yup!"
    #        gregg "Well, I better get going before I'm late for work."

    #        player "Ok! Thanks so much for fixing my bike!"

    #        gregg "No problem! It beats bagging groceries at the Ham Panther all day!"
    #        gregg "Oh that reminds me, we're having a little get together this evening if you wanna come. Me, Angus, and a friend of ours."

    #        player "Sure, that sounds fun! I'm not doing anything tonight anyway."

    #        gregg "Cool, we're meeting at six. We live on the floor above the bakery."

    #        player "Sounds good. See ya then!"

    #        gregg "Hey do you have Chattrbox? You should add me!"

    #        "You haven't used Chattrbox in quite a while."
    #        "Regardless, you get his account name and make a note to reinstall the app later."

    #        gregg "Alright, see ya later!"

    #        "He jogs over to his own bike and rides off as the sun begins to rise."

    #hide gregg with dissolve
    #stop music fadeout 2.0

    #"Now then, time to go back inside and take a hot shower."

    #scene bg bathroom with fade

    #"You somehow managed to put off taking a shower until late afternoon."
    #"It's about time to head to Gregg's place."
    #"You drove the bike around the yard a bit to make sure it works and you're fairly confident it can make it to town."
    #"You grab your daily carry stuff then head down to the shed."




    

    
    
    
    
    
    
    
    
    

    #"The sun had gone down by the time you made it home."
    #"You lazed around and watched a few videos on your phone for a while until you were hungry enough to start dinner, then you continued to laze around until it was time for bed."
    #try tinkering with the bike, go to bed early since gregg is showing up in the morning


    #scene bg bedroom with fade

    
    
    #stop music fadeout 1.0

    


    

    #    scene bg basement1 with dissolve

    #"Gregg had messaged you on Chattrbox a few hours ago asking you to bring over the tools he left behind."
    #"You gather his things into the bag then zip it up and sling it over your shoulder."
    #"Oof, this thing's heavy!"
    #"You manage to bear with it and roll your bike outside, stepping into the night."
    #"It's cold and breezy out with soft moonlight coming through the clouds."
    #"Nice night for a ride."
    #"You close the shed door behind you and hop on your bike, revving it a few times before venturing into the darkness."

    #scene bg parkdark with fade

    #"You pull up to the curb next to the Bear Essentials Bakery and check the time on your phone."
    #"You're a little earlier than you expected, thanks to the lack of cops in Possum Springs to deter you from riding fast."
    #"But... the building looks abandoned?"
    #"Lights are off, the sign says closed, and the only apparent entrances are locked."
    #"No response when you bang on the door either."
    #"Does Gregg really live here on the second floor or was he messing with you?"
    #"You can't even text him because the only wifi spots available are password protected."
    #"You have no choice other than to wait and see if Gregg or Angus show up."
    #"Crossing your arms, you lean against the building and sigh."
    #"Your breath is easily visible in this weather, the contrails spiraling upward and being whisked away by the wind."
    #"You remember pretending to be a dragon when you were a child, blowing out \"smoke\" when it was cold out."
    #"You reminisce over moments like those and try spewing fire like you always wanted to."
    #"Nope, still just smoke."
    #"Which is really just hot air."
    #play sound "sound/footsteps.mp3"
    #"Your thoughts are interrupted by the sound of snow crunching behind you."
    #"Footsteps."
    #"They're coming closer."
    #"More than one person."
    #"You risk a glance over your shoulder, more worried that someone saw you acting out your dragon fantasies rather than someone coming to mug you."
    #"You're pleasantly surprised to find Angus walking toward you with a pizza box in his arms."
    #"And he's got a friend in tow."
    #"That must be the guy Gregg was talking about. He's a short birdy fellow with a rucksack on his back."

    #show angus neutral flip at left:
    #    yalign angusheight
    #show germ neutral at right
    #with dissolve

    #angus "Hello, [name]! Gregg hasn't let you inside yet?"

    #player "Hey Angus. Nah, I haven't seen him. The place looks empty."

    #angus "Hmm. He's probably watching TV in the dark and couldn't hear you."
    #angus "This is Germ by the way. Germ, this is [name]."

    #germ "Hi [name]! I hope you like video games! I brought some with me."

    #"He adjusts his bag to emphasize his point."

    #menu:
    #    "I love video games!":
    #        player "Nice to meet you uh... Germ? And yeah, I love video games!"
    #    "They're alright.":
    #        player "Nice to meet you uh... Germ? And yeah, video games are alright."

    #"You're not sure if you heard his name right but just smiles and doesn't correct you."
    #"Kind of an odd name but who are you to judge?"

    #angus "And I bought pizza! I didn't know what kind you liked so I just got cheese."

    #player "Cheese is fine."
    #player "So are we gonna go in or...?"

    #angus "Oh right. Forgot you guys are probably freezing."
    #angus "Come with me."

    #hide angus
    #hide germ
    #with dissolve

    #"You and Germ follow Angus to the back of the building."
    #"It feels a bit sketchy, but you doubt a guy carrying a pizza is going to mug you."
    #"He starts up the metal stairway of the emergency exit."

    #show angus neutral flip at left with dissolve:
    #    yalign angusheight

    #angus "Sooo, fun fact. The stairs inside are broken."
    #angus "They caved in before we bought the place. That's why we have to take the fire escape to get to the second floor."

    #player "Caved in? How does something like that even happen?"

    #"Angus shrugs."

    #angus "This building isn't exactly up to code."
    #angus "I don't think it's even legal for us to live here but it's the cheapest option and nobody's stopped us yet."

    #hide angus with dissolve

    #"You climb up the staircase after Angus with Germ taking up the rear."
    #"When you reach the second floor, you have to crawl through a window to get inside."

    #scene bg greggapartment with fade

    #play music "music/dissonance_to_chill_to.mp3" fadein 1.5

    #"Gregg is passed out on a stained couch in front of a TV."
    #"Beer bottles litter the floor around him."

    #show angus neutral flip at left with dissolve:
    #    yalign angusheight

    #angus "Honey, I'm home! And I picked up two hitchhikers!"

    #"The startled fox rolls off the couch and hits the floor with a thud."

    #show gregg neutral at right with dissolve

    #gregg "AAAAAAAAAAHH!"

    #"He quickly regains his composure, acting like nothing had just happened."

    #gregg "[name]! Germ! What's up?"

    #angus "I found Germ wandering around on the way back from the pizza joint, and [name] was just sitting out front."

    #gregg "Oops, that's my fault. I shoulda been waiting out there for ya, [name]."
    #gregg "Please accept Angus's pizza as an apology on my behalf."

    #player "Apology accepted."

    #angus "I'm happy I could be of service."

    #"Angus slides the pizza onto a table and opens a cabinet to grab some paper plates and plastic cups while Gregg pulls a 2-liter bottle of soda out from a mini fridge in the corner."
    #"Meanwhile Germ sneaks away to the television and unzips his bag."

    #germ "I'm gonna set up the games."

    #angus "I'll get you a plate, Germ."

    #germ "Thanks."

    #angus "[name], you can just set your backpack down wherever, you know."

    #player "Oh right, Gregg left his tools at my place so I brought 'em over."

    #"You take off the backpack and hand it to Gregg."

    #gregg "Aww, thanks for not stealing them!"

    #"He carelessly tosses it against the wall beside the couch."

    #player "Anytime."

    #"Angus opens up the pizza box and hands you a plate."

    #angus "Guests first."

    #player "You don't have to tell me twice!"

    #"You grin and take a couple slices then move over so Gregg can get some while you pour yourself a drink."

    #gregg "So you rode your motorcycle here right? How's she run?"

    #player "Pretty good once I got some fuel in her."

    #angus "I'm glad Gregg could help you fix her up."

    #gregg "And that she didn't explode."

    #"Angus fills up a plate for Germ, then takes the remainder of the pizza for himself."

    #angus "Gregg, could you get drinks for me and Germ?"

    #gregg "Sure thing!"

    #hide angus
    #hide gregg
    #with dissolve

    #"Gregg pours extra drinks as you and Angus make your way to the couch."
    #"Germ is crouched by the TV hooking up the connectors to the very outdated cube shaped console sitting on the floor."
    #"Angus gives Germ his plate and grabs a controller for you, Gregg, and himself."

    #show angus neutral at right:
    #    yalign angusheight
    #    xalign 1.1
    #show germ neutral flip at left:
    #    yalign germheight
    #    xalign -.02
    #with dissolve

    #angus "Thanks for bringing your console, Germ. I'll take the busted controller this time."

    #germ "If you insist."

    #"Gregg comes by shortly after and sets the drinks on a small table then sits on the couch with his plate in his lap."

    #show gregg neutral:
    #    yalign greggheight - .5
    #    xalign .7
    #with dissolve

    #gregg "Angus and I had to sell our consoles when we moved, [name]. We were very sad."

    #angus "I mostly play on PC."

    #gregg "*I* was very sad."

    #player "Where'd you move from?"

    #angus "Bright Harbor."

    #if newname.upper() == "SCOTT":
    #    player "Ah right, you mentioned living in Bright Harbor before."
    #if newname.upper() == "ALEC":
    #    player "Ah right, you mentioned living in Bright Harbor before."
    #if newname.upper() == "BETH":
    #    player "Ah right, you mentioned living in Bright Harbor before."
    #if newname.upper() == "BETHANY":
    #    player "Ah right, you mentioned living in Bright Harbor before."

    #gregg "We used to live here in Possum Springs, then moved to Bright Harbor, then back here."

    #"Sounds like the two of them have some history going pretty far back."
    #"It just now occurs to you that they might be more than just friends."

    #player "Sorry if this is a dumb question but are you two... together?"

    #"Gregg snuggles up to Angus, who leans his head on him."

    #gregg "Yup! "

    #angus "I can barely remember a time when I wasn't with Gregg."

    #germ "*Ahem*"

    #"Germ turns to you with two game cases in his hands."

    #germ "What game should we play?"

    #gregg "You decide, [name]."

    #menu:
    #    "The platformer fighting game.":
    #        $ gameChoice = "fighting"
    #        "You point at the fighting game."
    #    "The board-based party game.":
    #        $ gameChoice = "party"
    #        "You point at the party game."
    #player "That one."

    #germ "K."

    #"He takes the undersized disc and pops it into the console."
    #"Germ opts to stay sitting on the floor, while you, Gregg, and Angus fill up the couch. You all enjoy a few bites of pizza while the intro video plays."

    #germ "This is the like, newest game I have."

    #gregg "Isn't this game 20 years old?"

    #germ "Yup!"

    #"Germ hits start and sets up the game."

    #angus "Ugh, I hate getting grease on the controller."

    #gregg "That's what pants are for."

    #"Gregg wipes his paws on his pants."

    #angus "Be right back, I'm gonna grab some napkins."

    #"Angus gets up and steps over the wires on the way to the table."
    #"He comes back with a stack of napkins and hands them out to everyone before sitting back down."

    #gregg "Ready?"

    #angus "Yeah."

    #"You all pick a character and begin a round."

    #if gameChoice == "fighting":

    #    "Germ is surprisingly good at this game. His inputs are efficient and he punishes with grace."
    #    "Despite that, he gives you and the others a fair chance by leaving his defenses open."
    #    "Gregg's aggressive plays allow him to take a couple of lives, at the cost of his character getting killed as well more often #than not."
    #    "Angus seems to be trying to get used to the controls, which only adds to the hilarity when he accidentally knocks someone off #the stage."
    #    "You just try to survive as long as you can and land a few hits whenever you can."
    #    "Unsurprisingly Germ wins the round."#

    #    gregg "Angus. You press X to jump."

    #    "Gregg points to the button on Angus's controller."

    #    angus "Well I wish you would have told me before I died a million times!"

    #    "Germ unassumingly eats his pizza while waiting for the next round to start. Everyone chooses a new character and you go to a random stage."
    #    "As soon as it loads, Gregg immediately jumps off and dies."

    #    gregg "Wait I thought I was the other guy! Restart!"

    #    germ "No redoes."

    #    "Against your better judgement, you decide to taunt Gregg, both in real life and in the game."

    #    player "Yeah, no redoes."

    #    "You blow a raspberry at the fox as your character dances on screen."
    #    "Your in-game taunt ends up getting you killed but thankfully Gregg restrains himself from doing the same to you in reality."
    #    "Angus fares a little better this time."
    #    "You all go easy on him and avoid targeting him unless he engages first. Gregg however is out for blood, doing whatever it takes to get you off the stage."
    #    "Usually Germ ends up finishing both of you off."
    #    "Eventually it's just Germ and Angus left standing. You eat your pizza and watch while Gregg coaches Angus."
    #    "It all comes to an anticlimactic conclusion when Angus misses an easy punish and slowly falls off the bottom of the stage."

    #    gregg "Angus! You have to press B and up at the same time to recover!"

    #    angus "I was doing that!"

    #    gregg "No like, you have to slam the stick like this."

    #    "Gregg demonstrates."

    #    angus "Hrm."

    #    "You start up another round. This time you all have the same idea to gang up on Germ."
    #    "He doesn't seem to mind, and he methodically takes you all on simultaneously."
    #    "You and Gregg manage to get a few combos off on him but once again the match ends with a showdown between Angus and Germ."
    #    "Germ shields against Angus's special then completely whiffs his own attack, giving Angus a chance to launch him off stage."

    #    gregg "OOOOOOOOOOOOOOH! GOT HIM!"

    #    "You all have a laugh at the outcome, especially after Gregg's reaction to it."


    #elif gameChoice == "party":

    #    "You decide on a board then your characters all roll a die and move forward however many spaces."
    #    "Each space you land on has a different effect, whether it's gaining or losing money, acquiring an item, teleporting to a different spot on the board, or a variety of other events."
    #    "And at the end of each turn, you have to play a minigame. Sometimes it's a free-for-all, sometimes it's 2 vs. 2 or 1 vs. 3 with randomly selected teams."
    #    "The game is designed to be impossible to play seriously no matter how hard you try, with all its randomness and janky controls."
    #    "As frustrating as it can be to lose everything because the game felt like it, it's difficult to stay mad when you get your points swapped with the guy in first place on the next turn."
    #    "There's a lot of downtime between minigames since you just have to press a button to roll the die and watch the game play out, giving you ample time to munch on your pizza."
    #    "Germ is such a pro at this game he eats his while playing the minigames."
    #    "Gregg's aggressive plays are counterbalanced by his incredibly bad luck throughout the round, landing him in last place."
    #    "Angus on the other hand plays safely. Perhaps a bit too safely, since he usually ends up missing chances to get points."
    #    "It all culminates in a last minute exchange where Germ risks everything on a duel between you and him. Of course the minigame you have to play for the championship is entirely based on chance."
    #    "Basically you have to jump onto one of the colored quadrants of a carousel and hope it's not the wrong one."
    #    "It spins around for a while and when it stops a monster chained to the wall eats whoever is on the space closest to it."
    #    "If no one is on that spot, you choose another one and it takes another spin. This goes on indefinitely until one of you dies."
    #    "Germ goes first, picking red. You jump on yellow and you both go for a spin."
    #    "When it starts to slow down it looks like Germ is about to lose but he ends up just out of the monster's range when it stops. Death narrowly avoids you as well."
    #    "Now you both hop off and choose a quadrant again."
    #    "You both last a shockingly large number of turns. A statistically improbable amount. But sooner or later one of you has to die."
    #    "The tension is rising. Will you outlast your opponent? Or does he have lady luck on his side tonight? Who will be the one to get eaten?"

    #    gregg "Oh my god, I can't watch."

    #    "Gregg covers his eyes. Germ jumps on the yellow spot. You're up next."

    #    player "Aaah I can't decide!"

    #    "Gregg takes a quick peek to offer his coaching."

    #    gregg "Red!"

    #    angus "Green."

    #    germ "Anything but blue."

    #    "It's all random anyway so you just press A and jump onto whatever space. You end up on blue."
    #    "The merry-go-round spins up and the monster approaches with a hungry look in its eyes."
    #    "As you come to a crawl, Germ coasts right past the kill area. Green and red go by and then finally it stops on blue."
    #    "Your character gets gobbled up and all your points are taken away, just like that."

    #    angus "Ooh!"

    #    "Gregg uncovers his eyes while the next scene loads."

    #    gregg "What happened? Who lost?"

    #    angus "[name] got eaten!"

    #    gregg "OOOOOH! GERM IS THE MASTER OF LUCK!"
    #    gregg "AWOOOOOOOOOO!"

    #    "Gregg sure seems happier about this outcome than Germ does. The final results screen pops up, showing Germ on top and you on bottom."
    #    "Angus got second place and Gregg got third."

    #    player "How did you know it was gonna be blue?"

    #    "Germ shrugs."

    #    germ "I had a feelin.'"


    #fade to black and back

    #hide gregg
    #hide germ
    #hide angus
    #with dissolve

    #stop music fadeout 1.5

    #"The night goes on with the four of you having a good time playing games until Germ says he has to go back home."
    #"At that point you were tired and getting ready to call it quits anyway. You coil up your controller's wire and help Germ pack away his system."
    #"Zipping up his bag, he stands up and waves to you."

    #show germ neutral flip at left:
    #    yalign germheight
    #with dissolve

    #germ "See ya!"

    #hide germ with dissolve

    #"That's all he says before going to leave through the window."
    #"He's certainly an odd guy, but he's very friendly."
    #"Gregg and Angus finish cleaning up the plates and napkins and come up to you."

    #show gregg neutral flip at left:
    #    yalign greggheight
    #show angus neutral at right:
    #    yalign angusheight
    #with dissolve

    #gregg "Whew, that was fun."

    #angus "It sure was."

    #player "Yeah."

    #"There's an uncomfortable silence as nobody is sure what to say and everyone just wants to hurry this up and go to bed."

    #gregg "So Angus, what do you think? Dragons and Dungeons next week?"

    #angus "Sure, that sounds good. Perhaps our new friend would like to join us?"

    #player "I'd be down for that. Just have to check my schedule first."

    #angus "Ah, the persistent problem of finding a time where everyone is available."

    #gregg "No problem dude, just let us know when you're free and we'll work something out."

    #angus "Do you use Chattrbox by any chance? We could coordinate a date on there."

    #player "Yeah, hold on."

    #"You pull out your phone and exchange contact info with Angus."
    #"From there, you thank him and Gregg for the pizza and say your goodbyes before climbing out the window and going down the fire escape."

    #hide gregg
    #hide angus
    #with dissolve

    #scene bg parkdark with dissolve

    "It was refreshing to hang out with a group again."
    "Gregg's upbeat personality is fun to be around, and Angus is a really sweet guy."
    "It's hard to pin down how you really feel about Germ since he was so quiet, but he seems cool."
    "You hop onto your bike and ride back home, reflecting on how much your life has changed in just a few short days."
    "You're enjoying a fresh independent lifestyle but you're also making new friends and coming out of your shell. It feels good."

    scene bg home_interior_night with fade

    "When you arrive at home, you notice both Gregg and Angus sent you a message on Chattrbox."

    gregg "Awesome night dude, can't wait to hang again!"
    gregg "I usually get off work at ham panther in the afternoon if you wanna swing by and ride bikes and stuff."

    angus "Just making sure you made it home safely."
    angus "Had a fun night with you all. Come by the bakery anytime if you're ever in the area and just wanna chat or something."
    angus "You won't be a bother, I don't get that many customers."

    "You send them both a short thank you message and let them know you had fun too before turning in for the night."

    scene bg black with fade

    # Day 4, saturday
    $ currentDay = 4
    $ currentDate = "December 4"

    play music "music/home_again.mp3" fadein 1.0
    scene bg home_interior_day with fade

    "It's been a few days since you moved in and you've just about settled into your new life."
    "Most of the anxiety has melted away, and you're now comfortable living as you see fit and taking things at your own pace."
    "This morning you help yourself to a large breakfast, a long hot shower, and plenty of free time to browse the web."
    "Sitting around all day can get kinda boring though."
    "Maybe you should see if Gregg or Angus are free?"
    "Nah, don't want to seem too clingy."
    "You could explore town a bit. There's still a lot you've yet to see."
    "But where exactly would you go?"
    "You pace around the house pondering this question and wind up in what must have been the smoking room, judging by the stench of cigarette smoke permeating the air even after all these years."
    "You thought these things went out of style a century ago but here we are."
    "Not like a little smoke bothers you at this point though."
    "You recline in one of the big fancy chairs in the room and close your eyes."
    "Maybe you'll just nap away the boredom."
    "..."
    "No, this is too boring."
    "Your hand wanders over to the side table and picks up the book that was resting on it."
    "You lazily turn your head to the side and read the title."
    "\"Cryptids of the Western Hemisphere.\""
    "Opening it up to the bookmarked page, you find an article on the Jersey Devil, a weird skinny goat thing with wings."
    "The paranormal sure loves its goats, doesn't it?"
    "Upon reading further, it appears the Jersey Devil is nothing more than a fabrication by hysterical religious country bumpkins."
    "There's not even anything unique about him, he's just a winged goat with devil connotations who sometimes steals chickens."
    "As you close the book, your fingers brush against a bump on its spine."
    "Turning it over reveals a sticker, not unlike the kind you'd find on a library book."
    "Hold on a second, this *is* a library book!"
    "This thing must have been sitting here overdue for ages!"
    "You should return this to the library soon. You're certain they're just dying to get this book back."
    "They might even be so glad to see it again that they'll waive the late fee."
    "It's not like they could charge you a fee if even they wanted to, right?"
    "It's not your book, you just happened to find it."
    "Regardless of the consequences, you've been given a quest and you intend to see it through to the end."

    stop music fadeout 1.5

    "This is the most excited you've ever been to go to the library."

    scene bg library_floor1 with fade

    play music "music/deweydecimal_loop.mp3" fadein 1.0

    "Possum Springs sure has an impressive library."
    "It's a three story building with lavish old-timey architecture and has been very well maintained."
    "Gargoyles adorn the outside while giant pillars and arches frame the murals on the inside."
    "The interior has been modernized with new carpet and a fresh coat of paint that accentuate the comfortingly dim lighting."
    "You stare at the multitude of books organized neatly on shelves as you walk up to the reception desk. Sitting there is the same bear you met at the cafe the other day."
    "What did the barista call her?"
    "\"Selmers?\""
    "She looks up from writing something in a notepad."

    show selma neutral flip at right with dissolve

    selma "Oh hey, it's you."

    player "Hey."
    player "You're... Selmers, right?"

    "Her carefree demeanor wavers slightly and there's a hint of disdain in her voice."

    selma "That's what most folk call me."
    selma "I remember you from Posspresso but I didn't get your name."

    player "[name]."

    selma "Nice to officially meet you, [name]."
    selma "Welcome to the Possum Springs Public Library. Is there anything I can do for you?"

    "You take one last look at the book in your hand then slide it over the counter."

    player "I found a book that belongs here and wanted to return it."

    "Selmers picks up the book and gives it a look over with an intrigued expression before scanning it into the system."
    "She rotates her chair to face the computer monitor and clicks the mouse a few times."

    selma "Wow, this was checked out way before I even started working here."
    selma "Where'd you find this?"

    player "It was uhh..."

    menu:
        "Lying at the bottom of a well":
            player "...lying at the bottom of a well."
        "Left in an abandoned house":
            player "...left in an abandoned house."
        "Sitting on a bench":
            player "...sitting on a bench."

    #suspicious selma sprite goes here
    selma "Hmm."

    #back to normal sprite
    selma "That explains why it never found its way back here until now. Glad you returned it, it's the only copy we had."

    player "I don't have to pay the late fee, do I?"

    "That gets a chuckle out of her as she sets the book aside."

    selma "Naw, consider it on the house. It was probably written off as lost forever, so thanks for bringing it back."

    player "No problem."

    selma "Will that be all? Or would you like to get a library card while you're here?"

    "You raise a brow."

    player "How'd you know I didn't have one?"

    selma "I know everyone who has one."
    selma "Possum Springs is a small town and the number of people here who have a library card in 2021 is even smaller."

    player "Oh."
    player "Well since I'm here, I might as well."

    selma "Aight. Just need you to fill out this form and show me a valid ID."

    "She pulls a sheet of paper out from a filing cabinet and pushes it toward you."
    "You grab a pen from the holder and quickly fill it out."
    "Once you're done, you pull out your driver's license and pass both it and the sheet back to Selmers."

    selma "K, just have to type this in real quick..."

    "She looks over your license and makes a few keystrokes before handing it back."

    selma "...and now all of this..."

    "She waves the application form in the air."

    selma "...then scan it in and print your card from the office."
    selma "You're welcome to explore and find some books to check out while I do that. I'll have your card ready by the time you're done."

    player "Ok! Be back in a bit."

    hide selma with dissolve

    "You leave her to her work and go over to the bookshelves across the room, skimming over book titles without really reading them."
    "You're not looking for anything in particular but maybe something will grab your attention."
    "Nope, nothing here stands out."
    "That elevator in the corner of your eye however is a different story."
    "This floor seems to be dedicated to boring nonfiction, so the fiction section must be up above."
    "That's probably where that book you just returned will get shelved. You wonder if there are any others like it your father might have checked out as well."
    "It's kinda weird. Like you're retracing the footsteps your father took at some point."
    "You feel like you're following a treasure map and slowly piecing together his interests along the way."
    "It's neat seeing what he was like, but it also fills you with remorse for not getting to know him better while he was alive."
    "He'll always be some vague idea of a man in your mind and not someone you had a real bond with."
    "You shake off the feelings bubbling inside you and go call down the elevator."

    stop music fadeout 1.0

    "You've kind of lost interest in the books around you but you still want to finish exploring the library at least."
    "The doors open with a mechanical grinding sound and you ride up to the second floor."

    play music "music/Stagnant_Tone-down.mp3" fadein 2.0

    "Here the walls are painted a salmon pink and minty green and the lights are brighter. It no longer has that regal feeling of the first floor, but it's still warm and comforting here."
    "Desks with computers line the nearest wall and lead into the children's book section, as evidenced by the Charity Bearity mural thing in the corner."
    "You turn away from it and head down an aisle more suited to your age, where you spend some time reading titles and a few back cover descriptions to get your mind off things."
    "Your browsing leads you down each aisle until you reach the last one, where you discover a young mouse sitting on the floor among a pile of books."
    "She seems to be so engrossed in the book in her hands, she doesn't notice of your presence."
    "You consider leaving so as to not disturb her, but then you spot the poorly lit sign indicating that this is the horror section."
    "This would be where where the cryptids book and any others similar to it would be found, right?"
    "You curiously enter the aisle and make your way through it, scouring the titles."
    "You keep an eye out for anything related to cryptids, trying not to make any noise."
    "As you're perusing a shelf, you feel your leg bump into something and hear a startled squeak from beside you."

    show lori anxious3 at left with dissolve:
        xzoom -1

    "You look down and see the mouse girl pressed up against the bookshelf, frozen in place with the look of a deer caught in the headlights."
    "You step back and clear your throat, about to say \"Excuse me\" when suddenly she lets out the breath she'd been holding in."

    show lori breath flip

    lori "*Huff huff huff* Sorry, sorry!"

    show lori sad2 flip

    "She hastily shovels her books aside so you can get past."

    player "No, I'm the one who should be apologizing..."

    show lori anxious3 flip

    "She glances back up to you."

    lori "Wait a minute... Haven't I seen you before?"

    "Your memory finally catches up and you recognize her as the girl who was listening to that weird music on the ride into town."

    lori "You were on the bus the other day, weren't you?"

    # if player asked her to turn down music and was rude:
    if loriInteractionRude == True:

        player "Oh yeah, I remember you!"
        player "I think your music is what's been giving me nightmares lately."

        show lori sad flip

        lori "I just keep getting in your way I guess..."

        "She mumbles, looking away."
        "You shrink down, realizing how rude you're being."
        "You should try being more amicable."
        "And if that doesn't work, you could always just leave her alone."
        "The girl clears her throat and looks back up to you."

        show lori anxious2 flip

        lori "So are you visiting Possum Springs or something?"

        player "I just moved in actually."
        player "My name's [name]."

        lori "Lori."

        "You squat down and crane your neck to read the titles of the books in her little pile."

        player "Whatcha reading?"

        show lori neutral flip

        "She seems to lighten up in response to your interest in her reading material."

        lori "Oh these? Just some spooky stories to read in the dark."

        player "You a big horror fan?"

        lori "Well, I *am* going to film school to make horror movies."

        player "Really? What kind of movies do you watch?"

        show lori nervous2 flip

        lori "Uh, scary ones? Ones about existential dread and incomprehensible terrors mostly but I also watch a ton of monster movies."

        player "Nice! That reminds me, I just returned a book on monsters. \"Cryptids of the Western Hemisphere\" is what it was called I think."

        show lori neutral flip

        "Lori's eyes go wide in excitement."

        lori "I've been looking for that book for forever! I used to check it out all the time when I was a kid!"
        lori "It's kind of a cliché but my favorite cryptid is the skinwalker. The stories about them always felt the most realistic, even if they did get samey."

        player "Yeah? Mine's uh, the Jersey Devil. It's supposed to live around this area haha."

        lori "That's true!"
        lori "I tried hunting for it when I was younger. I'm still not convinced it won't show up out of nowhere one day."

        "You can tell she's really into this kind of stuff. Her ears are perked up and her voice is eager to go on and on about it."
        "You listen to her ramble about scary things, just smiling and nodding your head until she asks a question."

        lori "Hey, have you seen the movie The Nightmare Before Longest Night?"
        lori "Some friends of mine are throwing a little party this evening at the bakery and we're gonna watch it."
        lori "And I figured since you're new in town and like spooky things you might wanna come?"

        player "Sure, that'll be fun!"

        lori "Awesome! See you there!"

        player "You bet!"
        player "I guess I'll let you get back to your books now. See you later!"



    # if player changed seats without talking to her
    if loriInteractionNull == True:

        player "Oh yeah, I remember you!"
        player "Do you live here? I just moved in the other day."

        show lori neutral flip

        lori "Yup! Been here my whole life til I started going to film school a few months ago. I'm here on break now."

        player "Nice! What kind of films do you like?"

        lori "Most kinds, but horror in particular. Like, existential dread and incomprehensible terrors but regular monster movies are cool too!"

        player "Yeah I noticed you have a knack for horror. Funny enough, I just got finished returning a book on cryptids."

        "You squat down and pick up a book from the pile scattered on the floor, reading the title. \"Picnic by the Roadside.\""

        lori "It wouldn't happen to have been \"Cryptids of the Western Hemisphere\" would it?"

        player "How'd you know?"

        lori "I've been looking for that book forever! I used to check it out all the time as a kid but I haven't seen it in a while. It's one of the best encyclopedias on cryptids!"

        player "Hopefully they'll put it on the shelf soon and you can snag it before anyone else does."

        lori "That would make my day."
        lori "What's your favorite cryptid?"
        lori "I know it's kind of cliché but mine's the skinwalker. The stories about them always felt the most realistic, even if they did get samey."

        player "Yeah? Mine's uh, the Jersey Devil. It's supposed to live around this area haha."

        lori "That's true!"
        lori "I tried hunting for it when I was younger. I'm still not convinced it won't show up out of nowhere one day."

        "You can tell she's really into this kind of stuff. Her ears are perked up and her voice is eager to go on and on about it."
        "You listen to her ramble about scary things, just smiling and nodding your head until she asks a question."

        lori "Hey, have you seen the movie The Nightmare Before Longest Night?"
        lori "Some friends of mine are throwing a little party this evening at the bakery and we're gonna watch it."
        lori "And I figured since you're new in town and like spooky things you might wanna come?"

        player "Sure, that'll be fun!"

        lori "Awesome!"
        lori "Before I forget, what's your name?"

        player "[name]."

        lori "Lori."

        player "Nice to meet you Lori!"

        lori "Likewise!"

        player "I guess I'll let you get back to your books now. See you later!"


    # if player asked about the music and was bold
    if loriInteractionBold == True:

        player "Hey! What a coincidence seeing you here!"

        lori "Not really. Possum Springs is like, really small. We would have run into each other sooner or later."

        player "Seems like it! I don't believe I caught your name earlier. I'm [name]."

        lori "Nice to meet you again, [name]! I'm Lori!"

        player "I still haven't gotten around to listening to that album yet but it's on my to do list. Been adjusting after moving in."

        show lori neutral flip

        lori "I get that, resettling and stuff. I've been away from home for a while and I'm getting used to living next to train tracks again."

        player "Oof. I live a little bit away from them and have a bunch of trees to block out most of the noise but the trains are still pretty loud."

        lori "To think I used to play and take naps and read books right between the tracks."

        player "That sounds... dangerous."

        lori "It is."

        player "Huh."

        "You squat down and take a look at some of the books strewn about. Most of them are from this aisle apparently."

        player "So are you reading here?"

        lori "Just some spooky stories to read in the dark. It's technically studying material."

        player "Studying for what?"

        lori "Film school assignments!"

        "She holds up a book, \"Monster Design in Cinema.\""

        player "Cool! That reminds me, I just returned an encyclopedia on weird creatures. \"Cryptids of the Western Hemisphere\" is what it was called I think."

        "Lori's eyes go wide in excitement."

        lori "I've been looking for that book for forever! I used to check it out all the time when I was a kid!"
        lori "It's kind of a cliché but my favorite cryptid is the skinwalker. The stories about them always felt the most realistic, even if they did get samey."

        player "Yeah? Mine's uh, the Jersey Devil. It's supposed to live around this area haha."

        lori "That's true!"
        lori "I tried hunting for it when I was younger. I'm still not convinced it won't show up out of nowhere one day."

        "You can tell she's really into this kind of stuff. Her ears are perked up and her voice is eager to go on and on about it."
        "You listen to her ramble about scary things, just smiling and nodding your head until she asks a question."

        lori "Hey, have you seen the movie The Nightmare Before Longest Night?"
        lori "Some friends of mine are throwing a little party this evening at the bakery and we're gonna watch it."
        lori "And I figured since you're new in town and like spooky things you might wanna come?"

        player "Sure, that'll be fun!"

        lori "Awesome!"

        player "I guess I'll let you get back to your books now. See you later!"



    "You give her a friendly smile and stand back up."

    lori "Bye!"

    "She waves a tiny paw at you then resumes reading while you scoot around her and out of the aisle."

    hide lori with dissolve

    "Where to now?"
    "There's still another floor to explore. You've just about exhausted your options on this floor so it's time to head up."
    "The elevator rattles louder this time as its doors open and close, making you question just how safe this thing really is."

    stop music fadeout 2.0

    "Safe enough to get you to the third floor unharmed is the answer you get soon enough."
    "Dust floats through the air, tickling your nostrils as soon as the elevator doors open."
    "The lighting on this floor is much more subdued and the walls are painted a dark blue. "
    "You creep forward, wondering if there's anybody up here."
    "It's dead silent save for the sounds of the heating unit. You pass by each aisle and confirm you're alone."
    "Come to think of it, this whole building is pretty empty. It's just you, Selmers, and Lori, each on different floors."
    "Selmers was right about not many people using the library these days."
    "Getting back to the matter at hand, you wonder what the purpose of this floor in particular is."
    "A quick look around reveals it's for really old media and records apparently."
    "Things like last century's yearbooks, outdated almanacs, newspaper clippings, and even some tomes that remind you of the ones back home."
    "As you're scouting the area, something catches your eye: a big glowing box on one of the desks."
    "It looks like one of those old tube computer monitors, but even bulkier."
    "And warmer."
    "You can feel the heat coming off it from a few feet away."
    "This must be one of those microfilm projector things."
    "A microfiche, you think it's called."
    "There's no film loaded into it though so there's nothing on the screen."
    "Someone must have forgotten to turn it off when they used it last."
    "You flip the power switch off, plunging the room into near total darkness."
    "Welp, that about concludes your tour of the library today."
    "You make your way back to the elevator and return to the ground floor. Selmers should have your card ready by now."
    "As you walk up to the counter empty handed, the bear looks up with a casual grin."

    show selma neutral at right with dissolve

    selma "Find what you were looking for?"

    player "Not quite, but that's more my fault than the library's."

    selma "If you're looking for a book in particular, I can help you find it if we have it."

    player "Thanks, I'll keep that in mind."

    selma "I also got your card printed. Here ya go."

    "She slides the card over the counter."

    selma "It expires three years from today, or one year after your last check out. Whichever comes first."

    player "Thank you!"

    selma "Wish I got paid commission for these. But I don't. Haha."

    player "How often do you convince someone to sign up for a card?"

    selma "Almost as often as someone new comes in."
    selma "I have experience in sales."

    player "Wow."

    selma "And if you don't mind me trying to sell you on something else, the library's hosting an event this coming Tuesday at 4:00PM where we read books aloud to small children."
    selma "We're short on staff so we're asking for volunteers."
    selma "It'd be nice if you could, y'know, come and read for the kids. We'll have juice and cookies too."

    menu:
        "I'll think about it.":
            $ selmaNeutral = True

            player "I'll think about it."

            selma "That's better than a flat out no I guess."

            "You can't help but feel a twinge of guilt. You look away momentarily, mulling over whether you should go or not."

            selma "Anyway is that all I can do for you?"

            "You refocus your attention back to her."

            player "Oh, yeah. Thanks, have a nice day."

            selma "You too."

        "Sorry, don't think I can make it.":
            $ selmaBad = True

            player "Sorry, don't think I can make it."

            selma "I expected as much. Don't worry, we'll find someone else."
            selma "Or I'll just pull double duty like last time."

            player "That understaffed, huh?"

            selma "Yup."

            "You can't help but feel some sympathy toward her. Maybe you could come out and help for an hour or two."

            selma "Well if you change your mind, let me know."

            player "Will do."

            selma "Anyway, do you need assistance with anything else?"

            player "Nope. I'm good, thanks."

            selma "K. Have a nice day."

            player "You too."

        "I'd be happy to!":
            player "I'd be happy to!"
            $ selmaGood = True

            selma "That- was not the response I was expecting. You sure? Those kids can be real punks sometimes."

            player "It's no trouble, I can handle them."

            selma "If you say so. Let me know if you change your mind later."

            player "Sure."

            selma "Thanks though. It means a lot and it would be cool seeing you here."

            "She has a genuinely appreciative smile on her face, but there's something else behind it you can't quite grasp."
            "Does she just want you to come help out or is there more to it?"

            selma "Anyway is there anything else I can do for you?"

            "You refocus your attention back to the conversation at hand."

            player "Oh yeah, no I'm good."

            selma "Ok. Hope you have a nice day!"

            player "Thanks, you too!"

    hide selma with dissolve

    scene bg bakery with dissolve

    "On your way home, you think about how surprisingly lively Possum Springs is."
    "Already you've been invited to several events and met some pretty cool people."
    "You never imagined how much happier you'd be living out here."
    "When you get to your house, you decide to make some lunch and chill out until evening."
    "Nightfall creeps up on you quickly and you suddenly realize you don't have a specific time to be at the bakery."
    "Wait a minute, bakery? Like the one Gregg and Angus live above?"
    "Surely they'd know something about a party underneath their apartment."
    "You shoot them both a text and wait a while."
    "No response."
    "Screw it, you should just head out now. Better to be early than to arrive after the party's over."
    "You hastily freshen up, then hop on your bike and ride into town."
    "As you pull up to the store, you hear the final notes of a song blasting from inside, rattling the windows."
    "Bright light leaking through inhibits your view of the interior until you step inside and your eyes adjust."

    play music "music/whenskiesclear_loop.mp3" fadein .5

    "Standing on the stage are some familiar faces who are just as shocked to see you as you are to find them here."
    "Gregg with a guitar, Angus at the mic, Mae on bass, and Bea from the hardware store next to a keyboard and laptop."

    show bea at right:
        xalign 2.0

    show angus at left:
        xalign -1.0

    "On the wall behind them is a DVD player screensaver being displayed from a projector mounted on the ceiling."

    show lori neutral at right:
        yalign loriheight
        xalign 1.02
    with dissolve

    lori "[name]! You made it!"

    "You look to the source of the voice. You didn't even notice the mouse girl sitting at one of the tables. She stands up and runs toward you."

    lori "Sorry I forgot to give you a time to come. To be honest I wasn't sure when we were meeting!"

    player "Uh, it's fine."

    "You're still confused from discovering Gregg and Angus are in a band with Mae and the hardware store girl."

    lori "Guys, this is [name]! [name], that's Gregg, Angus, Mae, and Bea!"

    "She points to each of them as she lists their names."

    player "I've already met everyone, actually."

    "Gregg hops down from the stage with his guitar still strapped over his body."

    show gregg neutral flip at left:
        yalign greggheight
        xalign -.12
    with dissolve

    gregg "Yeah, we played video games and ate pizza the other day."

    show lori breath

    lori "Whaaaaaat? Really??"

    show bea neutral at right:
        yalign beaheight
        xalign .9
    with moveinright

    bea "Mae and I saw them at the Ol' Pickaxe too."

    lori "Oh gosh, I-I thought..."

    "Lori trails off and shrinks down in shame."

    show angus neutral flip at left
    with moveinleft

    angus "It's cool. [name] is cool."

    lori "Sorry for inviting [name] without knowing if it was ok... I thought it was going to be a bigger party..."

    gregg "No, it's fine. Tell ya what, we'll go out to eat after putting things away here. You hungry, [name]?"

    player "I could eat."

    bea "I can make time for something quick at the diner. And I can get dinner to-go for my dad while we're there."

    gregg "Cool! Let's pack up and get the heck outta here!"

    "Gregg hops back on stage and kicks open his worn guitar case. Angus, Bea and Mae go ahead and start putting their things away while Lori waits at a table."

    hide lori
    hide gregg
    hide angus
    hide bea
    with dissolve

    show mae neutral at right:
        xalign 1.5

    menu:
        "Offer to help clean":
            #+1 trust

            player "Let me help you with that!"

            show gregg neutral flip at left:
                yalign greggheight
            with dissolve

            gregg "Hm? Oh sure. Can you unplug those amps and put 'em in the storage closet over there?"

            player "'Course!"

            "You readily do as he requested while the others put away their instruments."
            "Angus coils up the mic wire and collapses the tripod while Bea folds up the table her keyboard was on and stuffs the laptop in her bag."
            "Mae strummed on her bass a few times, adjusting the tuning before putting it away in a case and helping out with general cleaning."
            "She was awfully quiet and seemed to keep her distance from you, only occasionally making weird glances in your direction. She whispers something to Bea."
            "You brush it off and finish helping, bumping into Gregg as he stowed the last speaker."

            player "I didn't know you guys were in a band. I thought this was just gonna be a movie party."

            gregg "Is that what Lori told you? We ended up watching the movie early on, then Bea wanted to test a song she's been writing."

            player "Bea writes music?"

            gregg "Yeah, she just finished going to school for that sort of thing."
            gregg "Honestly, I haven't picked up my guitar in ages and kinda suck at playing now."
            gregg "But it was fun getting together and playing again!"

            player "I never would have imagined all you guys were in a band."

            gregg "Believe me, this is the least crazy thing about us."
            gregg "Hey be right back, I need to hit the bathroom."

            hide gregg with dissolve
            show bea neutral at right:
                xalign 2.0

            "The fox locks away all the gear with a key then heads to the back of the building and out the exit door."
            "Rather than question where exactly he's going, you decide to approach Lori who had been seated at a table looking stressed as she scrolls through her phone."

            show lori sad at right:
                yalign loriheight
                xalign 1.06
            with dissolve

            player "You ok?"

            show lori neutral

            lori "Huh? Oh, yeah I'm fine! You guys done?"

            player "I think so. Just waiting on Gregg to get back."

            "You chat with Lori while Mae, Bea and Angus converse amongst themselves."
            "After a minute or so Gregg walks back in and approaches you. The others hop down from the stage and gather around."
            "The crocodile has her bag slung over one shoulder and her keyboard pinned between her arm and her side."

            show bea neutral at right:
                yalign beaheight
                xalign .96
            with moveinright

            bea "Ready to go?"

        "Hang back with Lori":
            $ loriAP = loriAP + 1

            show bea neutral at right:
                xalign 2.0

            "You pull up a seat across from Lori, who looks stressed as she scrolls through her phone."

            show lori sad at right:
                yalign loriheight
                xalign 1.06
            with dissolve

            player "You ok?"

            show lori neutral

            lori "Huh? Oh, yeah I'm fine!"
            lori "...Sorry I made things awkward earlier."

            "You shrug nonchalantly."

            player "Don't worry about it. It all worked out in the end."

            if loriAP > 1:
                lori "Shame you missed out on the movie though... maybe we can watch it together another time?"

                player "I'd love that! It's been ages since I've last seen it!"

                lori "I watch it every year hahaha!"

            else:
                lori "Yeah..."

            "Out of the corner of your eye you see Gregg rush out the exit toward the back of the building while the others finish putting everything away."

            player "Hey so, dumb question, but are they like, in a band?"

            "You gesture toward the group on the stage."

            lori "Oh! Yeah, well, they used to be. But Bea just finished her degree in music studies and wanted to test a song she's been writing so they brought out all their old instruments."

            player "Wow. Did it turn out well?"

            lori "Nnnnot really. Gregg's pretty rusty with his guitar."
            lori "Don't let him know I said that though!"

            "Just then, Gregg returns from whatever it was he was doing and everyone gathers around the table you and Lori are seated at."
            "Bea has her bag slung over one shoulder and her keyboard pinned between her arm and her side."

            show bea neutral at right:
                yalign beaheight
                xalign .96
            with moveinright

            bea "Everything's packed up. You ready to go?"


    show angus neutral at left:
        yalign angusheight
        xalign -1.0

    show gregg neutral flip at left:
        yalign greggheight
        xalign -.2
    with moveinleft

    gregg "Yup!"

    show angus neutral flip at left:
        yalign angusheight
        xalign .12
    with moveinleft

    angus "Indeed!"

    lori "Mh-hm!"

    player "Yeah!"

    show mae sad1 at right:
        yalign maeheight
        xalign .67
    with moveinright

    mae "Sure."

    "Bea adjusts her grip on the keyboard and turns toward the door."

    bea "Let's roll."

    hide mae
    hide gregg
    hide bea
    hide angus
    hide lori
    with dissolve

    "You all file out through the doorway and into the cold dark street."

    stop music fadeout 1.5

    show bea neutral at right:
        yalign beaheight
        xalign 1.08
    with dissolve

    "Bea turns toward the group and does a headcount."

    bea "There's too many of us to fit in my car so I guess we're walking."

    show angus neutral flip at left:
        yalign angusheight
        xalign .08
    show gregg neutral flip at left:
        yalign greggheight
        xalign -.1
    with dissolve

    gregg "I volunteer to sit in Angus's lap to make space."

    bea "That would work if I didn't have a big box of records in the passenger seat, and a keyboard soon to be occupying the back."

    gregg "Aww."

    hide gregg
    hide angus
    with dissolve

    bea "Be right back."

    hide bea with dissolve

    "Bea starts toward the Ol' Pickaxe where her car is parked."

    show mae panic flip at left:
        yalign maeheight
    with dissolve

    mae "I'll go with you!"

    "Mae hastily runs off to catch up to Bea."

    show mae at right:
        yalign maeheight
        xalign 2.0
    with move
    show bea at right:
        yalign beaheight
        xalign 2.0

    "You consider going with them just so your body can warm up by walking but the moment of opportunity has already passed."
    "You're all just standing here with nothing else to do so why not break the ice?"

    show angus neutral flip at left:
        yalign angusheight
        xalign .0
    show gregg neutral flip at left:
        yalign greggheight
        xalign -.12
    show lori neutral at right:
        yalign loriheight
        xalign 1.06
    with dissolve

    player "So why is there a stage in the middle of the bakery?"

    angus "It's a holdover from the previous business. We used to break in and play music on it way back in the day."
    angus "No need for breaking in now."

    gregg "Lame."

    angus "Nowadays it usually gets used for banquets and whatever other local events need a stage."

    lori "Like the Harfest play!"

    gregg "Yeah, like that thing literally nobody cares about but we still do for some reason."

    "You stand around idly chatting waiting for Mae and Bea to come back."
    "How long does it take to put away a keyboard??"

    show bea neutral at right:
        yalign beaheight
        xalign 1.0
    with moveinright
    show mae sad1 at right:
        yalign maeheight
        xalign .7
    with moveinright

    "Seems Lori was thinking the same thing. When the pair finally return, she makes a quip."

    lori "Did ya get lost along the way?"

    bea "Har har. Come on, we doing this or not?"

    mae "Yeah. Let's go."

    hide gregg
    hide angus
    hide lori
    with dissolve

    "Bea stands between you and Mae as your party advances, footsteps crunching against the snow."
    "While the others joke and converse, you sneak a glance at Mae. You can feel that there's something conflicting her and that she doesn't want to be here."
    "Unfortunately you don't know what you can do about it other than feel bad for her."

    hide bea
    hide mae
    with dissolve

    show mae neutral at right:
        xalign 2.0

    "The diner turns out to only be a few blocks away. It's a repurposed train car with an orange neon sign reading CLIK CLAK DINER."

    show angus neutral left:
        yalign angusheight
        xalign -2.0
    show lori neutral right:
        yalign loriheight
        xalign 2.0

    show gregg neutral flip at left:
        yalign greggheight
        xalign -.15
    with dissolve

    gregg "Here we are!"

    "Gregg holds the door open for everyone. Inside, you're met with a cramped, cluttered space, vaguely reminiscent of Art Deco design, covered with photos, paintings, and other artwork on the walls."
    "You're seated at a booth and given a menu that has the typical diner offerings."
    "Pizza, burgers, bacon and eggs, club sandwiches, and even pierogies. You all make your selections and chat while the food is cooked."

    show bea neutral at right with dissolve:
        yalign beaheight
        xalign 1.18

    bea "So [name], I heard you moved here recently? What are you doing in Possum Springs?"

    player "Eh, just wanted to get away from home, ya know? Move out and be independent and all that stuff."
    player "I have to say, I'm enjoying Possum Springs a lot more than I thought I would."

    bea "Really? Almost everyone I know can't wait to escape from here."

    "A subtle hush falls over the group. Bea quickly changes the topic."

    bea "Anyway, you got a job here yet?"

    player "Nope. Living off of savings at the moment. Why, you know anybody who's hiring?"

    show lori neutral at right:
        yalign loriheight
        xalign .85
    with dissolve

    lori "I could scrounge together something and pay you a little if you help me work on my movie."

    player "You're making a movie?"

    lori "Yup! It's partly a school project but it's also something I just wanna do."
    lori "I'm out in the woods or by the tracks nearly every day if you wanna come and watch or set up equipment or maybe even act in it?"

    player "Sounds spooky. I'll definitely consider it."

    "Lori giggles at your choice of words."

    bea "*Ahem*"
    bea "I could use a hand at the shop if you're interested. Backbreaking work but decent untaxed, under the table pay."

    player "What do I have to do?"

    bea "Lift heavy stuff, maybe direct a customer toward said heavy stuff, and on rare occasion move the heavy stuff to their car."

    player "Noted. I'll consider that as well."

    show angus neutral flip at left:
        yalign angusheight
        xalign .0
    with dissolve

    gregg "I could try putting in a good word for you at Ham Panther. I don't think they're hiring right now though."

    angus "I've got my paws full just trying to pay myself at the bakery so..."

    gregg "Maybe Mae could get you something at the arts council if you're into that."

    "All eyes turn toward an unsuspecting Mae. She looks like she wasn't paying much attention to the conversation and was caught off guard."

    show mae panic at right:
        yalign maeheight
        xalign .7
    with dissolve

    mae "Oh uh, yeah. I teach art stuff at the Deep Hollow County Arts Council on Fridays and Saturdays. Painting, clay sculpting, photography..."

    lori "Mae's the one who taught me how to use a camera!"

    show mae sad1

    "Mae shrugs."

    mae "At this point, Lori's more comfortable with cameras than I am. I just know enough to teach the basics."

    player "Gotchya. I'll check it out if I'm feeling artsy."

    show mae neutral

    "Mae flashes you a forced smile. Luckily the awkward moment is interrupted by the waitress coming by with your food."
    "Food has a way of lightening the mood. Mae relaxes and even becomes more talkative as the evening goes on."
    "Even though your meal isn't very good, you still have a pleasant time with your new friends."
    "Towards the end of the night, Bea gets a box for her leftovers and the waitress drops off the meal she ordered for her father."
    "When it comes time to pay the bill, Gregg insists that he cover for you but you politely decline, knowing you can spare the cash more comfortably."
    "Ironically, Angus is the one to put down his debit card for both himself and Gregg."
    "Bea pays for her own, and Mae asks the waitress to put hers and Lori's meals on one bill."

    show mae blush

    "Lori wordlessly expresses her gratitude by resting her head on Mae's shoulder and wrapping her arm around Mae's. For the first time this night you see Mae smile in earnest."

    #scene transition

    show mae neutral

    "Once you're outside, you all crowd around under a streetlight and discuss your plans for the rest of the night."

    gregg "This was great. We should do this again."

    lori "Yeah, it was awesome seeing you guys playing as a band again!"

    "Bea lights a cigarette."

    bea "Always a joy. But I think I'm gonna go home, relax and watch some TV with my dad now."

    lori "Hmm, yeah I should get home too before my dad starts worrying where I am so late."

    mae "I'll drive you home so you don't have to walk back in the dark Lori."

    lori "Thanks!"

    gregg "Me and Angus will probably watch some streams then go to sleep."

    player "Yeah, sleep sounds good right about now. It was fun hanging out with you all though."

    bea "Before I forget, you have Chattrbox right? Add me and we can talk more about having you work at the Pickaxe."

    lori "Oh and add me too in case you decide to help me out on my film!"

    "You pull out your phone and get their Chattrbox names."
    "You'll have to wait until you have wifi again before it registers but it's no big deal. You pocket your phone and give them a smile."

    player "Sweet. I'm open to just chatting too if you want."

    bea "Sure."

    lori "Of course!"

    hide lori
    hide gregg
    hide angus
    hide bea
    hide mae
    with dissolve

    "You walk as a group back to the bakery before parting ways. Gregg and Angus go around to the back of the building, while Mae, Bea and Lori go to the parking lot by the Ol' Pickaxe."
    "You hop on your motorcycle and rev her up for the trip home, where you promptly get ready for bed."
    "You add Bea and Lori to your Chattrbox then set your phone to 'Do not disturb' mode and fall asleep with your face buried in your pillow."

    scene bg black with fade


label church1:
    # day 5, sunday, dec 5
    scene bg home_interior_day with fade

    "Your first week in Possum Springs has come to a close."
    "Really this is only your sixth day here, but it's Sunday so you're counting it as having been a week."
    "Each new day further cements your routine. Wake up, shower, eat breakfast, play around on the internet for a bit, and so on."
    "The excitement of moving into an unfamiliar town has worn off, yet you still seek the thrills you've felt over the past few days."
    "You should get out of this dusty old house and go on an adventure today."

    #scene bg outsidePlayerHouseSnowClearSky
    play sound "sound/door open and close.mp3"
    scene bg home_exterior_night with fade

    "The snowstorm has finally subsided."
    "The skies are bright and clear once again, but the ground is going to be covered with a thick blanket of snow for a while."
    "That shouldn't hinder your ability to get around though. \nNow then, where shall you go today?"
    "Why not visit the top of that big hill in town? You bet you can see everything in Possum Springs from up there!"

    jump churchScene1

label jobs1:
    # day 6, monday
    $ currentDay = 6
    $ currentDate = "December 6"
    scene bg home_interior_day with fade

    "Another day, a new adventure awaits."
    "Or something like that."
    "Either way, you make yourself presentable and prepare to go out."

    menu:
        "{cps=0}Where do you want to go?{/cps}"
        "Ol' Pickaxe" if workingWithBeaCompleted == False:
            jump workingWithBea
        "Help Lori with film project" if loriHelpCompleted == False:
            jump loriFilm
        "Check out the arts council" if maeArtsCompleted == False:
            jump maeArts
            
      
label day7:
    #day 7, tuesday, dec 7
    #

    #add a random event where you hang out with germ. maybe you see him hauling animal feed across town in a stolen shopping cart, making him look homeless
            
            
            
label jobs2:
    # day 8, wednesday, dec 8
    "Another day, a new adventure awaits."
    "Or something like that."
    "Either way, you make yourself presentable and prepare to go out."

    menu:
        "{cps=0}Where do you want to go?{/cps}"
        "Ol' Pickaxe" if workingWithBeaCompleted == False:
            jump workingWithBea
        "Help Lori with film project" if loriHelpCompleted == False:
            jump loriFilm
        "Check out the arts council" if maeArtsCompleted == False:
            jump maeArts
            
            
            
            
            

    

label day9:
    # day 9, thursday
    $ currentDay = 9
    $ currentDate = "December 9"

    scene bg home_interior_day with fade

    "As you're eating breakfast, a you suddenly feel like you're forgetting something."
    "Wasn't there something you were supposed to do today?"
    "Oh yeah, Selmers is hosting an event at the library this afternoon and asked if you could help out!"
    "Huh?"
    "Your phone just vibrated and a text message appeared on the screen. It's from Lori."
    "It says \"Hey just wanted to let you know me and Gregg are gonna be filming at the historical society this evening if you wanna come help!\""
    "Well shoot, you can't do both."

    menu:
        "{cps=0}Where do you want to go?{/cps}"
        "Library":
            jump selmaLibraryReading
        "Historical Society":
            jump loriGreggHistorical

    label day10a:
    # day 10, friday
    $ currentDay = 10
    $ currentDate = "December 10"

    scene bg home_interior_day with fade

    "Another day, a new adventure awaits."
    "Or something like that."
    "Either way, you make yourself presentable and prepare to go out."

    menu:
        "{cps=0}Where do you want to go?{/cps}"
        "Ol' Pickaxe":
            jump beaAntiqueShop
        "Bakery":
            "to the bakery"
            #visit bakery but are surprised by lack of coffee. learn that they have a deal with posspresso where they don't sell coffee and possprsso doesn't sell certain baked goods. angus mentions his favorite drink there and you offer to get him one in exchange for your confection. at the cafe you find selma, and you can give her your treat as apology for missing the library event
        "Explore town":
            jump maeLoriSleepover

label anotherday:
#another germ scene, he slips on ice, you help him home, visit his animal shelter


    label day10:
        # day 10, thursday
        $ currentDay = 10
        $ currentDate = "December 16"
        
        "Another day, a new adventure awaits."
    "Or something like that."
    "Either way, you make yourself presentable and prepare to go out."

    menu:
        "{cps=0}Where do you want to go?{/cps}"
        "Ol' Pickaxe":
            jump beaAntiqueShop
        "bakery":
            "to the bakery"
            #visit bakery but are surprised by lack of coffee. learn that they have a deal with posspresso where they don't sell coffee and possprsso doesn't sell certain baked goods. angus mentions his favorite drink there and you offer to get him one in exchange for your confection. at the cafe you find selma, and you can give her your treat as apology for missing the library event
        "Explore town":
            jump maeLoriSleepover
            


label day:
    #farmer's market?
    #group hangout at ??? with ???
    #germ is invited but couldn't make it
            
            
            
            
            
            
            
            
            
            
            
label nextday:

    menu:
        "Play video games with Gregg and Angus":
            jump dragonsDungeons1
        "Train Tracks" if loriFilmCompleted == False:
            jump loriFilm


    label day11:
        # day 11, friday
        $ currentDay = 11
        $ currentDate = "December 17"

        jump posspresso_group1

    label day12:
        # day 12, saturday
        $ currentDay = 12
        $ currentDate = "December 18"

        menu:
            "Arts Council":
                jump artsCouncilScene
            "Train Tracks" if loriFilmCompleted == False:
                jump loriFilm
            "DnD with Gregg and Angus" if dragonsDungeons1Completed == False:
                jump dragonsDungeons1


    label day13:
        # day 13, sunday
        $ currentDay = 13
        $ currentDate = "December 19"

        menu:
            "Church":
                jump churchWeek2
            "Ol' Pickaxe":
                scene bg pickaxe with fade

                play music "music/picknaxe_loop.mp3" fadein 1.0

                "You head down to the hardware store and find Bea manning the counter."

                show bea apron at right with dissolve:
                    yalign beaheight

                bea "Hey [name]. Me and Selma are going out to the Arts Council tonight for some poetry. You wanna come?"

                player "Sure!"

                bea "Meet us there at around 7:00, k?"

                player "Sounds good. See you then!"

                stop music fadeout 2.0

                bea "See ya."

                hide bea with dissolve

                jump beaSelmaPoetry
            #"Library":
                #jump beaSelmaPoetry
            #give option to go to library as well, selma tells invites player to poetry thing

    label day14:
        # day 14, monday
        $ currentDay = 14
        $ currentDate = "December 20"

        scene bg home_interior_day with fade

        "Welp, it's Longest Night Eve. Better write a scene for this."


    label day15:
        # day 15, tuesday
        $ currentDay = 15
        $ currentDate = "December 21"

        jump longestNightOpening

    label day16:
        # day 16, wednesday
        $ currentDay = 16
        $ currentDate = "December 22"

        jump endDemo


    label olPickaxeWeek1:
        # make beaSelmaPoetry available only after the cafe meetup

        scene bg pickaxe with fade

        play music "music/picknaxe_loop.mp3" fadein 1.0

        "You head down to the hardware store and find Bea manning the counter."

        show bea apron at right with dissolve:
            yalign beaheight

        bea "Hey [name]. Me and Selma are going out to the Arts Council tonight for some poetry. You wanna come?"

        player "Sure!"

        bea "Meet us there at around 7:00, k?"

        player "Sounds good. See you then!"

        stop music fadeout 2.0

        bea "See ya."

        hide bea with dissolve

        jump beaSelmaPoetry


        #menu:
            #"Sure!":

                #player "Sure!"

                #bea "Meet us there at around 7:00, k?"

                #player "Sounds good. See you then!"

                #stop music fadeout 2.0

                #bea "See ya."

                #hide bea with dissolve



                #jump beaSelmaPoetry
            #"Nope.":

                #player "Sorry, I think I'm busy around that time."

                #bea "No big deal. See ya around."

                #stop music fadeout 2.0

                #player "Bye!"

                #hide bea with dissolve

    label endDemo:
        scene bg black with fade
        "That concludes the demo! Thanks so much for playing! Stay tuned for more to come!"
        "Credits"
        "Project Management: Fishy"
        "Writing: Kodiak, Ferrin, MegaBirb, Tymime, Fishy, V-25 Sean"
        "Programming: Kodiak"
        "Music: Tymime, EightbyteOwl, Elias Lang, Ferrin, JunoDeer"
        "Character Sprites: Equestria Prevails, TRPCWings, Balderdash, LataviaBoy1999, Tymime, Starxeil, Lauri, EightbyteOwl"
        "Background Art: Eightbyteowl, Coldiru, Nukathefloof, TRPCWings, Balderdash, LataviaBoy1999, Careybou, WorkerQ, KDD, Lauri"
        "Licensing info: The contents of this game are licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 License	https://creativecommons.org/licenses/by-nc-sa/3.0/us/"
        return

    return
