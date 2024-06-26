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
        
        show lori neutral at left with dissolve:
            xzoom -1
        
        player "Whoa! Lori, you startled me!"
        
        lori "Sorry..."
        
        player "It's fine, I was just... I found this wallet on the ground and was returning it."
        player "This is Mae's house, right?"
        
        lori "Yup! Is she home? Did you knock on the door yet?"
        
        player "Err, not yet..."
        
        lori "Well what's the hold up? It's freezing out here and I wanna go inside!"
    else:
        lori "Um, hello?"
        
        "You turn around and see a timid mouse girl with an overstuffed bag on her back."
        
        show lori neutral at left with dissolve:
            xzoom -1
        
        player "Hey...?"
        
        "A look of realization dawns on her."
        
        lori "What a minute... I know you!"
        
        "She does look kinda familiar, but it's hard to tell in the lighting."
        
        lori "We met on the bus, remember?"
        
        "You try to remember back to that night."
        
        call loriFlashback
        
        scene bg street with fade
        
        show lori neutral at left:
            xzoom -1
        
        player "Oh right, now I recall! Lori, right?"
        
        lori "Yup! What're you doing at Mae's house?"
        
        player "I found this wallet on the street and came to return it."
        
        lori "Did you knock on the door yet?"
        
        player "No..."
        
        lori "Then how do you expect anyone to open it?"
        
    "Lori reaches past you and rings the door bell."
    
    "A pleasant chime echoes from within and a moment later, the door opens."

    show mae neutral at right with dissolve
    
    mae "Lori!"
    mae "Annnnd.... you?"
    
    player "Hey uhh, I found your wallet lying on the sidewalk. Your license had your address, so I just came by to return it."
    
    "You hold the wallet out for her. Mae takes it and rummages around inside it."

    show mae panic
    
    if metMae == True:
        mae "Wow, I didn't even know I lost this. Thanks, [name]!"
        
        show mae happy
    
        "Her demeanor visibly brightens now that she's reunited with her wallet. You're glad you finally got that over with."
    else:
        mae "Wow, I didn't even know I lost this. Thanks... what was your name again?"
        
        player "[name]."
        
        show mae skeptical at left

        "She narrows her eyes at you."

        mae "Do I know you from somewhere?"
        
        player "I'm new in town. I think we passed by each other at the bus station?"
        
        mae "I'm Mae. Mae Borowski. Nice to meet you!"
        
        player "Same!"

        mae "So what made you decide to come all the way out to Possum Springs?"

        player "You know, the relaxing countryside, the fresh air, peace and quiet... oh and inheriting a house up past the train tracks."
        player "The old man was nice enough to put it in my name before he died a few years back."

        show mae sad1

        "Mae looks away and mumbles to herself."

        mae "Died...?"

        show mae panic at left
        
        mae "Err how many years ago? If you don't mind my asking...?"
        
        player "Like five I think?"

        "She suddenly looks like she's seen a ghost."
        
        mae "Uhh wow, very interesting!"
        mae "Well thanks for returning my wallet and all but I've gotta get back to doing stuff right now!"
    
    mae "Come on in, Lori, food's almost ready!"
    
    candy "Mae honey, is that Lori? Come wash your paws and get some dinner!"
    
    show candy neutral at right with dissolve
    
    ####to do: alternate version if you've already met Candy
    
    candy "Oh? Who's this? A friend of yours?"
    
    mae "[heshethey] just stopped by to drop off something I lost."
    
    candy "Mae, did you lose your wallet again?"

    show mae angry

    mae "Mom!"

    candy "What? I can't count the number of times you've lost that thing. Did you tell [himherthem] thank you?"

    show mae grump

    mae "Yes Mom, I'm not five anymore. I know how to talk to people."
    
    candy "Well? Aren't you going to invite [himherthem] to join us for supper?"
    
    player "That's okay, I don't really want to intrude..."

    candy "Oh, don't be shy, dear! I insist!"

    "Well, that settles it, you guess. It's not like you can say no to a kind lady offering you food."
    "She invites you inside and walks you through the kitchen to the dining area with Lori and Mae in tow."
    
    mae "..."

    lori "What?"

    mae "Nothing."

    scene bg maekitchen with fade
    #play music "music/Stagnant_Tone-down.mp3" fadein 1.0

    "The dining table is small and square shaped with only four chairs. You awkwardly take a seat adjacent to Lori and across from Mae."
    "Mrs. Borowski goes to the stove to stir the pot with a ladle before turning off the burner."

    show candy neutral at right
    show lori neutral at left
    show mae sad1 at left
    with dissolve

    candy "You all sit tight, and I'll have a bowl out for everyone in just a minute!"

    mae "Aren't we gonna wait for Dad to come home?"

    candy "Not tonight, hun. Your father called to say he'd be working a little late and to go ahead and have dinner without him."

    mae "Oh."

    "There's another awkward pause as Mrs. Borowski takes a tray of toasted garlic bread out of the oven."

    candy "So, [name], I'm curious about how and where Mae lost her wallet this time. It didn't slip through a grate again, did it?"
    candy "She spent hours fishing it out last time hehehe!"
    
    mae "Mom! Enough!"

    player "I just found it lying in the snow on the sidewalk. I guess it must have fallen out of her pocket when she was jumping around on the rooftops."
    
    "Mrs. Borowski gasps."
    
    candy "Mae!"
    candy "I thought you'd given up that habit!"
    
    "Mae groans."
    
    mae "Ugh, it's just a bit of harmless fun. Lori came back in town so we wanted to play rooftop tag for old time's sake."
    
    candy "Tsk tsk! Such a bad influence!"

    "Mrs. Borowski sets a steaming bowl of soup in front of you while glaring at Mae."

    mae "Whatever Mom, nobody got hurt so it's not a big deal."
    
    candy "You might not be so lucky next time! And with all the snow! What if you or Lori had slipped?"
    candy "Then you'd be having your little sleepover at the hospital without any homemade soup!"

    "Mrs. Borowski finishes setting the dinner table and takes a breath to calm herself."

    candy "I suppose now's not the time to lecture you when we have guests over. Go on, enjoy the soup!"
    
    lori "Thanks for making dinner for us Mrs. B!"
    
    player "Yeah, it smells really good."
    
    "You dip a spoon into your bowl and blow on it before taking a bite (sip?)."
    "Your taste buds still get scalded but it's worth it for the taste."
    
    mae "Heh, nothin' beats mom's cooking."
    
    "You chat with your newfound tablemates while enjoying the sweet and spicy soup. When you're done, Mrs. Borowski offers you a second bowl, which you happily accept."
    "She's very... motherly. Not just to Mae, but to Lori and yourself as well."
    "She's eager to know more about you and your wellbeing."
    "Lori is kinda shy and awkward, and Mae acts like a rebellious teenager at times, but it feels like everyone is part of one family while at the table."
    
    candy "...and have you seen the most recent painting Mae's been working on?"

    player "I haven't really seen any of Mae's artwork yet."

    candy "You should! She's improved so much in the past few years, she could be the next Picasso!"

    show mae grump

    mae "Mom, please. It's not that good."

    candy "Nonsense! That cute little coffee shop at the end of town bought some of your originals so clearly someone thinks they're worth good money!"
    candy "In fact, why don't you go show [name] your room so they can see your art while I take care of the dishes?"
    
    mae "M-my room??"
    mae "It's not really in a condition for anyone to be up there!"
    
    candy "Yet you invited Lori to stay the night?"
    
    mae "Hrmmph."
    mae "...Fine, come on upstairs."
    
    scene bg maebedroom with dissolve
    
    "Mae leads you and Lori up the stairs to a room which you're pretty sure is actually a repurposed attic."
    "It's messy and cluttered with all kinds of posters and pictures on the walls. It reminds you of a stereotypical punk teenager's bedroom you'd see in a movie."
    "She's even got a bass in here."
    "Mae walks over to the easel next to the nightstand and gestures to it."
    
    mae "It's not finished, but here it is."

    "An ominous head floating in a dark, starry void with glowing eyes stares back at you."

    menu:
        "I like it.":
            player "Very nice. I like it a lot."

            show mae sad1

            mae "Meh, it's nothing special..."

            player "Well I think your mother was right, it belongs in a museum!"

            show mae skeptical
            show lori shrug at right with dissolve

            lori "\"So do you!\""

            show mae skeptical

            "You and Lori bust out laughing."

            show mae laugh

            "Even Mae can't help but smirk at yours and Lori's silly movie references."

            mae "Heheh."

            show mae neutral

            mae "Anyway, I'm not very happy with how this one turned out. I'm not sure I'll ever get around to finishing it."

        "It's creepy.":

            player "It's creepy."

            show mae angry

            mae "It's supposed to be. That's the whole point."

            show lori shrug at right with dissolve

            lori "Creepy is good! I like creepy."

            player "It kinda disturbs me."

            show mae sad1

            mae "Meh, I guess it's not for everyone."
            mae "I'm not very happy with how it turned out either. I probably won't ever get around to finishing it."

        "What inspired you?":

            player "Very interesting. What inspired you?"

            mae "Um, nothing in particular. Just came to me in a dream I guess."

            show lori shrug at right with dissolve

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
    
    menu:
        "Are you two dating?":
            "You clear your throat, not sure of what to say but this akward silence has gone on long enough."
            
            player "So... Are you two like a couple or what?"
            
            "Why did you say that?"

            show mae freakout

            mae "Huh?"

            show lori anxious3

            show mae panic

            mae "A couple???"
            
            player "Yeah like."
            player "Um."
            player "So you're not dating?"

            "You get the feeling you've made a tremendous error."

            show lori breath
            show mae freakout

            lori "Whaaaaaat? You thought Mae and I were dating???"

            mae "We're not- That doesn't even- HOW??"

            "Oh God, you messed up."

            player "I just thought... I mean I always see you together so..."

            "There is no way you can salvage this."

            "Mae and Lori exchange a glance at each other then giggle among themselves. You contribute little more than an embarrassed chuckle."

            show lori cheeky
            show mae laugh

            lori "Hahahaha does it really seem like we're dating? I had no idea!"

            mae "Hahaha yeah we're just really good friends is all!"
            mae "If anything, I see Lori almost like a little sister!"

            player "Sorry, I just had a dumb moment."

            show mae neutral

            mae "It's alright. My life is full of dumb moments."
            mae "Anyway, I think we've all had our fill of my weird art. Let's head back downstairs."
        "Any sleepover plans":
            "You clear your throat, not sure of what to say but this akward silence has gone on long enough."
            
            player "So... you two have any cool sleepover plans?"
            
            lori "We're mostly just gonna watch a bunch of horror movies and draw."
            
            mae "Yeah. Maybe paint our claws if we get around to it."
            
            player "Cool, cool."
            player "Well I hope you two have fun with that. I think I should get going though. It's getting kinda late out."
    
            mae "Yeah... sorry my room's a wreck haha. Let's all head back downstairs."

    scene bg maelivingroom with dissolve
    #stop music fadeout 2.0

    show candy neutral at left
    show lori neutral at right
    show mae neutral at right
    with dissolve

    "From the lobby you can see Mrs. Borowski washing the dishes in the kitchen sink. The clock on the wall near her shows it's way later than you thought it was."

    player "Hey Mrs. Borowski! I think I'm gonna head home now. Thanks again for the meal!"

    candy "Going home so soon? Stay safe out there!"

    player "I will! Thanks for having me over!"

    hide candy with dissolve

    "You turn to Mae and Lori."

    player "And sorry, I didn't mean to take up so much of your evening."

    mae "It's cool."

    lori "Yeah, it was a pleasant surprise seeing you tonight, [name]!"

    player "See you guys later!"

    lori "See ya!"

    mae "Bye, [name]!"

    hide mae
    hide lori
    with dissolve

    "Mae opens the door for you and you give a last friendly wave as you wander into the night back to your house."
    
    $ dayWalletFound = 0

    $ metMae = True

    return