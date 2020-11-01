import json
import requests
from resources.util import main_screen, instructions, draw, API_KEY
import os
import time 
import csv
from playsound import playsound

# Live ISS location
position_res = requests.get("http://api.open-notify.org/iss-now.json")  
iss_position = position_res.json()["iss_position"]

# ISS location on map
map_res = requests.get(f"https://www.mapquestapi.com/staticmap/v5/map?key={API_KEY}&locations={iss_position['latitude']},{iss_position['longitude']}")
map_res.raw.content_decode = True

# People in Space 
people_response = requests.get("http://api.open-notify.org/astros.json")
people = people_response.json()["people"]



# Save ISS location as a picture 
with open("ISS_location.png", "wb") as f:
    f.write(map_res.content)


main_screen()
print(instructions)
input("Press Enter to continue")
name = ""
while not name:
    name = input("Please enter your name : ")

main_screen()
print(f"""Hello {name}, We are on a quest to travel to the International space station! 
Don't worry, you won't be alone, there will be company, these astronauts there are waiting for you! """)
for person in people:
    print("- " + person["name"])


print(f"The ISS is currently located at {iss_position['latitude']}, {iss_position['longitude']}")
print("In a few seconds, the image of the ISS location on map will appear to you!")
time.sleep(15)
os.system("ISS_location.png")
input("Let's begin, shall we? (Press Enter)")


with open("texts.csv") as csv_data:
    sheet = csv.DictReader(csv_data)  # csv file is basically an excel spreadsheet
    for row in sheet:   # navigating through each row in the sheet 
        main_screen()
        print(f"Level { row['number'] }")
        print(row['paragraph'])
        time.sleep(2)
        input("Press Enter when you're done reading :)")
        print(row["additional_message"]) 
        time.sleep(4)
        os.system(os.path.join('illustrations', row['pic']))
        print("Now the part you just unlocked will appear to you!")
        time.sleep(2)
        draw(row["part"])
        t = 5
        while t:
            print(t, end="\r")
            time.sleep(1)
            t -= 1

confirmation = "x"

if confirmation not in ["y", "n"]:
    confirmation = input("Now that our SpaceShip is assembled, are you ready? ( y or n )").lower().strip()
    if confirmation == 'n':
        print("Congratulations, you just missed a once in a lifetime chance . . .")
        exit()


print(f"You have completely built your SpaceShip, goodluck on your journey, {name}!")

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear') # Clear Terminal window
print("We'll see you on the dark side of the moon")
playsound(os.path.join("rocket", "fly.mp3"))


