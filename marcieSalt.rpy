label marcieSalt:
    "After aquiring your new doo-dad, you watch as a mousey older lady drags a particularly massive bag of salt to the register. Bea eyes it with apprehension as she rings it through."

    marcie "Either they keep putting more salt in these bags every year, or I keep getting older! How've you been, Beatrice? Work isn't treating you too hard?"

    bea "Hello Marcie. It's been a tough few days, but the blizzard let up and I haven't had to shovel today so that's an improvement."

    marcie "Good, good. You've always been such a hard worker, dear, hopefully you get some time off soon."

    "Despite her apparant exhaustion, bea smiles slightly at the warmth of the old woman's words before looking back to the sack of salt on the floor."

    bea "Marcie, are you gonna be okay to get home with this? This bag's well over 60 pounds."

    marcie "Oh, I know that. You guys deliver within town limits though, right?"
    marcie "You could just drop it off for me later today."

    bea "Uhhh..."
    #Sorry, our truck can't drive in this snow. Needs new tires...
    bea "Sorry, I don't know if I'll be able to get it to you today. Lots of orders are backed up..."
    
    "Bea's eyes meet yours and you can see how worn down she is from unloading probably over 100 of those bags earlier."

    "You guess you could help, she did get you your wrench after all. Plus, that poor old lady is liable to die just trying to get that back out of the store."
    
    menu:
        "Offer to help":
            $ sympathetic = sympathetic + 1
            $ gentle = gentle + 1
            $ helpmarcie = True
            
            "You hope you don't regret this later..."

            player "Excuse me, would you like some help carrying that out of here?"
            
            "bea and the older woman look back at you with surprise, but you catch something else in Bea's face that she quickly hides. Relief? Respect?"

            marcie "Oh, thank you young man/woman/thing, I'll take you up on that if you're offering!"
        "Carry it yourself, boomer":
            "That thing looks heavy. You don't need to show off and carry it for anyone."
    

    "Bea visibly relaxes at your words, and you can almost hear some of the tension leave her shoulders."

    bea "Thanks, [name]. I owe you one for this, don't worry."

    player "It's no problem, I have some time today anyway."

    "You reach down and heft the bag up to your knee."
    "Dear god, this is heavy, it's like it's made of... Well, rocks."
    "With a mighty heave, you swing it up and onto your shoulder before straightening. Bea raises an eyebrow."
    
    player "I'm fine, it's just my first bag of the day."
    
    "Bea rolls her eyes."

    bea "Don't slip and die, I'm not liable if you do."

    "You're not sure if that's true, but you walk out of the door regardless, it's too late to give up on your task."
    "You look around at the few cars on the street outside and wonder which one belongs to the old lady."
    "As you turn to look at her, you see her start walking up the street, so you follow, straining with each step as the heavy bag cuts into your shoulder."
    "But the lady just keeps walking."

    player "Excuse me, which car is yours, ma'am?"

    marcie "Oh, I don't have a car, we're going back to my house. Don't worry, it's only a block away!"

    "Oh."
    "Your back already aching, you resign yourself to the task. You would be the worst person ever if you quit now, so you keep following behind the surprisingly quick old mouse."

    marcie "Nearly there now! The name's Marcie by the way."

    player "-pant- My name is [player]."

    #Dad thing here?

    marcie "And what brings you to Possum Springs? I know everyone in this town, and I don't know you."

    player "I inherited a house here, and I don't really have anywhere else to go."

    marcie "I see... Well, I won't pry. Nothing wrong with keeping something to yourself."

    "You can only grunt in acknowledgement as you continue to wrestle the bag up a hill. It feels like a lifetime since you used some of these muscles."
    "After what feels like 3000 years, the two of you arrive at the front sidewalk of a small house."

    marcie "That's the one, just leave it by the front step there."

    "After a short dash up the walk to the front door you let the bag tumble from your arms with a hefty thud."
    player "-pant- -pant- Th-there we go, that wasn't so bad..."

    "You hope you can get out of bed tomorrow."
    "Marcie turns toward you with a twinkle in her eye."

    marcie "I truly do appreciate your help, you know. People are usually more focussed on their own problems and interests, but not you."

    player "Aw, it was nothing, really. I'm sure anybody else would have done it."

    "You rub your shoulder where a seam in the bag feels like it is permanently indented on your skin."

    marcie "You might be right, but I still appreciate it. And don't worry, I can spread this myself. I'm not *that* old!"

    player "Ha, alright."

    "As you turn around and walk back to the street, Marcie calls over to you."

    marcie "I'll see you around, [player]! I could always use someone to help out, and there's something in it for you next time!"

    "You raise a hand in farewell and continue your walk, feeling lighter, literally and figuratively. What a pushy woman. Still, it feels good to help."
    
        #jump nextscene or something
#lots of ways to go with this, and some things could be changed since it's a pretty barebones interaction, but it at least introduces another character and shows the player that there is more to the town than the main characters. Perhaps Marcie has a continuing storyline if you keep checking things out, idk

        #Speedwalk out of there:
        #change this so marcie has to bribe you to do it
        #Nope, that looks heavy and I would like my spine to stay intact.
        #$ chaotic = chaotic + 1
        #$ askedHelp = False

        #You start to turn 360 degrees and walk away, but the lady turns and holds you under her gaze.

        #marcie "Ah, you look like you're strong enough to carry this for me. What do you say? Beatrice here has enough on her plate without worrying about me."

        #Looks like there's no way out of this without alienating the shopowner, and unfortunately if you ever need another tool she's the only person in town that can get it for you. You force a friendly smile.

        #player "I guess I have some time, let me grab that for you."

#Probably just connect this to a point in the first option where you offer

#maybe we can give the player the option to back up check out the house before the end of the day instead of helping, but choosing this option would probably close off some Marcie stuff and lower Bea's opinion of you. Idk, all sorts of shit can be done and my formatting isn't great

    return