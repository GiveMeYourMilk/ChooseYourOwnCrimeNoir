# Choose.py
# by Wylder G., Tabor F., 
# Description: starter code for the Choose Your
# Own Adventure Project

# Music
'FL Studios Gunshot FX'
'John Coltrane: In a Sentimental Mood'

# Import Statements
from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox
import os

root = Tk()
w = Label(root, text="Choose Your Own Adventure")
w.pack()

# Beginning Dialogue
os.startfile('coltrane.mp3')
messagebox.showinfo("...", "July 10th, 2023. A day at work.")
messagebox.showinfo("Prologue", "'Congratulations on this "
                        "new position. It's gonna be a brand n"
                        "ew start for you as one of my detecti"
                        "ves. Hopefully things don't get too bo"
                        "ring for you. For now, rest up until "
                        "tomorrow. Enjoy your night.'")
name = simpledialog.askstring("Prologue", "'By the way, what was"
                                   " your name again?")
messagebox.showinfo("Prologue", "" + name + ", I'll remember that.")
messagebox.showinfo("Prologue", "Later that night.")
messagebox.showinfo("Prologue", "'Too many papers tonight..."
                        " Hey, excuse me sir. No visitors after-")
os.startfile('gunshot.mp3')
messagebox.showinfo("Prologue", "BANG")
messagebox.showinfo("A New Case", "The next day.")
os.startfile('coltrane.mp3')
messagebox.showinfo("A New Case", "You're excited for a new"
                        " start at your workplace. In your car, "
                        "you notice sirens near the building an"
                        "d as you get closer see investigators. "
                        "As you park your car and rush to the s"
                        "cene, you can't help but think your fi"
                        "rst case might be coming sooner than y"
                        "ou thought.")
messagebox.showinfo("A New Case", "'What happened?' you ask one of the"
                        " nearby officers.")
messagebox.showinfo("A New Case", "\n'The boss, he was shot and killed', he answers."
                        "\n    " 
                        "\n'What!?' you yell out in surprise. Quickly you, cal"
                        "m down and walk a short distance away from everyone."
                        "You realize that your next move could change you ent"
                        "ire life and career.")

def intro():
    """ Introductory Function -> starts the story going """

    choice = simpledialog.askinteger("A New Case", "\n What will you do?" + \
                                 "\n (1) Take on the case yourself in secret" + \
                                 "\n (2) Ignore the situation and walk away" + \
                                 "\n (3) Quit the job at the agency" + \
                                 "\n (4) Pursue vengeance on the people that did this")
                                 
    if choice == 1:
        iwork()
    elif choice == 2:
        iignore()
    elif choice == 3:
        iquit()
    elif choice == 4:
        ivengence()
    else:
        intro()

################ Amiel's Functions #####################

    ### MAP OF FUNCTIONS ###
"""
]1_1
    ]2_1
        ]3_1
            ]4_1
    ]2_2
        ]3_2
            ]4_2
                ]5_1
    ]2_3
        ]2_2
"""
def iwork():
    messagebox.showinfo("Secrecy and Solitude", "You decide to work in"
                        " secrecy and solitude. What is your next choice?")
    choice = simpledialog.askinteger("Secrecy and Solitude",
                                     "(1) Go back to the crime scene; Reinvestigate"
                                     "\n(2) Re-interrogate your prime suspect"
                                     "\n(3) Go over your evidence once more")
    if (choice == 1):
        messagebox.showinfo("Secrecy and Solitude",
                            "You go back to the crime scene to reinvestigate, and"
                            " find a new letter. You open the letter and it says"
                            "\n\n    'TO: ROBERT M: Great job on the hit Robert, that"
                            " detective won't be snooping in private affairs anymore"
                            ", here is the $15,000, as promised' -S ")
        iwork2_1()
    elif (choice == 2):
        messagebox.showinfo("Secrecy and Solitude",
                            "You see him in the nearby alleyway, on the way to"
                            " his home, harassing an innocent woman.")
        iwork2_2()
    elif (choice == 3):
        messagebox.showinfo("Secrecy and Solitude",
                            "You find new evidence in an hour log that gives"
                            " your prime suspect the time to commit the murder")
        iwork2_3()
    else:
        iwork()

