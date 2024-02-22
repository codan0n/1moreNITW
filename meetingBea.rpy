label meetingBea:
    if beaQuestPosspresso == True:
        scene bg olpickaxe with dissolve
        
        "One long trek back to the hardware store later..."
        
        show bea apron at center with dissolve
        
        bea "What the eff, you went all the way to Posspresso?! No wonder it took you so long."
        bea "This coffee's nearly frozen solid..."
        
        player "You should have been more specific."
        player "So about that wrench..."
        
        bea "Ugh. I guess a deal's a deal. Here, take it."
        bea "Just remember to bring it back as soon as you're done with it."
        
        player "I will. I literally just need to loosen two bolts."
        
        if exploredHouse == False:
            call marcieSalt
        else:
            bea "Good for you. Now if that's all you need, I've still got rock salt to move."
            
            hide bea with dissolve
            
            "Through the window, you can see the sun going down. It's about time for you to head back home."
            
            jump day2Evening
        
        
        
        
        
        
        
        
        
        
        
        
        "You returned to the hardware store to uphold you end of the bargain with the cashier."
        "She's still moving bags of salt around."
        
        show bea apron at center with dissolve
        
        #to do: bea responds differently based on your choice earlier
        bea "Wow, you actually came back. You must be desperate."
        
        "You set the coffee cup and your bag on the counter."
        
        bea "And you even got me a treat as well?"
        
        menu:
            "Claws off, that one's mine.":
                player "Claws off, that one's for me."
                
                bea "Relax, I'm just kidding."
                bea "Thanks for the coffee though, I needed it. Here's your wrench. Be sure to bring it back once you're done with it."
            "Err, yeah totally!":
                $ beaAP = beaAP +1
                
                player "Err, yeah totally!"
                
                bea "Oh! How sweet of you."
                
                "She digs the cinnamon roll out of the bag and nibbles on it."
                
                player "Can I have that wrench now?"
                
                bea "Yeah, here you go. Just be sure to bring it back once you're done with it."
                
        player "Of course."
        
        #bea "If that's all you need"
        bea "Now if you'll excuse me, these bags aren't gonna haul themselves."
        
        player "Right. I'll uh see you later then. And thanks."
        
        bea "Don't mention it."
        #bea "Same."
        
        bea "Now if you'll excuse me, I have more salt to haul."
        
        "She takes a sip of the coffee you just delivered and wanders to the back room."
        
        hide bea with dissolve
        
        "As you're about to leave the store, a short cat in an orange sweater bursts in."

        #"The croc sighs and pulls out an electronic cigarette. It lights up as she takes a puff from it."

        #hide bea with dissolve

        #"While she's away, you pass the time by taking a look around the shop."
    
        "Bea chastises you for getting her cold coffee and going so far when the bakery was right next door, but a deal is a deal. She likes Posspresso's fancier coffees more anyway."
        
        jump day2Evening
        
        
        
    elif beaQuestBakery == True:
        scene bg olpickaxe with dissolve
        
        
        "You returned to the hardware store to uphold you end of the bargain with the cashier."
        "She's still moving bags of salt around."
        
        show bea apron at center with dissolve
        
        "You return from the bakery and Bea thanks you for getting her hot coffee and gives you the wrench."
        #"If you went to the bakery first, you can give her a cookie. If you went after the hardware store you'll have a cinnamon roll and bea will comment on either."
        
        #to do: bea responds differently based on your choice earlier
        bea "Wow, you actually came back. You must be desperate."
        
        "You set the coffee cup and your bag on the counter."
        
        bea "And you even got me a treat as well?"
        
        menu:
            "Claws off, that one's mine.":
                player "Claws off, that one's for me."
                
                bea "Relax, I'm just kidding."
                bea "Thanks for the coffee though, I needed it. Here's your wrench. Be sure to bring it back once you're done with it."
            "Err, yeah totally!":
                $ beaAP = beaAP +1
                
                player "Err, yeah totally!"
                
                bea "Oh! How sweet of you."
                
                "She digs the cinnamon roll out of the bag and nibbles on it."
                
                player "Can I have that wrench now?"
                
                bea "Yeah, here you go. Just be sure to bring it back once you're done with it."
                
        player "Of course."
        
        #bea "If that's all you need"
        bea "Now if you'll excuse me, these bags aren't gonna haul themselves."
        
        player "Right. I'll uh see you later then. And thanks."
        
        bea "Don't mention it."
        #bea "Same."
        
        bea "Now if you'll excuse me, I have more salt to haul."
        
        "She takes a sip of the coffee you just delivered and wanders to the back room."
        
        hide bea with dissolve
        
        "As you're about to leave the store, a short cat in an orange sweater bursts in."

        #"The croc sighs and pulls out an electronic cigarette. It lights up as she takes a puff from it."

        #hide bea with dissolve

        #"While she's away, you pass the time by taking a look around the shop."
        
        


        
        jump day2Evening
        
        
        
    else:
        #first time entering the store
        $ metBea = True
        
        #bea mentions her coworkers called in sick or got injured or something
        
        scene bg olpickaxe with dissolve

        play music "music/picknaxe_loop.mp3" fadein 1.0

        #"Walking inside, you have to dodge boxes and miscellaneous items strewn about like they're in the middle of reorganizing their inventory."
        "Walking inside, an assortment of nails, screws, tapes, paints, and most importantly tools are on display. It's surprisingly well stocked for such a small town."
        "You guess the folk around here rely on building and repairing their own stuff more than people in the city do."
        #"Then again, country folk are more likely to use these sorts of things for repairs and home improvement. You weren't even allowed to put thumbtacks in the walls in your apartment in the city but here"
        "Snow shovels sure seem to be selling quick these days."
        #"The goth crocodile behind the counter just finished selling one to a customer and yawns before welcoming you."
        "The goth crocodile behind the counter just finished selling one to a customer."
        "Her tired eyes drift to look in your direction."        
        
        #"Behind the counter stands a bluish green crocodile giving off gothic vibes."
        #"Her tired eyes sluggishly drift to look in your direction."

        show bea apron at right with dissolve

        beaunknown "Welcome to the Ol' Pickaxe. Let me know if I can help you find any- *yawn*"
        beaunknown "-...thing."

        player "I need a wrench."
        
        beaunknown "Check the wrench aisle. Over thataway."
        
        "She points a finger to the other side of the store."

        #player "I'd rather not have to buy a full set. Don't you have single wrenches for sale?"
        
        #beaunknown "Yeah, they're over where the kits are."

        "She shrugs."
        
        beaunknown "Dunno if the one you want is in stock though."
        
        player "Thanks..."
        
        hide bea with dissolve
        
        "You go off to where she pointed to have a look."
        "There's a whole shelf with nothing but wrenches dangling off hooks for you to peruse."
        "Monkey wrenches, dogbone wrenches, alligator wrenches, crowfoot wrenches..."
        #"There doesn't seem to be any hex wrenches in the size you need however."
        "The one you need appears to be missing however."
        "At least not as a standalone item. It's only available as part of a larger kit that comes with a million other tools and has a price tag to reflect it."
        #"Let's see, 8mm, 8.5mm, 9mm, 9.6mm, 9.9mm, 9.99mm, 10.01mm... hey!"
        #"All of them are in stock except the one you need!"
        "You catch a glimpse of the cashier dragging a large bag of road salt between aisles and decide to approach her."
        
        show bea apron with dissolve

        player "Excuse me. You don't seem to have the tool I need in stock. I mean, outside of this overpriced kit."
        
        bea "Oh. Sorry about that."
        
        "She continues dragging the bag towards the pile near the front of the store."
        "You clear your throat."
        
        #do you need help dragging those bags?
        #I can handle it myself. Besides, it gives me an excuse not to deal with customers.
        
        $ askedHelp = False
        
