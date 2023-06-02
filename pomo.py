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
    else:
        os.system("aplay done.wav")


def pomodoro():
    pomodoro_duration = int(input("Duração do pomodoro (minutos): "))
    short_break_duration = int(input("Duração da pausa curta (minutos): "))
    long_break_duration = int(input("Duração da pausa longa (minutos): "))
    pomodoros_completed = 0

    while True:
        os.system("clear")  # Limpa o terminal no Linux/Unix
        # os.system('cls')  # Limpa o terminal no Windows

        print(f"Pomodoro {pomodoros_completed + 1}: Trabalhando...")
        for remaining in range(pomodoro_duration * 60, 0, -1):
            minutes = remaining // 60
            seconds = remaining % 60
            print(f"{minutes:02d}:{seconds:02d}", end="\r")
            time.sleep(1)

        pomodoros_completed += 1
        if pomodoros_completed % 4 == 0:
            os.system("clear")  # Limpa o terminal no Linux/Unix
            # os.system('cls')  # Limpa o terminal no Windows

            print("\n")
            play_sound()
            print(f"Pomodoro concluído! Pausa longa de {long_break_duration} minutos.")

            os.system("clear")  # Limpa o terminal no Linux/Unix
            # os.system('cls')  # Limpa o terminal no Windows
            choice = input("Digite 'y' para iniciar a pausa ou 'n' para sair: ")
            os.system("clear")  # Limpa o terminal no Linux/Unix
            # os.system('cls')  # Limpa o terminal no Windows
            if choice.lower() == "n":
                print("Encerrando o cronômetro Pomodoro...")
                return

            for remaining in range(long_break_duration * 60, 0, -1):
                minutes = remaining // 60
                seconds = remaining % 60
                print(f"{minutes:02d}:{seconds:02d}", end="\r")
                time.sleep(1)
        else:
            os.system("clear")  # Limpa o terminal no Linux/Unix
            # os.system('cls')  # Limpa o terminal no Windows

            print("\n")
            play_sound()
            print(f"Pomodoro concluído! Pausa curta de {short_break_duration} minutos.")

            os.system("clear")  # Limpa o terminal no Linux/Unix
            # os.system('cls')  # Limpa o terminal no Windows
            choice = input("Digite 'y' para iniciar a pausa ou 'n' para sair: ")
            os.system("clear")  # Limpa o terminal no Linux/Unix
            # os.system('cls')  # Limpa o terminal no Windows
            if choice.lower() == "n":
                print("Encerrando o cronômetro Pomodoro...")
                return

            for remaining in range(short_break_duration * 60, 0, -1):
                minutes = remaining // 60
                seconds = remaining % 60
                print(f"{minutes:02d}:{seconds:02d}", end="\r")
                time.sleep(1)

        print("\n")

        os.system("clear")  # Limpa o terminal no Linux/Unix
        # os.system('cls')  # Limpa o terminal no Windows
        play_sound()
        choice = input("Digite 'y' para continuar ou 'n' para sair: ")
        os.system("clear")  # Limpa o terminal no Linux/Unix
        # os.system('cls')  # Limpa o terminal no Windows
        if choice.lower() == "n":
            print("Encerrando o cronômetro Pomodoro...")
            return

        os.system("clear")  # Limpa o terminal no Linux/Unix
        # os.system('cls')  # Limpa o terminal no Windows
        print("Reiniciando...\n")


# Executa o cronômetro Pomodoro
pomodoro()
