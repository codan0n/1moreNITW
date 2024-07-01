# This is the main script called upon when a new game is selected

#### Define characters
define mae = Character("Mae : ", color="#ff3f54")
define bea = Character("Bea : ", color="#4f7175")
define gregg = Character("Gregg: ", color="#e8971a")
define angus = Character("Angus: ", color="#6fbc92")
define lori = Character("Lori: ", color="#c1e0fc")
define germ = Character("Germ: ", color="#a384e5")
define selma = Character("Selmers : ", color="#d15384")
define narrator = Character("")
define candy = Character("Candy : ")
define stan = Character("Stan : ")
define name = Character("You : ")
define driver = Character("Driver : ")
define trish = Character("??? : ")
define harleyunknown = Character("??? : ")
define harley = Character("Harley : ")
define receptionist = Character("??? : ")
define marcie = Character("Marcie : ")
define kid = Character("Kid : ")
define cashier = Character("Cashier : ")
define pa = Character("PA : ")
define raccoon = Character("Raccoon : ")
define danny = Character("Danny : ")
define madamespectre = Character("Madame Spectre : ")


label before_main_menu:
    python:
        from enum import Enum
        
        drinkenum = Enum('drinkenum', 'MOCHA SPECIAL AMERICANO CAPPUCCINO')
        animalenum = Enum('animalenum', 'REPTILE BIRD MAMMAL')
        hobbyenum = Enum('hobbyenum', 'MOVIES BOOKS MUSIC')
    
    return

#init python:
#    from enum import Enum
#
#    #testenum = Enum('testenum', 'ORANGE APPLE GRAPE')

label after_load:   
    init python:
        from enum import Enum
        
        drinkenum = Enum('drinkenum', 'MOCHA SPECIAL AMERICANO CAPPUCCINO')
        animalenum = Enum('animalenum', 'REPTILE BIRD MAMMAL')
        hobbyenum = Enum('hobbyenum', 'MOVIES BOOKS MUSIC')
    
    return


