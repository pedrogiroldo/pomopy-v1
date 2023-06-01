import time

def pomodoro():
    pomodoro_duration = 25  # duração de um pomodoro em minutos
    short_break_duration = 5  # duração da pausa curta em minutos
    long_break_duration = 15  # duração da pausa longa em minutos
    pomodoros_completed = 0  # contador de pomodoros concluídos

    while True:
        print(f"Pomodoro {pomodoros_completed + 1}: Trabalhando...")
        time.sleep(pomodoro_duration * 60)  # converte para segundos

        pomodoros_completed += 1
        if pomodoros_completed % 4 == 0:
            print(f"Pausa longa de {long_break_duration} minutos.")
            time.sleep(long_break_duration * 60)
        else:
            print(f"Pausa curta de {short_break_duration} minutos.")
            time.sleep(short_break_duration * 60)

        print("Pomodoro concluído! Reiniciando...\n")

# Executa o cronômetro Pomodoro
pomodoro()
