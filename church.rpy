label church1:
    $ metCandy = True
    
    "There sure are a lot of people heading up to the top of that hill today."
    "You wonder if there's some sort of event going on."
    "There's gotta be free food up there if so many people are gathering in one spot."

    scene bg church_exterior with fade
    
    "Aww, no free food. It's just a church."
    "At least the view is nice. You can see for miles from up here!"
    "Forests near and far, fields in the distance, all the buildings in town... You think you can make out the top of your house from here too!"
    "Stained glass decorates the classically designed architecture of the church building. It's one of the few places in Possum Springs you've seen with fully intact windows and no graffiti."
    "That the statue of the fire-breathing pope guy by the welcome sign must be doing a good job of guarding the premises."
    "A large crowd of people begins pouring out of the church."
    "Some walk right past you, giving you friendly smiles and hellos, while others hang back and chat among themselves here in the courtyard."
    "To your surprise, you spot Mae amid the last to pass through the doors, accompanied by what looks like her parents."
    "Mae impatiently drags them toward the parking lot until she notices you, whereupon she jumps back in shock."
    
    show mae freakout at right with dissolve
    
    mae "Oh. It's you."

    "You get the feeling she wants to leave as soon as possible so you keep your response short."

    player "Hey Mae. I was just passing through. Guess I'll see you lat-"
    
    show stan neutral at left:
        xzoom -1
    show candy neutral at left:
        xzoom -1
    with dissolve
    
    stan "Well hello there! I believe we've met before at the Ham Panther. Good seeing you again!"
    
    if gender == "masculine":
        candy "You all know each other already? I feel so left out! Mae, is this your boyfriend?"
    elif gender == "feminine":
        candy "You all know each other already? I feel so left out! Mae, is this your girlfriend?"
    elif gender == "neutral":
        candy "You all know each other already? I feel so left out! Mae, is this your... er... boyfriend? Girlfriend? I'm sorry, I can't quite tell."
    
    mae "What? No!"
    
    "Dammit, Mae's parents aren't going to let you get away that easily."
    "You give them a cordial nod and greeting."
    
    player "Hi there. I'm [newname]. I just moved in last week."

    candy "Nice to meet you [newname]! I'm Mae's mother, Candy."

    stan "I don't have my name tag on me at the moment but rest assured I'm still Stan."
    stan "Working at the Panther is just my part time job. Raising Mae is my full time one hahaha!"

    "Great, dad jokes. You grin and bear it."
    "Mae is more up front in her distaste for them and tries to pull her parents away."

    show mae grump

    mae "Ugh you're embarrassing me, Dad! Let's go already!"

    candy "Hold on kitten, I promised I'd give Dorothy the recipe for my peppermint cake."
    
    mae "It's literally just vanilla cake mix and crushed peppermint! That's the whole recipe!"
    
    stan "And I wanted to see what Jacob's been up to lately."

    mae "You already see him every day at work!!"
    
    candy "Why don't you show your new friend around, Mae? We won't be long."

    mae "Ugggghhhhhh!!! Why aren't you listening to me!"

    show mae grump at offscreenright with move
    
    "Mae storms off toward the woods."
    
    candy "Oh dear, she's been so rambunctious lately. What a shame, I thought she'd finally grown out of it..."

    stan "She gets it from your side of the family."

    candy "I'm so sorry, [name]. Could you go check on her? She's a lot to handle but she's sweet once you get to know her, I promise."

    player "It's ok. I'll go make sure she's alright. It was nice meeting you."

    candy "Oh thank you! We'll catch up later!"

    player "No problem. See you around!"

    stan "See ya!"

    hide stan
    hide candy
    with dissolve
        
    
        
    return