label start:

    ###testing
    
    #$ loriAP = 10
    #$ maeAP = 10
    #$ beaAP = 30
    #
    #$ highestAP = max(loriAP, maeAP, beaAP)
    #
    #"highest AP is [highestAP]"
    #
    #if highestAP == loriAP:
    #    "lori is best girl"
    #elif highestAP == maeAP:
    #    "mae is best girl"
    #elif highestAP == beaAP:
    #    "bea is best girl"

    #### variables

    #### misc
    #$ currentDate = "December 1"
    $ currentDay = 1
    $ weekNumber = 1
    $ gender = ""

    #### character affinity
    $ maeAP = 0
    $ beaAP = 0
    $ greggAP = 0
    $ angusAP = 0
    $ loriAP = 0
    $ selmaAP = 0
    $ germAP = 0

    #### personality points
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

    #### scene specific variables
    $ libraryCard = False
    $ bakeryVisited = False
    $ tgInvite = False
    $ tgFailsafe = False
    $ exploredHouse = False
    $ hasKey = False
    $ doorStuck = False
    $ hasCoffee = False    
    $ hasShedKey = False
    $ seenFlyer = False
    $ foundBandGig = False
    $ haveOverdueBook = False
    $ cinnamonRoll = False
    $ dayWalletFound = 0
    $ bandGig1Complete = False
    
    #### quest started status
    $ beaQuestStarted = False
    $ bikeQuestStarted = False
    $ libraryQuestStarted = False
    $ selmaQuestStarted = False
    $ officeQuestStarted = False
    
    #### quest status
    $ beaQuestBakery = False
    $ beaQuestPosspresso = False

    #### quest completion status
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
    $ artsCouncilCompleted = False
    $ beaQuestComplete = False
    $ bikeQuestComplete = False
    $ libraryQuestComplete = False
    $ selmaQuestComplete = False
    $ officeQuestComplete = False
    
    
    $ metLori = False
    $ metMae = False
    $ metBea = False
    $ metAngus = False
    $ metSelma = False
    $ metGerm = False
    $ metMarcie = False
    $ metCandy = False

    
    $ libraryVisits = 0
    $ posspressoVisits = 0
    
    
    $ libraryGuests = []
    $ posspressoGuests = []
    
    ####events options
    $ houseEventsDay = ["houseOffice", "houseBook", "houseKey"]
    $ houseEventsNight = ["houseOffice", "houseBook", "houseKey"]
    
    $ townEventsDay = ["townGerm1", "townAngus1", "townRooftops1", "townBridge1"]
    $ townEventsNight = [""]

    
    
    
    
    #########testing
    
    #$ pastry = 0
    #
    #python:
    #    from enum import Enum
    #    
    #    #slot = Enum('A', 'B', 'C', 'D', 'E')
    #
    #    #class Weekday(Enum):
    #    #
    #    #    MONDAY = 1
    #    #
    #    #    TUESDAY = 2
    #    #
    #    #    WEDNESDAY = 3
    #    #
    #    #    THURSDAY = 4
    #    #
    #    #    FRIDAY = 5
    #    #
    #    #    SATURDAY = 6
    #    #
    #    #    SUNDAY = 7
    #    #
    #    #n(str(Weekday.WEDNESDAY.name))
    #    #
    #    #n(str(Weekday(1).name))
    #    #
    #    #i = 2
    #    #
    #    #if i == 1:
    #    #    n(str(Weekday(i).name))
    #    #elif i == 2:
    #    #    n(str(Weekday(i).name))
    #        
    #        
    #    pastryenum = Enum('pastryenum', 'MUFFIN CUPCAKE CROISSANT')
    #        
    #    #later
    #    "later..."
    #    
    #menu:
    #    "What pastry do you want?"
    #    "muffin":
    #        "you have chosen your pastry"
    #        $ pastry = pastryenum.MUFFIN
    #    "cupcake":
    #        "you have chosen your pastry"
    #        $ pastry = pastryenum.CUPCAKE
    #    "croissant":
    #        "you have chosen your pastry"
    #        $ pastry = pastryenum.CROISSANT
    ##python:
    #    #from enum import Enum
    #if pastry == pastryenum.MUFFIN:
    #    "ya got a muffin"
    #elif pastry == pastryenum.CUPCAKE:
    #    "ya got a cupcake"
    #elif pastry == pastryenum.CROISSANT:
    #    "ya got a croissant"
    #else:
    #    "code ain't working"
    #    
    #"fin"

    ######### end testing
    
    
    
    # Start day 1
    
    python:
        from enum import Enum
        

    ####add walking in snow sound effect
    
    scene bg cafe with dissolve

    play sound "sound/storebell.mp3"
    
    ###mention lack of internet at home
    
    "After treking through the snow for what felt like hours, you bask in the warmth and delectable aroma of the cafe, the only one in town if that map you got from the bus station is to be believed."
    "Back home there were so many coffee shops you could simply walk across the street to chill at another one if the one you were sitting in didn't tickle your fancy."
    "Posspresso... That's a new one. Either it's some hick chain you've never heard of or it's a local joint."
    "The interior looks like someone's old home repurposed into a diner, then repurposed into a coffee shop."
    "The picnic table is a nice touch to make the place stand out. As you pass by it, you notice it's covered in etchings of peoples initials and crude sayings."
    "The local artists' amateur paintings and cheap grandma tier wallpaper really brings it all together."
    #nuke possum springs carved into table
    "Dare you say, this place has... soul."
    "Behind the counter, a young feathered lady with brick red feathers smiles and waves at you."

    show trish neutral at right with dissolve

    trish "Hi there, welcome to Posspresso! I'll be with you in just a minute!"
    
    "She's busy helping another customer at the moment, giving you time to look over the menu."
    #"There's a variety of breakfast-y food and drinks to choose from as well as some sweets."
    
    show selma neutral at left:
        xzoom -1
    with dissolve
    
    selma "Crazy snow we're getting, huh?"
    
    trish "I know right! Perfect day for a hot drink though!"

    #selma "I'll drink to that"
    selma "For real."
    selma "Hmm, I'm feelin' a salted caramel mocha today."

    trish "Ya want whipped cream on top?"

    selma "Hell yeah."

    trish "Hahaha will that be all for you, Selmers?"

    #selma "Throw in a cinnamon roll too please."
    selma "Throw in a strawberry waffle too please."
    
    trish "Alright, that'll be... seven dollars and eighty five cents!"

    "The bear pulls a crumpled $10 bill out of her pocket and slides it over."

    selma "Keep the change."

    trish "Thank you very much! I'll have that ready for you just as soon as I can!"
    
    selma "Thanks~"

    hide selma with dissolve
    
    show trish neutral at center with move

    "The bear steps away and the barista looks over to you."

    trish "Ain't seen you around before!"
    
    define trish = Character("Trish : ")
    
    trish "Welcome to Posspresso! You can call me Trish!"
    trish "Have you decided what you'd like?"

