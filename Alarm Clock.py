# Python Alarm Clock

import time
import datetime
import pygame

def alarm_clock(alarm_time):
    print(f"Alarm Set For {alarm_time}")
    music_ = "Make Me Laugh - Televisions.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time == alarm_time:
            print("TIME UP")
            pygame.mixer.init()
            pygame.mixer.music.load(music_)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)
            is_running = False
        


        time.sleep(1)

        


if __name__ == "__main__":
    alarm_time = input("Enter Alarm Time (H:M:S): ")
    alarm_clock(alarm_time)

