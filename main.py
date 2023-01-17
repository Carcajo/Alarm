from datetime import datetime
import pyglet
import keyboard

def validate_time(alarm_time):
    if len(alarm_time) != 8:
        return "Неверный формат, попробуйте снова"
    else:
        if int(alarm_time[0:2]) > 23:
            return "Неверный формат часов, попробуйте снова"
        elif int(alarm_time[3:5]) > 59:
            return "Неверный формат минут, попробуйте снова"
        elif int(alarm_time[6:8]) > 59:
            return "Неверный формат секунд, попробуйте снова"
        else:
            return "ok"

while True:
    alarm_time = input("Введите время будильника в следующем формате 'HH:MM:SS' \n Время будильника: ")

    validate = validate_time(alarm_time)
    if validate != "ok":
        print(validate)
    else:
        print(f"Будильник установлен на время {alarm_time}...")
        break

alarm_hour = int(alarm_time[0:2])
alarm_min = int(alarm_time[3:5])
alarm_sec = int(alarm_time[6:8])

while True:
    now = datetime.now()

    current_hour = now.hour
    current_min = now.minute
    current_sec = now.second

    if alarm_hour == current_hour:
        if alarm_min == current_min:
            if alarm_sec == current_sec:
                print("Подъем!")
                sound = pyglet.media.load('alarm.mp3', streaming=False)
                sound.play()
                pyglet.app.run()

