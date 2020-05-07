import time
import random


def print_normal(string):
    print(string)
    time.sleep(1)


def intro_start(select):
    print_normal("You find yourself standing in an open field," +
                 "filled with grass and yellow wildflowers.")
    print_normal(f"Rumor has it that a {select} is somewhere around here," +
                 "and has been terrifying the nearby village.")
    print_normal(f"In front of you is a house.")
    print_normal(f"To your right is a dark cave.")
    print_normal(f"In your hand you hold your " +
                 "trusty (but not very effective) dagger.")


def door(select):
    print_normal(f"You approach the door of the house.")
    print_normal("You are about to knock when " +
                 f"the door opens and out steps a {select}.")
    print_normal(f"Eep! This is the {select}'s house!")
    print_normal(f"The {select} attacks you!")


def enter_door(select, list):
    print_normal(f"You approach the door of the house.")
    print_normal(f"You are about to knock when " +
                 f"the door opens and out steps a {select}.")
    print_normal(f"Eep! This is the {select}'s house!")
    print_normal(f"The {select} attacks you!")
    print_normal(f"You feel a bit under-prepared for this," +
                 "what with only having a tiny dagger.")
    fight_or_run(select, list)


def cave(select, list):
    print_normal(f"You peer cautiously into the cave.")
    print_normal(f"It turns out to be only a very small cave.")
    print_normal(f"Your eye catches a glint of metal behind a rock.")
    print_normal(f"You have found the magical Sword of Ogoroth!")
    print_normal(f"You discard your silly old dagger and " +
                 "take the sword with you.")
    print_normal(f"You walk back out to the field.")
    list.append('magical sword')
    list.append('cave')
    door_or_cave(select, list)


def person_already_in_cave(select, list):
    print_normal("You peer cautiously into the cave.")
    print_normal("You've been here before, and gotten all " +
                 "the good stuff. It's just an empty cave now.")
    print_normal("You walk back out to the field.")
    door_or_cave(select, list)


def fight(select):
    print_normal(f"You do your best...")
    print_normal(f"but your dagger is no match for the {select}.")
    print_normal(f"You have been defeated!")
    askingchoice()


def runaway(select, list):
    print_normal(f"You run back into the field. Luckily, " +
                 "you don't seem to have been followed.")
    door_or_cave(select, list)


def wins(select):
    print_normal(f"As the {select} moves to attack, " +
                 "you unsheath your new sword.")
    print_normal("The Sword of Ogoroth shines brightly" +
                 "in your hand as you brace yourself for the attack.")
    print_normal(f"But the {select} takes one " +
                 "look at your shiny new toy and runs away!")
    print_normal(f"You have rid the town of the {select}. You are victorious!")
    askingchoice()


def inputing_value(select, list):
    response = input("(Please enter 1 or 2.)\n")
    if response == '1':
        if 'magical sword' in list:
            door(select)
            fight_or_run(select, list)
        else:
            enter_door(select, list)
    elif response == '2':
        if 'cave' in list:
            person_already_in_cave(select, list)
        else:
            cave(select, list)
    else:
        inputing_value(select, list)


def door_or_cave(select, list):
    print_normal("Enter 1 to knock on the door of the house.")
    print_normal("Enter 2 to peer into the cave.")
    print_normal("What would you like to do?")
    inputing_value(select, list)


def fight_or_run(select, list):
    response = input(f"Would you like to (1) fight or (2) run away?\n")
    if response == '1':
        if 'magical sword' in list:
            wins(select)
        else:
            fight(select)
    elif response == '2':
        runaway(select, list)
    else:
        askingchoice()


def main():
    a = ['pirate', 'dragon', 'gorgon', 'wicked fairie', 'troll']
    select = random.choice(a)
    list = []
    intro_start(select)
    door_or_cave(select, list)


def askingchoice():
    responses = input("Would you like to play again? (y/n)")
    if responses == 'y':
        print_normal("Excellent! Restarting the game ...")
        main()
    elif responses == 'n':
        print_normal("Thanks for playing! See you next time.")
        exit()
    else:
        askingchoice()


def play_game():
    main()
    askingchoice()

play_game()
