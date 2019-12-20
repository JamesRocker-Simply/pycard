from build_card import card_graphics as cg
import os

if __name__ == "__main__":
    user = str(os.getlogin()).replace('.', ' ').capitalize()
    cg.build_card(user)
