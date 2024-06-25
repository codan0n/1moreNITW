label maeLoriSleepover:

    "It's about time you deliver that wallet you found to its rightful owner."
    "The address on the ID said they reside on Maple Street."

    scene bg street with fade
    
    "This is the place. Why do you suddenly feel nervous about doing this?"
    "Is she gonna think you're stalking her?"
    "Maybe you should just leave the wallet on the doorstep or in the mailbox."
    "While you're contemplating what to do, you hear a voice from behind."
    
    
    if metLori == True:
        lori "[name]?"
        lori "What are you doing here?"
        
        "You turn around and see Lori with an overstuffed bag on her back."
        
        player "Whoa! Lori, you startled me!"
        
        lori "Sorry..."
        
        player "It's fine, I was just... I found this wallet on the ground and was returning it."
        player "This is Mae's house, right?"
        
        lori "Yup! Is she home? Did you knock on the door yet?"
        
        player "Err, not yet..."
        
        #menu:
        #    "Knock on the door":
        #    
        #    "Give wallet to Lori":
        
        lori "Well what's the hold up? It's freezing out here and I wanna go inside!"
        
        "Lori reaches past you and rings the door bell."
    else:
        lori "Um, hello?"
        
        "You turn around and see a timid mouse girl with an overstuffed bag on her back."
        
        player "Hey...?"
        
        "A look of realization dawns on her."
        
        lori "What a minute... I know you!"
        
        "She does look kinda familiar, but it's hard to tell in the lighting."
        
        lori "We met on the bus, remember?"
        
        "You try to remember back to that night."
        
        call loriFlashback
        
        player "Oh right, now I recall! Lori, right?"
        
        lori "Yup! What're you doing at Mae's house?"
        
        player "I found this wallet and came to return it."
    
    



            "The pleasant chime echoes from within. A moment later, a confused Mae opens the door with a sheepish Lori hiding behind her."

            show lori anxious2 flip at left:
                yalign loriheight
                xalign .15
            show mae freakout flip at left:
                yalign maeheight
                xalign 0.0
            with dissolve

            mae "[newname]? What are you doing here? How did you even know I lived here?"

            "You try to ignore the smells and bring your attention back to the matter at hand."
            player "Hey, sorry to bother you, but I found your wallet lying on the sidewalk. Your license had your address, so I just came by to return it."

            "You hold the wallet out for her. Mae takes it and looks inside, verifying it is in fact hers."

            show mae panic flip

            mae "Wow, I didn't even know I lost this. Thanks, [newname]!"

            show mae happy flip

            "Her demeanor visibly brightens now that she's reunited with her wallet. Lori pokes her head out and waves to you."

            show lori neutral flip:
                yalign loriheight
                xalign .26
            with move
            show mae neutral flip

            lori "Hi, [newname]!"

            player "Hey, Lori! Having dinner with the Borowskis tonight?"

            lori "Yup!"

            candy "Mae honey, who's at the door?"

            show candy neutral at right with dissolve

            "Mrs. Borowski comes into view as she leans around a corner. Seeing you, she puts on a cheerful face and comes up behind Lori and Mae."

            candy "Why, hello again! [newname], right? To what do we owe the pleasure?"

            player "Just returning something of Mae's."

            candy "Mae, did you lose your wallet again?"

            show mae angry flip

            mae "Mom!"

            candy "What? I can't count the number of times you've lost that thing. Did you tell [himherthem] thank you?"

            show mae grump flip

            mae "Yes Mom, I'm not five anymore. I know how to talk to people."

            "Lori stifles a giggle. Poor Mae, her mother is too sweet for her own good."

            candy "You know, [newname], if you'd like you're welcome to have dinner with us tonight! I'm just about finished making a big pot of zuppa toscana!"

            "You can see it on Mae's face, she's embarrassed and you *are* kind of interrupting her thing with Lori tonight. You ought to get going and leave them be."

            player "That's okay, I don't really want to intrude..."

            candy "Oh, don't be shy, dear! I insist!"

            "Well, that settles it, you guess. Against your better judgement, you nod your head. It's not like you can say no to a kind lady offering you food."
            "She invites you inside and walks you through the kitchen to the dining area with Lori and Mae in tow."

            mae "..."

            lori "What?"

            mae "Nothing."

            scene bg maekitchen with fade
            play music "music/Stagnant_Tone-down.mp3" fadein 1.0

            "The dining table is small and square shaped with only four chairs. You awkwardly take a seat adjacent to Lori and across from Mae."
            "Mrs. Borowski goes to the stove to stir the pot with a ladle before turning off the burner."

            show candy neutral at right
            show lori neutral flip at left:
                yalign loriheight
                xalign .26
            show mae sad1 flip at left:
                yalign maeheight
                xalign 0.0
            with dissolve

            candy "You all sit tight, and I'll have a bowl out for everyone in just a minute!"

            mae "Aren't we gonna wait for Dad to come home?"

            candy "Not tonight, hun. Your father called to say he'd be working a little late and to go ahead and have dinner without him."

            mae "Oh."

            "There's another awkward pause as Mrs. Borowski takes a tray of toasted bread out of the oven. Luckily, Lori thinks of something to say to break the silence."

            lori "So, whatchya been up to today, [newname]?"

            player "Just exploring town. Getting used to the layout, that sort of thing. That's how I ended up stumbling upon Mae's wallet."

            "Mrs. Borowski steps in to set a steaming bowl of soup in front of you. The spices are enough to make your eyes water."

            candy "And we're very glad you did!"
            candy "Nobody wants to spend a sleepover night worrying about identity theft and cancelling all their credit cards."

            player "A sleepover? Oh, so that's why you're here tonight, Lori."

            lori "Yep! Mae and I are gonna have a movie marathon later."

            player "Sounds like a good time!"

            "Mrs. Borowski finishes setting bowls and silverware for everyone, then places a dish full of sliced bread in the center of the table."

            show mae neutral flip

            candy "Go ahead and dig in!"

            lori "Thank you, Mrs. Borowski!"

            player "Yeah, thanks!"

            candy "You're very welcome!"

            "You flash her a grateful smile as you raise your spoon, giving it a quick blow before you take in your first mouthful of kale, bacon, and broth."
            "The spice has a strong kick to it that accentuates the meat, and the soaked kale rounds out the flavor with a touch of earthiness."
            "Unfortunately, the heat also scalds your tongue, so you're forced to grab a slice of bread and nibble on it while you wait for it to cool. The others seem to have the same idea."
            "You eventually brave another spoonful, this time scooping up a chunk of potato and a bit of sausage. Both are incredibly soft and easy to chew after brewing in a pot for hours."
            "After a few more spoonfuls, the red pepper loses its edge, and you can appreciate the underlying flavors. There's actually a lot of sweetness buried within, not unlike a sweet and sour soup."
            "And there's something in particular that you can't quite identify that makes it unique and truly memorable."

            candy "How are you liking it, [newname]?"

            player "It's amazing! I wish I could cook this well."

            candy "Heeheehee! The secret's in the ginger root!"

            "You can tell she's got a lot of pride in her cooking by the way she looks at you."
            "And it's clearly deserved, judging by the dish she's graciously provided you tonight."
            "What's more, the way she's treating you feels alien."
            "It's as if she's treating you like you're...family?"
            "As you all finish your dinner, she engages you, Lori, and Mae in small talk as though she's actually interested and cares about what you each have to say."
            "Like you were all her own loving children."
            "Well, Mae obviously is, but the way Mrs. Borowski acts, an outsider might think you and Lori were as well."
            "It's not a feeling you're altogether too familiar with, but...it's nice."

            candy "...and have you seen the most recent painting Mae's been working on?"

            player "I haven't really seen any of Mae's artwork yet."

            candy "You should! She's improved so much in the past few years, she could be the next Picasso!"

            show mae grump flip

            "Mae groans."

            mae "Mom, stop. It's not that good."

            candy "Nonsense! I bet an art collector would pay a high price to have it in their collection!"
            candy "In fact, why don't you go show [newname] your room so they can see your art while I take care of the dishes?"

            mae "...Fine."

            #transition to mae's bedroom
            scene bg maebedroom with dissolve

            "Mae leads you and Lori up the stairs to a room which you're pretty sure is actually a repurposed attic."
            "It's messy and cluttered with all kinds of posters and pictures on the walls. There's a definite rebellious vibe to it, like a stereotypical caricature of every teenager's bedroom."
            "She's even got a bass in here."
            "Mae walks over to the easel next to the nightstand and gestures to it."

            show mae grump flip at left with dissolve

            mae "It's not finished yet, but here it is."

            "An ominous head floating in a dark, starry void with glowing eyes stares back at you."

            menu:
                "I like it.":
                    player "Very nice. I like it a lot."

                    show mae sad1 flip

                    mae "Meh, it's nothing special..."

                    player "Well I think your mother was right, it belongs in a museum!"

                    show mae skeptical flip
                    show lori shrug at right with dissolve:
                        yalign loriheight

                    lori "\"So do you!\""

                    show mae skeptical flip

                    "You and Lori bust out laughing."

                    show mae laugh flip

                    "Even Mae can't help but smirk at yours and Lori's silly movie references."

                    mae "Heheh."

                    show mae neutral flip

                    mae "Anyway, I'm not very happy with how this one turned out. I'm not sure I'll ever get around to finishing it."

                "It's creepy.":

                    player "It's creepy."

                    show mae angry flip

                    mae "It's supposed to be. That's the whole point."

                    show lori shrug at right with dissolve:
                        yalign loriheight

                    lori "Creepy is good! I like creepy."

                    player "It kinda disturbs me."

                    show mae sad1 flip

                    mae "Meh, I guess it's not for everyone."
                    mae "I'm not very happy with how it turned out either. I probably won't ever get around to finishing it."

                "What inspired you?":

                    player "Very interesting. What inspired you?"

                    mae "Um, nothing in particular. Just came to me in a dream I guess."

                    show lori shrug at right with dissolve:
                        yalign loriheight

                    lori "Mae gets a lot of inspiration from her dreams. I'm kinda jealous."

                    player "Do you often have spooky dreams?"

                    mae "Yes. No. Kinda. I dunno."
                    mae "Anyway, I'm not very happy with how this one turned out so I'm probably never gonna finish it."

            show lori sad

            lori "Aww..."

            show mae sad1

            mae "It's not the first time I've abandoned a project."

            "Mae stares at her painting for a while, seemingly criticizing it in her head."

            show lori nervous

            "Lori patiently waits at her side, watching her with a contagious smile."

            show mae blush

            "Mae eventually lets up and smiles back."

            "Seeing them like that, a thought pops into your mind. You clear your throat."

            player "So... How long have you two been...?"

            show mae freakout

            mae "Huh?"

            show lori anxious3

            lori "Been what?"

            player "You know, like, together?"

            show mae panic flip

            mae "Together?"

            player "Yeah like... as a couple?"

            "A look of realization forms on both of their faces."

            show lori breath
            show mae freakout flip

            lori "Whaaaaaat? You thought Mae and I were dating???"

            mae "We're not- That doesn't even-"

            "Oh God, you messed up."

            player "I mean, uh...oops."

            "There is no way you can salvage this."

            "Mae and Lori exchange a glance at each other then giggle among themselves. You contribute little more than an embarrassed chuckle."

            show lori cheeky
            show mae laugh flip

            lori "Hahahaha does it really seem like we're dating? I had no idea!"

            mae "Hahaha yeah we're just really good friends is all!"

            player "Sorry, my mistake! I shouldn't have assumed!"

            show mae neutral flip

            mae "It's alright. In any case, I think we've all had our fill of my weird art. Let's head back downstairs."

            player "Sure."

            scene bg maelivingroom with dissolve
            stop music fadeout 2.0

            show candy neutral flip at left
            show lori neutral at right:
                yalign loriheight
                xalign .725
            show mae neutral at right:
                yalign maeheight
                xalign 1.05
            with dissolve

            "From the lobby you can see Mrs. Borowski washing the dishes in the kitchen sink. The clock on the wall near her shows it's way later than you thought it was."

            player "Hey Mrs. Borowski! I think I'm gonna head home now. Thanks again for the meal!"

            candy "Going home so soon? Stay safe out there!"

            player "I will! Thanks for having me over!"

            hide candy with dissolve

            "You turn to Mae and Lori."

            player "And sorry, I didn't mean to take up so much of your evening."

            mae "It's cool."

            lori "Yeah, it was a pleasant surprise seeing you tonight, [newname]!"

            player "See you guys later!"

            lori "See ya!"

            mae "Bye, [newname]!"

            hide mae
            hide lori
            with dissolve

            "Mae opens the door for you and you give a last friendly wave as you wander into the night back to your house."
            "You return home, feeling less stressed for the time being, and you skip having lunch since Mrs. Borowski already took care of that."

            jump advanceDay

        #"Leave it alone":
            #set flag so can no longer find wallet
            #"You ultimately decide to steer clear of it."
            #"It's not your problem. It's probably just trash someone neglected to find a bin for. You simply keep walking and forget about it."
            #jump locationMenu