#    $ drinkenum = Enum('drinkenum', 'MOCHA SPECIAL AMERICANO CAPPUCCINO')
    $ chosenDrink = 0

    menu:
        "{cps=0}I'll have uh...{/cps}"
        "What she had":
            $ selmaAP = selmaAP + 1
            $ chosenDrink = drinkenum.MOCHA
            "Not sure what else to get, you just order the same thing the previous customer got."
        
        "Posspresso Special":
            $ bold = bold + 1
            $ chosenDrink = drinkenum.SPECIAL
            "You order the Posspresso Special. There's no description for it, but you wanted to try something new and local."
            "You also get an everything bagel with cream cheese to go along with it."

        "Americano":
            $ cynical = cynical + 1
            $ chosenDrink = drinkenum.AMERICANO
            "You order an americano and a blueberry bagel with honey butter spread to go along with it."
            "Gotta have something sweet to balance out the bitterness."

        "You're not sure...":
            $ introverted = introverted + 1
            $ chosenDrink = drinkenum.CAPPUCCINO
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
            #cute baristas get bigger tips
        
        "No tip":
            $ chaotic = chaotic + 1
            "The barista is just doing what's expected of her job, right? It's her employer's responsibility to pay her, not you."
            "Right?"

    trish "And can I get a name for you?"

    $ nameValid = False
    #$ player = Character("[name] : ")
    $ player = Character("You : ")
    #jump namescript1
    label namescript1:

        python:
            name = renpy.input("Oh shoot, what's your name again?", length = 14)
            name = name.strip()
            nameValid = True
            # prevents the player from naming themselves certain names and names them Alex if nothing is input
            if name.upper() == "MAE":
                "Choose another name."
                nameValid = False
            if name.upper() == "MARGARET":
                "Choose another name."
                nameValid = False
            if name.upper() == "BEA":
                "Choose another name."
                nameValid = False
            if name.upper() == "BEATRICE":
                "Choose another name."
                nameValid = False
            if name.upper() == "GREGG":
                "Choose another name."
                nameValid = False
            if name.upper() == "GREG":
                "Choose another name."
                nameValid = False
            if name.upper() == "ANGUS":
                "Choose another name."
                nameValid = False
            if name.upper() == "GERM":
                "Choose another name."
                nameValid = False
            if name.upper() == "JEREMY":
                "Choose another name."
                nameValid = False
            if name.upper() == "LORI":
                "Choose another name."
                nameValid = False
            if name.upper() == "SELMA":
                "Choose another name."
                nameValid = False
            if name.upper() == "SELMERS":
                "Choose another name."
                nameValid = False
            if name.upper() == "STAN":
                "Choose another name."
                nameValid = False
            if name.upper() == "CANDY":
                "Choose another name."
                nameValid = False
            if name.upper() == "TRISH":
                "Choose another name."
                nameValid = False
            if name.upper() == "MARCIE":
                "Choose another name."
                nameValid = False
            if name == "":
                #default name in case you don't type anything
                name = "Alex"
                nameValid = True

        if nameValid == True:
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

    trish "Alright [name], I'll have that ready for y'all in just a minute!"
    
    player "Thanks."

    hide trish with dissolve

    "You look around for a place to sit. That bear girl already found a table near the wall and has plugged a laptop into a power outlet."
    "Taking a seat by a window, you gaze out at the blinding white landscape."
    "It seems winter decided to come early this year. It's the beginning of December but the entire county is coated in a blanket of snow."
    "You heard there was a blizzard on its way and but you didn't think it would be this intense."
    "It's been snowing nonstop since you arrived in Possum Springs last night and sadly you left your favorite jacket behind at your old place."
    "The town seems ill-prepared as well. You lost count of how many abandoned cars you saw on the way here, stuck in a ditch and buried under a foot of snow."
    "A few people were shovelling snow off the streets but at the rate it's coming down, they need a snow plow and a few metric tons of rock salt."
    "You're lucky Posspresso even decided to open on a day like this."
    "Your eyes come to focus on your reflection in the glass, noticing you still have some snow on your..."

#    $ animalenum = Enum('animalenum', 'REPTILE BIRD MAMMAL')
    $ animaltype = 0
    
    menu:
        "{cps=0}Your eyes come to focus on your reflection in the glass, noticing you still have some snow on your...{/cps}"
        "Scales":
            $ animaltype = animalenum.REPTILE
            "...scales. Because you're a reptile, of course."
            "Oh god how long have you been walking around with that bit of shed skin stuck to your face? How embarassing."
        "Fur":
            $ animaltype = animalenum.MAMMAL
            "...fur. Because you're a mammal, of course."
            "You pat down a patch of fur that the wind blew out of place but it keeps sticking up."
        "Feathers":
            $ animaltype = animalenum.BIRD
            "...feathers. Because you're a bird, of course."
            "You try to pat down a few that are sticking up, but they are refusing to cooperate."
            
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
    
    player "Thanks."
    #player "How could I not enjoy it?"
    #player "I couldn't imagine not enjoying coffee."
    
    hide trish with dissolve

    if chosenDrink == drinkenum.SPECIAL:
        "You fetch your bagel and steaming hot beverage from the counter and head back to your seat."
        "The mug contains a dark concoction with a layer of light foam, topped with dark chocolate shavings."
        "You blow on it then take a sip."
        "..."
        "It's a mixture of overwhelming bitterness and sweetness."
        "The flavor is earthy and potent with a burnt chocolate aftertaste."
        "It's an exceptionally strong drink that leaves you wanting more of it."
        "You can't resist taking another satisfying sip before moving on to your bagel."
        "Nothing special here, just an ordinary bagel topped with seeds and herbs with ample cream cheese stuffed between its halves."
    
    elif chosenDrink == drinkenum.AMERICANO:
        "You fetch your bagel and steaming hot beverage from the counter and head back to your seat."
        "The mug contains a plain dark brew with a few bubbles on the surface."
        "You blow on it then take a sip."
        "..."
        "So bitter. So good."
        "No fancy flavors required, just a couple shots of espresso and good old fashioned water. The way god intended."
        "You can't resist taking another satisfying sip before moving on to your bagel."
        "It's full of juicy blueberries and the honey butter spread oozes pure sweetness. Good thing you have a strong drink to wash down this sugar overdose."

    elif chosenDrink == drinkenum.CAPPUCCINO:
        "You fetch your waffle and steaming hot beverage from the counter and head back to your seat."
        "The mug contains a gradient of different flavors. A dark espresso mixture on the bottom that turns into a milky white cream the further up you go, topped with a layer of foam."
        "You blow on it then take a sip."
        "..."
        "It gives you two distinct flavors of steamed milk and espresso. One is light and the other is strong, neither overpowering the other."
        "Can't go wrong with a classic drink like this, even if it is kinda plain."
        "You can't resist taking another satisfying sip before moving on to your waffle."
        "The sweet chocolate chips combined with the melted butter send your taste buds to heaven with a first class ticket."
    
    elif chosenDrink == drinkenum.MOCHA:
        "You fetch your waffle and steaming hot beverage from the counter and head back to your seat."
        "The glass mug reveals a light brown mixture with a layer of chocolate on the bottom. Up top is a layer of whipped cream, with a drizzle of caramel and sea salt"
        "You lick away some of the cream then take a sip of the actual drink."
        "..."
        "The salt contrasts with the sugary taste of chocolate and caramel, which balance the bitterness of espresso."
        "All the flavors combine into an exquisite beverage that gives you everything you could want in a drink."
        "You can't resist taking another satisfying sip before moving on to your waffle."
        "Juicy strawberries are baked right into it, offering a sweet sensation with nearly every bite of the savory buttermilk waffle."

    "Meanwhile, the bear on the other side of the room taps away on her keyboard, her claws making quite a racket."
    "You can hear a lot of frustrated backspacing after she types a long block of text."
    "That reminds you, you're connected to the internet now."
    "You pull out your phone and alternate between poking the screen and devouring your breakfast."
    "It may be a while before you get internet again, so you should download something to keep yourself busy later on."
    
    
