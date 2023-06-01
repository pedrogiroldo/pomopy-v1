import time


def pomodoro():
    pomodoro_duration = int(
        input("Duração do pomodoro: ")
    )  # duração de um pomodoro em minutos
    short_break_duration = int(
        input("Duração da pausa curta: ")
    )  # duração da pausa curta em minutos
    long_break_duration = int(
        input("Duração da pausa longa: ")
    )  # duração da pausa longa em minutos
    pomodoros_completed = 0  # contador de pomodoros concluídos

    while True:
        print(f"Pomodoro {pomodoros_completed + 1}: Trabalhando...")
        for remaining in range(pomodoro_duration * 60, 0, -1):
            minutes = remaining // 60
            seconds = remaining % 60
            print(f"{minutes:02d}:{seconds:02d}", end="\r")
            time.sleep(1)

        pomodoros_completed += 1
        if pomodoros_completed % 4 == 0:
            print(f"Pausa longa de {long_break_duration} minutos.")
            for remaining in range(long_break_duration * 60, 0, -1):
                minutes = remaining // 60
                seconds = remaining % 60
                print(f"{minutes:02d}:{seconds:02d}", end="\r")
                time.sleep(1)
        else:
            print(f"Pausa curta de {short_break_duration} minutos.")
            for remaining in range(short_break_duration * 60, 0, -1):
                minutes = remaining // 60
                seconds = remaining % 60
                print(f"{minutes:02d}:{seconds:02d}", end="\r")
                time.sleep(1)

        print("Pomodoro concluído! Reiniciando...\n")


# Executa o cronômetro Pomodoro
pomodoro()