def iwork2_1():
    choice = simpledialog.askinteger("Secrecy and Solitude",
                                     "(1) Hah, what nonsense"
                                     "\n (2) It seems careless for a criminal mastermind like 'S' to"
                                     " slip up like this, I should investigate. Who is this 'Robert M'?")
    if (choice == 1):
        messagebox.showinfo("Secrecy and Solitude",
                            "It seems you just gave up your only lead by sheer lack of interest."
                            " Your story ends here")
    elif (choice == 2):
        messagebox.showinfo("Secrecy and Solitude",
                            "Robert Malcone, 13 counts of armed robbery, 2 counts "
                            "of manslaughter, and suspect for dozens of murder "
                            "cases; street alias, 'The Gun'"
                            "\n\nRobert must be the hired hand for whoever 'S' is.")
        messagebox.showinfo("Secrecy and Solitude",
                            "You now can either freelance with this new information, or give"
                            " this information to the police"
                            "\n\nDo you follow up freelance, or go to the police with this newfound information?")
        iwork3_1()
    else:
        iwork2_1()

def iwork2_2():
    choice = simpledialog.askinteger("Secrecy and Solitude",
                                     "(1) 'Hey, Giordini, I have some questions to ask you!'"
                                     "\n(2) Oh... this dirtbag is just ASKING FOR IT! (knuckle cracking)")
    if (choice == 1):
        messagebox.showinfo("Secrecy and Solitude",
                            "He bolts off")
        iwork3_2()
    elif (choice == 2):
        messagebox.showinfo("Secrecy and Solitude",
                            "The fight is over quickly, for his only real targets of his 'collections' are "
                            "the elderly...")
        messagebox.showinfo("Secrecy and Solitude",
                            "Although it seemed right at the time, this was in fact a poor choice. "
                            "Giordini now refuses to cooperate with the police in the attempt "
                            "to find out who really killed your boss.")
        messagebox.showinfo("Secrecy and Solitude",
                            "Along with all this, you are being sued by copious amounts of "
                            "agencies, the likes of many that you had not even knew existed. "
                            "It seems your days of working detective are over.")
    else:
        iwork2_2()

def iwork2_3():
    choice = simpledialog.askinteger("Secrecy and Solitude",
                                     "(1) Reinterrogate your prime suspect. Discuss new information "
                                     "with him (get some answers)"
                                     "\n (2) Turn over new evidence to the police, a full force is "
                                     "stronger than one man")
    if (choice == 1):
        messagebox.showinfo("Secrecy and Solitude",
                            "You see him in the nearby alleyway, on the way to"
                            " his home, harassing an innocent woman.")
        iwork2_2()
    elif (choice == 2):
        messagebox.showinfo("Secrecy and Solitude",
                            "When you turn over the case, your co-workers could see that "
                            "this case was distressing you, so they relieve you when they "
                            "get access to this new evidence. You can no longer work on the "
                            "case")
    else:
        iwork2_3()

def iwork3_1():
    choice = simpledialog.askinteger("Secrecy and Solitude",
                                     "(1) Follow up on Roberts possible ties to the hit"
                                     "\n(2) Give this newfound information to the police")
    if (choice == 1):
        messagebox.showinfo("Secrecy and Solitude",
                            "You discover that Robert had also been working as a 'collection"
                            " agent' for the Mafia. His boss is none other than the elusive 'Silvone'."
                            " Silvone must be 'S'")
        messagebox.showinfo("Secrecy and Solitude",
                            "This man... Silvone, epiphany of a scumbag, murderer of innocent"
                            " men, women, and children all alike. This dirtbag deserves to die..."
                            " Should I murder this man? Chances are he might get out again if"
                            " I bring him to the station... Rich men walk. But if I kill him, I stoop to"
                            " his level")
        iwork4_1()
    elif (choice == 2):
        messagebox.showinfo("Secrecy and Solitude",
                            "The other detectives see you have become too invested in the case,"
                            " and with this newfound information, they are able to take the case"
                            " away from you. You lose control of the case")
    else:
        iwork3_1()

def iwork3_2():
    choice = simpledialog.askinteger("Secrecy and Solitude",
                                     "(1) Chase him"
                                     "\n(2) Shoot him")
    if (choice == 1):
        messagebox.showinfo("Secrecy and Solitude",
                            "You follow him to his hideout, and hear ludicrous amounts of cursing, "
                            "then you hear Giordini talking to one another")
        messagebox.showinfo("Secrecy and Solitude",
                            "'Did that cop follow you here?' 'Who do you take me for?, I'm 'The Gun', "
                            "Its not hard to outrun a pig")
        iwork4_2()
    elif (choice == 2):
        messagebox.showinfo("Secrecy and Solitude",
                            "He died, what did you expect")
        messagebox.showinfo("Secrecy and Solitude",
                            "You lost your only lead because you forgot what a gun does. Good job.")
    else:
        iwork3_2()

