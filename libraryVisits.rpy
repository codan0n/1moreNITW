label libraryVisit1:
    $ haveOverdueBook = False

    #"This is the most excited you've ever been to go to the library."

    scene bg library_floor1 with fade

    play music "music/deweydecimal_loop.mp3" fadein 1.0

    "Possum Springs sure has an impressive library."
    "It's a three-story building with lavish old-timey architecture, and has been very well maintained."
    "Gargoyles adorn the outside while giant pillars and arches frame the murals on the inside."
    "The interior has been modernized with new carpet and a fresh coat of paint that accentuate the comforting dim lighting."
    "You stare at the multitude of books organized neatly on shelves as you walk up to the reception desk. Sitting there is a bear currently writing something down in a notepad."
    "Unexpectedly, she looks somewhat familiar. It takes you a moment to place where you know her from."
    "She was the bear you saw at the café the other day!"
    "What did the barista call her?"
    "\"Selmers?\""
    "She looks up from her task as you approach."

    show selma neutral flip at right with dissolve:
        yalign selmaheight

    selma "Oh hey. It's you."

    player "Hey."
    player "You're... Selmers, right?"

    "Her carefree demeanor wavers slightly and there's a hint of disdain in her voice."

    selma "That's what most folks call me."
    selma "I remember seeing you at Posspresso, but I didn't get your name."

    player "[newname]."

    selma "Nice to officially meet you, [newname]."
    selma "Welcome to the Possum Springs Public Library. Is there anything I can do for you?"

    "You take one last look at the book in your hand then slide it over the counter."

    player "I found a book that belongs here and wanted to return it."

    "Selmers picks up the book and gives it a look over with an intrigued expression before scanning it into the system."
    "She rotates her chair to face the computer monitor and clicks the mouse a few times."

    selma "Whoa, this was checked out way before I even started working here."
    selma "Where'd you find this?"

    player "I found it...uh..."

    menu:
        "Left in an abandoned house":
            player "...left in an abandoned house. Was just lying there, and I figured you'd probably want it back!"
        "In my new home":
            player "...in my new home. I just moved into Possum Springs, and I found this in one of the rooms of the place I'm living in."

    #suspicious selma sprite goes here
    selma "Hmm."
    
    #back to normal sprite
    selma "That explains why it never found its way back here until now. Glad you returned it, it's the only copy we had."

    player "I don't have to pay the late fee, do I?"

    "That gets a chuckle out of her as she sets the book aside."

    selma "Nah, consider it on the house. It was probably written off as lost forever, so thanks for bringing it back."

    player "No problem."

    selma "Will that be all? Or would you like to get a library card while you're here?"

    "You raise a brow."

    player "How'd you know I didn't have one?"

    selma "I know everyone who has one."
    selma "Possum Springs is a small town and the number of people here who have a library card in 2021 is even smaller."

    player "Oh."
    player "Well since I'm here, I might as well."

    selma "Aight. Just need you to fill out this form and show me a valid ID."

    "She pulls a sheet of paper out from a filing cabinet and pushes it toward you."
    "You grab a pen from the holder and quickly fill it out."
    "Once you're done, you pull out your driver's license and pass both it and the sheet back to Selmers."

    selma "Just have to type this in real quick..."

    "She looks over your license and makes a few keystrokes before handing it back."

    selma "...and now all of this..."

    "She waves the application form in the air."

    selma "...then scan it in and print your card from the office."
    selma "You're welcome to explore for a bit while I do this. I'll have your card ready by the time you're done."

    player "Okay! Be back in a bit."

    hide selma with dissolve

    "You leave her to her work and go over to the bookshelves across the room, skimming over titles without really reading them."
    "You're not looking for anything in particular but maybe something will grab your attention."
    "...Nope, nothing here stands out in the slightest."
    "That elevator in the corner of your eye, however, is a different story."
    "This floor seems to be dedicated to nonfiction, so the fiction section must be up above."
    "That's probably where that book you just returned will get shelved. You wonder if there are any others like it your father might have checked out as well."
    "It's kinda weird. Like you're retracing the footsteps your father took at some point."
    "You feel like you're following a treasure map and slowly piecing together his interests along the way."
    "It's neat seeing what his interests might have been, but it also fills you with remorse for not getting to know him better while he was alive."
    "He'll always be some distant, vague idea of a person in your mind instead of a man you had an actual, real bond with."
    "You shake off the feelings bubbling inside you and go call down the elevator."

    stop music fadeout 1.0

    "You've kind of lost interest in the books around you but you still want to finish exploring the library at least."
    "The doors open with a mechanical grinding sound and you ride up to the second floor."

    play music "music/Stagnant_Tone-down.mp3" fadein 2.0

    "The walls here are painted salmon pink and minty green, and the lights are brighter. It no longer has that regal feeling of the first floor, but it's still warm and comforting here."
    "Desks with computers line the nearest wall and lead into the children's section, as evidenced by the mural in the corner with some sort of cartoon bear emblazoned on it."
    "The character looks vaguely familiar, but you draw a blank and shrug. Probably just something you remember from when you were a kid."
    "You turn away from the mural and head down an aisle more suited to your age, where you spend some time reading descriptions on the backs of book covers to get your mind off things."
    "Your browsing leads you down each aisle until you reach the last one and find a mouse girl sitting on the floor among a pile of books."
    "She seems to be so engrossed in the book she's holding that she doesn't notice of your presence."
    "You consider leaving so as to not disturb her, but then you spot the poorly lit sign indicating that this is the horror section."
    "This would be where where the cryptids book you returned and similar books would be found, right?"
    "You curiously enter the aisle and make your way through it, scouring the titles."
    "You keep an eye out for anything related to cryptids, trying not to make any noise."
    "As you're perusing a shelf, you feel your leg bump into something and hear a startled squeak from beside you."

    show lori anxious3 flip at left with dissolve:
        yalign loriheight

    "You look down and see the mouse girl pressed up against the bookshelf, frozen in place with the look of a deer caught in the headlights."
    "You step back and clear your throat, about to apologize, when suddenly she lets out the breath she'd been holding in."

    show lori breath flip

    lori "*Huff huff huff* Sorry, sorry!"

    show lori sad2 flip

    "She hastily shovels her books aside so you can get past."

    player "No, I'm the one who should be saying sorry. I didn't mean to scare you."

    show lori anxious3 flip

    "She glances back up at you."

    lori "Wait a minute...haven't I seen you before?"

    "Your memory finally catches up and you remember her as the girl who was listening to that weird music on the bus ride into town."
    "You didn't expect to see so many people you'd recognize here at the library, but it's a welcome surprise."

    lori "You were on the bus the other day, weren't you?"

    if loriRude == True:

        player "Oh yeah, I remember you!"
        player "I think your music is what's been giving me nightmares lately."

        show lori sad flip

        lori "I just keep getting in your way I guess..."

        "She mumbles, looking away."
        "You shrink down, realizing how rude you're being. You were like that on the bus too."
        "Maybe you should try being more amicable?"
        "And if that doesn't work, you could always just leave her alone."
        "The girl clears her throat and looks back up to you."

        show lori anxious2 flip

        lori "So are you visiting Possum Springs or something?"

        player "I just moved here, actually."
        player "My name's [newname]."

        lori "Lori."

        "You squat down and crane your neck to read the titles of the books in her little pile."

        player "Whatcha reading?"

        show lori neutral flip

        "She seems to lighten up in response to your interest in her reading material."

        lori "Oh these? Just some spooky stories to read in the dark."

        player "You a big horror fan?"

        lori "Well, I *am* going to film school to make horror movies."

        player "Really? Do you watch a lot of horror movies yourself?"

        lori "Oh yeah. I mean, I watch other movies, but horror movies are my favorite."

        player "What kinds?"

        show lori nervous2 flip

        lori "Uh, scary ones? Ones about existential dread and incomprehensible terrors mostly, but I also watch a ton of monster movies."

        player "Nice! That reminds me, I just returned a book on monsters. \"Cryptids of the Western Hemisphere\" is what it was called, I think."

        show lori neutral flip

        "Lori's eyes go wide in excitement."

        lori "I've been looking for that book for forever! I used to check it out all the time when I was a kid!"
        lori "It's kind of a cliché, but my favorite cryptid is the skinwalker. The stories about them always felt the most realistic, even if they did get samey after a while."

        player "Yeah? Mine's uh, the Jersey Devil. It's supposed to live around this area, I guess? Haha."

        lori "That's true!"
        lori "I tried hunting for it when I was a kid. I'm still not convinced it won't show up out of nowhere one day."

        "You can tell that she's really into this kind of stuff. Her ears are perked up, and her voice is eager to go on and on about it."
        "You listen to her ramble about scary things and the like, just smiling and nodding your head until she asks a question."

        lori "Hey, have you seen the movie \"The Nightmare Before Longest Night\"?"

        player "Once or twice, I think. Why?"

        lori "Some friends of mine are throwing a little party this evening at the bakery, and we're gonna watch it."
        lori "And I figured since, y'know, you're new in town and like spooky things, you might wanna come?"

        player "Sure, that'll be fun!"

        lori "Awesome!"

        player "I guess I'll let you get back to your books now. See you later!"

    if loriNeutral == True:

        player "Oh yeah, I remember you!"
        player "Do you live here? I just moved into town the other day."

        show lori neutral flip

        lori "Yup! Was here my whole life until a few months ago when I left to attend film school. I'm here on break right now."

        player "Film school, huh? What kind of films do you like?"

        "You squat down, deciding you'd rather sit on the floor and chat than stare down at her awkwardly."

        lori "Most kinds, but horror's my favorite. Like, existential dread and incomprehensible terrors especially, but regular monster movies are cool too!"

        player "That's cool. Funnily enough, I just got finished returning a book on cryptids."

        lori "It wouldn't happen to have been \"Cryptids of the Western Hemisphere\" would it?"

        player "How'd you know?"

        "Lori's eyes go wide in excitement."

        lori "I've been looking for that book for forever! I used to check it out all the time as a kid, but I haven't seen it in a while. It's one of the best encyclopedias on cryptids!"

        player "Hopefully they'll put it on the shelf soon and you can snag it before anyone else does."

        lori "That would make my day."
        lori "What's your favorite cryptid?"
        lori "It's kind of a cliché, but mine is the skinwalker. The stories about them always felt the most realistic, even if they did get samey after a while."

        player "Yeah? Mine's uh, the Jersey Devil. It's supposed to live around this area, I guess? Haha."

        lori "That's true!"
        lori "I tried hunting for it when I was a kid. I'm still not convinced it won't show up out of nowhere one day."

        "You can tell that she's really into this kind of stuff. Her ears are perked up, and her voice is eager to go on and on about it."
        "You listen to her ramble about scary things and the like, just smiling and nodding your head until she asks a question."

        lori "Hey, have you seen the movie \"The Nightmare Before Longest Night\"?"

        player "Once or twice, I think. Why?"

        lori "Some friends of mine are throwing a little party this evening at the bakery, and we're gonna watch it."
        lori "And I figured since, y'know, you're new in town and like spooky things, you might wanna come?"

        player "Sure, that sounds fun!"

        lori "Awesome!"
        lori "Before I forget, what's your name?"

        player "[newname]."

        lori "Lori."

        player "Nice to meet you Lori!"

        lori "Likewise!"

        player "I'll let you get back to your books now, but I'll see you later!"

    if loriBold == True:

        player "Hey! What a coincidence seeing you here!"

        lori "Not really. Possum Springs is like, really small. We would have run into each other sooner or later."

        player "It's definitely starting to seem that way. I don't believe I caught your name before? I'm [newname]!"

        lori "Nice to meet you again, [newname]! I'm Lori!"
        
        player "I still haven't gotten around to listening to that album yet, but it's on my to-do list. Been adjusting after moving in."

        show lori neutral flip

        lori "I get that, resettling and stuff. I've been away from home for a while, and I'm getting used to living next to train tracks again."

        player "Oof. I live a ways away from the tracks and have a bunch of trees to block out most of the noise, but the trains are still pretty loud."

        lori "Can't believe I used to play, take naps, and read books right between the tracks."

        player "That sounds...dangerous."

        lori "It was."

        player "Huh."
        
        "You squat down and take a look at some of the books strewn about, most of them from this aisle."
        
        player "So, what are you reading here?"

        lori "Just some spooky stories to read in the dark. It's technically studying material."

        player "Studying for what?"

        lori "Film school assignments! I'm actually on break right now, but I want to get ahead."

        "She holds up a book, \"Monster Design in Cinema.\""

        player "Cool! That reminds me, I just returned some kind of encyclopedia on weird creatures. \"Cryptids of the Western Hemisphere\", I think?"

        "Lori's eyes go wide in excitement."

        lori "I've been looking for that book for forever! I used to check it out all the time as a kid, but I haven't seen it in a long time. It's one of the best encyclopedias on cryptids!"

        player "I just happened to find it, really. Maybe they'll put it on the shelf soon, and you can snag it before anyone else does!"

        lori "That would make my day!"
        lori "What's your favorite cryptid?"
        lori "It's kind of a cliché, but mine is the skinwalker. The stories about them always felt the most realistic, even if they did get samey after a while."

        player "Yeah? Mine's uh, the Jersey Devil. It's supposed to live around this area, I guess? Haha."

        lori "That's true!"
        lori "I tried hunting for it when I was a kid. I'm still not convinced it won't show up out of nowhere one day."

        "You can tell that she's really into this kind of stuff. Her ears are perked up, and her voice is eager to go on and on about it."
        "You listen to her ramble about scary things and the like, just smiling and nodding your head until she asks a question."

        lori "Hey, have you seen the movie \"The Nightmare Before Longest Night\"?"

        player "Once or twice, I think. Why?"

        lori "Some friends of mine are throwing a little party this evening at the bakery, and we're gonna watch it."
        lori "And I figured since, y'know, you're new in town and like spooky things, you might wanna come?"

        player "Sure, that'll be fun!"

        lori "Awesome!"

        player "I'll let you get back to your books now, but I'll see you at the party!"



    "You give her a friendly smile and stand back up."

    lori "Bye!"

    "She waves her hand at you, then resumes reading while you scoot around her and out of the aisle."

    hide lori with dissolve

    "Where to now?"
    "There's still another floor to explore. You've just about exhausted your options on this one, so it's time to head up."
    "The elevator rattles louder this time as its doors open and close, making you question just how safe this thing really is."

    stop music fadeout 2.0

    "Apparently safe enough to get you to the third floor in one piece is the answer you get."
    "Dust floats through the air, tickling your nostrils as soon as the elevator doors open."
    "The lighting on this floor is much more subdued, and the walls are painted a dark blue. "
    "You creep forward, wondering if there's anybody up here."
    "It's dead silent save for the sounds of the heating unit. You pass by each aisle and confirm you're alone."
    "Come to think of it, this whole building is pretty empty. It's just you, Selmers, and Lori, each on different floors."
    "Selmers was right about not many people using the library these days."
    "Getting back to the matter at hand, you wonder what the purpose of this floor in particular is."
    "A quick look around reveals that it's for really old media and records."
    "Things like last century's yearbooks, outdated almanacs, newspaper clippings, and even some tomes that remind you of the ones back home."
    "As you're scouting the area, something catches your eye: a big glowing box on one of the desks."
    "It looks like one of those old tube computer monitors, but even bulkier."
    "Warmer, too. You can feel the heat coming off it from a few feet away."
    "This must be one of those microfilm projector things. A microfiche, you think it's called."
    "Someone must have forgotten to turn it off when they used it last."
    "Curious, you take a look at the film that's currently loaded onto it."
    "Seems to be a number of newspaper clippings from decades past. None of them seem all that connected, but a few have some more paranormal themed headlines."
    "None of it is terribly interesting to you, and you're about to look away when one clipping catches your eye."
    "Some story about a tale from the 1800's featuring...miners?"
    "This one actually does intrigue you. You read about an incident where a group of miners took revenge on their exploitative boss, holding him down and forcefully removing his teeth."
    "You get a little nauseous imagining such imagery, but press onward."
    "The story goes on to say that the miners created a secret society from that incident, taking the teeth and passing them down to new members over the years."
    "It finally ends with talking about the members' descendants who occasionally find teeth with strange markings in their home, proving the story's validity."
    "Wow. You know it's just a story from an old newspaper clipping, but you genuinely feel a little unsettled by what you've just read."
    "You flip the power switch off, plunging the room into near total darkness."
    "..."
    "Welp, that about concludes your tour of the library today."
    "You hastily make your way back to the elevator and return to the ground floor. Selmers should have your card ready by now."
    "As you walk up to the counter empty handed, the bear looks up with a casual grin."

    show selma neutral at right with dissolve:
        yalign selmaheight

    selma "Find what you were looking for?"

    player "Not quite, but that's more my fault than the library's."

    selma "If you're looking for a book in particular, I can help you find it if we have it."

    player "Thanks, I'll keep that in mind."

    selma "I also got your card printed. Here you go."

    "She slides the card over the counter."

    selma "It expires three years from today, or one year after your last check out. Whichever comes first."

    player "Thank you!"

    selma "Wish I got paid commission for these. But I don't. Haha."

    player "How often do you convince someone to sign up for a card?"

    selma "Almost as often as someone new comes in."
    selma "I have experience in sales."

    player "Wow."

    selma "And if you don't mind me trying to sell you on something else, the library's hosting an event this coming Tuesday at 4:00 PM where we read books aloud to younger children."
    selma "We're short on staff, so we're asking for volunteers."
    selma "It'd be nice if you could, y'know, come and read for the kids. We'll have juice and cookies too."

    menu:
        "I'll think about it.":
            $ selmaNeutral = True

            player "I'll think about it."

            selma "That's better than a flat out \"no\", I guess."

            "You can't help but feel a twinge of guilt. You look away momentarily, mulling over whether you should go or not."

            selma "Anyway, is that all I can do for you?"

            player "Oh, yeah. Thanks, have a nice day."

            selma "You too."

        "Sorry, don't think I can make it.":
            $ selmaBad = True

            player "Sorry, don't think I can make it."

            selma "I expected as much. Don't worry, we'll find someone else."
            selma "Or I'll just pull double duty like last time."

            player "That understaffed, huh?"

            selma "Yup."

            "You can't help but feel some sympathy toward her. Maybe you could come out and help for an hour or two."

            selma "Well, if you change your mind, let me know."

            player "Will do."

            selma "Anyway, do you need help with anything else?"

            player "Nope. I'm good, thanks."

            selma "K. Have a nice day."

            player "You too."

        "I'd be happy to!":
            player "I'd be happy to!"
            $ selmaGood = True

            selma "That...that was not the response I was expecting. You sure? Those kids can be real punks sometimes."

            player "It's no trouble! I can handle 'em."

            selma "If you say so. Let me know if you change your mind later."

            player "Sure."

            selma "Thanks, though. It means a lot, and it would be cool seeing you here."

            "She has a genuinely appreciative smile on her face, but there's something else behind it you can't quite grasp." 
            "Whatever it is, it makes you want to smile back."

            selma "Anyway, is there anything else I can do for you?"

            "Her voice calls you back to the conversation at hand."

            player "Oh, sorry. Nah, I'm good."

            selma "Okay. Hope you have a nice day!"

            player "Thanks, you too!"

    hide selma with dissolve
    
    return