label meetingBea:
    if wentToPosspresso:
        "Bea chastises you for getting her cold coffee and going so far when the bakery was right next door, but a deal is a deal."
    elif metAngus:
        $ metBea = True
        "give bea the coffee you got for yourself. this frees you up to do 1 more action in town before going home, whether going back to the bakery or wandering around town"
        
    else:
        #first time entering the store
        $ metBea = True
        scene bg ol pickax with dissolve

        play music "music/picknaxe_loop.mp3" fadein 1.0

        "Plenty of boxes and miscellaneous items are strewn about like they're in the middle of reorganizing their inventory."
        "An assortment of nails, screws, tapes, paints, and most importantly tools are on display. It's surprisingly well stocked for a little country bumpkin town."
        "You guess the folk around here rely on building and repairing their own stuff more than people in the city do."
        #"Then again, country folk are more likely to use these sorts of things for repairs and home improvement. You weren't even allowed to put thumbtacks in the walls in your apartment in the city but here"
        "Snow shovels sure seem to be selling quick these days."
        #"The goth crocodile behind the counter just finished selling one to a customer and yawns before welcoming you."
        "The goth crocodile behind the counter just finished selling one to a customer."
        "Her tired eyes sluggishly drift to look in your direction."        
        
        
        #"Behind the counter stands a bluish green crocodile giving off gothic vibes."
        #"Her tired eyes sluggishly drift to look in your direction."

        show bea apron at right with dissolve:
            yalign beaheight

        beaunknown "Welcome to the Ol' Pickaxe. Let me know if I can help you find any- *yawn*"
        beaunknown "-...thing."

        player "You don't happen to have any 10mm allen wrenches, do you?"
        
        beaunknown "Check the wrench kits. Over thataway."
        
        "She points a finger to the other side of the store."

        player "I'd rather not have to buy a full set. Don't you have single wrenches for sale?"
        
        beaunknown "Yeah, they're over where the kits are."

        "She shrugs."
        
        beaunknown "Dunno if the one you want is in stock though."
        
        player "Thanks..."
        
        hide bea with dissolve
        
        "You go off to where she pointed to have a look."
        "There's a whole shelf with nothing but wrenches dangling off hooks for you to peruse."
        "Let's see, 8mm, 8.5mm, 9mm, 9.6mm, 9.9mm, 9.99mm, 10.01mm... hey!"
        "All of them are in stock except the one you need!"
        "You catch a glimpse of the cashier girl dragging a large bag of road salt between aisles and decide to approach her."
        
        show bea apron with dissolve

        player "Excuse me. You don't have the wrench I need in stock."
        
        bea "Oh. Sorry about that."
        
        "She continues dragging the bag towards the pile near the front of the store."
        "You clear your throat."
        
        menu:
            "When would you get a new shipment?":
                $ gentle = gentle + 1
                $ mature = mature + 1
                player "When do you think you'll get a new shipment. I need this wrench as soon as possible."
                
                bea "Yesterday, but I'm not about to move all those boxes and open the one that might have your wrench today when I've already got a huge backlog of work to do."
                
                player "Oh..."
                
                bea "Not unless you get me a coffee."
                
                player "What?"
                
                "She yawns again and leans agains a shelf."
                
                bea "Didn't get much sleep last night. If you go next door to the bakery and buy me a coffee, then *maybe* I can be persuaded to prioritize your request."
                
                "You don't really have a choice if you want to fix your bike ASAP."
                
                player "Deal."
                player "What kind of coffee do you like?"
                
                bea "Something dark. Like my soul or something, I don't care."
            "What's your return policy?":
                $ bold = bold + 1
                "You're backed into a corner and have no choice but to cheat a little."
            
                player "Say, what's your return policy?"
            
                bea "I know what you're planning. You're gonna buy the kit, use it to tighten one bolt then return it."
                
                "Dammit, she caught on immediately."
                
                bea "Tell you what."
                bea "If you go to the bakery next door and get me a coffee... *yawn* ... I'll loan you the wrench."
                #she might have you buy her a coffee, and she'll let you borrow a wrench from the kit
                #bea "If you get me a coffee I'll loan you a wrench from one of those kits."
                bea "Just be sure to return it or I will hunt you down."
                
                player "Sheesh, wake up on the wrong side of the bed or something?"
                
                bea "More like never went to sleep in the first place. You gonna get my caffeine or not?"
                
                player "Fine. What kind ya like?"
        
                bea "Something dark. Like my soul or something, I don't care. Just make it quick or the deal's off."
        
        hide bea with dissolve
        
        "She drops the bag onto the stack with the others then shuffles to the back of the store, presumably to grab another one."
        "Well that's a quest if you've ever seen one. You step outside and begin searching for this bakery."