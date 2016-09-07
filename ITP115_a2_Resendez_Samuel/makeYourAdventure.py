#Samuel Resendez
#ITP 115
#Assignment 2
#September 11th, 2016
#Description:
#This program gives a short story, about a youth in wartime.

print("""The date is April 12th, 1862. Exactly one year since the great divison happened. And, since
that time, the condition has only gotten worse. You heard your father over dinner, muttering about the
appalling loses that had been suffered. And now it was your turn to take up the fight.""")
print("You receive a letter in the mail. And it asks one simple question: will you stand for you country?")
print("So, now its your choice. What do you do? :")
print("a) Fight like the patriotic citizen you are.")
print("b) Ignore the call to arms, and continue to live the comfy life.")
choiceOne = input(">>")
if choiceOne.lower() == "a":
    print("""Thats the spirit, my friend. You have chosen an honorable route. Incredibly unpragmatic, but, thats
beside point. You enlist, and are drafted to one of the most prestigious regiments: the 1st Infantry Regiment.
As the front line, you are immediately called forth to fight the formidable opponent. Your first mission?
Frontal Assault.""")
    print("Do you choose to: ")
    print("a) continue and fight.")
    print("b) call in sick that day.")
    print("c) play dead to avoid the brunt of the conflict.")
    choiceTwo = input(">>")
    if choiceTwo.lower() == "a":
        print("""In true story protagonist fashion, you wade through the onslaught unscathed, singlehandedly dismantling
    the opposition and winning the game. Congratulations!""")
    if choiceTwo.lower() == "b":
        print("""No one believes you for a second. They drag you out of the tent, and put you to lead the charge.
        Good luck buddy. """)
    if choiceTwo.lower() == "c":
        print("""A brilliant move. Except for one detail. Unbeknownst to you, they brought the cavalry. And, well,
        I'll leave it to your imagination to fill in the rest. Good night, my friend <3.""" )

if choiceOne.lower() == "b":
    print("""The cowardly, though decidedly pragmatic choice. Now, despite your apparent lack of dedicaton to your
country, the government chooses to send you another letter, this one asking about rations and donating to
support the troops.
So now, what do you do? Do you:
a) Provide rations and money to the war effort?
b) Blow off the letter, refusing to do anything to help your country. """)
    choiceThree = input(">>")
    if choiceThree.lower() == "a":
        print("""Good on you! You're supporting your country, albeit indirectly. Congratulations, you made it!  """)
    if choiceThree.lower() == "b":
        print("""C'mon man, but your country though? Like, you don't even have to put yourself in bodily harm for
this one, this is just out of pure selfishness. And for that, the government hunts you down, for refusing to
comply with wartime regulations. I'm sorry, but you, good sir, lose.""")
