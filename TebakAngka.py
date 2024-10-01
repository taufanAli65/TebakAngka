import random as rd
import os
import time

#kl os.system('cls') gabisa coba ganti cls dengan clear

#pesan selamat datang dan peraturan
def welcome_message():
    """
    menampilkan selamat datang dan menjelaskan peraturan
    """
    print("="*65)
    print("Guess The Number".center(65))
    print("="*65)
    print("welcome to the game, the rule is simple")
    print("You just need to guess a number between 1-20. Depend on what level u choose.")
    print("It will says on your screen if your guess is too high or too low")
    print("Your guess limit is 5 guess")
    print("Let's begin, shall we?")
    print("="*65)
    time.sleep(8)
    os.system('cls')

#user memilih level
def user_choose_level() :
    """
    proses user memilih level
    """
    global random_number
    global akhir_number
    akhir_number = 0
    level_text = """Choose level :
1. Guess number 1-10
2. Guess number 1-15
3. Guess number 1-20
4. Custom"""
    print(level_text)
    level = [1, 2, 3, 4]
    try :
        memilih_level = int(input("Choose Level : "))
    except ValueError :
        error_message()
        time.sleep(2)
        os.system('cls')
        print(level_text)
        memilih_level = int(input("Choose Level : "))
    while memilih_level not in level :
        error_message()
        time.sleep(2)
        os.system('cls')
        print(level_text)
        memilih_level = int(input("Choose Level : "))
    if memilih_level == 1 :
        akhir_number = int(10)
    elif memilih_level == 2 :
        akhir_number = int(15)
    elif memilih_level == 3 :
        akhir_number = int(20)
    elif memilih_level == 4 :
        akhir_number = 0
        while akhir_number <= 0 :
            try :
                akhir_number = int(input("Max Number : "))
                if akhir_number <= 0 :
                    raise ValueError
            except ValueError :
                error_message()
    os.system('cls')
    random_number = rd.randint(1, akhir_number)

#pesan error
def error_message() :
    """
    menampilkan pesan error
    """
    print("Error, data yang diinput tidak valid. Coba lagi")

#User menebak angka
def get_user_guess() :
    """
    proses user menebak. terdapat parameter too low/too high
    """
    global user_guess
    user_guess = 0
    while user_guess <= 0 :
        try :
            user_guess = int(input("Guess the number : "))
            if user_guess <= 0 :
                raise ValueError
        except ValueError :
            error_message()
    if user_guess > random_number :
        print("Too High")
        time.sleep(2)
        os.system('cls')
    elif user_guess < random_number :
        print("Too Low")
        time.sleep(2)
        os.system('cls')
    else :
        os.system('cls')
        print("Correct, your number is ", random_number)

#kalo dihapus kodenya error
user_guess = 0

#sistem permainan
def user_guess_process() :
    """
    proses user menebak sampai 5 kali
    """
    global guess_remain
    guess_remain = 5
    while user_guess != random_number and guess_remain > 0:
        print("Guess Remain : %d"%(guess_remain))
        get_user_guess()
        if user_guess == random_number and guess_remain == 1:
            break
        guess_remain -= 1
    if guess_remain == 0 :
        os.system('cls')
        print("Mission failed, U already guess the wrong number 5 times")
        print("Better luck next time")

#sistem skor
def user_score() :
    if guess_remain == 4 :
        print("U must be very lucky person")
    elif guess_remain == 3 :
        print("2 guesses, not bad")
    elif guess_remain == 2 :
        print("3 guesses, your luck rate is average")
    elif guess_remain == 1 :
        print("I run out of words...")

#sistem untuk memulai permainan
def play_game() :
    welcome_message()
    user_choose_level()
    user_guess_process()
    user_score()

#sama seperti fungsi play_game() tanpa wellcome massage
def play_again() :
    user_choose_level()
    user_guess_process()
    user_score()

#game berakhir
def game_ended() :
    # time.sleep(2)
    os.system('cls')
    print("="*65)
    print("Number Guess".center(65))
    print()
    print("*****Game ended*****".center(65))
    print("="*65)

#bertanya ke user untuk memulai permainan kembali
def ask_user_play_again() :
    time.sleep(0.5)
    get_user_play = input("Do you want to play again?[yes/no]")
    while get_user_play == "yes" :
        os.system('cls')
        play_again()
        get_user_play = input("Do you want to play again?[yes/no]")
        if get_user_play == "no" :
            break
    if get_user_play == "no" :
        game_ended()
    elif get_user_play not in ["yes", "no"] :
        error_message()
        time.sleep(0.5)
        os.system('cls')
        ask_user_play_again()
                 
play_game()
ask_user_play_again()