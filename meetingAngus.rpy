label meetingAngus:
    if metBea == True and metAngus == False:
        #on the quest to get bea coffee, this is first time in bakery
        $ metAngus = True
        
        scene bg bakery_interior with dissolve
        
        show angus neutral at left with dissolve:
            xzoom -1
        
        "this happens if this is your first time in the bakery and you're getting bea coffee"
        
        "blah blah blah get coffee, then return to bea"
        
        jump meetingBea
        
        
    
    elif metBea == True and metAngus == True:
        #means you are doing bea's coffee quest and you visited the bakery before meeting Bea
        
        scene bg bakery_interior with dissolve
        
        show angus neutral at left with dissolve:
            xzoom -1
            
        show gregg neutral at right with dissolve
        
        angus "Back already?"
        
        gregg "I bet [heshethey] Couldn't resist another one of your snacks~"
        
        "blah blah blah get coffee, then return to bea"
        
        jump meetingBea
        
        
    elif metBea == False and metAngus == True:
        #means you went to the bakery first and have not yet met Bea. This case shouldn't happen because if you go to the bakery first it will automatically take you to the ol pickax immediately after
        ""
        
    elif metBea == False and metAngus == False:
        #means you have not visited Bea and this is your first time in the bakery
        $ metAngus = True
        
        scene bg bakery_exterior with dissolve
        
        "You decide to check out the bakery first."
        "The smell of confections, pastries, and coffee fills the air around it."

        scene bg bakery_interior with fade

        play sound "sound/storebell.mp3"
        play music "music/Indecisive_Redux.mp3" fadein 1.0

        #"As soon as you walk in, the scent of peppermint hits you like a truck."
        #"You feel bad for the baker behind the counter who has to put up with this for hours every day."
        #"At least he probably comes home smelling nice."
        
        "A bell on the door chimes as you step inside and a voice calls out from the back of the shop."
        
        angusunknown "I'll be with you in just a moment!"
        
        "You look over the treats behind the glass case while you wait."
        
        "A bear comes around the corner, holding a tray of peppermint frosted cookies between mittened paws."
        
        show angus neutral at left with dissolve:
            xzoom -1
        
        angusunknown "Sorry for the wait, these were ready to come out of the oven."
        angusunknown "What can I get you?"
        
        #"He pulls a tray full of holiday themed cookies out from the oven then turns to you with a warm smile."

        #angusunknown "Welcome! I'll be with you in just a second!"

        #"You nod to him as he sets the tray on a cooling rack and moves a fresh batch into the oven."

        #hide angus with dissolve

        #"You take the time to look over the menu, deciding on a coffee to get for the hardware store crocodile."
        #"You also pick out a treat from the glass case for yourself."

        #angusunknown "Sorry for the wait. What can I get you?"
        
        #$ cinnamonRoll = False
        #honestly just remove this choice, it doesn't affect anything and bloats the game with too many choices at once
        #menu:
        #    "Poppy seed muffin":
        #        $ confectionChoice = "muffin"

        #        player "I'll have one poppy seed muffin, please!"
        #    "Cinnamon roll":
        #        $ confectionChoice = "cinnamon roll"
        #        $ cinnamonRoll = True
                
        #        player "I'll have a cinnamon roll, please!"
        #    "Glazed lemon cake":
        #        $ confectionChoice = "cake"
                
        #        player "I'll have a slice of lemon cake, please!"
        #    "Raspberry scone":
        #        $ confectionChoice = "scone"

        #        player "I'll have a raspberry scone, please!"
        
        player "Those smell really good! Can I get a couple to go?"
        
        angusunknown "Of course! Will that be all for you?"
        
        player "Yep. For now at least."
        
        "The baker uses a pair of tongs to grab your cookies and drops them into a paper bag."
        
        angusunknown "Here you go! I'll ring you up over here."
        
        "You pull a piping hot cookie from the bag and nibble on it while completing your purchase."
        
        player "Ow! Hot!"
        
        angusunknown "Please do be careful. I know it's freezing outside but I literally just pulled those out of the oven."
        
        player "I couldn't resist."
        
        angusunknown "I'll take you willing to burn your tongue for my baking as a compliment."
        
        "The bear rings up your order and you swipe your card on the machine."
        
        angusunknown "Thanks, have a good day!"
        
        player "You too!"
        
        hide angus with dissolve
        
        "You exit the store satisfied with your sugary snack and make your way to the hardware store."
        
        jump meetingBea
        
        
        
        
        
        
        
        #angus talks about how nice hot treats are on a cold day, do the cold day dialogue
        
        
        
        
        
        
        #player "Oh and a coffee to go. Black."

        #angusunknown "Sure! Would you like me to heat it up?"

        #"You look over your shoulder at the snowy environment."

        #player "Please do."

        "The baker catches you looking outside and chuckles as he grabs the cookies with a pair of tongs."

        angusunknown "Haha that snow came out of nowhere, didn't it? My winter coat isn't even fully grown in yet!"

        menu:
            "I like the cold.":
                player "I like the cold."

                angusunknown "I do too, but I'd say I'm better equipped to handle it than most."
            "I hate the cold.":
                player "I hate the cold."

                angusunknown "I don't mind it but it makes me sleepy. I think it makes everyone sleepy."
            "The cold doesn't bother me.":
                player "The cold doesn't bother me."

                angusunknown "Well that's good, cause I have a feeling we're in for a loooong winter."

        play sound "sound/storebell.mp3"
        
        "The bell on the door chimes as the baker sets your snack inside a small toaster oven."
        #"You take a look over your shoulder and to your surprise it's the fox from the grocery store!"

        show gregg neutral at right with dissolve

        #gregg "Hey Angus! And look who we have here!"
        gregg "Oh honey, I'm home! Hey, you didn't say we were having guests!"

        "The fox from the grocery store swaggers up to the counter and makes a grandiose gesture toward you, grinning from ear to ear."
        
        gregg "Remember me?"

        #gregg "This is who I was telling you about earlier!"

        if wentWithGregg == True:
            player "Of course! How could I forget the kind stranger who gave me a ride home?"
            player "Thanks for not murdering me and leaving my body in a ditch."
            
            gregg "What can I say? I'm a gentleman!"
            gregg "Ain't that right, Angus dear?"
        
            #gregg "The one I drove home yesterday and has that big house in the woods!"

            #angus "Just how many strangers did you drive home yesterday, Gregg?"
            
            angus "When you want to be one."

            player "I never would have expected people out here to be so... considerate."

            angus "Oh don't worry, you'll meet some jerks sooner or later."

            gregg "Not us though! We're super chill and nice!"
            gregg "By the way this is Angus. All you need to know about him is that he is the best."

            angus "Oh you."

            player "Nice to meet you, Angus. I'm [name]."

            angus "It's a pleasure to meet you as well."

            "It seems everyone knows each other in this town. Like everyone's in one big family."
            "It's kinda heartwarming."

            play sound "sound/storebell.mp3"

            "The bear's ears perk up in response to the toaster oven's timer."
            #"Everyone's attention shifts to the toaster oven when the timer dings."
            "Gregg leans over the counter and sniffs at your treat as Angus removes it."

            gregg "Cinnamon, yum."

            player "Can I get that to go please?"

            angus "Of course!"

            player "Thanks."

            "He drops the cinnamon bun into a small bag, then places that inside a bigger bag and sets it on the counter alongside your coffee."
            "As he does so, you pull out your wallet and dig out your debit card."

            angus "Paying with card? Here you go. The machine takes a minute to process though."

            "He slides a tablet with a card reader plugged in toward you."
            "You insert your card and sure enough it gets stuck on the processing screen."
            "..."
            "After a while, Angus clears his throat and breaks up the lull in the conversation."

            angus "So is Gregg gonna be chauffeuring you every time you need groceries or do you have another way of getting around?"
            angus "Sorry if that sounded rude, I'm just wondering what your living situation is like."

        elif wentWithGregg == False:
            player "Sort of."
            
            gregg "Sort of?! Yer breakin' my heart here!"
            
            player "Haha sorry, it was a long day for me."
            
            gregg "Well I'm glad you made it home alive!"
        
            #gregg "The one who's new in town! Fancy meeting you here!"
            gregg "By the way, I don't think I properly introduced myself yesterday. I'm Gregg!"
            
            gregg "He performs an exaggerated bow."

            #"He holds out his paw and you take hold of it. He's got a firm, eager handshake."

            player "[name]."
            
            gregg "And this is Angus. All you need to know about him is that he is the best."

            angus "Oh you."

            player "Nice to meet you, Angus. I'm [name]."

            angus "It's a pleasure to meet you as well."

            "It seems everyone knows each other in this town. Like everyone's in one big family."
            "It's kinda heartwarming."

            play sound "sound/storebell.mp3"

            "The bear's ears perk up in response to the toaster oven's timer."
            #"Everyone's attention shifts to the toaster oven when the timer dings."
            "Gregg leans over the counter and sniffs at your treat as Angus removes it."
            
            gregg "Cinnamon, yum."

            player "Can I get that to go please?"

            angus "Of course!"

            player "Thanks."

            "He drops the cinnamon bun into a small bag, then places that inside a bigger bag and sets it on the counter alongside your coffee."
            "As he does so, you pull out your wallet and dig out your debit card."

            angus "Paying with card? Here you go. The machine takes a minute to process though."

            "He slides a tablet with a card reader plugged in toward you."
            "You insert your card and sure enough it gets stuck on the processing screen."
            "..."
            "After a while, Angus clears his throat and breaks up the lull in the conversation."

            angus "So Gregg tells me you're new in town? How are you liking Possum Springs?"
            
            player "It's quite different from what I'm used to but it's nice so far."
            
            angus "That's good, I'm glad you're liking it. It's not as exciting as the city but you come to enjoy the quiet life."
            angus "How are you getting around? Gregg said you walked to the Panther yesterday."
            angus "Sorry if that sounded rude, I'm just wondering what your living situation is like."
            
            
            #gregg "And this is my bf"

            #angus "I'm Angus. It's a pleasure to meet you."
            

        "The machine beeps and you take back your card. Angus passes you your receipt as you're talking."

        player "Actually I've got a motorcycle I'm trying to repair."
        #I've never worked on this sort of thing though so it might take a while."

        "Gregg's ears are the ones to perk up this time."

        gregg "Did I hear \"motorcycle?\""

        angus "That is what [heshethey] said."

        gregg "I can help you fix it!"
        gregg "I learned a bunch of stuff from working on my own bike! I bet I can get yours running smoothly in a jiffy!"

        ###choice whether to try to decline gregg or welcome him. he insists either way

        player "That would be great! It doesn't run at all at the moment."

        angus "Don't worry, Gregg is great at getting broken things to work. He built that robot thing this one time..."

        gregg "Yeah, I can come to your place tomorrow morning and check it out!"

        player "That would help me out a lot, thanks so much!"

        #if wentWithGregg == True:

            #player "You remember how to get to my place?"

            #gregg "Yup!"

            #player "Cool, I'll see you in the morning then!"

            #gregg "See ya!"

        #elif wentWithGregg == False:

            #player "Oh, I guess you'd need to know where I live."

            #gregg "That would be useful to know, yes."

            #"You hastily jot down your address on the back of the receipt with a pen that was lying on the counter and hand it to Gregg."

            #gregg "Sweet! I'll be there first thing tomorrow!"

            #player "Awesome! See ya then!"
        
        
        
        "You grab your things and prepare to brave the cold outside once more."
        
        player "And thanks for the coffee, Angus! It's just what I needed for another quest I'm on!"

        angus "Quest?"
        angus "Well, I'm glad I could be of assisance. Have a nice day!"

        player "You too!"

        stop music fadeout 2.0

        hide gregg
        hide angus
        with dissolve