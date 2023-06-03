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
    else:  # Linux
        os.system("aplay done.wav")


def clear_terminal():
    if platform.system() == "Windows":
        os.system("cls")  # Clear the terminal in Windows
    elif platform.system() == "Darwin" or platform.system() == "Linux":
        os.system("clear")  # Clear the terminal in macOS and Linux


def format_time(minutes, seconds):
    return f"{minutes:02d}:{seconds:02d}"


def get_input(prompt):
    return input(prompt).strip().lower()


def start_break(duration, break_type):
    clear_terminal()
    print(f"\n{break_type} break of {duration} minutes.")
    play_sound()

    for remaining in range(duration * 60, 0, -1):
        minutes = remaining // 60
        seconds = remaining % 60
        print(f"Time remaining: {format_time(minutes, seconds)}", end="\r")
        time.sleep(1)

    print("\n")
    clear_terminal()


def pomodoro():
    clear_terminal()
    print("=== Pomodoro Timer ===")

    pomodoro_duration = int(input("Pomodoro duration (minutes): "))
    short_break_duration = int(input("Short break duration (minutes): "))
    long_break_duration = int(input("Long break duration (minutes): "))
    pomodoros_completed = 0

    while True:
        clear_terminal()
        pomodoros_completed += 1

        print(f"Pomodoro {pomodoros_completed}: Working...")
        for remaining in range(pomodoro_duration * 60, 0, -1):
            minutes = remaining // 60
            seconds = remaining % 60
            print(f"Time remaining: {format_time(minutes, seconds)}", end="\r")
            time.sleep(1)

        if pomodoros_completed % 4 == 0:
            start_break(long_break_duration, "Long")
        else:
            start_break(short_break_duration, "Short")

        choice = get_input("Enter 'y' to start the next session or 'n' to exit: ")

        if choice == "n":
            print("Exiting the Pomodoro timer...")
            return

        clear_terminal()
        print("Restarting...\n")
        time.sleep(1)


# Run the Pomodoro timer
pomodoro()
