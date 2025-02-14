import time
import os

def display_logo(file_path):
    try:
        with open(file_path, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("ERROR: Logo file not found.")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()
display_logo("logo.txt")
print("Starting MTOS...")
time.sleep(3)
print("Version 0.1 2025 Alpha build 0001")
