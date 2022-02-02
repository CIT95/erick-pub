import random
# Week 4 Learn Together
# Music Picker
relaxing = ["Jazz", "Country", "Classical", "Soft Rock", "Lo-Fi", "Vaporwave"]
upbeat = ["Funk", "Jazz", "Rock", "Pop", "Disco", "Ska"]
time = ["Morning", "Noon", "Night"]
username = input("Hello! Welcome to the music genre picker.\n"
                 "What is your name?\n")
for time_of_day in time:
    if time_of_day == "Morning":
        morningchoice = random.choice(relaxing)
        print(f"The genre you should listen to this morning is "
              f"{morningchoice}.")
    elif time_of_day == "Noon":
        noonchoice = random.choice(relaxing + upbeat)
        print(f"The genre you should listen to this afternoon is "
              f"{noonchoice}.")
    elif time_of_day == "Night":
        nightchoice = random.choice(upbeat)
        print(f"The genre you should listen to tonight is "
              f"{nightchoice}.")
okay = input("Are these choices to your liking? Yes or No\n").lower()
if okay == "yes":
    print("Enjoy your music today!")
else:
    print("Please run again to get another selection.")
