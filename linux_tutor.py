import json
import random
import os
import sys
from termcolor import colored

# Load Linux commands from JSON (New Format: List of Dictionaries)
def load_commands():
    with open("commands.json", "r") as file:
        return json.load(file)  

COMMANDS = load_commands()

# Show command details
def show_command_info(command_name):
    found = False
    for cmd in COMMANDS:
        if cmd["name"] == command_name:
            print(colored(f"\n🔹 Command: {cmd['name']}", "green", attrs=["bold"]))
            print(colored(f"📌 Category: {cmd['category']}", "blue"))
            print(colored(f"📜 Description: {cmd['description']}", "cyan"))
            found = True
            break

    if not found:
        print(colored(f"❌ Command '{command_name}' not found!", "red"))

# Search for commands
def search_commands(keyword):
    print(colored(f"\n🔎 Searching for '{keyword}'...\n", "blue"))
    results = [cmd for cmd in COMMANDS if keyword.lower() in cmd["name"]]

    if results:
        for cmd in results:
            print(colored(f"👉 {cmd['name']}: {cmd['description']}", "green"))
    else:
        print(colored("❌ No matching commands found!", "red"))

# Quiz mode
def quiz_mode():
    print(colored("\n🧠 QUIZ MODE: Identify the Command!", "yellow", attrs=["bold"]))
    
    command_info = random.choice(COMMANDS)  # Pick a random command
    command_name = command_info["name"]
    
    print(colored(f"📌 Description: {command_info['description']}", "cyan"))
    answer = input(colored("🔹 Your Answer: ", "yellow")).strip()

    if answer.lower() == command_name:
        print(colored("✅ Correct!", "green"))
    else:
        print(colored(f"❌ Incorrect! The correct command is: {command_name}", "red"))

# Practice mode
def practice_mode():
    print(colored("\n🎯 PRACTICE MODE: Try the Command!", "yellow", attrs=["bold"]))
    
    command_info = random.choice(COMMANDS)
    
    print(colored(f"📌 Description: {command_info['description']}", "cyan"))
    print(colored(f"💡 Example: {command_info['name']}", "magenta"))
    
    user_input = input(colored("\n🔹 Type the command: ", "yellow")).strip()

    if user_input == command_info["name"]:
        print(colored("✅ Correct!", "green"))
    else:
        print(colored("❌ Incorrect! Try again.", "red"))

# Interactive CLI
def main():
    os.system("clear")
    print(colored("🚀 Linux Command Tutor CLI", "green", attrs=["bold", "underline"]))

    while True:
        user_input = input(colored("\n🔹 Enter a Linux command (or 'exit'/'search [keyword]'/'quiz'/'practice'): ", "yellow")).strip()

        if user_input.lower() == "exit":
            print(colored("👋 Exiting... Happy Learning!", "cyan"))
            sys.exit()
        elif user_input.startswith("search "):
            keyword = user_input.split(" ", 1)[1]
            search_commands(keyword)
        elif user_input.lower() == "quiz":
            quiz_mode()
        elif user_input.lower() == "practice":
            practice_mode()
        else:
            show_command_info(user_input)

# Run the CLI
if __name__ == "__main__":
    main()