label beaQuestions:
    menu:
        "Do you need help with that?" if askedHelp == False:
            $ sympathetic = sympathetic + 1
            $ askedHelp = True
            
            player "That bag sure looks heavy. Do you need help with that?"
        
            beaunknown "I can handle it myself. Besides, it gives me an excuse not to deal with customers as much."
            
            jump beaQuestions
        
        "When would you get a new shipment?":
            $ gentle = gentle + 1
            $ mature = mature + 1
            player "When do you think you'll get a new shipment. I need this tool as soon as possible."
            
            bea "Yesterday. But I'm not about to move all those boxes and open the one that might have your thing today when I've already got a huge backlog of work to do."
            
            player "..."
            
            bea "Not unless you get me a coffee."
            
            player "What?"
            
            "She yawns again and leans agains a shelf."
            
            bea "Didn't get much sleep last night. If you go out and buy me a coffee, then *maybe* I can be persuaded to prioritize your request."
            
            "You don't really have a choice if you want to fix your heating situation at home."
            
            player "Deal."
            player "What kind of coffee do you like?"
            
            bea "Dark. Like my soul or whatever, I don't care."
        "What's your return policy?":
            $ bold = bold + 1
            $ chaotic = chaotic + 1
            
            "You're backed into a corner and have no choice but to cheat a little."
        
            player "Say, what's your return policy?"
        
            bea "I know what you're planning. You're gonna buy the kit, use it to tighten one bolt then return it."
            
            player "N-no."
            
            "Dammit, she caught on immediately."
            
            bea "Tell you what."
            bea "If you get me a coffee... *yawn* ...I'll loan you a wrench."
            #she might have you buy her a coffee, and she'll let you borrow a wrench from the kit
            #bea "If you get me a coffee I'll loan you a wrench from one of those kits."
            bea "Just be sure to return it or I will hunt you down."
            
            player "Sheesh, wake up on the wrong side of the bed or something?"
            
            bea "More like never went to sleep in the first place. You gonna hook me up with some caffeine or not?"
            
            player "Fine. What kind of coffee do you like?"
    
            bea "Dark. Like my soul or whatever, I don't care."
    
    hide bea with dissolve
    
    "She drops the salt bag into a pile with the others then shuffles to the back of the store. You hear her start dragging another bag."
    #"Well that's a quest if you've ever heard one. You step outside and begin your hunt for coffee."
    "It feels like you've just been given a quest. You better get that gator some coffee. It's a hell of a lot cheaper than buying that whole wrench kit."
    
    
