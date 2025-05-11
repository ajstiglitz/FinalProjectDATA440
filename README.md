### FinalProjectDATA440 Project Overview
---

### Description
The purpose of this code is to create a Graphical User Interface (or GUI) using Python's PyQt5 library that has the functionality of a dice roller, a player sheet, and a plot-creator. 

The dice available to roll include a four-sided die, six-sided die, an eight-sided die, a ten-sided die, a twelve-sided die, and a twenty-sided die. 

The player sheet allows the user to import a picture of their player, and text boxes to fill out characteristics like Name, Class, Race, Alignment, Level, and Age. There are also places to input the player inventory, the character's features and traits, as well as other proficiencies and languages.

The plot-creator allows the user to test different scenarios related to dice rolls to compare the distribution of variances.

The GUI is intended for use alongside the tabletop role-playing game Dungeons & Dragons (DND). DND is a fantasy game where players can create their own characters and roleplay as them going on adventures. Attached to these characters are what's known as "Ability Scores," which include Strength, Dexterity, Constitution, Intelligence, Wisdom, and Charisma.
These ability scores can vary depending on Race, Class, and/or Level, and depending on how high or low a score is, you may have to add or subtract a value from a dice roll.

#### Purpose:
The reason for the creation of this GUI was to make the calculation of dice rolls with the modifiers easier for players. Instead of having to do it by hand, this interface is meant to automatically calculate the results of a roll based on a player's ability scores.

Additionally, it also keeps the character information easily available.

Link to DND Official Site: https://dndstore.wizards.com/us/en

Link to DND Wikipedia page: https://en.wikipedia.org/wiki/Dungeons_%26_Dragons

---

### How to use the Project
This project contains a main.py file which is run in the command line to make the GUI appear.

To run the project, make sure that you are in the correct directory before trying to run the program, or you will end up with an error.

For example, if FinalProjectData440 is sitting in your Downloads folder, and your are in the C:\Users\YourUser directory when you open the command line, do the command 'cd Downloads'

Your resulting filepath would then look something like: C:\Users\YourUser\Downloads

From there, call cd FinalProjectData440 to get into the repository.

Once you are in the correct folder, use the command 'uv run main.py' and the GUI should open up for you.

This project uses a virtual environment that contains all of the needed Python libraries to get the code working.

Link for more information about uv virtual environments: https://docs.astral.sh/uv/pip/environments/

---

### Quickstart
This project uses Python version 3.12, Matplotlib version 3.10.1, Numpy version 2.2.4, and PyQt5_Qt5 version 5.15.2 (though there is also a file PyQt5 version 5.15.11.dist-info which contains metadata of a package).

This project also has some extra libraries present like Pandas and PyGame because in the initial conception of the project there was an intent to integrate the PyGame library into the interface (though this ended up not happening).

---

### Folders of FinalProjectDATA440 Repository
- figures/
    - Where the plots are saved to from the graphing tab
- src/
    - gifs/
        - This file contains the gifs for the dice roller.
    - The src folder contains the code for:
        - Creating a loading the attributes for tab one.
        - The code for the "Inspired" checkbox and proficiency label for tab one.
        - The random number generators that represent the different dice for tab one.
        - The working dice roller code and the resulting labels for tab one.
        - Showing the gifs of the dice for tab one.
        - A general helper file that can be used for checking directories.
        - A file for letting the user upload a photo for their charater for tab two.
        - The interface creation and implementation for tab one.
        - The interface creation and implementation for tab two.
        - The interface creation and implementation for tab three.
- writeup/
    - This folder contains the final writeup for the project. The writeup has more information on the math behind the graphs in tab three, and the basis for the project itself.

---

### Breakdown of the Different.py files in src
1. buttons.py
2. diceroller.py
3. helpers.py
4. qtcomponents.py
5. tabone.py
6. tabthree.py
7. tabtwo.py

### 1) buttons
The purpose of this file is to create and assemble the some elements used by tab one. Specifically the attribute adjuster, the proficiency bonus adjuster, and the inspiration checkbox.

### 2) diceroller
The purpose of this file is to create and assemble the some elements used by tab one. Specifically, the random number generators for the different die (D4, D6, D8, D10, D12, and D20), the gif visual that appears depending on the die the user chose, the roll results, and the dropdown that chooses the attributes that is being rolled for.

### 3) helpers
The purpose of this file is to check if a directory exists, and if not, to create it.

### 4) qtcomponents
This file contains classes related to uploading images by the user to be used in tab three.

### 5) tabone
This file has different classes all related to the creation and assembly of the PyQt5 components for tab one in the GUI.

### 6) tabthree
This file has different classes all related to the creation and assembly of the PyQt5 components for tab three in the GUI.

### 7) tabtwo
This file has different classes all related to the creation and assembly of the PyQt5 components for tab two in the GUI.

---

### Links to resources/code used in the project
- The drag and drop code was gotten from stack exchange. The comment in the file 'qtcomponents.py' that says "*Check README*" refers to the link below where the code was found:
    - Link: https://stackoverflow.com/questions/60614561/how-to-ask-user-to-input-an-image-in-pyqt5 
- Here are some links to the PyQT5 websites used that explained how to use the different elements:
    - Link: https://www.riverbankcomputing.com/static/Docs/PyQt5/
    - Link: https://doc.qt.io/qtforpython-6/ 
- And here is a link to the style sheet that was used in this project:
    - https://github.com/GTRONICK/QSS/blob/master/ManjaroMix.qss
        - The file was renamed to 'style.qss' because the style sheet used before the one above was named that already in the code.