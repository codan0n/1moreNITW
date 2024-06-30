label angusBakeryIntro:
    #this variant is for visiting the bakery before ever going to the hardware store
    
    $ bakeryVisited = True
    $ metAngus = True
        
    scene bg bakery_exterior with dissolve
    
    "You decide to check out the bakery first."
    "The smell of pastries, confections, and coffee fills the air around it."

    scene bg bakery_interior with fade

    #play sound "sound/storebell.mp3"
    #play music "music/Indecisive_Redux.mp3" fadein 1.0
    
    "A bell on the door jingles as you open it and step inside."
    "Despite the modern furnishings, the cracks in the walls reveal this building's age."
    "It's pretty spacious though, even with the massive stage taking up a large portion of the room. Must be a leftover from the previous business."
    "Music plays softly from the speaker resting upon it."
    #"A bell on the door chimes as you step inside and a voice calls out from the back of the shop."

    "A voice calls out from the back of the shop."
    
    angus "I'll be with you in just a moment!"
    
    "You look over the treats behind the glass case while you wait, trying to decide what to get."
    "Before long, a bear comes around the corner, holding a tray of peppermint frosted cookies between mittened paws."
    
    show angus neutral at left with dissolve:
        xzoom -1
    
    angus "Sorry for the wait, these were ready to come out of the oven."
    angus "What can I get you?"
    
    player "Those smell really good! Can I get a couple to go?"
    
    angus "Of course! Will that be all for you?"
    
    player "Yep. For now at least."
    
    "The baker uses a pair of tongs to grab a couple of cookies and drops them into a paper bag."
    
    angus "Here you go! I'll ring you up over here."
    
    "You pull a piping hot cookie from the bag and nibble on it while completing your purchase."
    
    player "Ow! Hot!"
    
    angus "Please do be careful. I know it's freezing outside but I literally just pulled those out of the oven."
    
    player "I couldn't resist. It's so good!"
    
    angus "I'm glad you enjoy it enough to scald your tongue, but I assure you they're just as good after they've cooled down."
    
    "The bear rings up your order and you swipe your card on the machine."
    
    angus "Thanks, have a good day!"
    
    player "You too!"
    
    hide angus with dissolve
    
    "You exit the store satisfied with your sugary snack and make your way to the hardware store."
    
    jump meetingBea