def iwork4_1():
    choice = simpledialog.askinteger("Secrecy and Solitude",
                                     "(1) End his life"
                                     "\n(2) Bring him in yourself")
    if (choice == 1):
        messagebox.showinfo("Secrecy and Solitude",
                            "In a storm of rage, and short-sightedness, you pull the trigger. "
                            "This for only a breif moment are you relieved as you are brought "
                            "into custody yourself for murder in the first degree.")
    elif (choice == 2):
        messagebox.showinfo("Secrecy and Solitude",
                            "You bring him in, and are greeted with promotion, relief and "
                            "celebrations of all sorts. You find that bringing him in has alleviated "
                            "your troubles and you can finally move on. Thorugh this capture you "
                            "end up taking the position as lead detective, and replace your old "
                            "boss.")
    else:
        iwork4_1()

def iwork4_2():
    choice = simpledialog.askinteger("Secrecy and Solitude",
                                     "(1) Call for backup (running for police is a probable cause "
                                     "for a search warrent)"
                                     "\n(2) Go in vigilante, you can't risk losing you handle on this "
                                     "case")
    if (choice == 1):
        messagebox.showinfo("Secrecy and Solitude",
                            "They hear you calling for backup outside of their hideout. "
                            "It seems you still haven't mastered the art of not talking loudly. "
                            "They bring you in before you can disclose the location of the "
                            "hideout to the police.")
        messagebox.showinfo("Secrecy and Solitude",
                            "After hours of torture, they assume you are just a goon of the "
                            "police, and that you know nothing. They let you go, but not "
                            "before adequate bruising")
        messagebox.showinfo("Secrecy and Solitude",
                            "You overheard their chatter as they move their hideout to a "
                            "new location, 'Hey Silvone, this guy is just a dunce, knows "
                            "nothing. Wouldn't want more heat drawn to another murder. "
                            "*chatter*, yeah we messed him up good, we wont talk.")
        messagebox.showinfo("Secrecy and Solitude",
                            "'SILVONE', you think in your head (as you learned your lesson "
                            "about talking loudly last time), he is the head of the mafia, and "
                            "now we have probable cause to search his offices. We can finally "
                            "bring him down!")
        iwork5_1()
    elif (choice == 2):
        messagebox.showinfo("Secrecy and Solitude",
                            "You get shot. C'mon it's a hideout of armed assailants.")
    else:
        iwork4_2()

def iwork5_1():
    choice = simpledialog.askinteger("Secrecy and Solitude",
                                     "(1) 'Silvone will get out if I don't take care of him; I need to "
                                     " kill him so his lawyers don't get him out again.'"
                                     "\n(2) 'This time, we have REAL evidence, we need to pursue "
                                     "the LEGAL path")
    if (choice == 1):
        messagebox.showinfo("Secrecy and Solitude",
                            "You are there, holding a gun to his face, past all his handcuffed "
                            "goons, all struggling to make sure you don't kill thier meal ticket. "
                            "You do the only thing left and pull the trigger.")
        messagebox.showinfo("Secrecy and Solitude",
                            "BANG, Silvone is dead, and now you are in jail, good going.")
    elif (choice == 2):
        messagebox.showinfo("Secrecy and Solitude",
                            "You go back over evidence, and discover that the gun the "
                            "hitman used on your superior and the guns used in crimes "
                            "assosiated with 'S' are in fact from the same weapon. The "
                            "hitman is just a hired hand and Silvone, and now you have the "
                            "real evidence to prove the injustice Silvone has caused.")
        messagebox.showinfo("Secrecy and Solitude",
                            "You bring him in, and are greeted with promotion, relief and "
                            "celebrations of all sorts. You find that bringing him in has alleviated "
                            "your troubles and you can finally move on. Thorugh this capture you "
                            "end up taking the position as lead detective, and replace your old "
                            "boss.")
    else:
        iwork5_1()
################ Niraj's Functions #####################
def iignore():
    messagebox.showinfo("The Detective Allergic to Murders",
                        "You decide to ignore the case despite some people"
                        " looking at you for answers. 'Well, it's just gonna"
                        " have to be someone else' you think. Lost in your t"
                        "houghts, you fail to notice a shady figure overlooking"
                        " the whole scene.")
    messagebox.showinfo("The Detective Allergic to Murder",
                        "The next day...")
    messagebox.showinfo("The Detective Allergic to Murder",
                        "Going through your usual morning routine,"
                        " you drive to work. There, you see the same"
                        " situation as yesterday and the situation seems "
                        "strangely familiar.")
    messagebox.showinfo("The Detective Allergic to Murder",
                        "You see the partner that was assigned to you"
                        "\n the other day and ask, 'What happened here?'" + \
                        "\n"
                        "\n 'Another murder happened, and it ain't pretty'"
                        ", he promptly answers."
                        "\n"
                        "\n You stand there shocked. Another murder? What to "
                        "do now...")
    ignore()
