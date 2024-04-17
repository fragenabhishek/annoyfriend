import random
import pyautogui as pg
import time

def type_messages(message, animals, iterations, delay):
    time.sleep(2)  # Delay before starting to give you time to switch focus
    for _ in range(iterations):
        animal = random.choice(animals)
        message_to_type = f"{message} {animal}"
        pg.write(message_to_type)
        pg.press('enter')
        time.sleep(delay)

if __name__ == "__main__":
    custom_message = input("Enter the message you want to type: ")
    custom_animals = input("Enter the animals separated by commas (e.g., monkey, donkey, dog): ").split(',')
    custom_iterations = int(input("Enter the number of iterations: "))
    custom_delay = float(input("Enter the delay between each iteration (in seconds): "))
    
    type_messages(custom_message, custom_animals, custom_iterations, custom_delay)
