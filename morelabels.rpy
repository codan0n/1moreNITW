#more labels

label houseOffice:
    "while searching the house you find a room you've never been in before, the office"
    $ officeQuestStarted = True
    jump afterExploringHouse

label houseShed:
    "After searching the house, you come across a rickety looking shed outside."
    "Pushing the snow out of the way, you find the door is locked."
    if hasKey == True:
        "You recall you found a key earlier that looks like it might fit the lock."
        "You run inside to retrieve it, but it's so rusted it snaps off inside the lock. Damn!"
        $ doorStuck = True
    else:
        "Maybe there's a key somewhere inside. Or maybe you'll have to find... alternative methods of entry."
    $ bikeQuestStarted = True
    jump afterExploringHouse
    
label houseBook:
    "You decide to explore your home some more. You don't find a wrench but you do find an overdue library book"
    "You should return it to the library."
    $ libraryQuestStarted = True
    jump afterExploringHouse