def ignore():
    choice = simpledialog.askinteger("The Detective Allergic to Murder",
                                     "\n(1) Work. This case could"
                                     " be your last if you're not careful" + \
                                     "\n(2) Give the lie you did it and confess for your sins."
                                     "\n(3) Ignore the murder. Not your problem")
    if (choice == 1):
        work()

    elif (choice == 2):
        confess()
    elif choice == 3:
        nope()
    else:
        ignore()
def work():
    messagebox.showinfo("Accepting Fate",
                        "You finally realize that something's up and it's"
                        " about time you took action. You head to the "
                        "headquarters to finalize your decision.")
def confess():
    messagebox.showinfo("A Stupid Liar",
                        "You lose your mind and confess to the two murders that"
                        " have happened. Absolutely no one believes you and"
                        " this results you being stripped of your badge "
                        "and sent to an asylum for mental analysis. Thus"
                        " ends your career as a detective.")
    messagebox.showinfo("A Stupid Liar",
                        "INSANITY ENDING")
def ignore2():
    messagebox.showinfo("The Next Victim",
                        "Late at night, you're looking at other cases th"
                        "at might be available for you. Suddenly the door"
                        "\n opens." + \
                        "\n 'Detective " + name + "?'")
    messagebox.showinfo("The Next Victim",
                        "Turning around you answer the person who"
                        " called. 'Yes that's me. How may I-")
    os.startfile('gunshot.mp3')
    messagebox.showinfo("The Next Victim", "BANG")
    messagebox.showinfo("The Next Victim",
                        "Bleeding out, you see the killer walking away "
                        "with confidence. 'Idiot', you think to yourself."
                        " Pulling out your gun you shoot the killer who"
                        " instantly goes down. You smile."
                        " At least you go down as a hero.")
    messagebox.showinfo("The Next Victim",
                        "FALSE HERO ENDING")
################ Robat's Row Row Row your boat gently down the stream robat Functions #####################
def iquit():
    choice = simpledialog.askinteger("Choose wisely",
                                     "This is the next part of the story.  Now you must choose 1 or 2 again.")
    if (choice == 1):
        messagebox.showinfo("The End",
                            "You chose right.  THE END")

    elif (choice == 2):
        messagebox.showinfo("The End",
                            "You chose ok.  THE END")
    else:
        choice2()

################ GiveMeYourMilk Functions #####################
        #204863 204863 204863 204863 204863 204863
def ivengence():
    choice = simpledialog.askinteger("Choose wisely",
                                     "This is the next part of the story.  Now you must choose 1 or 2 again.")
    if (choice == 1):
        vignore()

    elif (choice == 2):
        vfollow()

    else:
        ivengence()

def vignore():
    messagebox.showinfo("END",
                        "You look at the letter, put it down and"
                        " walk away. That letter isn't what you "
                        "need right now. You're barely a detective "
                        "you're not a world class ninja spy assassin."
                        " As you walk away you realise that was it,"
                        " you're last chance to live out your dream"
                        " of being a classic detective like the ones"
                        " your grandfather would tell you about watching"
                        " in classic films and now it's over now. You walk home"
                        " with your head hung low, knowing that your"
                        " dream is lost.")
def vfollow():
    choice = simpledialog.askinteger("Rooftop",
                                     "You catch hitman on rooftop"
                                     "\n Kill him(1) or Question him(2)")
    if (choice == 1):
        fkill()

    elif (choice == 2):
        fquestion()

    else:
        vfollow()

def fkill():
    choice = simpledialog.askinteger("Killer",
                                     "What will you do with his body?"
                                     "\n Hide it(1) or Display it(2)")
    if (choice == 1):
        khide()

    elif (choice == 2):
        kdisplay()

    else:
        fkill()

def khide():
    messagebox.showinfo("END",
                        "You hide the body where it"
                        " will never be found. Your guilt won't let you"
                        " show your face work anymore now")

def kdisplay():
    messagebox.showinfo("END",
                        "With the body so visble it isn't"
                        " hard for the police to discover"
                        " enough evidence to put you away"
                        " for a long time")

################ Winikka's Functions #####################
# Note this is an alert of the Winikka Broadcast System
# This is only a test
# Winikka is not really going to code a function here
# If he were to code, he would put it here.
# This is just to show you how to collaborate using Git

################ Main #####################
intro()

root.destroy()
