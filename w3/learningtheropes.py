print("""           ____ __
          { --.\  |          .)%%%)%%
           '-._\\ | (\___   %)%%(%%(%%%
               `\\|{/ ^ _)-%(%%%%)%%;%%%
           .'^^^^^^^  /`    %%)%%%%)%%%'
  jgs     //\   ) ,  /       '%%%%(%%'
    ,  _.'/  `\<-- \<
     `^^^`     ^^   ^^
""")

print("Welcome to Learning the Ropes.")
print("Your job is to defeat the flying red dragon in the next village over.")
quesiton1 = input("Are you a knight or are you a mage? \n").lower()
if quesiton1 == "mage":
    question2 = input("You grab your robes and head to the basement for your" +
                      "training. Once you arrive you are told a dragon is"
                      "terrorizing a near by village and you are to assist"
                      "What will you pack in your bag?\n"
                      "Anti-Fire Potion or Anti-Fire Shield?\n").lower()
    if question2 == "anti-fire potion":
        question3 = input("With your potions packed you head out."
                          "What method of transport will you take?\n"
                          "Horse, Walk, Teleport?\n").lower()
        if question3 == "horse":
            print("The Dragon sees you coming from a mile away."
                  "He shoots a fireball while you arnt prepared "
                  "and are cooked.\nGame over.")
        elif question3 == "walk":
            print("You walk into what use to be a village. Its all been burned"
                  " to the ground.\nGame Over.")
        elif question3 == "teleport":
            print("You take a sip of your Anti-Fire Potion and cast the "
                  "teleport. You appear in the village square ready to fight. "
                  "You cast a few spells and the dragon falls out of the sky "
                  "into a nearby field.\nYou Win!")
    else:
        print("You grab the shield ready to fight the dragon. As you try"
              " to cast your spell the shield gets in the way and the "
              "dragon destorys the village.\nGame Over.")
else:
    print("As a knight you have no way to attack the flying dragon and are "
          "sent back to the barracks.\nGame Over. ")
