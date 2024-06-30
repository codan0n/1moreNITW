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
        
    "You find Mae sitting on the edge of a cliff in the woods, moping."
    
    player "Hey."

    show mae sad1 at left with dissolve:
        xzoom -1
        
    "Mae looks over her shoulder and sighs."

    mae "Hey."
    mae "Sorry about all that."
    
    player "Don't worry about it."
    
    mae "..."
    
    player "So uhhhh..."
    player "You come here often?"
    
    mae "Here as in the cliffside or here as in church?"
    
    player "Both?"
    
    mae "My mom works at the church."
    mae "I come with her and Dad, but just on Sundays."
    mae "It makes them happy."
    
    player "Your parents are nice."
    
    mae "Yeah. I guess I shouldn't make things so hard for them."
    
    "You brush aside some snow and sit down, your feet dangling from the edge."
    "Mae seems to forget you're there after a while."
    
    mae "You're still here?"

    player "Is that a problem? I'll leave you alone if you want."
    
    mae "Nah, it's whatever."
    mae "...Hey I have a question for you."

    "Mae turns toward you."

    mae "Are you actually religious?"
    
    player "What? Where did that come from?"
    
    mae "You came to the biggest church in town alone, dude."
    mae "Single people in their 20s don't do that without a reason."
    mae "...So? Are you?"
    
    menu:
        "Kinda? I don't know.":
            player "Kinda? I don't know."

            mae "That's pretty much how I feel."
            mae "Like, I'm pretty sure there's some supernatural stuff in the universe but maybe it's just in my head."
            mae "And even if it is real, who's to say this religion is correct or if that one is, or more likely it's one that hasn't been invented yet."

            player "That's one way to think about it."
            player "I don't believe we're going to Hell or whatever just cause we didn't happen to worship the right god."
            player "Maybe it doesn't even matter who's running the universe or what happens when we die. What we believe doesn't change reality."
            player "I mean, if we're on a ship that's heading somewhere and we can't control it, it'll arrive at the same place regardless of where we choose to believe it's going, if that makes sense."

            mae "I guess."
            mae "It's just--"
            mae "When you witness something that doesn't make sense, the only way to explain it is to believe there's a higher power controlling things behind the scenes, you know?"

            player "Yeah."

            mae "I dunno, I feel like some things are meant to happen but I can't figure out *why.*"

            player "Hm. I dunno either."
            player "Maybe we're just like ants to some cosmic god and we're not really meant to understand things outside our influence."

            mae "Oh well. Church can be fun sometimes at least. The people are kind. We help the community. And there's free food involved sometimes. I can't complain."
            


        "Not really.":
            player "Not really."

            mae "Why'd you come here then?"

            player "I dunno. Even if I don't believe in this stuff I still find it interesting."

            mae "That's fair I guess. I'm not really sure if I believe in it myself."
            mae "I mean, there's stuff that I can't explain without saying God did it or whatever but that doesn't necessarily mean there is actually a God."

            player "That doesn't mean there *isn't* actually a God though."

            mae "I know! And that's what makes it frustrating!"
            mae "Never knowing for sure."

            player "I try not to think about it. It doesn't really impact my life one way or another."

            mae "I envy people who can think like that."
            mae "Oh well. Even if it is all a shame, church can be fun sometimes at least. The people are kind. We help the community. And there's free food involved sometimes. I can't complain."

        "Yeah.":
            player "Yeah. I'm not super into it but I do believe there's a God or something like that."

            mae "That's about how Bea feels too."

            player "What about you?"

            mae "I dunno. I change stances like every month and I'm not sure which side I'm rooting for."

            player "I hope you find the answers you're looking for one day."

            mae "That's just it, the lack of answers means it can go either way! How am I supposed to know anything?"

            player "It's not about knowing, it's about believing."

            mae "Now you sound like Pastor Kate."

            player "Well it's true."
            player "Even if I *knew* there wasn't a God I could still believe in one."
            player "It's the principle that matters."

            mae "Mmh, I guess."

            "Mae looks down at the snow on the ground."

            mae "Oh well, even if I don't get it, church can be fun sometimes at least. The people are kind. We help the community. And there's free food involved sometimes. I can't complain."
    
    player "I knew it!"
    
    mae "?"
    
    player "I came here because I sensed there would be free food."
    
    mae "Snrk"
    mae "So that's why you showed up!"
    
    player "You got me. Guess I'm going to hell now."

    "Mae finally eases up and cracks a smile."
    
    mae "Heh"
    
    "The two of you chat about philosophical stuff you both barely comprehend for what feels like hours until Mae's parents eventually start calling for her."
    
    stan "Mae! Come on, it's time to go!"
    
    mae "Oh *now* we can leave."
    mae "Thanks for coming out and talking with me."
    mae "I was already bored to tears during service and my parents take F O R E V E R chatting with everyone."
    
    player "Anytime."

    "You give her a wave as she runs past you toward the church."

    mae "See ya around!"

    player "See ya!"

    hide mae with dissolve

    "You stick around for a while enjoying the comfy scenery before getting up and going about the rest of your day."
    
    return