#    $ hobbyenum = Enum('hobbyenum', 'MOVIES BOOKS MUSIC')
    #$ hobbyenum = Enum('hobbyenum', 'MOVIES BOOKS MUSIC')
    $ playerHobby = 0
    
    menu:
        "{cps=0}It may be a while before you get internet again, so you should download something to keep yourself busy later on.{/cps}"
        "Download movies":
            $ playerHobby = hobbyenum.MOVIES
            $ loriAP = loriAP + 1 #because she's known for liking movies
            #$ greggAP = greggAP + 1 #because choosing movies over books is something gregg would relate to, idk
            "This will give you something to pass the time. Hopefully the TV at home is modern enough for you to stream from your phone, you don't wanna get stuck watching these on a 5 inch screen."
            "You spend some time curating which movies you're interested in and finding working links."
        
        "Download books":
            $ playerHobby = hobbyenum.BOOKS
            $ mature = mature + 1
            $ selmaAP = selmaAP + 1
            "Books will last longer than movies and are more enjoyable anyway. Plus you can brag about being an adult who reads, an endangered species in the modern age."
            "You spend some time curating which books you're interested in and finding working links."
            
        "Download music":
            $ playerHobby = hobbyenum.MUSIC
            $ beaAP = beaAP + 1
            #$ maeAP = maeAP + 1
            "You'd rather not suffer in silence. Even if you've got nothing else to do you can always rock out to something."
            "You spend some time curating which albums you're interested in and finding working links."
    
    "Hours go by and the setting sun reminds you that you still need to go shopping to stock your pantry, preferably before it gets dark."
    
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
    
    "You step out into the snowy landscape and begin the next leg of your journey. Next stop: Ham Panther."
    #fade to white
    
    stop music fadeout 2.0
    
    scene bg ham_panther with fade

    #play music "music/itsadrag_loop.mp3" fadein 1.0

    "Now here's a familiar place. The soulless, sterile, yet gross corporate chain grocery store, Ham Panther."
    "You kick the snow off your boots and venture in. You're just shopping for the basics so you grab a basket and get to work."
    "Rice, beans, lentils... The shelves are damn near empty but you manage to get what you need to survive."
    #You pass by some townsfolk whose shopping carts are filled to the brim in response to the storm, though it's mostly junk food.
    "You pass by some townsfolk whose shopping carts are filled to the brim, no doubt in response to the snowstorm."
    "Two of them were arguing so aggressively over the last carton of eggs, you thought you were about to witness a murder."
    #"These small towns really are something."
    #"Should you pick up milk as well?"
    "Miraculously there are a few milk jugs left."
    "Which one should you get, almond milk or normal milk?"
    
    $ groceryItem = ""
    
    menu:
        "{cps=0}Which one should you get, almond milk or normal milk?{/cps}"
        "Almost milk":
            $ groceryItem = "almond milk"
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
            $ groceryItem = "skim milk"
            
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

    show gregg apron at center with dissolve

    gregg "Heya!"

    "A chipper fox greets you as you approach the register."
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

    gregg "Oh yeah that one's pretty good. You should check out Bear Essentials sometime. It's the bakery on main street. Serves pretty good coffee too."
    #as long as you don't need anything fancy
    
    player "I'll be sure to pop in sometime."
    
    gregg "This town ain't much but there's plenty of stuff to do if you know where to look!"
    
    player "I'll uh, keep an eye out I guess?"
    
    gregg "There's a ton of abandoned buildings to explore, the lake should be frozen enough for ice skating soon, uhhh some people go scrap fishing in the old trolley station but it smells like somebody died down there so I don't often go, oh and my band is getting together to do this-"
    
    player "Haha yeah that sure sounds exciting! Can I pay for my groceries now?"
    
    gregg "Oh sorry about that."
    
    "He presses a button on the register and you can finally swipe your card."
    
    gregg "Have a nice day!"
    
    player "Thanks, you too."
    
    hide gregg with dissolve
    
    "You grab your bagged groceries and begin walking back to your new home as the sun descends into the hilly landscape, only getting mildly lost along the way."
    
    scene bg home_interior_night with fade
    
    "You've had enough of the cold by the time you reach your house. You crank the heat up to the max but the air coming through the vents is hardly any warmer than it is outside."
    #"What the hell, it was doing this last night too."
    #"In fact, it feels colder!"
    #"You better not wake up to find yourself frozen to death because this machine "
    #"You're gonna be so mad if you freeze to death in your sleep."
    "Exhausted from trudging through snow all day, you put away your groceries as quickly as possible then wrap yourself in several blankets."
    if playerHobby == hobbyenum.MOVIES:
        "With your face pressed against a cold pillow, you watch a movie until you fall asleep."
    elif playerHobby == hobbyenum.MUSIC:
        "With your face pressed against a cold pillow, you listen to music until you fall asleep."
    elif playerHobby == hobbyenum.BOOKS:
        "With your head pressed against a cold pillow, you read a book until you fall asleep."

    # Day 2, tuesday
    $ currentDay = currentDay + 1
    #$ currentDate = "December 2"
    $ nightTime = False
    
    
    scene bg home_interior_day with fade
    
    "You awaken just as cold as you were when you went to bed. The air blowing through the vents never got any warmer."
    "Seriously, you need to figure out what is up with the furnace."
    "A memory arises from when you were a young child watching your father reignite the heater. Makes sense that this place would need some maintenance after being abandoned for so long."
    "You look around for the furnace but the inner workings are blocked by a grate that's screwed in tight with some weird proprietary screw type you've never seen before."
    "You try using various tools and objects you found lying around to loosen the bolts but none of them work." 
    #"even resorting to attempting to pry it open"
    "The map you downloaded at the cafe says there's a hardware store in town. Maybe they'll have the screwdriver you need."
    
    #jump to meeting bea scene, starting with town square
    #insert walk to main street and description here, plus optional bakery part
    
    "You put on a jacket and boots and make your way towards the center of the town, to the main street."
            
    scene bg roads_day with dissolve
    
    #"You try to follow the map but without GPS "
    #"Without GPS you get a bit lost but eventually stumble upon what must be the main street."
    #"blah blah blah general description of the surroundings."
    "Old brick buildings line the streets as you approach your destination. Some of them look lived in, others look like they're about to crumble."
    "Some look like both."
    "Squirrels frantically hop around burying nuts in the snow in a last ditch effort to stow away food for the coming months."
    #i think the memorial statue is between the shops?
    #"pass by the trolley station but it's boarded up. You take a peek inside."

    "That looks like the hardware store up ahead, but the aroma from the nearby bakery draws you in."
    "Where will you go?"
    
    menu:
        "{cps=0}Where will you go?{/cps}"
        "Bakery":
            jump angusBakeryIntro
            #gregg mentions he's on a long lunch break since it's a slow day, but that he is still clocked in  
        
        "Hardware store":
            jump meetingBea
        
    
    
    #2 stage furnace, 1 not igniting
    #low power heater not enough. you recall fixing a loose wire on a heater before and think it's the same problem (or your dad did when you were little at your city house)
    #go to hardware store for screwdriver > need to do favor for bea for her to let you borrow it > get distracted along the way > go to bakery and get invited to dnd and get bea's coffee > give bea coffee > deliver bag for marcie > go home
    #you can visit the bakery before the hardware store, but you'll just get a pastry for yourself and you'll have to return later to get bea's coffee
    #reason that you could go to posspresso but it'll be cold by the time you get back
    #point is, you need to visit the bakery for the plot to progress
    #try to visit bakery but they're on break, so you decide to explore town a bit
        #randomized, can bump into angus feeding squirrels in the park, germ feeding cats at abandoned grocery store, see mae and lori jumping on rooftops. mae drops her wallet and you pick it up to return to her later. no money in it of course. you're on a ~2 week timer from the time you find the wallet to return it (otherwise you return it in a brief mundane scene and don't get to see the lori mae sleepover). If you haven't met Lori and Mae yet at the pickax, then trigger the flashback scene at mae's house.
    
    
    #### to do: if there aren't any more scenes for exploring the house, remove option to explore house. Add it back when more options are available
    #### 
    #if not houseEventsDay:
    #    "You've already explored the house enough for now."
    #
    #
    #menu:
    #    "{cps=0}What should you do?{/cps}"
    #    "Explore home" if houseEventsDay:
    #    #####"Explore home":
    #        if exploredHouse == False:
    #            call unexploredHouse
    #        
    #        #if houseEvents is empty, you can no longer explore the house
    #        if not houseEventsDay:
    #            $ houseFullyExplored = True
    #            "You've already explored the house enough."
    #        
    #        $ randomSelected = renpy.random.choice(houseEventsDay)
    #        
    #        $ exploredHouse = True
    #        
    #        if randomSelected == "houseOffice":
    #            $ houseEventsDay.remove("houseOffice")
    #            $ houseEventsNight.remove("houseOffice")
    #            call houseOffice 
    #        #elif randomSelected == "houseShed":
    #        #    $ houseEvents.remove("houseShed")
    #        #    call houseShed
    #        elif randomSelected == "houseBook":
    #            $ houseEventsDay.remove("houseBook")
    #            $ houseEventsNight.remove("houseBook")
    #            call houseBook 
    #        elif randomSelected == "houseKey":
    #            $ houseEventsDay.remove("houseKey")
    #            $ houseEventsNight.remove("houseKey")
    #            call houseKey 
    #        else:
    #            "You've already explored the house enough."
    #            $ houseFullyExplored = True
    #        
    #        jump afterLookingForTool
    #        
    #    "Go into town":
    #        jump intoTown
    #        
    #    "Do nothing":
    #        "Yeahhh you don't really feel like doing anything today."
    #        "You sit back and mindlessly stare at your phone for a few hours."
    #        
    #        
    #    #"Posspresso":
    #        #minor event
    #        #can meet with characters you've met before here at random, if they're available
    #        #"You don't see how a coffee shop is gonna have what you need but a bit of caffeine never killed anyone."
    #
    #    #"Town outskirts":
    #        #minor event
    #        #"To hell with this, you'll wander around outside somewhere."
    #        
            
