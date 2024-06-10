#label meetingBea:
#    if beaQuestPosspresso == True:
#        #triggers when you come to the store with posspresso drinks
#        scene bg olpickaxe with dissolve
#        
#        "One long trek back to the hardware store later..."
#        
#        show bea apron at center with dissolve
#        
#        bea "What the eff, you went all the way to Posspresso?! No wonder it took you so long."
#        bea "This coffee's nearly frozen solid..."
#        
#        player "You should have been more specific."
#        player "So about that wrench..."
#        
#        bea "Ugh. I guess a deal's a deal. Here, take it."
#        bea "Just remember to bring it back as soon as you're done with it."
#        
#        player "I will. I literally just need to loosen two bolts."
#        
#        if exploredHouse == False:
#            call marcieSalt from _call_marcieSalt
#        else:
#            bea "Good for you. Now if that's all you need, I've still got rock salt to move."
#            
#            hide bea with dissolve
#            
#            "Through the window, you can see the sun going down. It's about time for you to head back home."
#            
#            jump day2Evening
#        
#    elif beaQuestBakery == True:
#        #triggers when you come to the store with drinks from bakery
#        scene bg olpickaxe with dissolve
#        
#        "You returned to the hardware store to uphold you end of the bargain with the cashier."
#        #"She's still moving bags of salt around."
#        
#        show bea apron at center with dissolve
#        
#        #"If you went to the bakery first, you can give her a cookie. If you went after the hardware store you'll have a cinnamon roll and bea will comment on either."
#        
#        #to do: bea responds differently based on your choice earlier
#        bea "Wow, you actually came back. You must be desperate."
#        
#        "You set the coffee cup and your bag on the counter."
#        
#        bea "And you even got me a treat as well?"
#        
#        menu:
#            "Claws off, that one's mine.":
#                player "Claws off, that one's for me."
#                
#                bea "Relax, I'm just kidding."
#                bea "Thanks for the coffee though, I needed it. Here's your wrench. Be sure to bring it back once you're done with it."
#            "Err, yeah totally!":
#                $ beaAP = beaAP +1
#                
#                player "Err, yeah totally!"
#                
#                bea "Oh! That's surprising. How sweet of you."
#                
#                if cinnamonRoll == True:
#                    "She digs the cinnamon roll out of the bag and nibbles on it."
#                
#                else:
#                    "She digs the remaining cookie out of the bag and nibbles on it."
#                
#                player "Can I have that wrench now?"
#                
#                bea "Yeah sure. Just remember to bring it back once you're done with it."
#                
#        player "Of course."
#        
#        #bea "If that's all you need"
#        bea "Now if you'll excuse me, these bags aren't gonna haul themselves."
#        
#        player "Right, I guess I'll see you later then. And thanks."
#        
#        bea "Don't mention it."
#        
#        "She takes a sip of the coffee you just delivered before heading to the back room."
#        #bea "Same."
#        
#        hide bea with dissolve
#        
#        if exploredHouse == False:
#            call marcieSalt from _call_marcieSalt_1
#            
#            jump day2Evening
#        else:
#            jump day2Evening
#            
#            #bea "Now if you'll excuse me, I have more salt to haul."
#            
#            #"She takes a sip of the coffee you just delivered and wanders to the back room."
#            
#            #"As you're about to leave the store, a short cat in an orange sweater bursts in."
#
#            #"The croc sighs and pulls out an electronic cigarette. It lights up as she takes a puff from it."
#
#            #hide bea with dissolve
#
#            #"While she's away, you pass the time by taking a look around the shop."
#        
label meetingBea:
    #first time entering the store
    ####can do a simple check if $ metAngus == True towards the end to have a unique line about revisitng the bakery for coffee
    $ metBea = True
    
    scene bg olpickaxe with dissolve

    #play music "music/picknaxe_loop.mp3" fadein 1.0
    
    "Walking inside, an assortment of nails, screws, paints, and tools are on display. It's surprisingly well stocked for such a small town."
    "You guess the folk around here rely on building and repairing their own stuff more than people in the city do."
    "Snow shovels sure seem to be high demand these days."
    "The gothy crocodile behind the counter just finished selling one to a customer before glaring at you."

    show bea apron at right with dissolve

    bea "Welcome to the Ol' Pickaxe. Let me know if I can help you find any- *yawn*"
    bea "-...thing."

    player "I need a screwdriver."
    
    bea "Ask for one at the bar across town."
    
    player "Hah. No but seriously I need a screwdriver."
    
    bea "Check the screwdriver aisle. Over thataway."
    
    "She points a claw to the other side of the store."

    player "Thanks..."
    
    hide bea with dissolve
    
    "You go off to where she pointed to have a look. There's a wide variety of different kinds but the one you need eludes you."
    "You found some that look like the right shape but there's an empty space for the size you need."
    "It's only available as part of a larger kit that comes with a million other tools and has a price tag to reflect it."
    "After wandering the aisle a few times hoping to spot a singular one somewhere, you catch a glimpse of the cashier dragging a large bag of road salt and decide to approach her."
    
    show bea apron at center with dissolve:
        ypos 1150

    player "Excuse me, you don't seem to have the tool I need in stock. I mean, outside of this overpriced kit."
    
    bea "Oh. Sorry about that."
    
    "She continues dragging the bag towards the pile near the front of the store."
    "You clear your throat."
    
    $ offeredHelp = False
    
    label beaQuestions:
    menu:
        "Do you need help with that?" if offeredHelp == False:
            $ sympathetic = sympathetic + 1
            $ offeredHelp = True
            
            player "That bag sure looks heavy. Do you need help with that?"
        
            bea "I can handle it myself. Besides, it gives me an excuse not to deal with customers as much."
            
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
            
            "You're backed into a corner and have no choice but to cheat the system a little."
        
            player "Say, what's your return policy?"
        
            bea "Forget it, I know what you're planning. You're gonna buy the kit, use it to tighten one screw then return it."
            
            player "N-no."
            
            "Dammit, she caught on immediately."
            
            bea "Tell you what."
            bea "If you get me a coffee... *yawn* ...I'll loan you the tool."
            bea "Just be sure to return it or I *will* hunt you down."
            
            player "Sheesh, wake up on the wrong side of the bed or something?"
            
            bea "More like never went to sleep in the first place. You gonna hook me up with some caffeine or not?"
            
            player "Fine, I'll do it. It's cheaper than buying the full kit, that's for sure."

            bea "Just make sure they don't put too much creamer in it. It ruins the flavor."

    hide bea with dissolve

    "She drops the salt bag into a pile with the others then shuffles to the back of the store. You hear her start dragging another bag."
    #"Well that's a quest if you've ever heard one. You step outside and begin your hunt for coffee."
    #"It feels like you've just been given a quest. You better get that gator some coffee. It's a hell of a lot cheaper than buying that whole wrench kit."
    "It feels like you've just been given a quest."
    "You step out of the shop and look around. Where could you get coffee for that crocodile?"
    "There's Posspresso but it's a long way and the drink would surely get cold on the way back."


label day2roam:
    scene bg roads_day with fade

    "Where will you go?"

    menu:
        "{cps=0}Where will you go?{/cps}"
        "Bear Essentials Bakery":
            $ beaQuestBakery = True
            
            jump meetingAngus

        "Ol Pickaxe":
            scene bg olpickaxe with dissolve
        
            show bea apron at center with dissolve
            
            bea "Oh hey you're back. Got my coffee yet?"
            
            player "Nope."
            
            bea "Then what are you doing here?"
            
            player "I dunno."
            
            bea "..."
            bea "I've got work to do."
            
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