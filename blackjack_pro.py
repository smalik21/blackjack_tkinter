import tkinter as tk
import random
import sys
import os

# Get the path of the script, whether it is running as a script or as an executable
if getattr(sys, 'frozen', False):
    # If running as an executable
    script_dir = sys._MEIPASS
else:
    # If running as a script
    script_dir = os.path.dirname(os.path.abspath(__file__))

# import card images
def import_card_images() -> list:
    card_set  = []
    card_types = ['club', 'diamond', 'heart', "spade"]
    face_cards = ['jack', 'queen', 'king']
    extension = ".png"
    for card_type in card_types:
        for card in range(1, 11):
            filename = f"{script_dir}/blackjack_cards/{card}_{card_type}{extension}"
            image = tk.PhotoImage(file=filename)
            card_set.append((card, image))
    for card_type in card_types:
        for card in face_cards:
            filename = f"{script_dir}/blackjack_cards/{card}_{card_type}{extension}"
            image = tk.PhotoImage(file=filename)
            card_set.append((10, image))
    return card_set

def shuffle_deck():
    global card_deck
    random.shuffle(card_deck)

def draw_dealer():
    while d_score < 21 and d_score <= p_score:
        draw_card("dealer")
    game_result()       # call game result function after # TODO


def draw_player():
    draw_card("player")

# draw card
def draw_card(name : str) -> None:
    global card_deck        # global card deck accessed
    card = card_deck.pop(0)      # card taken from deck
    card_deck.append(card)      # card inserted back
    set_score(name, card)

def set_score(name : str, card) -> None:
    # define global variables
    global dealer_score
    global player_score
    global dealer_frame
    global player_frame
    global d_score
    global p_score
    
    if name == 'dealer':
        d_score += card[0]
        dealer_score.set(d_score)
        tk.Label(dealer_frame, image=card[1]).pack(side='left')

    elif name == 'player':
        p_score += card[0]
        player_score.set(p_score)
        tk.Label(player_frame, image=card[1]).pack(side='left')
        if p_score > 21:
            game_result()
    else:
        print("Error, set_score")

def game_result():
    global d_score
    global p_score

    if p_score > 21:
        result.set("Result: Dealer WINS!")
    elif d_score > 21:
        result.set("Result: Player WINS!")
    elif d_score > p_score:
        result.set("Result: Dealer WINS!")
    elif d_score < p_score:
        result.set("Result: Player WINS!")
    

# new game
def new_game(): 
    # define global variables
    global dealer_score 
    global player_score 
    global dealer_frame
    global player_frame
    global d_score
    global p_score

    # set scores to "zero"
    d_score = 0
    p_score = 0
    dealer_score.set(0)
    player_score.set(0)
    result.set("Result: ")

    # destroy current car frames
    dealer_frame.destroy()
    player_frame.destroy()

    # create new card frames
    dealer_frame = tk.Frame(main_window, background='green')
    dealer_frame.grid(row=1, column=1, columnspan=3, sticky='news')
    player_frame = tk.Frame(main_window, background='green')
    player_frame.grid(row=2, column=1, columnspan=3, sticky='news')
    
    # draw initital cards
    draw_card("dealer")
    draw_card("player")
    draw_card("player")

if __name__ == '__main__':
    # INTERFACE

    # main window
    main_window = tk.Tk()
    main_window.geometry('640x480-100+100')
    main_window.title("BlackJack-Pro")
    # weight configurations
    main_window.columnconfigure(0, weight=1, minsize=100)        # result, score, and buttons
    main_window.columnconfigure(1, weight=1000)        # cards
    main_window.rowconfigure(1, weight=1)       # dealer score and cards
    main_window.rowconfigure(2, weight=1)       # player score and cards   
    main_window.rowconfigure(3, weight=1)       # buttons
    # main_window.rowconfigure(4, weight=0)       # empty

    # result label
    result = tk.StringVar()
    result_label = tk.Label(main_window, textvariable=result, background='yellow', font='FiraCode')
    result_label.grid(row=0, column=0, columnspan=2, sticky='nswe')
    result.set("Result: ")

    # score frame
    score_frame = tk.Frame(main_window, background='light blue')
    score_frame.grid(row=1, column=0, rowspan=2, sticky='news')
    score_frame.columnconfigure(0, weight=1)
    score_frame.rowconfigure(0, weight=1)
    score_frame.rowconfigure(1, weight=1)
    score_frame.rowconfigure(2, weight=1)
    score_frame.rowconfigure(3, weight=1)
    # score labels
    dealer_label = tk.Label(score_frame, text="Dealer", font='FiraCode')
    player_label = tk.Label(score_frame, text="Player", font='FiraCode')

    dealer_score = tk.IntVar()
    score_dealer = tk.Label(score_frame, textvariable=dealer_score, font='FiraCode')
    player_score = tk.IntVar()
    score_player = tk.Label(score_frame, textvariable=player_score, font='FiraCode')
    dealer_score.set(0)
    player_score.set(0)

    dealer_label.grid(row=0, column=0, sticky='ews')
    score_dealer.grid(row=1, column=0, sticky='new')
    player_label.grid(row=2, column=0, sticky='ews')
    score_player.grid(row=3, column=0, sticky='new')

    # card frames
    dealer_frame = tk.Frame(main_window, background='green')
    dealer_frame.grid(row=1, column=1, columnspan=3, sticky='news')
    player_frame = tk.Frame(main_window, background='green')
    player_frame.grid(row=2, column=1, columnspan=3, sticky='news')
    dealer_frame.rowconfigure(0, weight=1)
    player_frame.rowconfigure(0, weight=1)

    # buttons frame
    buttons_frame = tk.Frame(main_window, borderwidth=10, background='dark blue')
    buttons_frame.grid(row=3, column=0, columnspan=3, sticky='news')

    # buttons
    dealer_draw = tk.Button(buttons_frame, text="DEALER", command=draw_dealer)
    dealer_draw.grid(row=0, column=0)
    dealer_draw.config(padx=20)
    player_draw = tk.Button(buttons_frame, text="PLAYER", command=draw_player)
    player_draw.grid(row=0, column=1)
    player_draw.config(padx=20)
    new_game_button = tk.Button(buttons_frame, text="New Game", command=new_game)
    new_game_button.grid(row=0, column=2)
    new_game_button.config(padx=20)
    shuffle_button = tk.Button(buttons_frame, text="SHUFFLE", command=shuffle_deck)
    shuffle_button.grid(row=0, column=3)
    shuffle_button.config(padx=20)

    deck = import_card_images()
    card_deck = deck.copy()     # create a copy of deck
    shuffle_deck()
    d_score = 0
    p_score = 0

    new_game()

    main_window.mainloop()