label day2Evening:
    scene bg roads_day with fade
    
    "It's getting late. You should hurry home."
        
    scene bg home_interior_night with fade
        
    
    "Fixing the heater ended up being a quick and simple fix."
    #"luckily nothing exploded"
    "Just had to loosen the screws, turn the gas valve, and reignite the flame with a lighter."
    "Exactly as you had watched your father do it all those years ago."
    "Luckily you didn't mess it up and blow up the house."
    "You return the grate to its original position and tighten it by hand so you don't need the special snowflake screwdriver anymore."
    "What a long day. You don't have the energy to do anything other than go to bed."
    "You don't have any plans for tomorrow so it should be more chill though."
    
    scene bg black with dissolve  
    
label day3:
    # Day 3, wednesday
    $ currentDay = currentDay + 1
    $ screwDriverDay = currentDay
    #$ currentDate = "December 3"
    $ nightTime = False
    
    scene bg home_interior_day with fade
    
    #outline: you can explore your home or possum springs. You can also return the wrench where you'll end up meeting mae and lori
    "For the first time in a while, you awaken feeling rested and comfortable."
    "The heater does a good job of warming you up when it actually works."
    "You make breakfast and sit watching the snow through the dining room window. It looks so... lonely out there."
    "A barren landscape of frost and dead trees. You can't see any neighboring houses past the forests surrounding you. It's a far cry from the city life you're used to."
    "You finish your breakfast and ponder what you'll do with the rest of your day as you wash the dishes."
    
    #options: stay home and explore (minor event), go into town and return the wrench (minor event), library if you have the book (major event), posspresso (minor event), visit bakery (non event), explore random part of town (minor event) [current available options are  exploring the underground and uhhhhh, seeing germ feeding wild cats at the food donkey, maybe merge random posspresso meets into this list]
    
    
    $ screwdriverReturned = False
    
    #if you explore first then try to visit the hardware store, it'll be closed early. can still visit the bakery though.
    
    $ houseEventsDay.append("houseShed")
    
    if not houseEventsDay:
        "You've already explored the house enough for now. You should find something else to do."
    if not townEventsDay:
        "You're tired of exploring the town. You should find something else to do for now."
    
    call dailyExploration from _call_dailyExploration
    
    #if nightTime == True:
    #    "The sun has set and it's gotten dark out, but the night is still young. What should you do?"
    #    #"There's still some light in the day. What else should you do with your time?"
    #    
    #    $ nightTime = False
    #    
    #    if not houseEventsNight:
    #        "You've already explored the house enough for now."
    #    if not townEventsNight:
    #        "You're tired of exploring the town. You should find something else to do for now."
    #    
    #    menu:
    #        "{cps=0}What should you do?{/cps}"
    #        "Explore home":
    #            #minor event
    #            #need to add to list of available house exploration options if you found the key earlier
    #            #re-add house description if you haven't already explored the house
    #            #if exploredHouse == False:
    #            
    #            if exploredHouse == False:
    #                call unexploredHouse 
    #            
    #            $ nightTime = True
    #            
    #            #if houseEvents is empty, you can no longer explore the house
    #            if not houseEventsNight:
    #                $ houseFullyExplored = True
    #                "You've already explored the house enough."
    #            
    #            $ randomSelected = renpy.random.choice(houseEventsNight)
    #            
    #            $ exploredHouse = True
    #            
    #            if randomSelected == "houseOffice":
    #                $ houseEventsDay.remove("houseOffice")
    #                $ houseEventsNight.remove("houseOffice")
    #                call houseOffice 
    #            elif randomSelected == "houseBook":
    #                $ houseEventsDay.remove("houseBook")
    #                $ houseEventsNight.remove("houseBook")
    #                call houseBook 
    #            elif randomSelected == "houseKey":
    #                $ houseEventsDay.remove("houseKey")
    #                $ houseEventsNight.remove("houseKey")
    #                call houseKey 
    #            else:
    #                "You've already explored the house enough."
    #                $ houseFullyExplored = True
    #        "Explore town":
    #            $ nightTime = True
    #            
    #            "You have the urge to walk around town."
    #            
    #            $ randomSelected = renpy.random.choice(townEventsNight)
    #            
    #            if randomSelected == "townBridge1":
    #                $ townEventsDay.remove("townBridge1")
    #                $ townEventsNight.remove("townBridge1")
    #                $ townEventsDay.append("townBridge2")
    #                $ townEventsNight.append("townBridge2")
    #                call townBridge1
    #            #add one more event to the pool
    #            
    #            
    #        "Return screwdriver" if screwdriverReturned == False:
    #            #day or night
    #            $ screwddriverReturned = True
    #            
    #            "You promised the hardware store girl that you'd return the screwdriver after you were done with it."
    #            "You have no more use for it so you should give it back as soon as possible."
    #            
    #            call returnScrewdriverScene 
    #                
    #        "Do nothing":
    #            "Yeahhh you don't really feel like doing anything today."
    #            "You sit back and mindlessly stare at your phone for a few hours."

    scene bg home_interior_night with fade

    #"Night casts its shadow and you retire to your bedroom to rest until sunrise."
    "It's gotten late and you've become too tired to stay awake."
    "Time for some sleep. You retire to your bedroom and rest until sunrise."
    
    scene bg black with dissolve
    
