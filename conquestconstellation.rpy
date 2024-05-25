label cnc1:
    #notes
    #arrive at bakery, angus/gregg welcomes you and invites you to back room. selma is there shuffling cards. she briefly explains the rules of the game and you begin. germ pops in shortly afterwards and joins the game
    
    #can pick up and play every week, selma will summarize the previous session
    
    #major constellation is your class and your ancestor. For the player, this is determined by their species. Determines your abilities and skills.
    #minor constellation is basically your zodiac and gives eithre small buffs, passive bonuses, or a particular skill check
    
    #story revolves around solving a series of murders, reflecting the possum springs cult incident
    #plays similar to disco elysium
    #battles are 4 guys in a row style
    
    #setting is a fantasy magical worth entering its industrial age. dieselpunk/steampunk
    
    #rules of the game: similar to DnD, it's an adventure rpg. Selma handles the stats in the background and guides the story with battles, puzzles, intrigue and mystery. 
    
    #setting: For this session, we live in a world where magic is dying and technological advancements are changing the way people live. Few powerful wizards remain and those that are still alive have had their abilities diminished. It is believed that some sort of far away astronomical event has weakened the planet's connection to magic. The arcane arts are becoming lost now that a new era powered by steam and oil has arrived. The old ways have been forgotten but technology allows for new possibilities even magic couldn't provide. It's a time of opportunity and prosperity... for some. For others, their once simple and peaceful lives have been upturned by greed and war over resources
    
    #story: a string of murders has come to national attention when the old and wise king has been murdered. A group of investigators take to solving the mystery behind the motives and identity of the murderer
    # Bea is appointed as a field investigator to gather clues. Mae is immediately placed under suspicion for her past crimes but Bea clears her name. As thanks, Mae journeys with Bea to solve the mystery.
    # Gregg witnesses a kidnapping that he believes to be related to the murders and is seen by the cultists. Fearing for his life, he asks the adventurer Angus to take him somewhere far away where he'll never be recognized.
    # On their journey, Gregg hires the player for additional protection. As they reach the mountains, they encounter Germ. He has left society to live in the mountains because he was tired of people asking him to communicate with their dead loved ones. He believes that his power causes more death. He also finds it annoying when people ask him to do things.
    #next session, the player scouts ahead and encounters Bea and Mae investigating cult activity in the mountains
    
    #spells and sorcery
    
    #major constellations (dusk stars)
    #1. adina astra (gator, bea) - an astronomer who looked to the stars to make peace with her loss. theme of connections. Investigator class, smart.
    #2. big snake (not playable) - the villain? emerged from the earth and terrorized villages. the villages banded together as they were being choked by it.
    #3. castys (canine, gregg) - built a tower to heaven and was punished by the gods to sink to the depths of the sea, but refused to die. sneak class.
    #4. dohr the murderer (cat, mae) - minded his own business until insulted by the king. he murdered the king's family and then the king himself. Assassin/rage class.
    #5. Ferdinand The Mountaineer (bear, angus) - left home to climb the mountains, returned and felt the weight of the world. Adventure/survival class.
    #6. Tehrn The Medium (bird, germ) - spoke with the dead. when he died his spirit communicated through his body. Support class, with magic.
    #7. Sterling the Seer (gator, player option) - symbol of being left behind as the world changes. falsely believed the earth orbited the sun and was banished when the trush was revealed. Wizard class.
    #8. Simone the Fighter (deer, player option) - a freedom fighter, saboteur. became legendary through her escapades and evasion to capture. was killed in a charge against the pallace. Fighter class.
    #9. The Firemaker (bird, player option) - a wanderer through a snowy land, builds fires for light and warmth. Leader class, guidance.
    
    
    #minor constellations (constellations)
    #either passives/buffs/extra skills or behaves like homestuck aspects
    #1. Tollmetron (Germ) - rings at the end of the world - death follows you wherever you go
    #2. The Mice Writers (Gregg) - inventors of written language - generally gives a buff to linguistic skills - allows gregg to forge documents
    #3. The Broken Snake - first thing that talked - allows communication with animals
    #4. Rubello - pope who could exhale fire - proximity to fire enhances your abilities
    #5. Quinona - executed but could still talk - grants talkative perk, which makes people want to talk to you more
    #6. Mundy, The World Fish (mae) - a whale with the world on its back - figuratively carries the team, both to safety and danger. Your struggles ripple through the entire team and your enemies - In Mae's case, she determines the tide of battle and how everyone else goes along with her.
    #7. Marmanodes, The Little King - a tiny king - royal blood, makes others more likely to follow you, but makes some riducule you for being small.
    #8. Lucio The Fox (Bea) - speared to the earth to keep him down - prone to interfering in every matter, may need to be held back by his team
    #9. Invenerus - inventor of music - bard perk
    #10. Ibon - the first singer. drank the ocean to hear their voices and teach them to sing. connections to the black goat? - hypnosis perk
    #11. Harmonium - head of singing angels - holiness perk
    #12. A fish (angus) - just a fish? - enhances your abilities when you're in your element, detracts from them in other environments
    #13. Corvin the thief - a thief who believed in stealing everything - see everything through the lens of theivery. can steal the unstealable.
    

    #selma shows up as a merchant/nice weakened wizard
    #lori is the final boss
    
    scene bg bakery_interior with fade
    
    "You walk inside the bakery but no one is at the counter or tables."
    "The lights are on and the door was unlocked but it feels like you're breaking in."
    "You clear your throat."
    
    player "Ahem?"
    
    "A moment later Angus comes out from the back room."
    
    show angus neutral with dissolve
    
    angus "Hey there! Sorry, I went to the backroom for literally one minute and missed your arrival."
    
    player "It's fine."
    player "Is it just us or..?"
    
    "You hear a muffled voice call out from the back."
    
    gregg "Is that them? Hurry up and come back here so we can start the game!"
    
    angus "Sounds like Gregg is eager to get into it. We haven't had a chance to play in such a long time."
    angus "Right this way."
    
    hide angus with dissolve
    
    "Angus guides you to the back room, letting you go in front of him."
    "You grip your pocket knife in your jacket pocket, half expecting to get jumped."
    if metSelma == False:
        "To your surprise, you're welcomed with warm smiles by Gregg and the bear from the cafe sitting inside a cozy gaming room."
    else:
        "To your surprise, you're welcomed with warm smiles by Gregg and Selmers sitting inside a cozy gaming room."
    $ metSelma = True
    #say library if you've been to the library
    
    
    show selma neutral at right:
        xpos 2100
    show gregg neutral at right:
        xpos 1600
    with dissolve
    
    selma "Sup."
    
    gregg "Glad ya could make it!"
    
    "Gregg pulls out a chair for you."
    
    player "Thanks. I've always wanted to try one of these tabletop games but never really had a chance to."
    
    "Angus enters the room as you sit down and places a tray of freshly baked cookies on the table. Gregg immediately snatches one."
    
    show angus neutral at left with dissolve:
        xzoom -1
    
    angus "Help yourselves."
    angus "Where's Germ?"
    
    gregg "He texted saying he's running late and to start without him."
    
    angus "Hmm."
    angus "In that case, are we all settled in and ready to play?"
    
    player "I still have no idea how to play."
    
    angus "Oh right, this is your first time."
    angus "Selma, would you mind explaining? You know this game better than any of us."
    
    selma "Of course."
    selma "It's similar to most tabletop role playing games. I, the game master, come up with an overarching story..."
    selma "...while the heroes - that's you guys - venture on a quest to complete a certain objective or defeat a villain."
    selma "The gimmick with this one is instead of having classes or races as playable characters, you choose an ancestor based on a dusk star, which determines your role and skills."
    selma "There's also stats and stuff but don't worry, I'll handle most of the number crunching so you just have to worry about staying in character."
    
    angus "That about sums it up. Once you get started playing it'll become more clear what you're supposed to do."
    
    player "I think I get it. It's like that thing in school where the teacher gives a prompt and has the students come up with a story together."
    
    gregg "Pretty much. Except way cooler because you can roll for seduction."
    
    angus "Gregg is banned from rolling for seduction."
    
    gregg "Eh. It was overpowered."
    
    "Selma wracks her claws against the table."
    
    selma "Shall we begin?"
    
    gregg "Sure, I'm ready."
    
    angus "Cookies, check. Dice, check. Oh hold on..."
    
    "Angus pulls out his phone and types something. A moment later, dungeon synth starts playing from the speaker."
    #use vylet pony's girls who are wizards intro
    #musicians of ponyville
    #potion seller
    
    angus "Aaaand ready."
    
    selma "Alright, here's the setting I cooked up."
    selma "For this instance, we live in a world where magic is dying and technological advancements are changing the way people live."
    selma "Few powerful wizards remain and those that are still alive have had their abilities diminished. It is believed that some sort of far away astronomical event has weakened the planet's connection to magic."
    selma "The arcane arts are becoming lost now that a new era powered by steam and oil has arrived. The old ways have been forgotten but technology allows for new possibilities even magic couldn't provide."
    selma "It's a time of opportunity and prosperity... for some."
    selma "For others, their once simple and peaceful lives have been upturned by greed and war over resources."
    selma "Cities are raided and pillaged, borders redrawn, and more destructive weapons are built."
    selma "Amidst the turmoil, a string of murders has plagued the region. There are murmurs that a group of dark sorcerers are responsible."
    selma "Their motives are unclear, but rumor has it that they're recruiting members and amassing an army in secret."
    selma "Families are destroyed, and friendships are ended with a knife in the back. Neighbors turn on each other out of fear and paranoia."
    selma "How deep does this conspiracy go? What are the wizards' goals? What can be done to restore peace?"
    selma "Our adventuring party will attempt to answer these questions and either defeat the spellcasters..."
    selma "...Or join them."
    
    gregg "Neat."
    
    angus "I like it. A mix of magical fantasy and steampunk."
    
    selma "Thanks. So Gregg is the descendant of Castys this time and Angus you're based on Ferdinand?"
    
    angus "Yup."
    
    player "Wait, was I supposed to come with a character already?"
    
    "Gregg snaps his fingers."
    
    gregg "*That's* what I was forgetting!"
    gregg "Not a problem, we can just make a character for you right quick."
    
    if animaltype == "mammal":
        gregg "How about... Simone the fighter?"
        
        player "I uhh, actually don't know the dusk stars all too well. But a fighter sounds cool."
        
        selma "Ahh, the fighter role is one who leads the party to victory through valor and bravery."
        selma "Thematically, your story will revolve around seeking freedom, resistance to your oppressors, and the thankless struggle of fighting for your beliefs."
        selma "Do you think you have what it takes to be our noble warrior?"
        
        menu:
            "Play as the fighter?"
            "Sure":
                $ cnc_class = "fighter"
                player "Sure, that sounds like my kinda character."
            "What are my other options?":
                player "What other characters are there?"
                
                gregg "Let's see... We could use a firemaker."
                
                angus "Personally I think a seer would work better."
                
                player "Tell me more about those."
                
                selma "Basically the firemaker's lore is that he builds fires for warmth and light."
                selma "Thematically, you'll be offering hospitality and guidance to those around you, but be wary of the path you carve."
                #otherwise your enemies will know your position
                
                player "And the seer?"
                
                selma "The seer basically acts as the party's advisor and provides insight in regards to things others cannot see."
                selma "But you must be careful to interpret your visions correctly. Often things are not as they appear."
                
                player "Is there anyone else I can be?"
                
                angus "Technically yes but the rest are reserved by some friends who might join in later."
                
                menu:
                    "Who will you be?"
                    "The fighter":
                        $ cnc_class = "fighter"
                        player "I'll be the fighter."
                    "The firemaker":
                        $ cnc_class = "firemaker"
                        player "I'll be the firemaker."
                    "The seer":
                        $ cnc_class = "seer"
                        player "I'll be the seer."
                            
    elif animaltype == "bird":
        gregg "How about... The Firemaker?"
        
        player "I uhh, actually don't know the dusk stars all too well. But I like the sound of an pyromaniac."
        
        selma "He's more like a camper than an arsonist. Basically his lore is that he's a wanderer who built fires for warmth and light. He's an outcast, alone and lost in the world but feels blessed in the comfort of fire."
        selma "Thematically, you'll be offering hospitality and guidance to those around you, but be wary of the path you carve."
        #otherwise your enemies will know your position
        selma "Do you think you have what it takes to be our guiding light?"
        
        menu:
            "Play as the firemaker?"
            "Sure":
                $ cnc_class = "firemaker"
                player "Sure, that sounds like my kinda character."
            "What are my other options?":
                player "What other characters are there?"
                
                gregg "Let's see... We could use a fighter."
                
                angus "Personally I think a seer would work better."
                
                player "Tell me more about those."
                
                selma "The fighter role is one who leads the party to victory through valor and bravery."
                selma "Thematically, your story will revolve around seeking freedom, resistance to your oppressors, and the thankless struggle of fighting for your beliefs."
                
                player "And the seer?"
                
                selma "The seer basically acts as the party's advisor and provides insight in regards to things others cannot see."
                selma "But you must be careful to interpret your visions correctly. Often things are not as they appear."
                
                player "Is there anyone else I can be?"
                
                angus "Technically yes but the rest are reserved by some friends who might join in later."
                
                menu:
                    "Who will you be?"
                    "The fighter":
                        $ cnc_class = "fighter"
                        player "I'll be the fighter."
                    "The firemaker":
                        $ cnc_class = "firemaker"
                        player "I'll be the firemaker."
                    "The seer":
                        $ cnc_class = "seer"
                        player "I'll be the seer."
                        
                
                    
    elif animaltype == "reptile":
        gregg "How about... Sterling the seer?"
        
        player "I uhh, actually don't know the dusk stars all too well. What the heck is a seer?"
        
        selma "The seer basically acts as the party's advisor and provides insight in regards to things others cannot see."
        selma "But you must be careful to interpret your visions correctly. Often things are not as they appear."
        selma "Do you think you have what it takes to be our divine prophet?"
        
        menu:
            "Play as the seer?"
            "Sure":
                $ cnc_class = "seer"
                player "Sure, that sounds like my kinda character."
            "What are my other options?":
                player "What other characters are there?"
                
                gregg "Let's see... We could use a warrior."
                
                angus "Personally I think a firemaker would work better."
                
                player "Tell me more about those."
                
                selma "The fighter role is one who leads the party to victory through valor and bravery."
                selma "Thematically, your story will revolve around seeking freedom, resistance to your oppressors, and the thankless struggle of fighting for your beliefs."
                
                player "And the firemaker?"
                
                selma "Basically his lore is that he's a wanderer who built fires for warmth and light. He's an outcast, alone and lost in the world but feels blessed in the comfort of fire."
                selma "Thematically, you'll be offering hospitality and guidance to those around you, but be wary of the path you carve."
                #otherwise your enemies will know your position
                
                player "Is there anyone else I can be?"
                
                angus "Technically yes but the rest are reserved by some friends who might join in later."
                
                menu:
                    "Who will you be?"
                    "The fighter":
                        $ cnc_class = "fighter"
                        player "I'll be the fighter."
                    "The firemaker":
                        $ cnc_class = "firemaker"
                        player "I'll be the firemaker."
                    "The seer":
                        $ cnc_class = "seer"
                        player "I'll be the seer."
                            
    selma "Excellent! I'll have to make some minor adjustments to the story I had planned but that's not a problem."
    
    player "What are Gregg and Angus's roles again?"
    
    gregg "I'm based on Castys. She tried to sneak into heaven but got sent to the bottom of the sea as punishment."
    
    player "Wow did she die?"
    
    gregg "No, I think she was bound for heaven anyway so she got cursed with immortality."
    
    player "RIP."
    player "Well, I guess not-RIP."
    player "It's more like, stay alive in peace."
    
    angus "Live reaaaalllly long and prosper."
    angus "At the bottom of the ocean. With the fishes."
    
    player "And what about you?"
    
    angus "My ancestor was Ferdinand, who basically got so bored one day he decided to climb a mountain."
    
    player "As one does."
    
    angus "Yeah but once he came down from the mountain he felt like everything sucked forever."
    angus "Except mountains."
    
    player "So you're just a guy who loves mountains?"
    
    angus "In the context of the game, I'm the exploration and survival expert. A professional adventurer of sorts."
    
    selma "All characters have an important role to play for the success of your party's mission."
    selma "Gregg is a sneaky smooth-talker who can infiltrate any fortress. Angus's travel knowledge will keep your expedition running smoothly."
    selma "And you, [name], will be the glue that holds it all together and directs the party to their goal."
