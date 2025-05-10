### FinalProjectDATA440 Project Overview
---

### Description
The purpose of this code is to create a Graphical User Interface (or GUI) using Python's PyQt5 library that has the functionality of a dice roller, a player sheet, and a plot-creator. 

The dice availble to roll include a four-sided die, six-sided die, an eight-sided die, a ten-sided die, a twelve-sided die, and a twenty-sided die. 

The player sheet allows the user to import a picture of their player, and text boxes to fill out characteristics like Name, Class, Race, Alignment, Level, and Age. There are also places to input the player inventory, the character's features and traits, as well as other proficiencies and languages.

The plot-creator allows the user to test different scenarios related to dice rolls to check compare the distribution of variances.

The GUI is intended for use alongside the tabletop role-playing game Dungeons & Dragons (DND). DND is a fantasy game where players can create their own characters and roleplay as them going on adventures. Attached to these characters are what's known as "Ability Scores," which include Strength, Dexterity, Constitution, Intelligence, Wisdom, and Charisma.
These ability scores can vary depending on Race, Class, and/or Level, and depending on how high or low a score is, you may have to add or subtract a value from a dice roll.

#### Purpose:
The reason for the creation of this GUI was to make the calculation of dice rolls with the modifiers easier for players. Instead of having to do it by hand, this interface is meant to automatically calculate the results of a roll based on a player's ability scores.

Additionally, it also keeps the character information easily available.

Link to DND Official Site: https://dndstore.wizards.com/us/en

Link to DND Wikipedia page: https://en.wikipedia.org/wiki/Dungeons_%26_Dragons

---

### How to use the Project
- contains a main.py file which just needs to be run in the command line to make the gui appear
- maybe add some comments in the main.py on how to run the project?
- make sure you cd into the right folder 
- so if FinalProjectData440 is just sitting in your downloads folder and your are on C:\Users\YourUser when you open the command line
- do cd Downloads
- then cd FinalProjectData440
- from there you can do 'uv run main.py' and the GUI should open up for you.

---

### Quickstart
- explain what version of python this repository uses, as well as the other libraries like matplotlib, PyQt5, numpy, and if anything else is used talk about that
- also mention that there are some extra libraries like PyGame which are not used but are present because they were there planned to be used initially but later became obsolete
- provide a link to the uv website for more commands

---

### Folders of FinalProjectDATA440 Repository
- this needs to be done cleaner once I delete the useless files
- figures/
    - where the plots can be saved to
- src/
    - contains the code for:
        - ...
- writeup/
    - the final writeup for the project. Contains more info on the math behind the project and the basis for it (NOTE: refine later)

---

### Breakdown of the Different.py files in src
1. buttons.py
2. diceroller.py
3. helpers.py
4. interface.py
5. interfaceTest.py
6. plots.py
7. qtcomponents.py

NOTE: will probably have to rename a bunch of these files to make them more intuitive. Especially the ones with 'test' in the name since they aren't tests anymore

---

### Links to resources/code used in the project
- the drag and drop code was gotten from stack exchange, so make sure to have a comment in the file leading back to here in the README with a link to that code
- also probably the PyQT5 website 

---
### GENERAL NOTES:

what needs to be included here:
- should be focused on high-level overview 
- contain instructinos for others to use the code
- the writeup (which will be in a different folder) will have the additional background, more details about the data and methods, and discuss other conclusions/future work where applicable
- in my case the data will be about the math behind the plots and the advantage in terms of the distribution of max(X, x)
- file in folder for 'writeup' is just a placeholder to make it appear on git. shows the math i did by hand before coding

Overview includes:
- purpose of project
- language it's written in
- what it does and why it is useful
- Project requirements


What needs to be moved from the main repository into folders:
- tabonetest.py
- tabtwotest.py
- tabthreetest.py
- style.qss
    - might need to remove the style.qss and go into the widgets to add style, since it is not looking how I want.

NOTE: will need to remember to refactor the files when moved otherwise it won't work anymore

What needs to be added
- a saved graph into figures

What needs to be deleted:
- the D20Pygame.py
- the 'Dice' Folder
- 'data' folder also probably can be deleted. I am using arrays and not a .csv to read in the dice for the plot