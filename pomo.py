import os
import time
import platform


def play_sound():
    if platform.system() == "Windows":
        os.system(
            "powershell -c \"(New-Object Media.SoundPlayer 'done.wav').PlaySync()\""
        )
    elif platform.system() == "Darwin":
        os.system("afplay done.wav")
    else: # Linux
        os.system("aplay done.wav")


def clearTerminal():
    if platform.system() == "Windows":
        os.system("cls")  # Clear the terminal in Windows
    elif platform.system() == "Darwin" or platform.system() == "Linux":
        os.system("clear")  # Clear the terminal in macOS and Linux


def pomodoro():
    pomodoro_duration = int(input("Pomodoro duration (minutes): "))
    short_break_duration = int(input("Short break duration (minutes): "))
    long_break_duration = int(input("Long break duration (minutes): "))
    pomodoros_completed = 0

    while True:
        clearTerminal()

        print(f"Pomodoro {pomodoros_completed + 1}: Working...")
        for remaining in range(pomodoro_duration * 60, 0, -1):
            minutes = remaining // 60
            seconds = remaining % 60
            print(f"{minutes:02d}:{seconds:02d}", end="\r")
            time.sleep(1)

        pomodoros_completed += 1
        if pomodoros_completed % 4 == 0:
            clearTerminal()

            print("\n")
            play_sound()
            print(f"Pomodoro completed! Long break of {long_break_duration} minutes.")

            clearTerminal()

            choice = input("Enter 'y' to start the break or 'n' to exit: ")
            clearTerminal()

            if choice.lower() == "n":
                print("Exiting the Pomodoro timer...")
                return

            for remaining in range(long_break_duration * 60, 0, -1):
                minutes = remaining // 60
                seconds = remaining % 60
                print(f"{minutes:02d}:{seconds:02d}", end="\r")
                time.sleep(1)
        else:
            clearTerminal()

            print("\n")
            play_sound()
            print(f"Pomodoro completed! Short break of {short_break_duration} minutes.")

            clearTerminal()

            choice = input("Enter 'y' to start the break or 'n' to exit: ")
            clearTerminal()

            if choice.lower() == "n":
                print("Exiting the Pomodoro timer...")
                return

            for remaining in range(short_break_duration * 60, 0, -1):
                minutes = remaining // 60
                seconds = remaining % 60
                print(f"{minutes:02d}:{seconds:02d}", end="\r")
                time.sleep(1)

        print("\n")

        clearTerminal()

        play_sound()
        choice = input("Enter 'y' to continue or 'n' to exit: ")
        clearTerminal()

        if choice.lower() == "n":
            print("Exiting the Pomodoro timer...")
            return

        clearTerminal()

        print("Restarting...\n")


# Run the Pomodoro timer
pomodoro()