label day2roam:
    scene bg bakery_exterior with fade
    
    "Where will you go?"
    
    menu:
        "{cps=0}Where will you go?{/cps}"
        "Bear Essentials Bakery":
            $ beaQuestBakery = True
            
            jump meetingAngus

        "Ol Pickaxe":
            scene bg olpickaxe with dissolve
        
            show bea apron at center with dissolve
            
            beaunknown "Oh hey you're back. Got my coffee yet?"
            
            player "Nope."
            
            beaunknown "Then what are you doing here?"
            
            player "I dunno."
            
            beaunknown "..."
            beaunknown "I've got work to do."
            
            hide bea with dissolve
            
            jump day2roam
        "Posspresso":
            $ beaQuestPosspresso = True
            
            "Where can you get a coffee in this literally nowhere town?"
            "Well, you got some at Posspresso yesterday, so it's worth a shot to see if they're open today."
            "It's a bit of a walk though."
            
            scene bg cafe with fade
            
            show trish neutral at center with dissolve
            
            trish "Heya! Welcome back! I knew ya couldn't resist another cup o' joe but I didn't expect to see ya so soon!"
            
            player "Heh, it was pretty good, but I'm here on a fetch quest today."
            
            trish "Playin' delivery for someone else, huh?"
            
            player "Something like that."
            
            trish "Aww, I bet yer gettin' a gift for a cutie ya fancy~ Don't lie, I can see it in yer eyes!"
            trish "So what'll it be? It's on the house~"
            
            #player "Gimme the most bitter drink you've got."
            #player "She specifically requested it."
            
            player "Gimme something bitter."
            player "Something to match her bitter attitude..."
            
            trish "What was that?"
            
            player "Oh just a plain black coffee will do."
            
            trish "Comin' right up!"
            
            hide trish with dissolve
            
            "You find a place to sit while Trish makes the drink."
            "You're not looking forward to the long walk you have back towards town."
            "Hopefully the shop will still be open by the time you get there."
            
            show trish neutral at center
            
            trish "Aaaaand done!"
            trish "Hope yer date enjoys it!"
            
            player "She's not my..."
            
            trish "Here ya are riskin' life and limb out there in the snowstorm to get here, it warms my heart knowin' people love my coffee that much!"
            
            player "Right... well, thanks for the free coffee."
            
            trish "Anytime! Er no, not anytime. This is the one and only time actually."
            
            player "Fair. See you later!"
            
            trish "Come back soon!"
            
            hide trish with dissolve
            
            
            
            
            jump meetingBea