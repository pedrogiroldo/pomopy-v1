import time

def pomodoro():
    pomodoro_duration = int(input("Duração do pomodoro (minutos): "))  
    short_break_duration = int(input("Duração da pausa curta (minutos): "))  
    long_break_duration = int(input("Duração da pausa longa (minutos): "))  
    pomodoros_completed = 0  

    while True:
        print(f"Pomodoro {pomodoros_completed + 1}: Trabalhando...")
        for remaining in range(pomodoro_duration * 60, 0, -1):
            minutes = remaining // 60
            seconds = remaining % 60
            print(f"{minutes:02d}:{seconds:02d}", end="\r")
            time.sleep(1)

        pomodoros_completed += 1
        if pomodoros_completed % 4 == 0:
            print("\n")
            print(f"Pomodoro concluído! Pausa longa de {long_break_duration} minutos.")

            choice = input("Digite 'y' para iniciar a pausa ou 'n' para sair: ")
            if choice.lower() == "n":
                print("Encerrando o cronômetro Pomodoro...")
                return

            for remaining in range(long_break_duration * 60, 0, -1):
                minutes = remaining // 60
                seconds = remaining % 60
                print(f"{minutes:02d}:{seconds:02d}", end="\r")
                time.sleep(1)
        else:
            print("\n")
            print(f"Pomodoro concluído! Pausa curta de {short_break_duration} minutos.")

            choice = input("Digite 'y' para iniciar a pausa ou 'n' para sair: ")
            if choice.lower() == "n":
                print("Encerrando o cronômetro Pomodoro...")
                return

            for remaining in range(short_break_duration * 60, 0, -1):
                minutes = remaining // 60
                seconds = remaining % 60
                print(f"{minutes:02d}:{seconds:02d}", end="\r")
                time.sleep(1)

        print("\n")

        choice = input("Digite 'y' para continuar ou 'n' para sair: ")
        if choice.lower() == "n":
            print("Encerrando o cronômetro Pomodoro...")
            return

        print("Reiniciando...\n")

# Executa o cronômetro Pomodoro
pomodoro()