#    selma "We just need one last thing for character creation: what is your zodiac sign?"
#    selma "You can pick whatever you want but for this instance we decided to go with our real life zodiac constellations."
#    selma "This determines some minor skills, buffs, and themes."
#    
#$ zodiac = ""
#    
#label zodiacChoice:
#    menu:
#        "What is your zodiac?"
#        "Tollmetron":
#            $ zodiac = "tollmetron"
#            player "Tollmetron."
#            
#            selma "Oh dear, two tollmetron players in this instance..."
#            
#            player "Is that bad?"
#            
#            selma "Not necessarily... Unless you consider death following wherever you go to be bad."
#            
#            gregg "We're supposed to be solving murders though, right? So that might lead us right to the killers!"
#            
#            selma "Perhaps~"
#            #selma "But in this story you're chasing the death cult, so this might provide clues!"
#        "Rubello":
#            $ zodiac = "rubello"
#            
#            player "Rubello."
#            
#            selma "The firebreather... they got real creative with this one and determined that this would \'generally enhance your abilities in relation to your proximity to fire\' as per the guidebook."
#        "The Mice Writers":
#            $ zodiac = "micewriters"
#            
#            player "The Mice Writers"
#            
#            gregg "Hey me too!"
#            
#            player "What do I win?"
#            
#            selma "You'll have a heightened proficiency in linguistics and literature."
#            
#            gregg "Unfortunately this does not affect your grades in English class."
#        "The Broken Snake":
#            $ zodiac = "brokensnake"
#            player "The Broken Snake."
#            
#            selma "You can talk to animals. The Broken Snake was the first creature that talked. And was an animal. That's literally the rationale the guidebook gives for this ability."
#        "Quinona":
#            $ zodiac = "quinona"
#            player "Quinona."
#            
#            selma "You gain the talkative perk. Use it wisely."
#            
#            player "What does that mean?"
#            
#            angus "Gregg played with this one time. He abused it to ask endless questions and drive NPCs mad."
#            
#            selma "Along with the GM."
#        "Something else":
#            menu:
#                "What is your zodiac?"
#                "Mundy":
#                    $ zodiac = "mundy"
#                    player "Mundy."
#                    
#                    selma "While Mundy literally carries the world on his back, you carry it figuratively. Or more likely metanarratively."
#                    selma "Gameplay wise, status effects afflicted on you will affect everyone, friend or foe."
#                "Marmanodes":
#                    $ zodiac = "marmanodes"
#                    player "Marmanodes."
#                    
#                    selma "Royal blood makes you more charismatic and you're more likely to convince others to aide you."
#                "Lucio":
#                    $ zodiac = "lucio"
#                    player "Lucio."
#                    
#                    selma "Your ability is that you can't be kept down in combat."
#                    selma "Unless you're literally kept down like if you're pinned."
#                    selma "But otherwise if you're knocked out, you'll be back on your feet in no time."
#                "Invenerus":
#                    $ zodiac = "invenerus"
#                    player "Invenerus."
#                    
#                    selma "No way, me too!"
#                    selma "As the inventor of music, Invenerus bestows upon you bard powers. If you can come up with a rhyme related to your action, it'll add +1 to your roll."
#                "Ibon":
#                    $ zodiac = "ibon"
#                    player "Ibon."
#                    
#                    selma "Okay this one is a bit of a stretch but the official guidebook claims that Ibon had the power of hypnosis because he could teach fish to sing."
#                    selma "So now you get hypnosis."
#                "Something else":
#                    menu:
#                        "What is your zodiac?"
#                        "Harmonium":
#                            $ zodiac = "harmonium"
#                            player "Harmonium."
#                            
#                            selma "The head of singing angels grants you... the ability to make it stop raining."
#                            
#                            player "What."
#                            player "How is that useful?"
#                            
#                            selma "I dunno, I think the developers were running out of ideas when they got to this one."
#                        "The Fish":
#                            $ zodiac = "fish"
#                            player "The Fish."
#                            
#                            angus "Hey, same!"
#                            angus "Fish bros gotta stick together."
#                            
#                            selma "This one just means that your abilities are enhanced when you're in your home environment but they're worse in any other environment."
#                            
#                            angus "Like a fish in water versus on land."
#                            
#                            selma "Exactly!"
#                        "Corvin":
#                            $ zodiac = "corvin"
#                            player "Corvin."
#                            
#                            selma "Corvin gives you the ability to steal things that are otherwise unstealable."
#                            
#                            player "*Steals your heart*"
#                            
#                            gregg "Hey, give that back!"
#                        "Something else":
#                            jump zodiacChoice
                    
    angus "Alright, it sounds like we've got characters and setting sorted out. Are you all ready to start?"
    
    gregg "Dude I've been ready."
    
    player "Ready as spaghetti."
    
    selma "Alright then, our story begins with a roguish fox, getting himself into trouble as usual, but this time he may be in over his head."
    selma "It was an unspoken rule in this town to keep your windows barred at night and whatever you do, don't look outside after dark. Especially don't *be* outside."
    selma "Our first hero isn't very good at following directions however, and stumbles upon the a ritual being performed by the local wizard gang in the dead of night."
    
    gregg "\'Shit heck darn eff arse\' and several other obscenities spew from my mouth as I run for my life, through pitch black alleys and empty streets."
    gregg "Using my superior flexibility and athleticism, I vault over barrels, climb up fences, and jump across rooftops. Anything to escape my pursuers."
    
    selma "Chancing a look behind you, the men in dark hooded robes are right on your tail."
    selma "They seem to phase through walls and ceilings, inching ever closer no matter where you run."
    
    gregg "These guys don't give up, do they?"
    
    selma "They seemingly don't."
    
    gregg "Ohh am I supposed to fight them?"
    
    angus "One low level rogue versus several experienced spellcasters?"
    
    gregg "Come on, Selmers wouldn't let me die this early."
    gregg "Enough of this nonsense! Come and get me, nerds!"
    gregg "I brandish my iconic dagger, waving it at any wizard brave enough to step forth."
    
    selma "None of them step into range. They're busy charging up their spells from a safe distance."
    selma "However..."
    selma "A lone figure stands undetected, watching the scene unfold."
    selma "This is where you come in, [name]. How do you wish to proceed?"
    
    menu:
        "Direct confrontation":
            player "I'll help Gregg out in this fight. I uhh swoop in and back him up?"
            
            angus "You should say something heroic so he doesn't think you're one of them."
            
            player "Okay how about..."
            player "You look like you could use a little help?"
            
            gregg "That's kinda cringe."
            
            player "Don't complain! I'm trying to save you!"
            
            #throws a die in-universe
            "You pick up the 20 sided die and roll in across the table."
            
            player "I cast punch on the nearest wizard!"
            
            $ roll = renpy.random.randint(1, 19)
            
            "The die rolls off the table. Selmers picks it up for you."
            
            selma "You rolled a [roll]."
            
            if roll < 4:
                if cnc_class == "fighter":
                    selma "I'll just uh, bump that up a few points thanks to your warrior class. Your combat skills should offset your luck some."
                    
                    $ roll = roll + 10
            
            elif roll < 10:
                if cnc_class == "fighter":
                    selma "I'll bump that up a bit because you're a warrior. Your combat skills should offset your luck some."
                    
                    $ roll = roll + 7
            
            elif roll < 20:
                if cnc_class == "fighter":
                    selma "I'll bump that up a bit because you're a warrior. Your combat skills should offset your luck some."
                    
                    $ roll = roll + 10
            
            if roll < 4:
                selma "In the darkness, you mistake Gregg for a wizard and punch him in the snout."
                
                gregg "Ow! Who's side are you on?!"
                
                player "Sorry."
                
                selma "If it's any consolation, now the wizards are confused who's side you're on as well."
                selma "They ignore [player] for now and focus their spells on Gregg."
                selma "Bolts of lightning go over his head, narrowly missing."
                
                
            
            elif roll < 10:
                selma "You direct your attack at a wizard who got too close but he deflects it with a ward spell."
            
            elif roll < 20:
                selma "Before the poor wizard has a chance to react, you take a crack at his jaw, knocking him to the floor."
            
            elif roll <= 20:
                selma "You swiftly kick a wizard in the face, knocking him backward into a couple of his friends."
                
            
            
            
            #selma "I would caution against getting any closer out in the open. They simply hold the advantage with their longer range."
            selma "You're both forced into cover behind some wooden crates as a volley of elemental magic is hurled your way."
            
            gregg "Thanks for the save! But uh, I think we're kinda screwed now."
            
            player "Maybe you could sneak around them while I get their attention?"
            
            gregg "Excellent plan, kind stranger!"
            gregg "I'll stick to the shadows and go in for a backstab."
            
            player "And I'll just uh... sit here getting lightning bolts thrown at me."
            
            "Gregg picks up the die and rolls it."
            
            gregg "14. Come on, that's gotta be good enough for a successful sneak!"
            
            selma "It is."
            selma "Gregg remains unseen as he flanks around the fiendish group. They don't suspect a thing until one of them screams out, feeling the business end of your blade cut into his leg."
            selma "His buddies turn around and spot Gregg. They angrily chant an incantation and direct their aim at the rogue..."
            selma "...but before they can finish, the night sky brightens and beams of sunlight appear from over the horizon."
            selma "Your enemies recoil and hiss in pain, melting into shadows that disperse."
            
            gregg "I catch my breath then turn to the stranger who helped me."
            gregg "\'Are you alright? You can come out now, they're all gone.\'"
            
            player "I pop my head over the wooden crate I was taking cover behind."
            player "Yeah, they didn't even scratch me. Name's [name] by the way."
            
            gregg "A pleasure to fight by your side, [name]! You might already know me by the wanted dead or alive signs around town Gregg the Great!"
            
            selma "They don't say that, they just say Gregg the Nuissance."
            
            if cnc_class == "seer":
                player "\'So it was the sunlight that drove them away? We should be safe until sundown then.\'"
                
                gregg "Ohh is that what happened? I thought they just got startled when I snuck up on them and decided to flee."
                
                player "I'm not gonna stick around and find out. They're probably regrouping and will hunt us down come sundown."
                
                gregg "Hmm... In that case, I think I know someone who can help us!"
            else:
                player "We should get out of here before reinforcements arrive."
                
                gregg "Good thinking! I'm gonna stop by a friend's place before skipping town entirely. He'll be able to help chart a course for me."
                gregg "Since you bailed me out in that fight, you're welcome to come with. I could use a bodyguard hahaha!"
                
                player "Sounds like a plan. Who's this friend of yours?"
                
            
        "Indirect assault":
            player "Hiden in the shadows, I pick up a nearby rock and throw it at a wizard."
            
            selma "Ooh, taking a more subtle approach, I like it!"
            
            player "No need to jump into the fray and put myself in danger just yet. I wanted to help but I'm not that committed."
            
            gregg "Any help is appreciated!"
            
            selma "Roll for the efficacy of your stone throw."
            
            $ roll = renpy.random.randint(1, 19)
            
            "The die rolls off the table. Selmers picks it up for you."
            
            selma "You rolled a [roll]."
            
            if roll < 4:
                if cnc_class == "seer":
                    selma "I'll just uh, bump that up a few points thanks to your seer class. You should have more intuition as to where the rock will land."
                    
                    $ roll = roll + 10
            
            elif roll < 10:
                if cnc_class == "seer":
                    selma "I'll bump that up a bit because you're a seer. You should have more intuition as to where the rock will land."
                    
                    $ roll = roll + 7
            
            elif roll < 20:
                if cnc_class == "seer":
                    selma "I'll bump that up a bit because you're a seer. You should have more intuition as to where the rock will land."
                    
                    $ roll = roll + 10
            
            if roll < 4:
                selma "Your rock sails through the air and hits Gregg on the snout."
                
                gregg "Ow! Who's casting rock over there?"
                
                player "Sorry! That was supposed to be for the guy in the spooky cloak."
                
                gregg "That's alright, try again!"
                
                selma "Your element of surprise has been spoiled by your poor aim."
                selma "But on the bright side, the wizard group is now split into two, facing opposite directions."
                
                
            elif roll < 10:
                selma "Your rock sails through the air and plinks a wizard on the head. Enough to be an annoyance but not really to cause any damage."
                selma "Confused, the wizards look around for the unknown assailant."
                
                player "Yay I did something useful!"
                
                selma "Your position is concealed for now, but don't expect your foes to fall for the same trick again."
            
            elif roll < 20:
                selma "Your rock sails through the air and bounces off a wizard's head, knocking him to the ground."
                selma "Confused, the wizards look around for the unknown assailant."
                
                player "Yay I did something useful!"
                
                selma "Your position is concealed for now, but don't expect your foes to fall for the same trick again."
            
            elif roll >= 20:
                selma "Your rock sails through the air and strikes a wizard just before he could fire off his spell at Gregg. He spins as he falls to the ground and blasts one of his allies with a beam of light."
                selma "Confused, the wizards look around for the unknown assailant."
                
                player "Yay I did something useful!"
                
                selma "Your position is concealed for now, but don't expect your foes to fall for the same trick again."
                
            angus "At least now it's not so one-sided."
                
            gregg "Now it's a game of rock-dagger-fireball."
            gregg "Speaking of which, I'm rolling for stab damage."
            
            selma "I'm afraid you'll find it rather hard to stab someone from 30 feet away."
            
            gregg "Whaaaat?! Come on, let me stab someone already!"
            
            selma "You could charge in but you'll probably get shot with a lightning bolt before you get close enough."
            
            gregg "That's what I invest points in luck for!"
            gregg "CHAAAAARGE!!!"
            
            selma "You're a very lucky fox indeed. As you charge forward, blade pointed at the nearest foe, a gleam of light shines from the horizon."
            selma "Your enemies cover their faces and hiss. Their bodies seem to melt into the ground and their shadows scatter, leaving the battlefield empty."
            
            player "I guess it's safe for me to come out of hiding now?"
            
            gregg "Lemme sheath my dagger so it doesn't look like I'm gonna stab you for helping me. I promise I'm not that crazy."
            gregg "You alright? I didn't see them throw any spells your way."
            
            player "Yeah, I'm good. What about you? Those guys looked ready to vaporize you."
            
            gregg "They might have if you didn't show up! Thanks for the help, kind stranger!"
            
            player "Name's [name]. I can't really stand those creeps ruining my nightwalks so I thought I'd mess with them a little."
            
            gregg "Well I'm glad ya did! You from around here? I don't think we've met. Around these parts I'm known as Gregg the Magnificent!"
                
            selma "Nobody calls him that, they call him Gregg the Nuissance."
            
            gregg "Aww, why you gotta ruin my introduction?"
            
            if cnc_class == "seer":
                player "\'So it was the sunlight that drove them away? We should be safe until sundown then.\'"
                
                gregg "Ohh is that what happened? I thought they just got scared and left."
                
                player "I'm not gonna stick around and find out. They're probably regrouping and will hunt us down come sundown."
                
                gregg "Hmm... In that case, I think I know someone who can help us!"
            else:
                player "We should get out of here before reinforcements arrive."
                
                gregg "Good thinking! I'm gonna stop by a friend's place before skipping town entirely. He'll be able to help chart a course for me."
                gregg "Since you bailed me out in that fight, you're welcome to come with. I could use a bodyguard hahaha!"
                
                player "Sounds like a plan. Who's this friend of yours?"
            
            
            

            
        "Distraction":
            player "I cause a distraction"
            #firemaker starts a fire
            #non-firemaker makes noise and knocks stuff over
            #firemaker bonus
            gregg "My instincts are telling me this would be a good time to flee!"
    
    
    
    
    #selma "Eventually you're cornered, but just before they can fire off their destructive spells, a gleam of sunlight appears."
    #selma "Like phantoms, the wizards disappear into the shadows and make their retreat."
    #selma "The rogue waits only to catch his breath, then hurriedly makes his way to the only person he knows can help him."
    
    gregg "Angus!"
    
    angus "What?"
    
    gregg "No, I'm saying you're who can help me."
    
    angus "Oh right. Probably."
    
    selma "Gregg arrives at an apartment. The door is locked."
    
    #gregg "I frantically knock on the door"
    
    gregg "I kick down the door - wait, can I kick down the door?"
    
    selma "Roll for strength."
    
    $ roll = renpy.random.randint(1, 20)
    
    "Gregg picks up the 20 sided die and rolls it down the table."
    
    selma "[roll]."
    
    if roll < 5:
        gregg "Aw man."
    
        selma "You raise your foot and bring it down on the heavy wooden door, but you boot slips and causes your heel to turn farther than it should."
        selma "Your ankle is now sprained."
        
        gregg "Ow."
    
    elif roll < 13:
        selma "Your boot collides with the door repeatedly, flexing the boards but comes just shy of kicking it down."
        
    elif roll < 20:
        selma "Your boot comes down hard on the door, flinging it along its hinges inward."
        
    elif roll == 20:
        selma "Your boot hits just the right spot with enough power to break it free from its hinges. The door goes flying inside the building."
        
    selma "The commotion catches the attention of the lone resident, a gruff explorer in the middle of preparing for his next expedition."
    
    angus "I'm \'gruff\'?"

    selma "Gruff enough."
    
    
    gregg "Whew"
    
    
    #gregg on the run from cultists after witnessing a kidnapping and getting caught
    #he goes to angus, an adventurer, and asks him to take him far away

    #angus and gregg introduce their characters
    
    #everyone gets into costume visually
    
    
    
    #germ shows up on the way to the mountains
    
    
    
    
    
    
    
    
    return