label angusBakeryCoffee:

    #need variations for if you have never met angus, if you have met angus, if you visited the bakery before, if you didn't visit the bakery before
    #definitely need different versions for if you visited bakery prior, but can have just a small variation if you only met angus at the park
    
    scene bg bakery_interior with dissolve
    
    if bakeryVisited == False:
        "A bell on the door jingles as you open it and step inside."
        "Despite the modern furnishings, the cracks in the walls reveal this building's age."
        "It's pretty spacious though, even with the massive stage taking up a large portion of the room. Must be a leftover from the previous business."
        "Music plays softly from the speaker resting upon it."
        "A fox sits atop the main counter, chatting with the baker."
    else:
        "You open the door and step inside. A fox sits atop the main counter, chatting with the baker."

    show angus neutral at left with dissolve:
        xzoom -1


    if bakeryVisited == True:
        angus "Welcome back! Gregg, get off the counter, I have a customer."
    else:
        angus "Welcome! Gregg, get off the counter, I have a customer."
        
    show gregg neutral at right with dissolve
    
    gregg "I like being up here though! I makes me feel tall!"
    
    angus "Don't make me spray you with water."
    
    gregg "Ffffiiine."

    "The fox pouts and whines as he slides off. His boots make a loud *thud* as they hit the floor and the whole room shakes a bit."
    #every loose object in the room rattles
    
    gregg "Hey, it's you! I had a feeling we'd meet again!"
    gregg "Remember me?"
    
    menu:
        "Oh yeah":
            $ greggAP = greggAP + 1
            #$ autism = autism + 1
            
            player "The Ham Panther cashier at register number four?"
            player "How could I forget?"
            
            gregg "You do remember!!!"
            
            #angus "Calm down, hun."
            angus "You do make quite an impression on new people."
        "No?":
            $ chaotic = chaotic + 1
            $ mature = mature - 1
            
            player "Sorry, I'm drawing a blank here."
            
            gregg "I'll give you a hint: Ham Panther. Yesterday."
            
            player "I don't think I went there yesterday."
            
            gregg "Come on! Register number four! I scanned your [groceryItem]!"
            
            player "Sorry, doesn't ring a bell. I only drink whole milk."
            
            gregg "You're messing with me! I definitely saw you!"
            #gregg "Aw c'mon, you're breaking my heart!"
            
            angus "Maybe you never met and it was all in your head?"
            
            gregg "What are ya tryin' to say?! That I belong in a looney bin?"
            
            angus "Mh. Not yet. We'll continue to monitor your condition and make a determination at a later date."
            
            gregg "Hmph! You better come visit me in my padded cell often!"
            
            angus "Tell me how much the rent is, I might come live with you."
            
            player "I'm just kidding, I remember you."
            
            gregg "I knew it! I'm not insane!"
            
            angus "I'm not so sure about that."
            
    gregg "By the way, I don't think I caught your name yesterday."
    gregg "I'm Gregg, and that's Angus. All you need to know about him is that he is the best."

    angus "Oh you."
    
    if metAngus == True:
        angus "We actually met earlier. Like, just a few minutes ago. You said your name was...?"
    
        player "[name]"
    
        gregg "Nice to meet you, [name]! How are you enjoying Possum Springs so far?"
    else:
        "Nice to meet you guys. I'm [name]."
        
        gregg "[heshethey] said [heshethey] just moved into Possum Springs."
    
        angus "How are you enjoying it so far?"

    player "I'm slowly getting used to it."
    
    angus "Eh, it grows on you."
    
    player "I still haven't explored that much but the shops are cute."
    
    gregg "Don't go to Snack Falcon, that place sucks."
    
    angus "They never were the same after that fire."
    
    gregg "Too bad they never found the perp."
    
    "Gregg bursts into a laughing fit, holding his paws over his mouth in a vain attempt to cover up his snickering."
    "Angus shakes his head disapprovingly."
    
    angus "In any case, welcome to Possum Springs. You learn to make the most of this place. It's honestly not so bad."
    
    gregg "Could do a lot worse."
    
    angus "Anyway, could I get you something?"
    
    player "Just a hot black coffee. To go."
    
    angus "Good timing! I just brewed a fresh pot!"
    
    "Angus turns around and pours from the coffee pot into a cardboard cup and fixes a lid to it."
    
    ####if you have not visited the store prior, you buy cookies as well
    if bakeryVisited == False:
        "You're tempted to get a snack for yourself while you're here."
        
        player "Oh what the hell. I'll take a couple of those peppermint cookies as well. They smell too good to pass up."
        
        angus "Why thank you! I baked them just this morning."
        
        "With a pair of tongs, he reaches into the glass case and grabs a pair of cookies and drops them into a bag."
    
    "He rings up your order and you swipe your card on the machine before taking hold of the coffee cup."
    
    angus "Enjoy!"
    
    player "Thanks!"
    
    gregg "Hey wait, before you go-!"
    gregg "Wanna come and play Constellation Conquest with us?"
    
    angus "Gregg, they probably don't even know what that is. Nobody plays that game but us."
    
    gregg "Which is exactly why we need more players. We can't let the game die out!"
    
    player "What is it?"
    
    gregg "It's a tabletop game where you uhh... like you do stuff and go on adventures and... it's really fun I swear!"
    gregg "We get some friends together and play here every couple of weeks."
    
    player "Hmm. I'll think about it."
    
    angus "Our next session is scheduled for this Friday at 9:00."
    
    gregg "PM that is."
    
    angus "An important distinction."
    
    gregg "It's not my fault when instructions are unclear."
    
    angus "We understand if you can't make it on such short notice. Or if you're not interested. I will vouch for it being fun though."
    angus "We'll teach you how to play, it's not that hard."
    
    player "I'll see if I have time. For now though, I have to get back to my current quest."
    
    angus "Quest?"
    angus "Well, I'm glad I could be of assisance."
    
    gregg "See ya later!"
    
    player "Later guys."
    
    stop music fadeout 2.0

    hide gregg
    hide angus
    with dissolve
    
    #hide angus with dissolve
    
    "You exit the bakery and make your way to the hardware store, warming your hands on the coffee cup."
    
    $ metAngus = True
    
    return
    
    
