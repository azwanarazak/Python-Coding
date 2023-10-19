#!/usr/bin/env python

import random

def main():
    """Start a artist guessing game."""
    print("Persempahan pada AJL 2024!")

    Male_artist = [
        "Mawi",
        "Khai Bahar",
        "Awie",
        "Nabila Razali",
        "Misha Omar"
        
        ]

    x = random.choice(Male_artist)
    
    guess = None

    while x != guess:

        guess = str(input("Siapakah penyanyi pertama akan membuat persembahan? "))
        
        if x == guess: 
            print("Pilihan Kamu {}. Tahniah, dapatkan tiket AJL 2024 sekarang!".format(guess))
            break
        else:
            print("Pilihan kamu {}. Salah, klu adalah penulis lirik lagu M Nasir ".format(guess))

main()