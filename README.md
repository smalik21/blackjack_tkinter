# Blackjack Game using Tkinter in Python
This is a simple Blackjack game created using Python and Tkinter. In this game, the player can draw cards and the result is determined after the dealer draws. There is a button to shuffle the cards as well.

The game does not have the functionality of automatically starting a new game once the previous one ends, for that the user has to click on the `new game` button.

## Screenshots
![image](https://github.com/smalik21/blackjack_tkinter/assets/116386017/1d2d83a7-23b5-436b-9cfb-7fde144b09ed)

![image](https://github.com/smalik21/blackjack_tkinter/assets/116386017/dac957e6-251b-4cdd-9ebb-9f108548e03c)

![image](https://github.com/smalik21/blackjack_tkinter/assets/116386017/61afb1f2-8d70-498b-aeb6-b15cf74e95d7)

## Requirements
To run the game, you need to have Python 3.x installed on your system along with the following Python packages:
- tkinter
- random
## How to Run
To run the game, simply open a terminal or command prompt and navigate to the directory where the game files are located. Then, run the following command:
`python blackjack_pro.py`

Alternatively, navigate to the `dist` folder and run the `blackjack_pro.exe` file.

This will launch the game window and you can start playing.
## Cards Folder
The `blackjack_cards` folder contains the images of the cards used in the game. These images are in PNG format and are used to display the cards in the game window. The folder contains a total of 52 card images, one for each card in a standard deck of playing cards.

To use custom card images, simply replace the images in the `cards` folder with your own images. Make sure that the file names of the new images match the file names of the existing images, or modify the code accordingly to load the new images with different file names.
## How to Play
The rules of the game are simple. The goal is to get a hand value of 21 or as close to 21 as possible without going over. The player draws cards from the deck and can choose to stand (keep their current hand) or hit (draw another card). The dealer draws cards until their hand value is at least 17. If the player's hand value exceeds 21, they lose the game. If the dealer's hand value exceeds 21 or is lower than the player's hand value, the player wins. If the player's hand value is equal to the dealer's hand value, the game is a tie.
