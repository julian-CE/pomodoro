import time
import sys
import subprocess

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Time's up!")

def ask_user():
    confirm = input("Enter \"Y\" to start work period or \"Q\" to exit: ")
    if confirm.upper() != "Y" and confirm.upper() != "Q":
        print(f"Invalid input: {confirm.upper()}")
        ask_user()
    return confirm.upper()

def main():
    work_time = input("How many seconds would you like to work?: ")
    break_time = input("How many seconds would you like to take a break?: ")
    round_count = 1


    while ask_user() == "Y":
        print("Starting work period...")
        subprocess.run(["afplay", "./beep.mp3"])
        countdown(int(work_time))
        print(f"Work period {round_count} complete.")
        subprocess.run(["afplay", "./rooster.wav"])
        print("Starting break...")
        subprocess.run(["afplay", "./beep.mp3"])
        countdown(int(break_time))
        round_count += 1
        subprocess.run(["afplay", "./rooster.wav"])
    else:
        print("Exiting.")
        sys.exit()

main()
