label marcieSalt:
    #written by punchoid, edited by codanon
    "Might as well have a look around to see if there's anything else here you could use."
    "You wander through the aisles but nothing really cathes your eye."
    "The bell at the door chimes as another customer steps in. You hear the sound of a heavy bag being hefted up onto the counter."
    #You overhear her conversation with the cashier from a couple of aisles away."
    
    show marcie neutral at left:
        xzoom -1
    show bea neutral at right
    with dissolve
    
    #"After aquiring your new doo-dad, you watch as a mousey older lady drags a particularly massive bag of salt to the register. Bea eyes it with apprehension as she rings it through."

    marcie "Either they keep putting more salt in these bags every year, or I'm getting too old to be hauling these!"
    marcie "How've you been, Beatrice? Work isn't treating you too hard?"

    bea "Hi Marcie, good to see you in my shop again. It's been a tough week, but the blizzard finally let up and I haven't had to shovel snow today so that's an improvement."

    marcie "Good, good. You've always been such a hard worker, dear, hopefully you get some time off soon."

    #"Despite her apparant exhaustion, bea smiles slightly at the warmth of the old woman's words before looking back to the sack of salt on the floor."
    
    #bea "Always busy..."
    
    bea "There's always work to be done."
    bea "Are you gonna be okay getting home with this on your own? This bag's well over 40 pounds."

    marcie "Oh, I know that. You guys deliver within town limits though, right?"
    marcie "You could just drop it off for me later today."

    bea "It's just me here today. One called in sick and the other slid his car into a ditch so I'm scrambling to get everything done."
    #Sorry, our truck can't drive in this snow. Needs new tires...
    bea "Sorry, I don't know if I'll be able to get this salt to you today. Lots of orders are already backed up..."
    
    marcie "Well dang. The moment I run out of rock salt is right when the biggest blizzard of the decade hits..."
    
    "You look down at the wrench in your hand. You already did a favor for the cashier but maybe you should help out with this too. She looks like she's got a lot on her claws."
    "Plus, that poor old lady is liable to die just trying to get that back out of the store."
    #"Bea's eyes meet yours and you can see how worn down she is from unloading probably over 100 of those bags earlier."
    #"You guess you could help, she did get you your wrench after all. Plus, that poor old lady is liable to die just trying to get that back out of the store."
    
    menu:
        "Offer to help":
            $ sympathetic = sympathetic + 1
            $ gentle = gentle + 1
            $ beaAP = beaAP + 1
            $ helpmarcie = True
            
            "You hope you don't regret this later..."
            "You walk over to the counter and put on a friendly smile."

            player "Hi there! I couldn't help but notice what a heavy load you've got there. Would you like some help carrying that?"
            
            "Bea looks at you with mild surprise while the elderly woman greets you with a welcoming expression."
            #"bea and the older woman look back at you with surprise, but you catch something else in Bea's face that she quickly hides. Relief? Respect?"

            marcie "Oh how kind of you, young [manladycreature]. I'll take you up on that offer!"
            
            player "It's no trouble. I don't have anything better to do at the moment anyway."
            
            "Bea lets out a relieved sigh."
            
            bea "That would really help us out if you did."
            
            "You grab hold of the bag and hoist it onto your shoulder with a grunt. The jagged points dig into your skin but you try not to wince."
            
        "Carry it yourself, boomer":
            $ chaotic = chaotic + 1
            $ introverted = introverted + 1
            
            "That thing looks heavy. You don't need to show off and carry it for anyone."
            "You try to sneak out of the store but that old mouse notices and calls out to you."
            
            marcie "Excuse me young [manladycreature]! You look healthy and strong! Mind helping an elderly lady out?"
            
            player "Well, I mean..."
            
            marcie "Pretty please? There's something in it for you if you do."
            
            "Between the mouse's fingers is a $5 bill, she waves tantalizingly."
            "Sigh."
            "Fine, you'll do it but five dollars is the lowest you'll go."
            
            player "I guess I can spare some time. Let me grab that for you."
            
            "You put on a friendly face and hoist the bag up onto your shoulder with a grunt."
            "This thing is heavier than it looks and the jagged edges dig into your neck."
            "With your free hand, you grab the cash and stuff it in your pocket."
            
    bea "You got it?"
    
    player "Y-yeah, it's just an awkward shape."
    
    bea "Welcome to my world."
    bea "Just try not to slip and die, I'm not liable if you do."
    
    player "I'll try my best."
    player "Lead the way, miss."
    
    marcie "Right this way dear."
    
    scene bg roads_day with dissolve
    
    "You look around at the few cars on the street outside and wonder which one belongs to the old lady."
    "You follow her along the sidewalk, straining with each step as the heavy bag cuts into your shoulder."
    
    player "Excuse me, which car is yours, ma'am?"
    
    show marcie neutral at left with dissolve:
        xzoom -1

    marcie "Hm? Oh, I don't have one. How's that rock salt? Not too heavy is it?"
    
    player "N-no but I didn't sign up to drag this thing all the way across town."
    
    "The old mouse laughs and waves her hand dismissively."
    
    marcie "Don't worry, I don't live that far away! We're almost there."
    marcie "By the way, my name's Marcie."
    
    player "Nice to meet you Marcie, I'm..."
    
    marcie "[name], I know. We've met before, don't you remember?"
    
    player "Huh? I just got here like two days ago."
    
    marcie "Maybe so, but you've been here before, haven't you?"
    
    player "A couple of times. But that was more than a decade ago!"
    
    marcie "Has it been that long? My, time flies. You've grown so tall since I last saw you!"
    
    player "You recognized me? I was just a kid back then."
    
    marcie "I know those eyes anywhere. Striking, just like your father's. I'm so sorry about what happened to him."
    
    player "..."
    player "Yeah."
    player "You knew him well?"
    
    marcie "Not really, no. He mostly kept to himself. But he was kind whenever our paths crossed."
    marcie "Anyway, here we are! Just leave it by the front step there."
    
    "Thank goodness. You weren't sure how much further you could carry this thing uphill. You dump the bag on the ground and stretch out your spine."
    
    marcie "I truly appreciate your help, you know. Lots of folk are too focused on their own problems and interests to help out others, but not you."
    
    player "That's awfully kind of you to say."

    "You take a breath and rub your shoulder."
    
    marcie "You alright? Didn't straing yourself too hard, did you?"
    
    player "I'm fine. Just never had to do that before."
    player "I need to head home soon though. Sun's coming down and the wind is starting to pick up."
    
    marcie "Well don't let me keep you! I'm sure we'll run into each other soon."
    marcie "And you're welcome to stop by whenever you have the time! I'll make tea for us and we can catch up."
    
    player "Heh, I'd appreciate that. See you around, Marcie."
    
    marcie "See you around, [name]!"

    "You raise a hand in farewell and continue your walk, feeling lighter, literally and figuratively. What a pushy woman. Still, it feels good to help."
    
    
    #marcie "And don't worry, I can spread this myself. I'm not *that* old!"
    #marcie "I'll see you around, [player]! I could always use someone to help out, and there's something in it for you next time!"
    

    return