label day4:
    # Day 4 thursday
    $ currentDay = currentDay + 1
    #$ currentDate = "December 4"
    $ nightTime = False
    
    scene bg home_interior_day with fade
    
    "You're starting to get used to everything. A new home, a new town, a new independent routine..."
    "You've got a lot of freedom to do what you want for now, but you're going to have to find a way to make money soon."
    "For now though, your savings will hold you over and you can focus on settling in."
    "What will you do today?"
    
    call dailyExploration from _call_dailyExploration_1
    
    
    
    
    
    
    #if nightTime == True:
    #    "The sun has set and it's gotten dark out, but the night is still young. What should you do?"
    #    #"There's still some light in the day. What else should you do with your time?"
    #    
    #    $ nightTime = False
    #    
    #    if not houseEventsNight:
    #        "You've already explored the house enough for now."
    #    if not townEventsNight:
    #        "You're tired of exploring the town. You should find something else to do for now."
    #    
    #    menu:
    #        "{cps=0}What should you do?{/cps}"
    #        "Explore home" if houseEventsNight:
    #            #minor event
    #            #need to add to list of available house exploration options if you found the key earlier
    #            #re-add house description if you haven't already explored the house
    #            #if exploredHouse == False:
    #            
    #            if exploredHouse == False:
    #                call unexploredHouse 
    #            
    #            $ nightTime = True
    #            
    #            #if houseEvents is empty, you can no longer explore the house
    #            if not houseEventsNight:
    #                $ houseFullyExplored = True
    #                "You've already explored the house enough."
    #            
    #            $ randomSelected = renpy.random.choice(houseEventsNight)
    #            
    #            $ exploredHouse = True
    #            
    #            if randomSelected == "houseOffice":
    #                $ houseEventsDay.remove("houseOffice")
    #                $ houseEventsNight.remove("houseOffice")
    #                call houseOffice from _call_houseOffice
    #            elif randomSelected == "houseBook":
    #                $ houseEventsDay.remove("houseBook")
    #                $ houseEventsNight.remove("houseBook")
    #                call houseBook from _call_houseBook
    #            elif randomSelected == "houseKey":
    #                $ houseEventsDay.remove("houseKey")
    #                $ houseEventsNight.remove("houseKey")
    #                call houseKey from _call_houseKey
    #            else:
    #                "You've already explored the house enough."
    #                $ houseFullyExplored = True
    #        "Explore town":
    #            $ nightTime = True
    #            
    #            "You have the urge to walk around town."
    #            
    #            $ randomSelected = renpy.random.choice(townEventsDay)
    #            
    #            if randomSelected == "townBridge1":
    #                $ townEventsDay.remove("townBridge1")
    #                $ townEventsNight.remove("townBridge1")
    #                $ townEventsDay.append("townBridge2")
    #                $ townEventsNight.append("townBridge2")
    #                call townBridge1
    #            if randomSelected == "townGerm1":
    #                $ townEventsDay.remove("townGerm1")
    #                #$ townEventsNight.remove("townGerm1")
    #                #$ townEventsDay.append("townGerm2")
    #                #$ townEventsNight.append("townGerm2")
    #                call townGerm1
    #            if randomSelected == "townAngus1":
    #                $ townEventsDay.remove("townAngus1")
    #                #$ townEventsNight.remove("townAngus1")
    #                #$ townEventsDay.append("townAngus1")
    #                #$ townEventsNight.append("townAngus1")
    #                call townAngus1
    #            else:
    #                "There's nothing nowhere else to go for now."
    #            
    #            
    #            
    #        "Return screwdriver" if screwdriverReturned == False:
    #            #day or night
    #            $ screwddriverReturned = True
    #            
    #            "You promised the hardware store girl that you'd return the screwdriver after you were done with it."
    #            "You have no more use for it so you should give it back as soon as possible."
    #            
    #            call returnScrewdriverScene 
    #            
    #        "Do nothing":
    #            "Yeahhh you don't really feel like doing anything today."
    #            "You sit back and mindlessly stare at your phone for a few hours."
    #
    
    scene bg home_interior_night with fade

    #"Night casts its shadow and you retire to your bedroom to rest until sunrise."
    "It's gotten late and you've become too tired to stay awake."
    "Time for some sleep. You retire to your bedroom and rest until sunrise."
    
    scene bg black with dissolve
    
    
    
    #day5
    # Day 5 Friday
    $ currentDay = currentDay + 1
    #$ currentDate = "December 5"
    $ nightTime = False
    
    scene bg home_interior_day with fade    
    
    "Today's the day Gregg and Angus said they're meeting up to play some board game."
    "They're starting at night so you should have plenty of time to do something else for a while."
    "What will you do today?"
    
    call dailyExploration from _call_dailyExploration_2
    
    scene bg home_interior_night with fade
    
    #"The sun has set and it's gotten dark out, but the night is still young."
    #"The sun has set and it's gotten dark out, but the night is still young. What should you do?"
    #"There's still some light in the day. What else should you do with your time?"
    
    #"Tonight is when Gregg said he's gathering people to play Conquests and Constellations."
    "The time when Gregg and Angus said they'd be playing is fast approaching."
    "You head out to the meeting place, unsure of what you're getting into but excited nonetheless."
                    
    call tabletopGame1 from _call_tabletopGame1
    
         
    
    
    #day6
    # Day 6 Saturday
    $ currentDay = currentDay + 1
    #$ currentDate = "December 6"
    $ nightTime = False
    
    scene bg home_interior_day with fade
    
    "You're starting to get used to everything. A new home, a new town, a new independent routine..."
    "You've got a lot of freedom to do what you want for now, but you're going to have to find a way to make money soon."
    "For now though, your savings will hold you over and you can focus on settling in."
    "What will you do today?"
    
    call dailyExploration from _call_dailyExploration_3
    
    scene bg home_interior_night with fade

    #"Night casts its shadow and you retire to your bedroom to rest until sunrise."
    "It's gotten late and you've become too tired to stay awake."
    "Time for some sleep. You retire to your bedroom and rest until sunrise."
    
    scene bg black with dissolve
    
    #### make this happen on day 7 and make it a friday. keep 1 day of random explorations between the tabletop game, this, and church sunday
    
    #if you haven't already seen the poster for the band gig, you stumble upon it somehow and decide to check it out that night.
    
    #if foundBandGig == False:
    #    "As you wonder through town, a sheet of paper flutters through the wind. By chance it flies directly in your face."
    #    "You see it's a flyer for some sort of band gig happening... tonight?!"
    
    "Today's the day that band is playing at the bakery. You spend the day running errands and getting ready for tonight's big event."
    
    call bandGig1
    
    scene bg home_interior_night with fade

    #"Night casts its shadow and you retire to your bedroom to rest until sunrise."
    "It's gotten late and you've become too tired to stay awake."
    "Time for some sleep. You retire to your bedroom and rest until sunrise."
    
    
    
    #interim day
    
    scene bg home_interior_day with fade
    
    "What will you do today?"
    
    call dailyExploration
    
    
    scene bg home_interior_night with fade

    #"Night casts its shadow and you retire to your bedroom to rest until sunrise."
    "It's gotten late and you've become too tired to stay awake."
    "Time for some sleep. You retire to your bedroom and rest until sunrise."
    
    
    #day7
    # Day 7 Sunday
    $ currentDay = currentDay + 1
    #$ currentDate = "December 7"
    $ nightTime = False
    call church1
    
    return
    
    scene bg black with fade
    
    "Thanks for playing! One More Night in the Woods is still very early in development. Check out twitter.com/codavn for more info!"
    
    
    
    
    
    

   