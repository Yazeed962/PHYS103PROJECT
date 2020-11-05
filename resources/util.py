import os
import graphics as g

logo = r"""
   _____                      _____ __    _          ____        _ __    __         
  / ___/____  ____ _________ / ___// /_  (_)___     / __ )__  __(_) /___/ /__  _____
  \__ \/ __ \/ __ `/ ___/ _ \\__ \/ __ \/ / __ \   / __  / / / / / / __  / _ \/ ___/
 ___/ / /_/ / /_/ / /__/  __/__/ / / / / / /_/ /  / /_/ / /_/ / / / /_/ /  __/ /    
/____/ .___/\__,_/\___/\___/____/_/ /_/_/ .___/  /_____/\__,_/_/_/\__,_/\___/_/     
    /_/                                /_/                                          
"""  


instructions = """
    * Read and learn about different aspects of physics!
    * Each level you complete will unlock a new part of the SpaceShip.
    * You will get a picture of how your SpaceShip looks like after every level.
    * Unlock all parts to build the complete ship and travel to the ISS!
"""

API_KEY = "Taw2OkQahqJynpkpzasGOEwbFR9GTclF"



def draw(directory):
    try:
        win = g.GraphWin("Image", 700, 700)
        part = g.Image(g.Point(350, 350), directory)
        part.draw(win)
        win.getMouse()
        win.close()        
    except g.GraphicsError: # To avoid crashing when closing a graphics pop up
        pass       

def main_screen():
    os.system('cls' if os.name == 'nt' else 'clear') # Clear Terminal window
    print(logo)
  
